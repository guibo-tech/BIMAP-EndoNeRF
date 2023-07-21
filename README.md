# BIMAP-EndoNeRF

## Introduction
This project uses endoscopy images to generate a 3D reconstruction of the inside of the human body. This is done by using the endoscope's position and orientation as input to the NeRF network, along with the 2D images captured by the endoscope, and their corresponding depth maps. The NeRF network then generates a dynamic 3D model of the internal structure of the body that matches the captured images.


## Project Structure

```
BIMAP-EndoNeRF/
├── docs/                               # documentation
├── preprocessing/
│   ├── camposes_helper/                # required code to obtain cameraposes
│   │    ├── colmap_read_model.py
│   │    ├── colmap_wrapper.py
│   │    ├── colmap2nerf.py
│   │    ├── pose_utils.py
│   │    ├── cameraposes.py
│   ├── depth_helper/                   # required code to obtain depth maps
│   │    ├── midas/
│   │    ├── weights/                   # include here the downloaded torch model
│   │    ├── run.py
│   │    ├── utils.py
│   ├── preprocessing.py                # code to obtain poses and depth maps
│   ├── vid2frames.py                   # code to split the videos in frames
├── environment.yaml                    # Environment with required python packages
├── .gitignore                          # files and directories ignored by Git
├── LICENSE                             # license agreement
├── gltf2ply.py                         # transform gltf file to ply
├── vc_segmenter.py                     # vocal cord segmenter
├── pc_visualizer.py                    # visualizer to play point cloud animations
└── README.md                           # instructions for installation and usage
```

Download torch model in weights folder: [dpt_large_384](https://github.com/isl-org/MiDaS/releases/download/v3/dpt_large_384.pt)

## Usage

1. Video to images. The only required argument is --video_path. Look at code documentation to get the rest of arguments.

```shell
python vid2frames.py --video_path VIDEO_PATH.mp4
```

2. Obtaining camera poses and depth maps.

```shell
python preprocessing.py
```

5. Create folder "data":

```
BIMAP-EndoNeRF/
├── data/
│   ├── images/
│   ├── depth/
│   └── poses_bound.npy
```

6. 
