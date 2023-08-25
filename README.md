# Flashback

Flashback is a Python script that compiles videos from a specified folder either randomly or in sequence. It's possible to define the maximum output duration, minimum and maximum clip duration, and the order in which the videos are selected.

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
   
4. If you need to install brew for your system, follow the instructions [here](https://brew.sh/).

## Usage

Create a folder containing the videos you want to compile; aka a video pool.
For the video path, you can drag and drop the file in the terminal to get the path.

You can run the script using the following command:

```bash
python script_name.py --folder /path/to/videos --max-output-duration DURATION --min-clip-duration MIN_DURATION --max-clip-duration MAX_DURATION --order ORDER --extension EXTENSION
```

### Parameters

- `--folder`: Path to the folder containing videos (Required).
- `--max-output-duration`: Maximum output duration in seconds (Required).
- `--min-clip-duration`: Minimum clip duration in seconds (Required).
- `--max-clip-duration`: Maximum clip duration in seconds (Required).
- `--order`: Order of video selection (`rand` or `seq`). Defaults to `rand`.
- `--extension`: Input video file extension. Defaults to `MP4`.

### Recommended parameters

- `--max-output-duration`: 90 
- `--min-clip-duration`: 3
- `--max-clip-duration`: 8
- `--order`: `rand`

## Example

Compile videos randomly:

```bash
python script_name.py --folder /path/to/videos --max-output-duration 60 --min-clip-duration 5 --max-clip-duration 10 --order rand --extension MOV
```

Compile videos sequentially:

```bash
python script_name.py --folder /path/to/videos --max-output-duration 60 --min-clip-duration 5 --max-clip-duration 10 --order seq --extension MOV
```

## Output

The script will generate a compiled video file in the current directory with a filename containing the parameters used for compilation.

## License

## Limitations

- The script currently can handle only a few  open files, so if you want to create a long video > 5', then this will fail. Batch processing is not yet implemented.
- The script currently only supports either MP4 or MOV files. Other formats will be added in the future.
- Currently only works in MacOS with Apple Silicon.