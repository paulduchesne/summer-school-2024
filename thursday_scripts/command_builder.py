#!/bin/env python3

'''
Example functions for building and running FFmpeg commands
Only requires FFmpeg installed previously and Python standard lib.
'''

# Python standard library
import os
import re
import subprocess


def create(fullpath, output_path, height, width, dar, par) -> list:
    '''
    Builds FFmpeg command based on height/dar input
    Paths best receiving absolute paths correct for operating system
    Height and width examples '1920', '576'
    DAR examples '16:9', '1.85:1', ''
    PAR examples '1.000', ''
    '''

    if not os.path.exists(fullpath):
        return f"Path not recognised:\n{fullpath}"
    if not os.path.isfile(output_path):
        filename = os.path.split(fullpath)[-1]
        fname = f"{os.path.splitext(filename)[0]}.mp4"
        outpath = os.path.join(output_path, f"transcode_{fname}")
    else:
        outpath = output_path
    print(f"Fullpath {fullpath} - Output path {outpath}")
    print(f"Received DAR {dar} PAR {par} H {height} W {width}")

    ffmpeg_call = [
        "ffmpeg",
        "-i", fullpath
    ]

    video_settings = [
        "-c:v", "libx264",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-movflags", "faststart"
    ]

    mappings = [
        "-map", "0:v:0",
        "-map", "0:a?", "-dn",
        "-c:a", "aac"
    ]

    no_stretch_4x3 = [
        "-vf",
        "yadif,pad=768:576:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_sd_4x3 = [
        "-vf",
        "yadif,crop=672:572:24:2,scale=734:576:flags=lanczos,pad=768:576:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    scale_sd_4x3 = [
        "-vf",
        "yadif,scale=768:576:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    scale_sd_16x9 = [
        "-vf",
        "yadif,scale=1024:576:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_sd_15x11 = [
        "-vf",
        "yadif,crop=704:572,scale=768:576:flags=lanczos,pad=768:576:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_ntsc_486 = [
        "-vf",
        "yadif,crop=672:480,scale=734:486:flags=lanczos,pad=768:486:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_ntsc_486_16x9 = [
        "-vf",
        "yadif,crop=672:480,scale=1024:486:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_ntsc_640x480 = [
        "-vf",
        "yadif,pad=768:480:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    crop_sd_16x9 = [
        "-vf",
        "yadif,crop=704:572:8:2,scale=1024:576:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    sd_downscale_16x9 = [
        "-vf",
        "yadif,scale=1024:576:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    sd_downscale_4x3 = [
        "-vf",
        "yadif,scale=768:576:flags=lanczos,blackdetect=d=0.05:pix_th=0.10"
    ]

    hd_16x9 = [
        "-vf",
        "yadif,scale=-1:720:flags=lanczos,pad=1280:720:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    fhd_all = [
        "-vf",
        "yadif,scale=-1:1080:flags=lanczos,pad=1920:1080:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    fhd_letters = [
        "-vf",
        "yadif,scale=1920:-1:flags=lanczos,pad=1920:1080:-1:-1,blackdetect=d=0.05:pix_th=0.10"
    ]

    output = [
        "-nostdin", "-y",
        outpath
    ]

    # Calculate height/width to decide HD scale path
    height = int(height)
    width = int(width)
    aspect = round(width / height, 3)
    print(f"Aspect calculation: {aspect}")

    filters = []
    if height < 400 and width < 533 and dar == '4:3':
        filters = scale_sd_4x3
    elif height < 400 and width < 533 and dar == '16:9':
        filters = scale_sd_16x9
    elif height <= 486 and dar == '16:9':
        filters = crop_ntsc_486_16x9
    elif height <= 486 and dar == '4:3':
        filters = crop_ntsc_486
    elif height <= 486 and width == 640:
        filters = crop_ntsc_640x480
    elif height < 576 and width == 720 and dar == '4:3':
        filters = scale_sd_4x3
    elif height == 576 and width == 703 and dar == '4:3':
        filters = scale_sd_4x3
    elif height < 576 and width > 720 and dar == '16:9':
        filters = sd_downscale_16x9
    elif height < 576 and width > 720 and dar == '4:3':
        filters = sd_downscale_4x3
    elif height <= 576 and dar == '16:9':
        filters = crop_sd_16x9
    elif height <= 576 and width == 768:
        filters = no_stretch_4x3
    elif height <= 576 and par == '1.000':
        filters = no_stretch_4x3
    elif height <= 576 and dar == '4:3':
        filters = crop_sd_4x3
    elif height <= 576 and dar == '15:11':
        filters = crop_sd_15x11
    elif height == 576 and dar == '1.85:1':
        filters = crop_sd_16x9
    elif height < 720 and dar == '16:9':
        filters = sd_downscale_16x9
    elif height < 720 and dar == '4:3':
        filters = sd_downscale_4x3
    elif height == 720 and dar == '16:9':
        filters = hd_16x9
    elif width == 1920 and aspect >= 1.778:
        filters = fhd_letters
    elif height > 720 and width <= 1920:
        filters = fhd_all
    elif width >= 1920 and aspect < 1.778:
        filters = fhd_all
    elif height >= 1080 and aspect >= 1.778:
        filters = fhd_letters

    print(f"Filter command chosen: {filters}")

    if filters:
        return ffmpeg_call + video_settings + mappings + filters + output
    else:
        return "Unable to identify filter match for file!"


