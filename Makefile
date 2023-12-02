install:
	poetry install

# test:
# 	poetry run pytest

# test-coverage:
# 	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 .

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	rm -rf dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build

diff-json:
	poetry run gendiff -- fixtures/file1.json fixtures/file2.json
