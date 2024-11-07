import os
import shutil
import time

def archive_old_files(directory, archive_folder, days=30):
    now = time.time()
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.stat(file_path).st_mtime < now - days * 86400:
            shutil.move(file_path, archive_folder)

archive_old_files('/path/to/logs', '/path/to/archive')
