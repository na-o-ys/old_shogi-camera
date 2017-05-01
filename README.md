# System Requirements

## To execute on host machine

- Tensorflow
- Keras 2

## To execute on GPU container

Host machine requirements.

- AWS p2 instance
    - Ubuntu Server 16.04 LTS (HVM), SSD Volume Type
    - Disk: 100 GB SSD
    - GPU: NVIDIA Tesla K80
- CUDA Toolkit / CUDA Driver
- Docker Engine
- nvidia-docker

## To execute on noGPU container

- Docker Engine

# Run app

```
$ python3 cli.py
```

# Run Jupyter Notebook

GPU container

```
$ make notebook
```

noGPU container

```
$ NOGPU=1 make notebook
```

# (Optional) Build Containers

## GPU container

```
$ cd containers/gpu && docker build .
```

or

```
$ make build
```

## noGPU container

```
$ cd containers/nogpu && docker build .
```

or 

```
$ make build-nogpu
```
