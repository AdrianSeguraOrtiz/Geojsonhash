install:
	@poetry install

clean:
	@rm -rf build dist .eggs *.egg-info
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +

black: clean
	@poetry run isort --profile black *.py
	@poetry run black *.py

lint:
	@poetry run mypy geojsonhash/

release:
	@echo Bump version to v$$(poetry version --short)
	@git tag v$$(poetry version --short)
	@git push origin v$$(poetry version --short)

.PHONY: tests

tests:
	@poetry run python -m unittest discover -s tests/ --quiet