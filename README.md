# BIMAP-EndoNeRF

## Introduction
This project uses endoscopy images to generate a 3D reconstruction of the inside of the human body. This is done by using the endoscope's position and orientation as input to the NeRF network, along with the 2D images captured by the endoscope. The NeRF network then generates a 3D model of the internal structure of the body that matches the captured images.


## Project Structure

Prepare a data directory organized in the following structure:

```
BIMAP-EndoNeRF/
├── data/
│   ├── video/                # raw video
│   ├── images/               # raw rgb images
│   ├── images_pp/            # preprocessed images
│   ├── depth/                # depth images
│   ├── depth_seg/            # depth images + vocal cord segmentation
│   ├── pc_gltf               # point cloud gltf format
│   ├── pc_ply                # point cloud ply format
│   └── poses_bounds.npy      # camera poses & intrinsics in LLFF format
├── data_source/              # data set examples, backup tests, etc
│   ├── dataset/
│   └── tests/
├── docs/                     # documentation 
├── requirements.txt          # Python packages
├── .gitignore                # files and directories ignored by Git
├── LICENSE                   # license agreement
├── vid2frames.py             # generate frames from a video
├── gltf2ply.py               # transform gltf file to ply
├── vc_segmenter.py           # vocal cord segmenter
├── pc_visualizer.py          # visualizer to play point cloud animations
└── README.md                 # instructions for installation and usage

```

## Steps (14.06.2023)

1. Video to images (frames), select sharp images, select images where the camera position is similar. illumination.

python script to automatize

2. Colmap (important that output includes "sparse" and "images" folders)

run this line in conda environment ngp in the directory where the folder "images" is

python C:\<pathto>\instant-ngp\scripts\colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 16 --overwrite

3. Generate poses_bounds.npy

run the function gen_poses(dir_sparse_images) that is in path: C:\<pathto>\LLFF\llff\poses\pose_utils.py (cloned GitHub repository)

4. Extract depth maps with MIDAS (CUDA workstation) cloned GitHub repository

include in folder input the images used for colmap

in conda environment midas-py310:

python run.py --model_type dpt_beit_large_512 --input_path input --output_path output --grayscale

5. Create folder with folders:
- poses_bounds.py
- images
- depth



## Git - Tagging
Proper Tag usage is important for self-documenting commits that introduce, improve, or fix features. This will make semantic versioning much easier.
If necessary, in addition to the tag, include the card issue number.

[FEATURE]: A feature or functionality has been developed for the first time.

[IMPROVE]: Existing correct functionality has been improved.

[FIX]: Existing incorrect code has been fixed.

[TESTS]: A commit concerns test coverage or functionality only.

[CHORE]: Something that is not a feature, fix, improvement, test, release or pipeline commit. For example, a code style cleanup.

[CLEANUP]: To clean up redundant or outdated files.

[STYLE]: For commits regarding the style guidelines.

[MISC]: A general miscellaneous type of changes which does not lie in any of other categories.

[REPOSITORY]: When changes are related to repository structure and settings, creating tags, branches, shelves, folders and etc.

[RELEASE]: When a new installer version is created or anything for the Project release version (i.e. documentation, ...) was changed.

