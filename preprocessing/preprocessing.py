import subprocess
import sys

# Define the command lines
command1 = "python campose_helper/colmap2nerf.py --run_colmap --colmap_matcher exhaustive --aabb_scale 16 --overwrite"
command2 = "python campose_helper/cameraposes.py"
command3 = "python depth_helper/run.py --model_type dpt_large_384 --input_path images --output_path depth --grayscale"
command4 = "python image_resizer.py"

# Run the commands
print('Running COLMAP...')
subprocess.run(command1, shell=True)
print('Extracting poses in LLFF format from COLMAP...')
subprocess.run(command2, shell=True)
print('Creating depth maps...')
subprocess.run(command3, shell=True)
print('Resizing if required...')
subprocess.run(command4, shell=True)