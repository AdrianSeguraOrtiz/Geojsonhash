install:
	@poetry install

clean:
	@rm -rf build dist .eggs *.egg-info
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +

black: clean
	@poetry run isort --profile black geojsonhash/
	@poetry run black geojsonhash/

lint:
	@poetry run mypy geojsonhash/

release:
	@echo Bump version to v$$(poetry version --short)
	@git tag v$$(poetry version --short)
	@git push origin v$$(poetry version --short)

.PHONY: tests

tests:
	@poetry run pytest -s tests/ --quiet
