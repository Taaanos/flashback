import os
import random
import logging
logger = logging.getLogger(__name__)


def create_video_pool(folders, extension):
    """
    Create a pool of video files from given folders with a specific extension.

    Parameters:
    - folders (list): List of folder paths to search for video files.
    - extension (str): The file extension to look for (e.g., 'mp4').

    Returns:
    - list: A list of video file paths with the specified extension.
    """
    videos_in_folders = []
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(f'.{extension}'):
                    videos_in_folders.append(os.path.join(root, file))
    return videos_in_folders


def sort_videos(video_list, order):
    """
    Sort a list of video files either sequentially by modification time or randomly.

    Parameters:
    - video_list (list): List of video file paths to sort.
    - order (str): Sorting order ('chronological' or 'random').

    Returns:
    - list: Sorted list of video file paths.
    """
    if order == "chronological":
        return sorted(video_list, key=lambda x: os.path.getmtime(x))
    elif order == "random":
        random.shuffle(video_list)
        return video_list
    else:
        logger.error("Invalid order argument. Use 'chronological' or 'random'")
        return video_list
