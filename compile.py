import sys

from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import os
import argparse
from datetime import datetime


def compile_videos(folder, max_output_duration, min_clip_duration, max_clip_duration, order, extension):
    dir_name = os.path.basename(os.path.normpath(folder))
    output_filename = f"{dir_name}_{order}_{max_output_duration}_{min_clip_duration}_{max_clip_duration}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}"

    video_files = [f for f in os.listdir(folder) if f.endswith('.'+extension)]

    if order == 'rand':
        random.shuffle(video_files)
    else:
        video_files.sort(key=lambda x: os.path.getatime(os.path.join(folder, x)))
    clips = []
    total_duration = 0

    for video_file in video_files:
        print(f"Using video: {video_file}")
        if total_duration >= max_output_duration:
            break

        video_path = os.path.join(folder, video_file)
        video = VideoFileClip(video_path)

        if args.debug:
            video.save_frame(f"video_frame_{video_file}.png", t=video.duration/2)

        start_time = random.uniform(0, video.duration - min_clip_duration)
        end_time = random.uniform(start_time + min_clip_duration, min(start_time + max_clip_duration, video.duration))

        if start_time < 0:
            print(f"The video: {video_file} is too short to be used. Please use longer videos.")
            sys.exit(1)

        newclip = video.subclip(start_time, end_time).set_fps(video.fps)
        clips.append(newclip)
        total_duration += (end_time - start_time)

        video.reader.close()

    if args.debug:
        for clip in clips:
            clip.save_frame(f"clip_frame{video_file}.png", t=clip.duration/2)

    if clips:  # Check if there are valid clips
        final_video = concatenate_videoclips(clips)
        try:
            final_video.write_videofile(output_filename, codec="hevc_videotoolbox", ffmpeg_params=['-q:v', '50'])
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
    parser.add_argument('--folder', required=True, help='Path to the folder containing videos.')
    parser.add_argument('--max-output-duration', type=int, required=True, help='Maximum output duration.')
    parser.add_argument('--max-clip-duration', type=int, required=True, help='Maximum clip duration.')
    parser.add_argument('--min-clip-duration', type=int, required=True, help='Minimum clip duration.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode.')
    args = parser.parse_args()

    compile_videos(args.folder, args.max_output_duration, args.min_clip_duration, args.max_clip_duration, args.order, args.extension)
