#!/usr/bin/python3 -u
import argparse
import os
import secrets
import time

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="path to write", required=True)
parser.add_argument("--filesize", type=int, help="file size to write", required=True)
parser.add_argument("--folders", type=int, help="number of folders", default=50)
parser.add_argument("--files", type=int, help="number of files per folder", default=100)
args = parser.parse_args()

file_size = args.filesize
folders = args.folders
files_per_folder = args.files
base_path = args.path

file_data = secrets.token_bytes(file_size)
folder_i = 0

start_time = time.time()
last_time = time.time()
for folder_i in range(folders):
  os.mkdir(f"{base_path}/d{folder_i}")

  for file_i in range(files_per_folder):
    filename = f"{base_path}/d{folder_i}/f{folder_i}-{file_i}.dat"
    with open(filename, 'wb') as f:
      f.write(file_data)

  this_time = time.time()
  speed = file_size * files_per_folder / (this_time - last_time) / 1024 / 1024
  print(f"{speed:.2f} MB/s {base_path}/d{folder_i}")
  last_time = this_time

os.sync()
print(f"os.sync took {time.time() - last_time:.2f} seconds")

end_time = time.time()
average_speed = file_size * files_per_folder * folders / (end_time - start_time) / 1024 / 1024
print(f"File size: {file_size} bytes")
print(f"Total bytes written: {file_size * files_per_folder * folders / 1024 / 1024 / 1024:.2f} GB")
print(f"Total time {end_time - start_time:.2f}s")
print(f"Average speed {average_speed:.2f} MB/s")
