#!/bin/bash
if [ -z "$NOGPU" ]; then
  DOCKER_TAG=latest
  DOCKER_CMD=nvidia-docker
else
  DOCKER_TAG=nogpu
  DOCKER_CMD=docker
fi

$DOCKER_CMD run -it -v $PWD:/app naoys/shogi-camera:$DOCKER_TAG python3 cli.py $@
