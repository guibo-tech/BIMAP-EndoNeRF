import subprocess
import sys

# Define the command lines
command1 = "python campose_helper/colmap2nerf.py --run_colmap --colmap_matcher exhaustive --aabb_scale 16 --overwrite"
command2 = "python campose_helper/cameraposes.py"
command3 = "python depth_helper/run.py --model_type dpt_large_384 --input_path images --output_path depth --grayscale"

# Run the commands
print('Running COLMAP...')
subprocess.run(command1, shell=True)
print('Extracting poses in LLFF format from COLMAP...')
try:
    subprocess.run(command2, shell=True)
except subprocess.CalledProcessError as e:
    print("COLMAP failed for this set of frames. Please, try again with the same set or a different one. Options:\n\
          1. Run vid2frames.py and a try completely new interval. \n\
          2. Run vid2frames.py and try a longer interval. \n\
          3. Delete some frames of this set that are too similar. ")
    sys.exit(1)
print('Creating depth maps...')
subprocess.run(command3, shell=True)