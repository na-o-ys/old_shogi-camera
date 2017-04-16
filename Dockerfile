From ubuntu:16.04

RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y python3-dev python3-numpy git wget sudo

RUN git clone https://github.com/jayrambhia/Install-OpenCV.git && \
    cd Install-OpenCV/Ubuntu && \
    ./opencv_latest.sh

WORKDIR /app

RUN apt-get install -y python-pip python3-pip
RUN pip3 install scipy scikit-learn pandas matplotlib jupyter
