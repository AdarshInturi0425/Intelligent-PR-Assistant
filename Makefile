test:
	python3 -m unittest discover tests

run:
	python3 main.py

clean:
	rm -rf src/__pycache__ tests/__pycache__ .pr_cache.json