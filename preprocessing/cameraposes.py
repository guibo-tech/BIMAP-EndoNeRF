import numpy as np
from pose_utils import gen_poses
import os
os.rename('colmap_sparse', 'sparse')

# Get the absolute path of the script
script_path = os.path.abspath(__file__)

# Extract the directory name
script_directory = os.path.dirname(script_path)

# Call the function with the current directory
gen_poses(script_directory)

poses = np.load('poses_bounds.npy')

print(poses.shape)

    
for item in poses:
    item[0:4] = [1,0,0,0]
    item[5:9] = [0,1,0,0]
    item[10:14] = [0,0,1,0]
    item[15] = 0

for i, item in enumerate(poses):
    if item[-1]>500:
        print(i)

os.remove('poses_bounds.npy')
np.save('poses_bounds.npy',poses)