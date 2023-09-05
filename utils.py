import subprocess


def get_rotation(video_path):
    """
    Get the rotation angle of a video file.

    Parameters:
        video_path (str): The path to the video file.

    Returns:
        int: The rotation angle in degrees. Returns 0 if rotation info cannot be obtained.

    Raises:
        ValueError: If the rotation value cannot be parsed.
        Exception: For other errors while running the command.
    """
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


def get_video_resolution(video_path):
    """
    Get the resolution of a video file.

    Parameters:
        video_path (str): The path to the video file.

    Returns:
        tuple: (height, width) of the video. Returns (0, 0) if resolution info cannot be obtained.

    Raises:
        ValueError: If the resolution values cannot be parsed.
    """
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


def get_video_rotation(video):
    """
    Get the effective resolution of a video file, considering its rotation.

    Parameters:
        video (str): The path to the video file.

    Returns:
        tuple: (height, width) of the video, adjusted for rotation.
    """
    rotation_angle = get_rotation(video)
    height, width = get_video_resolution(video)
    if rotation_angle == 90 or rotation_angle == 270:
        height, width = width, height
        print(f"Video is rotated {rotation_angle} degrees. Switching width and height.")
    return height, width


def has_valid_resolution(video_path, h, w):
    height, width = get_video_resolution(video_path)
    return (height == h and width == w) or (height == w and width == h)  # assume aspect ratio is enforced