def run(ffmpeg_command) -> str:
    '''
    Use this command to run your FFmpeg MP4 command
    And capture the data for the black detection
    shell=False because you're inputting a list
    '''
    try:
        data = subprocess.run(ffmpeg_command, shell=False, capture_output=True, text=True)
        return data
    except subprocess.CalledProcessError as err:
        print(f"Subprocess failed to process command:\n{err}")


def get_blackspace_list(data) -> list:
    '''
    Retrieve FFmpeg log with blackdetect and check if
    second variable falls in blocks of blackdetected
    '''
    ffmpeg_data = data.stderr
    if len(ffmpeg_data) == 0:
        ffmpeg_data = data.stdout
    if len(ffmpeg_data) == 0:
        return 'No FFmpeg logs found'

    data_list = ffmpeg_data.splitlines()
    time_range = []
    for line in data_list:
        if 'black_start' in line:
            split_line = line.split(":")
            split_start = split_line[1].split('.')[0]
            start = re.sub("[^0-9]", "", split_start)
            split_end = split_line[2].split('.')[0]
            end = re.sub("[^0-9]", "", split_end)
            # Round up to next second for cover
            end = str(int(end) + 1)
            time_range.append(f"{start} - {end}")
    return time_range


def seconds_clash(time_ranges, seconds) -> bool:
    '''
    Create range and check for seconds within
    if clash found return True
    '''
    if not isinstance(seconds, int):
        seconds = int(seconds)

    for item in time_ranges:
        start, end = item.split(" - ")
        st = int(start) - 1
        ed = int(end) + 1
        if seconds in range(st, ed):
            print(f"Clash {seconds}: {item}")
            return True


def validate_transcode(fpath) -> str:
    '''
    Supply full file path for validating
    '''
    if not os.path.exists(fpath):
        return f"File path does not exists, please check and retry."

    # Check FFprobe can read file
    cmd = ['ffprobe', '-i', fpath, '-loglevel', '-8']
    check = subprocess.run(cmd, shell=False)
    if check.returncode != 0:
        return f"Error! File could not be read by FFprobe."

    # Check the transcode completed, not truncated    
    cmd = ['mediainfo', '--Output=General;%Duration%', fpath]
    check = subprocess.run(cmd, shell=False, capture_output=True, text=True)
    if len(check.stderr) == 0 and len(check.stdout) == 0:
        return f"Error! File duration is absent. File possibly truncated."

    # Check the transcode passes the MediaConch policy    
    cmd = ['mediaconch', '-p', 'basic_mp4_policy.xml', fpath]
    pass_fail = subprocess.run(cmd, shell=False, capture_output=True, text=True)
    if pass_fail.stdout.startswith(f'pass! {fpath}'):
        return f"File passed FFrobe check, file is whole and MediaConch policy:\n{pass_fail.stdout}"
    elif pass_fail.stderr.startswith(f'pass! {fpath}'):
        return f"File passed FFrobe check, file is whole and MediaConch policy:\n{pass_fail.stderr}"
    else:
        return f"File passed FFprobe check, but failed Mediaconch policy:\n{pass_fail.stdout} {pass_fail.stderr}"
