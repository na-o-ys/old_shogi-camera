# System Requirements

## To execute on a native machine

- Python 3.5
- Keras 2
- Tensorflow 1.1.0
- scipy, numpy, scikit-learn
- hdf5, h5py

## To execute on a Docker container (without GPU)

- Docker Engine

## To execute on a GPU container

Docker host requirements. (made for AWS p2 instance)

- GPU (NVIDIA Tesla K80)
- CUDA Toolkit / CUDA Driver
- Docker Engine
- nvidia-docker

# Quick Start

```
$ python3 cli.py
```

or execute on a Docker container,

```
$ NOGPU=1 ./run
```

# Build Containers

## GPU container

```
$ make build
```

## noGPU container

```
$ make build-nogpu
```
