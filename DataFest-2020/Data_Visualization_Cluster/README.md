## [DataFest 2020](https://projects.iq.harvard.edu/datafest2020/schedule)

### [Session Title](https://harvarddatafest2020.sched.com/event/YNuw/data-intensive-non-linear-dimensionality-reduction-and-visualization-t-sne-pca-using-notebooks-on-cluster-gpu-cpu-implementations?iframe=yes&w=100%&sidebar=yes&bg=no)
Data Intensive (Non)-Linear Dimensionality Reduction and Visualization (T-SNE & PCA) Using Notebooks on Cluster: GPU & CPU Implementations)

### Download Datasets
[Dropbox Link](https://www.dropbox.com/sh/jnqak5qhxol0zig/AABizfe1vaCbqSF1FjJmWZNya?dl=0)

You can check the structure of an HDF5 file in [HDF View Software](https://www.hdfgroup.org/downloads/hdfview/). The software is available for free by [The HDF Group](https://www.hdfgroup.org/downloads/hdfview/).


### Setup instructions

1. Install Anaconda 3: [Windows](https://www.anaconda.com/distribution/#windows), [macOS](https://www.anaconda.com/distribution/#macos), [Linux](https://www.anaconda.com/distribution/#linux)

If you are using FASRC CANNON cluster, load Anaconda 3 module by the following command in the terminal,

```sh
module load Anaconda3
```

2. Create a conda environment with Python 3.7.

```sh
conda create -n datafest python=3.7
source activate datafest
```

3. Install required modules to run the Jupyter notebook. Make sure you are targeting the correct environment by checking its path with `which conda` command in Linux.

```sh
pip install ipynb
pip install h5py
pip install sklearn
pip install matplotlib
pip install numpy
```

If you are using GPU power of your personal laptop to test the notebook, you need to install Jupyter notebook as well,

```sh
pip install jupyter
```

We will test t-SNE GPU implementation by Nvidia (RAPIDS). The installation by conda is listed in this [URL](https://rapids.ai/start.html#rapids-release-selector). We need cuML but can get all packages if interested. The command for all packages, Python 3.7, CUDA 10.0, and Stable version in Conda is:


```sh
conda install -c rapidsai -c nvidia -c conda-forge -c defaults rapids=0.11 python=3.7
```

Feel free to change the above command if you are using a different version of Python or CUDA version. Check the [RAPIDS start page](https://rapids.ai/start.html) to find out about the prerequisites. The supported operating systems for RAPIDS are `Ubuntu 16.04/18.04 or CentOS 7 with gcc 5.4 & 7.3`.

For parallel CPU implementation of t-SNE technique, we will test the [MulticoreTSNE](https://github.com/DmitryUlyanov/Multicore-TSNE) package. We can install it by the following `pip` command,

```sh
pip install MulticoreTSNE
```

4. If you are using the [OpenDemand](https://vdi.rc.fas.harvard.edu) interactive interface on FASRC CANNON cluster, make sure to activate `fasrc` [VPN](https://www.rc.fas.harvard.edu/resources/vpn-setup/) before launching the portal.

5. If on OpenDemand portal, check [SLURM partitions](https://www.rc.fas.harvard.edu/resources/running-jobs/#Slurm_partitions) to request a CPU or GPU partition that fits your need.
