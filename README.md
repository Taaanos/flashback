# Flashback
<img src="logo.jpg" width="200" height="200">

Flashback is an app that compiles videos by choosing from a small set of options.  

This app lets you choose video folders, set parameters like the video order (chronological or random), and create a single compiled video from those sources — the flashback.

## Motivation

Why Flashback⚡️? If you're like me, you probably have terabytes of videos sitting in your hard drives,
untouched and unwatched 🫠. The problem with many existing solutions, such as Apple Photos or GoPro Quik, 
is the lack of control over the original video quality and data. Often, you're required to import your videos into an 
app that maintains its own library, which can be a cumbersome process, especially for large collections.

Flashback provides a lightweight, straightforward alternative. It respects your original video quality and video locations, allows for 
local processing — no need to upload gigabytes of videos to a cloud service or to your phone. It's a flashback in its 
purest form, without the fancy music or edits. Simply point to the source folders, and get a flashback 
video ⚡️🎥 generated on your machine. It's a convenient way to relive memories without the hassle of editing 😌.

## Requirements

- Python 3.x
- moviepy
- ffmpeg
- macOS (videotoolbox is used for hardware acceleration taking advantage of the GPU in Apple Silicon)

## Installation

1. Clone this repository.
1. Install ffmpeg and mediainfo

   ```bash
   brew install ffmpeg
   ```

   ```bash
   brew install mediainfo
   ```

Note: If you need to install brew for your system, follow the instructions [here](https://brew.sh/).

1. Create a python virtual environment and activate it

   ```bash
   # create your virtual environment
   python -m venv env

   # activate your virtual environment
   source venv/bin/activate
   ```

1. Install the required python packages

   ```bash
   pip install -r requirements.txt
   ```


## Launching the App

Launch the app and shortly the GUI will pop up.

```bash
python3 ./main.py
```
![alt text](gui.png)

## Output

The app will generate a compiled video file in the set output directory with a filename containing the parameters used for compilation.

An output demo video from my video library can be viewed [here](https://youtu.be/sXir-y6wN8w?si=oZlH9bHf8ul1oySs). 

## Limitations

The GUI does not contain a progress bar yet.