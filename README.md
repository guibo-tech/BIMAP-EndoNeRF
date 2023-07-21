# BIMAP-EndoNeRF

## Introduction
This project uses endoscopy images to generate a 3D reconstruction of the inside of the human body. This is done by using the endoscope's position and orientation as input to the NeRF network, along with the 2D images captured by the endoscope, and their corresponding depth maps. The NeRF network then generates a dynamic 3D model of the internal structure of the body that matches the captured images.


## Project Structure

```
BIMAP-EndoNeRF/
├── docs/                               # documentation
├── EndoNeRF/                            # A NeRF-based framework for Endoscopic Scene Reconstruction (EndoNeRF)
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
│   ├── masks/           # only for EndoNeRF, create a mask images in black (same dimension as the RGB image input)
│   ├── gt_masks/        # only for EndoNeRF, create a mask images in black (same dimension as the RGB image input)
│   └── poses_bound.npy
```

## Point Cloud Reconstruction - EndoNeRF

0. Config file


Edit the configs/example.txt
Example
```shell
expname = reco_0003_training_2
datadir = ../reco_0003/
```

1. Training


Type the command below to train the model:

```shell
export CUDA_VISIBLE_DEVICES=0   # Specify GPU id
python run_endonerf.py --config configs/{your_config_file}.txt
```

Example
```shell
export CUDA_VISIBLE_DEVICES=0
python run_endonerf.py --config configs/oral2.txt --no_mask_raycast --no_depth_refine
```
We put an example of the config file in configs/example.txt. The log files and output will be saved to logs/{expname}, where expname is specified in the config file.

2. Reconstruction


After training, type the command below to reconstruct point clouds from the optimized model:

```shell
python endo_pc_reconstruction.py --config_file configs/{your_config_file}.txt --n_frames {num_of_frames} --depth_smoother --depth_smoother_d 28
```

Example
```shell
python3 endo_pc_reconstruction.py --config_file configs/oral2.txt --n_frames 45 --depth_smoother --depth_smoother_d 28
```
The reconstructed point clouds will be saved to logs/{expname}/reconstructed_pcds_{epoch}. For more options of this reconstruction script, type python endo_pc_reconstruction.py -h.

3. Visualization


We also build a visualizer to play point cloud animations. To display reconstructed point clouds, type the command as follows.

```shell
python pc_visualizer.py --pc_dir logs/{expname}/reconstructed_pcds_{epoch}
```
Example
```shell
python3 pc_visualizer.py --pc_dir logs/reco_0003_training_2/reconstructed_pcds_100000
```
Type python pc_visualizer.py -h for more options of the visualizer.

