#!/bin/bash
docker run -it -v $PWD:/app naoys/shogi-camera:nogpu python3 cli.py $@
