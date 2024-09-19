#!/bin/env python3

'''
Receive sys argv [1] with path to folder
containing video files, make list and
multiprocess in create() function
'''

# Python standard library
import os
import sys
import subprocess
from multiprocessing import Pool


def create(fpath) -> str:
    '''
    Builds FFmpeg command based on height/dar input
    '''

    if os.path.exists(fpath):
        pathname, filename = os.path.split(fpath)
        fname = f"{os.path.splitext(filename)[0]}.mp4"
        outpath = os.path.join(pathname, 'transcodes/')
        if not os.path.exists(outpath):
            os.mkdir(outpath, mode=0o777)
        print(f"Fullpath {fpath} - Output path {outpath}{fname}")

        ffmpeg_call = [
            "ffmpeg",
            "-i", fpath,
            "-c:v", "libx264",
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-movflags", "faststart",
            "-map", "0:v:0",
            "-map", "0:a?", "-dn",
            "-c:a", "aac",
            f"{outpath}{fname}"
        ]

        try:
            data = subprocess.run(ffmpeg_call, shell=False, capture_output=True, text=True)
            return data
        except subprocess.CalledProcessError as err:
            return f"Subprocess failed to process command:\n{err}"
    else:
        return f"Path not recognised:\n{fpath}"


def main():
    '''
    Launch the list of transcodes using multiprocessing pool
    '''
    if not sys.argv[1]:
        sys.exit("Please try again with path to media folder.")
    if not os.path.exists(sys.argv[1]):
        sys.exit("Please try again with correctly formatted path for media folder.")

    file_list = []
    for root, _, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith(('.mkv', '.mov')):
                file_list.append(os.path.join(root, file))

    if len(file_list) <= 1:
        sys.exit("Insufficient files in file path for multiprocessing example.")

    with Pool() as p:
        response = p.map(create, file_list)
        print(f"Response code for encoding: {response.returncode}")
        p.close()


if __name__ == "__main__":
    main()