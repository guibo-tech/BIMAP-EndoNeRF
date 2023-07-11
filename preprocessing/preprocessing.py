import subprocess

# Define the command lines
command1 = "python colmap2nerf.py --run_colmap --colmap_matcher exhaustive --aabb_scale 16 --overwrite"
command2 = "python cameraposes.py"
command3 = "python run.py --model_type dpt_beit_large_512 --input_path images --output_path depth --grayscale"

# Run the commands
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
# subprocess.run(command3, shell=True)