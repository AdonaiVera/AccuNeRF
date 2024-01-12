<div align="center">
  <a href="https://www.mit.edu/~arosinol/">
    <img align="right" src="./media/logo_iubh.jpg" width="100" alt="mit">
  </a>
</div>

<p align="center">
  <div align="center">
    <h1>AccuNeRF</h1>
  </div>
  <h1 align="center">
  ACCURATE 3D ACCIDENT RECONSTRUCTION USING NEURAL RADIANCE FIELDS</h1>
  <p align="center">
    <a href="https://www.adonaivera.com/"><strong>ADONAI VERA</strong></a>
    ·
    <a href="https://www.iu.de/hochschule/lehrende/grasnick-armin/"><strong>PROF. DR. ARMIN GRASNICK</strong></a>
  </p>
  <!-- <h2 align="center">In Review</h2> -->
  <h3 align="center">
    <a href="https://arxiv.org/abs/">Paper</a> |
    <a href="https://www.youtube.com/">Video</a> |
    <!-- <a href="">Project Page</a>-->
  </h3>
  <div align="center"></div>
</p>
<p align="center">
  <a href="#">
    <img src="./media/reconstruction_1.png" alt="" width="90%">
  </a>
</p>

<details open="open" style='padding: 10px; border-radius:5px 30px 30px 5px; border-style: solid; border-width: 1px;'>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#install">Install</a>
    </li>
    <li>
      <a href="#download-sample-data">Download Datasets</a>
    </li>
    <li>
      <a href="#run">Run</a>
    </li>
    <li>
      <a href="#citation">Citation</a>
    </li>
    <li>
      <a href="#license">License</a>
    </li>
    <li>
      <a href="#acknowledgments">Acknowledgments</a>
    </li>
    <li>
      <a href="#contact">Contact</a>
    </li>
  </ol>
</details>

## Install

Clone repo with submodules:
```
git clone https://github.com/AdonaiVera/AccuNeRF.git --recurse-submodules
git submodule update --init --recursive
```

Create a virtualenv 
```
conda env create --file environment.yml
conda activate accunerf
```


## Download Sample Data

pending

## External modules

git submodule add https://github.com/colmap/colmap colmap
git submodule add https://github.com/nerfstudio-project/nerfstudio nerfstudio
git submodule add https://github.com/LAStools LAStools


## Train your own data


## Run

EXPERIMENT=AccuNerf_2
GROUP=AccuNerf_2_group
NAME=AccuNerf_2
CONFIG=projects/neuralangelo/configs/custom/${EXPERIMENT}.yaml
GPUS=1  # use >1 for multi-GPU training!
torchrun --nproc_per_node=${GPUS} train.py \
    --logdir=logs/${GROUP}/${NAME} \
    --config=${CONFIG} \
    --show_pbar \
    --data.readjust.scale=0.5 \
    --max_iter=10000 \
    --validation_iter=99999999 \
    --model.object.sdf.encoding.coarse2fine.step=200 \
    --model.object.sdf.encoding.hashgrid.dict_size=19 \
    --optim.sched.warm_up_end=200 \
    --optim.sched.two_steps=[12000,16000]


CHECKPOINT=logs/${GROUP}/${NAME}/epoch_01555_iteration_000420000_checkpoint.pt
OUTPUT_MESH=logs/${GROUP}/${NAME}/neurangelo_result_2.ply
CONFIG=logs/${GROUP}/${NAME}/config.yaml
RESOLUTION=2048 # 300
BLOCK_RES=128
GPUS=1  # use >1 for multi-GPU mesh extraction
torchrun --nproc_per_node=${GPUS} projects/neuralangelo/scripts/extract_mesh.py \
    --config=${CONFIG} \
    --checkpoint=${CHECKPOINT} \
    --output_file=${OUTPUT_MESH} \
    --resolution=${RESOLUTION} \
    --block_res=${BLOCK_RES} \
    --textured

## Citation 📦


# Install Potree
# Install Nerfstudio
# Install colmap
git clone https://github.com/colmap/colmap
cd colmap
mkdir build
cd build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=all -GNinja
ninja
sudo ninja install


# Install potree convert and add automatic step.




# Install Potree convert
sudo apt-get install python-software-properties git
sudo apt-get install build-essential cmake g++
sudo apt-get install libboost-all-dev
sudo apt-get install cmake-curses-gui
sudo apt-get install gcc

LAS Tools
git clone https://github.com/m-schuetz/LAStools.git
cd LAStools/LASzip
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make

Potre Converter
git clone https://github.com/potree/PotreeConverter.git
cd PotreeConverter
mkdir build && cd build

# Change for the path that you have in local
sudo cmake -DCMAKE_BUILD_TYPE=Release -DLASZIP_INCLUDE_DIRS=/home/ado/Documents/potree/LAStools/LASzip/dll -DLASZIP_LIBRARY=/home/ado/Documents/potree/LAStools/LASzip/build/src/liblaszip.so ..
sudo make && sudo make install
sudo ln -s ~/LAStools/LASzip/build/src/liblaszip.so /usr/lib
PotreeConverter -h


./PotreeConverter/build/PotreeConverter  "/home/ado/Documents/potree/pointclouds/base_accunerf/point_cloud.ply" -o  "/home/ado/Documents/potree/pointclouds/base_accunerf/results"
/home/ado/Documents/potree/pointclouds/base_accunerf


PotreeConverter_linux_x64/PotreeConverter  "/home/ado/Documents/potree/pointclouds/base_accunerf/point_cloud.ply" -o  "/home/ado/Documents/potree/pointclouds/base_accunerf/results"
PotreeConverter_linux_x64



apt-get update && apt-get install -y \
    cmake g++ git libtbb-dev libtbb-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN git clone https://github.com/potree/PotreeConverter.git

# PotreeConverter
#  6cd121bc92b279461dd4116283939ae0067f4aa1 = version 2.1
#  d9387d52807bf8936fe98096b9992ea13b50ba94 = latest develop Dec 2, 2022
RUN cd PotreeConverter && git checkout d9387d52807bf8936fe98096b9992ea13b50ba94 && mkdir build && cd build && \
    cmake ../ && \
    make

## License 📌

Pending to ADD

## Acknowledgments 🤓

Based on [NeRF++ codebase](https://github.com/Kai-46/nerfplusplus) and inherits the same training data preprocessing and format.

## Build with 🛠️
_Mention the tools you used to create your project_

Pending to add

## Contact 🎁

If you are interested in building on top of this, feel free to reach out :) 
* **Adonai Vera** - *AI developer Geta Club* - [AdonaiVera](https://github.com/AdonaiVera)
