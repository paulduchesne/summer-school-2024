

import pathlib
import subprocess
import tarfile

# Directory where my film scans are
scan_dir = pathlib.Path.cwd() / 'source'
# Loop through all scans.
for film_scan in scan_dir.iterdir():
    # Check if film_scan is a directory (and not .DS_STORE)
    if film_scan.is_dir():
        print(film_scan)
        # Generate path for expected tarfile. 
        tar_path = (film_scan.parents[1] / 'tar' / f'{film_scan.stem}.tar')
        # Check if tar file exists
        if not tar_path.exists():
            # If not, create a tarfile
            with tarfile.open(tar_path, 'w') as f:
                # Iterate over contents of scan folder.
                for scan_file in film_scan.iterdir():
                    # Add the file to the tar.
                    f.add(scan_file)
        # Generate path for expected proxy file.
        proxy_path = (film_scan.parents[1] / 'proxy' / f'{film_scan.stem}.mp4')
        # Check if proxy is existing.
        if not proxy_path.exists():
            # Call FFmpeg to transcode the file.
            subprocess.call(['ffmpeg', '-i', f'{film_scan}/%07d.jpg',proxy_path])

        # Generate path for expected mediainfo path.
        mediainfo_path = (film_scan.parents[1] / 'mediainfo' / f'{film_scan.stem}.json')
        # Make directory if it doesn't exist
        mediainfo_path.parents[0].mkdir(exist_ok=True)
        # If mediainfo report doesn't exist
        if not mediainfo_path.exists():
            # create report by calling mediainfo
            minfo = subprocess.check_output(['mediainfo', '--Output=JSON', proxy_path]).decode()
            # open mediainfo file
            with open(mediainfo_path, 'w') as f:
                # write report.
                f.write(minfo)

