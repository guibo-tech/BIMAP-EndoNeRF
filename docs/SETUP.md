# Set up for EndoNeRF

## Introduction

**Nvidia Drive, Cuda and Torch installation guide**

A good guide, check it
https://github.com/mingyen066/Cuda-PyTorch-Installation-Guide

**Installing Nvidia drive**
https://www.youtube.com/watch?v=VP-R7LNSJXA

I read it is better to install the drive via SUDO, than downloading the drive from Nvidia homepage
check the drive for the GPU in the homepage: 
https://www.nvidia.com/download/index.aspx
then install via ubuntu terminal:
_sudo apt update
sudo apt upgrade
sudo ubuntu-drivers list
sudo apt install nvidia-driver-<version>_
than reboot system
_sudo reboot_

How to disable Secure Boot (Lenovo Legion 5 Pro), it was necessary to make Ubuntu identify the GPU
https://www.youtube.com/watch?v=n6OBZubyqmY

To check the cuda version for the Nvidia
https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

**Install cuda toolkit for the GPU**
Check what is the cuda version, download the correct one for GPU
https://developer.nvidia.com/cuda-toolkit-archive
commands:
$ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda_12.0.1_525.85.12_linux.run
$ sudo sh cuda_12.0.1_525.85.12_linux.run
or
make the downloaded CUDA toolkit package executable
chmod +x cuda_12.0.1_525.85.12_linux.run

Run the CUDA toolkit installation command with the appropriate options
sudo ./cuda_12.0.1_525.85.12_linux.run

While you are installing cuda, a prompt will be displayed, asking you whether to install "Driver", "CUDA Toolkit", "CUDA Samples",...
The "Driver" here means "Nvidia Graphics Driver"
Since we have already installed Driver in the previous step, do NOT install Driver (i.e., unselect Driver) 

**Add Cuda to Path**

This command will add the export PATH and export LD_LIBRARY_PATH lines to the end of the ~/.bashrc file.
After executing this command, the two lines will be appended to the ~/.bashrc file, which ensures that the CUDA binaries directory is added to the system's PATH and the CUDA library path is properly set.

_echo >> ~/.bashrc '
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64'_

for the changes to take effect in your current terminal session run
_source ~/.bashrc_ 

