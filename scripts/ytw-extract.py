import os
import sys

data_path = sys.argv[1]

os.system('python ./scripts/extract.py '+str(data_path)+'/yt-walking/')
