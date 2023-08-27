import sys

from moviepy.editor import VideoFileClip, concatenate_videoclips
import random
import os
import argparse
from datetime import datetime
import subprocess


def compile_videos(folder, max_output_duration, min_clip_duration, max_clip_duration, order, extension):
    dir_name = os.path.basename(os.path.normpath(folder))
    output_filename = f"{dir_name}_{order}_{max_output_duration}_{min_clip_duration}_{max_clip_duration}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}"

    video_files = [f for f in os.listdir(folder) if f.endswith('.' + extension)]

    if order == 'rand':
        random.shuffle(video_files)
    else:
        video_files.sort(key=lambda x: os.path.getctime(os.path.join(folder, x)))
    clips = []
    total_duration = 0

    for video_file in video_files:
        print(f"Using video: {video_file}")
        if total_duration >= max_output_duration:
            break

        # There is a bug in moviepy that doesn't respect the rotation metadata
        # see https://github.com/Zulko/moviepy/issues/1871
        video_path = os.path.join(folder, video_file)
        rotation_angle = get_rotation(video_path)
        height, width = get_resolution(video_path)
        if rotation_angle == 90 or rotation_angle == 270:
            height, width = width, height
            print(f"Video is rotated {rotation_angle} degrees. Switching width and height.")
        print(f"Video resolution: {width}x{height}")
        clip = VideoFileClip(video_path, target_resolution=(height,width))

        if args.debug:
            clip.save_frame(f"video_frame_{video_file}.png", t=clip.duration / 2)

        start_time = random.uniform(0, clip.duration - min_clip_duration)
        end_time = random.uniform(start_time + min_clip_duration, min(start_time + max_clip_duration, clip.duration))

        if start_time < 0:
            print(f"The video: {video_file} is too short to be used. Please use longer videos.")
            sys.exit(1)

        subclip = clip.subclip(start_time, end_time).set_fps(clip.fps)
        clips.append(subclip)
        total_duration += (end_time - start_time)

        clip.reader.close()

    if args.debug:
        for clip in clips:
            clip.save_frame(f"clip_frame{video_file}.png", t=clip.duration / 2)

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


def get_resolution(video_path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-of", "csv=s=x:p=0",
        video_path
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.stdout:
        try:
            dimensions = result.stdout.strip().split('x')  # strip and split
            dimensions = [int(dim) for dim in dimensions if dim]  # convert to int, ignoring empty strings
            if len(dimensions) == 2:
                return dimensions[1], dimensions[0]  # return height, width
            else:
                print("Failed to parse video dimensions.")
                return (0, 0)
        except ValueError:
            print("Failed to parse video dimensions.")
            return (0, 0)
    else:
        print("Could not get video dimensions.")
        return (0, 0)

def get_rotation(video_path):
    try:
        cmd = ["mediainfo", "--Inform=Video;%Rotation%", video_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        rotation = int(float(result.stdout.strip()))
        return rotation
    except ValueError:
        print(f"Could not parse rotation, received: {result.stdout.strip()}")
        return 0
    except Exception as e:
        print(f"Could not get video rotation. Error: {e}")
        return 0




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

    compile_videos(args.folder, args.max_output_duration, args.min_clip_duration, args.max_clip_duration, args.order,
                   args.extension)
