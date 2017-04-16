notebook:
	docker run -v $(PWD):/app -p 8888:8888 -e "JUPYTER_CONFIG_DIR=/app/jupyter" -it naoys/shogi-camera jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
