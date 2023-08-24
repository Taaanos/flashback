from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import os
import argparse
from datetime import datetime


def compile_videos(folder, max_output_duration, min_clip_duration, max_clip_duration):
    dir_name = os.path.basename(folder)
    output_filename = f"{dir_name}_{max_output_duration}_{min_clip_duration}_{max_clip_duration}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.MP4"

    video_files = [f for f in os.listdir(folder) if f.endswith('.MP4')]
    random.shuffle(video_files)

    clips = []
    total_duration = 0

    for video_file in video_files:
        if total_duration >= max_output_duration:
            break

        video_path = os.path.join(folder, video_file)
        video = VideoFileClip(video_path)

        start_time = random.uniform(0, video.duration - min_clip_duration)
        end_time = random.uniform(start_time + min_clip_duration, min(start_time + max_clip_duration, video.duration))

        subclip = video.subclip(start_time, end_time).set_fps(60)

        clips.append(subclip)
        total_duration += (end_time - start_time)

        video.reader.close()

    if clips:  # Check if there are valid clips
        final_video = concatenate_videoclips(clips)
        final_video.write_videofile(output_filename, codec="hevc_videotoolbox", ffmpeg_params=['-q:v', '50'])
    else:
        print("No valid clips found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile a video from a folder of videos in random order.")
    parser.add_argument("folder", help="Path to the folder containing videos.")
    parser.add_argument("max_output_duration", type=int, help="Maximum duration of the output video in seconds.")
    parser.add_argument("min_clip_duration", type=int, help="Minimum duration of each clip in seconds.")
    parser.add_argument("max_clip_duration", type=int, help="Maximum duration of each clip in seconds.")

    args = parser.parse_args()

    compile_videos(args.folder, args.max_output_duration, args.min_clip_duration, args.max_clip_duration)
