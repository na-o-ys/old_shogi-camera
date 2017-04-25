extract_board:
	docker run -v $(PWD):/app -it naoys/shogi-camera python3 extract_board.py $(IMG)
read_koma:
	docker run -v $(PWD):/app -it naoys/shogi-camera python3 learn/read_koma.py
notebook:
	docker run -v $(PWD):/app -p 8888:8888 -e "JUPYTER_CONFIG_DIR=/app/jupyter" -it naoys/shogi-camera jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
