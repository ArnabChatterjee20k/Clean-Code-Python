PYTHON=python3.9

.PHONY: typehint
typehint:
	mypy --ignore-missing-imports src/

.PHONY: test
test:
	echo "No echo test found"

.PHONY: lint
lint:
	pylint src/

.PHONY: checklist
checklist: lint typehint test

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr