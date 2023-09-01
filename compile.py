import sys

from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import os
import argparse
from datetime import datetime
from utils import get_video_rotation
from video_pool import create_video_pool, sort_videos


def compile_videos(folders, max_output_duration, min_clip_duration, max_clip_duration, order, extension):
    video_pool = create_video_pool(folders, extension)
    video_pool = sort_videos(video_pool, order)

    clips = []
    total_duration = 0

    for video in video_pool:
        print(f"Using video: {video}")
        if total_duration >= max_output_duration:
            break

        # There is a bug in moviepy that doesn't respect the rotation metadata
        # see https://github.com/Zulko/moviepy/issues/1871
        height, width = get_video_rotation(video)
        clip = VideoFileClip(video, target_resolution=(height, width))
        print(f"Used video path:{video}")
        video_name = os.path.basename(video)
        if args.debug:
            clip.save_frame(f"video_frame_{video_name}.png", t=clip.duration / 2)

        start_time = random.uniform(0, clip.duration - min_clip_duration)
        end_time = random.uniform(start_time + min_clip_duration, min(start_time + max_clip_duration, clip.duration))

        if start_time < 0:
            print(f"The video: {video_name} is too short to be used. Please use longer videos.")
            sys.exit(1)

        subclip = clip.subclip(start_time, end_time).set_fps(clip.fps)
        clips.append(subclip)
        total_duration += (end_time - start_time)

        clip.reader.close()

    if args.debug:
        for clip in clips:
            clip.save_frame(f"clip_frame{video_name}.png", t=clip.duration / 2)

    output_filename = (f"flashback_{order}_{max_output_duration}_{min_clip_duration}_{max_clip_duration}_"
                       f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}")
    if clips:  # Check if there are valid clips
        final_video = concatenate_videoclips(clips)
        try:
            final_video.write_videofile(output_filename, codec="hevc_videotoolbox", ffmpeg_params=['-q:v', '50',
                                                                                                   '-profile:v', 'main',
                                                                                                   '-level', '5.0',
                                                                                                   '-tag:v', 'hvc1',
                                                                                                   '-c:a', 'aac'])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("No valid clips found.")

    # Close all subclip readers
    for clip in clips:
        clip.reader.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compile videos either randomly or in sequence.')
    parser.add_argument('--order', choices=['rand', 'seq'], default='rand',
                        help='Order of video selection (rand or seq).')
    parser.add_argument('--extension', choices=['MOV', 'MP4'], default='MP4',
                        help='Extension of video files.')
    parser.add_argument('--folders', nargs='+', required=True, help='List of folders containing videos.')
    parser.add_argument('--max-output-duration', type=int, required=True, help='Maximum output duration.')
    parser.add_argument('--max-clip-duration', type=int, required=True, help='Maximum clip duration.')
    parser.add_argument('--min-clip-duration', type=int, required=True, help='Minimum clip duration.')
    parser.add_argument('--n', type=int, default=1, help='The number of repetitions of the video to compile.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode.')
    args = parser.parse_args()

    for i in range(args.n):
        compile_videos(args.folders, args.max_output_duration, args.min_clip_duration, args.max_clip_duration, args.order,
                   args.extension)

    print("Flashback done!")