**Install CuDNN:**
Download from homepage with login (https://developer.nvidia.com/rdp/cudnn-download)
cudnn-local-repo-ubuntu2004-8.8.0.121_1.0-1_amd64.deb 

install command
_sudo dpkg -i cudnn-local-repo-ubuntu2004-8.8.0.121_1.0-1_amd64.deb_

To install the key, run this command:
sudo cp /var/cudnn-local-repo-ubuntu2004-8.8.0.121/cudnn-local-A9E17745-keyring.gpg /usr/share/keyrings/

No to the the path /var/cudnn-local-repo-ubuntu2004-8.8.0.121 open a terminal and install the 3 packages: 
_sudo dpkg -i libcudnn8_8.8.0.121-1+cuda12.0_amd64.deb
sudo dpkg -i libcudnn8-dev_8.8.0.121-1+cuda12.0_amd64.deb
sudo dpkg -i libcudnn8-samples_8.8.0.121-1+cuda12.0_amd64.deb_

Test Cudnn

Change the directory to: _cd /usr/src/cudnn_samples_v8/mnistCUDNN_
Clean the previous build: _sudo make clean_
Build the mnistCUDNN program: _sudo make_
Run the mnistCUDNN program: _./mnistCUDNN_

I got an error and needed to install freeimage library
_sudo apt-get install libfreeimage-dev_

Verify installation: After installing the FreeImage library, ensure that the FreeImage.h header file is available in a directory that is included in the compiler's search path. You can verify this by checking the following locations:
    /usr/include/
    /usr/local/include/

Repeat again the previous steps, it will run correctly and Test Passed for using Cudnn and Cuda.

**Install Pytorch by pip**
https://www.youtube.com/watch?v=c0Z_ItwzT5o

check command here, mark stable - linux - pip - Python - CUDA 11.7
There is no Pytorch for cuda 12.0, as I googled, the version Pythorch CUDA 11.7 works for CUDA 12.0
https://pytorch.org/get-started/locally/

pip3 install torch torchvision torchaudio

Check whether PyTorch, torchvision, torchaudio is installed:
$ python3
Python 3.8.10 (default, Mar 13 2023, 10:26:41) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import torch
>>> torch.rand(3)
tensor([0.6327, 0.5860, 0.3513])

>>> torch.cuda.is_available()
True
>>> torch.cuda.device_count()
1
>>> torch.cuda.current_device()
0
>>> torch.cuda.device(0)
<torch.cuda.device object at 0x7f86d8d4a7f0>
>>> torch.cuda.get_device_name(0)
'NVIDIA GeForce RTX 3060 Laptop GPU'

>>> print(torch.__version__)
2.0.1+cu117
>>> import torchvision
>>> print(torchvision.__version__)
0.15.2+cu117
>>> import torchaudio
>>> print(torchaudio.__version__)
2.0.2+cu117

**Install git**
_sudo apt update
sudo apt install git
git --version_

**Install Miniconda**
Dowload from homepage
https://docs.conda.io/en/latest/miniconda.html

_cd ~/Downloads
chmod +x Miniconda3-py38_23.3.1-0-Linux-x86_64.sh
./Miniconda3-py38_23.3.1-0-Linux-x86_64.sh_
close and open terminal 
_conda --version_

**Installing the requirements for the Project**
Delete these lines from the requirements.txt. It is better to use the torch, torchvision from the system level.
torch>=1.4.0
torchvision>=0.2.1

_cd EndoNeRF
to get the correct pytorch and cuda I needed to create environment with Python 3.8
conda create -n endonerf _2 python=3.8

conda create -n endonerf python=3.6
conda activate endonerf
pip install -r requirements.txt
cd torchsearchsorted
pip install .
cd .._

**torchsearchsorted package**
It is using data type long for numpy and torch. Numpy newer than 1.20 uses data type int64 instead.

NumPy versions prior to 1.20 used the data type 'long' to represent 64-bit integers. Starting from NumPy version 1.20, the 'long' data type was deprecated, and the equivalent data type 'int64' should be used instead.

If you specifically need to use the 'long' data type, you can install an older version of NumPy that supports it. Versions 1.19.x or earlier should have the 'long' data type available. For example, you can install NumPy version 1.19.5, which is the latest release in the 1.19.x series:

pip install numpy==1.19.5





**My last set up on my computer**

OS: Ubuntu 20.04.6 LTS
Processor: AMD® Ryzen 5 5600h with radeon graphics × 12 
Graphic processor: NVIDIA GeForce RTX 3060 Laptop GPU
Nvidia drive: 525.116.04, CUDA version: 12.0
CUDA Toolkit 12.0.1(January 2023), installed cuda_12.0.1_525.85.12_linux.run

CuDNN:
libcudnn8_8.8.0.121-1+cuda12.0_amd64.deb
libcudnn8-dev_8.8.0.121-1+cuda12.0_amd64.deb
libcudnn8-samples_8.8.0.121-1+cuda12.0_amd64.deb



Miniconda: Python 3.8 | Miniconda3 Linux 64-bit



Python 3.8 	[Miniconda3 Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh)

**Nividia drive**
![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/ae29257e-be2f-413a-86dc-6ad2d714ebac)


**CUDA**

![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/7513645a-de1e-4157-a79f-60cae7b4dbf5)


**Cudnn**

![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/75a1ef99-1276-4f0a-9613-353a47923cf4)


![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/bc1269c7-40fb-49e5-91be-a8f666280b20)


**Test passed for Cudnn**

![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/04a58802-e0eb-4255-a066-7180aa7cb5ca)


![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/b41e59b7-eee7-4c6b-a5d6-7d2f919c29ad)


**Pytorch, torchvision, torchaudio installed and tested for cuda**



![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/f5e4049c-b279-493a-a299-a9bfc616ed23)


**torchsearchsorted package**



benchmark.py

![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/923e1047-a82f-47ec-8a77-311f59c813ef)

test.py


![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/b0fbc048-23d9-4539-8d93-5deeecdf6fb0)


test_searchsorted.py

Sometimes all 324 tests passes, sometimes 1 fails, sometimes 2 fails.

![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/fc69154b-e66f-4175-8f38-94f5384d1f9a)




![Image](https://github.com/guibo-tech/BIMAP-EndoNeRF/assets/132677623/639d6108-1394-49c0-8b91-f07769b7b022)



**Installation torchsearchsorted**

Even with the environment pretty well set up, it failed to install it with CUDA 12.0, due mismatch cuda 12.0 in system with Pytorch CUDA 11.7

I create env endonerf_2 python 3.8 and downgraded the CUDA 12.0 in system to the same version as PyTorch Cuda 11.7. Also installed Cudnn for cuda 11x

Is the Cuda 11.7 suitable for Geforce RTX 3060?

Yes, it worked and I could install the package downgrading to CUDA 11.7
But this package seems deprecated

