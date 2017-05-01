ifdef NOGPU
	DOCKER_CMD = docker
	DOCKER_TAG = nogpu
else
	DOCKER_CMD = nvidia-docker
	DOCKER_TAG = latest
endif

build:
	cd containers/gpu && docker build -t naoys/shogi-camera:latest .
build-nogpu:
	cd containers/nogpu && docker build -t naoys/shogi-camera:nogpu .
extract_board:
	$(DOCKER_CMD) run -v $(PWD):/app -it naoys/shogi-camera:$(DOCKER_TAG) python3 extract_board.py $(IMG)
read_koma:
	$(DOCKER_CMD) run -v $(PWD):/app -it naoys/shogi-camera:$(DOCKER_TAG) python3 learn/read_koma.py
notebook:
	$(DOCKER_CMD) run -v $(PWD):/app -p 8888:8888 -e "JUPYTER_CONFIG_DIR=/app/jupyter" -it naoys/shogi-camera:$(DOCKER_TAG) jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
