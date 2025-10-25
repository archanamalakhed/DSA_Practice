import sys
from pathlib import Path
if len(sys.argv) >=2:
    file_path = Path(sys.argv[1])
    print(f'you have passed this file name {file_path}')
else:
    print("No file path is given")
