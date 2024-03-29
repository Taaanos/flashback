# Flashback
<img src="logo.jpg" width="200" height="200">

Flashback is a Python tool that compiles videos from a specified folder either randomly or in sequence. 
It's possible to define the maximum output duration, minimum and maximum clip duration, and the order in which the videos 
are selected.

## Motivation

Why Flashback⚡️? If you're like me, you probably have terabytes of videos sitting on your machine,
untouched and unwatched 🫠. The problem with many existing solutions, such as Apple Photos or GoPro Quik, 
is the lack of control over the original video quality and data. Often, you're required to import your videos into an 
app that maintains its own library, which can be a cumbersome process, especially for large collections.

Flashback provides a lightweight, straightforward alternative. It respects your original video quality and allows for 
local processing—no need to upload ☁️ gigabytes of videos to a cloud service or to your phone. It's a flashback in its 
purest form, without the frills of fancy music or edits. Simply point to the source folders, and get a flashback 
video ⚡️🎥 generated on your machine. It's a convenient way to relive memories without the hassle 😌.

## Requirements

- Python 3.x
- moviepy
- ffmpeg
- macOS (videotoolbox is used for hardware acceleration taking advantage of the GPU in Apple Silicon)

## Installation

1. Clone this repository or download the script.
2. Install the required package using:

   ```bash
   pip install moviepy
   ```
3. Install ffmpeg. On macOS, you can use Homebrew:

   ```bash
   brew install ffmpeg
   ```
4. Install mediainfo using Homebrew:

   ```bash
   brew install mediainfo
   ```
      
5. If you need to install brew for your system, follow the instructions [here](https://brew.sh/).

## Usage

Create a folder containing the videos you want to compile; aka a video pool.
For the video path, you can drag and drop the file in the terminal to get the path.

Or simply select the folders you want to use as a video pool and drag and drop them in the terminal to get the paths.

You can run the script using the following command:

```bash
python compile.py --folders /path/to/videos1 /path/to/videos2 /path/to/videos3 --max-output-duration DURATION --min-clip-duration MIN_DURATION --max-clip-duration MAX_DURATION --order ORDER --extension EXTENSION --debug DEBUG
```

### Parameters

- `--folders`: Path to the folders containing videos (Required).
- `--max-output-duration`: Maximum output duration in seconds (Required).
- `--min-clip-duration`: Minimum clip duration in seconds (Required).
- `--max-clip-duration`: Maximum clip duration in seconds (Required).
- `--order`: Order of video selection (`rand` or `seq`). Defaults to `rand`.
- `--extension`: Input video file extension. Defaults to `MP4`.
- `--debug`: Enable debug mode. Defaults to `False`.

### Recommended parameters

- `--max-output-duration`: 90 
- `--min-clip-duration`: 3
- `--max-clip-duration`: 8
- `--order`: `rand`

## Output

The script will generate a compiled video file in the current directory with a filename containing the parameters used for compilation.

## Limitations

- The script currently can handle only a few  open files, so if you want to create a long video > 5', then this will fail. Batch processing is not yet implemented.
- The script currently only supports either MP4 or MOV files. Other formats will be added in the future.