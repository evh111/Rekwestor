import os, subprocess

# Converts the provided input file into an '.mp3' file.
def convert_to_mp3(in_file, out_title):

    # Extract file/path information.
    in_path = os.path.dirname(in_file)

    # Convert the file to '.mp3' format.
    subprocess.run([
        'ffmpeg',
        '-i', in_file,
        os.path.join(in_path, out_title + '.mp3')
    ])