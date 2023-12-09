.PHONY: all

all: run_game_parser run_random_forest run_random_forest_graph run_keras run_keras_executable run_keras_graph

run_game_parser:
	python3 game_parser.py

run_random_forest:
	cd random_forest && python3 random_forest.py

run_random_forest_graph:
	cd random_forest && python3 random_forest_graph.py

run_keras:
	cd keras && python3 keras.py || true

run_keras_executable:
	cd keras/__pycache__ && python3 keras.cpython-310.pyc

run_keras_graph:
	cd keras/__pycache__ && python3 keras_graph.py
