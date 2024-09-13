import pathlib
for filename in ['0086400.dpx', 'not_a_file.dpx']:
    pathlib_filename = pathlib.Path.cwd() / 'media' / 'dpx' / filename
    if pathlib_filename.exists():
        print(pathlib_filename, 'THE FILE EXISTS, HOORAY')
    else:
        raise Exception('WHERE IS FILE', pathlib_filename)
