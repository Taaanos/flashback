import subprocess


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
