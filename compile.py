import sys
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
from datetime import datetime
from utils import get_video_rotation
from video_pool import create_video_pool, sort_videos
from utils import has_valid_resolution
import logging
logger = logging.getLogger(__name__)


def compile_videos(folders, max_output_duration, min_clip_duration, max_clip_duration, order, extension, resolution, debug, output_location):
    
    videos = create_video_pool(folders, extension)
    videos = sort_videos(videos, order)
    
    output_filename = (f"{output_location}/flashback_{order}_{max_output_duration}_{min_clip_duration}_{max_clip_duration}_"
                       f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}")
       
    clips = []
    total_duration = 0

    if resolution:
        h, w = map(int, resolution.split(','))  # Convert the resolution string to integers for height and width

    for video in videos:
        logger.info(f"Using video: {video}")

        if resolution and not has_valid_resolution(video, h, w):  # Check for resolution if provided
            logger.debug(f"The video: {video} does not match the provided resolution {h}x{w}. Skipping...")
            continue

        if total_duration >= max_output_duration:
            break

        # There is a bug in moviepy that doesn't respect the rotation metadata
        # see https://github.com/Zulko/moviepy/issues/1871
        height, width = get_video_rotation(video)
        
        clip = VideoFileClip(video, target_resolution=(height, width))
        video_name = os.path.basename(video)
        
        if debug:
            clip.save_frame(f"video_frame_{video_name}.png", t=clip.duration / 2)

        start_time = random.uniform(0, clip.duration - min_clip_duration)
        end_time = random.uniform(start_time + min_clip_duration, min(start_time + max_clip_duration, clip.duration))

        if start_time < 0:
            logger.debug(f"The video: {video_name} is too short to be used. Skipping...")
        else:
            subclip = clip.subclip(start_time, end_time).set_fps(clip.fps)
            clips.append(subclip)
            total_duration += (end_time - start_time)

        clip.reader.close()

    if debug:
        for clip in clips:
            clip.save_frame(f"clip_frame{video_name}.png", t=clip.duration / 2)

   
    if clips:
        final_video = concatenate_videoclips(clips)
        try:
            final_video.write_videofile(output_filename, codec="hevc_videotoolbox", ffmpeg_params=['-q:v', '50',
                                                                                                   '-profile:v', 'main',
                                                                                                   '-level', '5.0',
                                                                                                   '-tag:v', 'hvc1',
                                                                                                   '-c:a', 'aac'])
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)
    else:
        logger.info("No valid clips found.")

    # Close all subclip readers
    for clip in clips:
        clip.reader.close()
