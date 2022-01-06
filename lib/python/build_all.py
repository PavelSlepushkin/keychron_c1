import subprocess
import os
import sys

BOARDS = [
    'keychron/k2/rgb',
    'keychron/k2/rgb/via',
    'keychron/k2/rgb/optical',
    'keychron/k2/rgb/optical_via']

error = False
for kb in BOARDS:
    if subprocess.run(f"qmk compile -kb {kb} -km all -j{os.cpu_count()}", shell=True).returncode != 0:
        error = True
if error:
    sys.exit(1)
