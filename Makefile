setup:
	python3 -m venv .venv

install:
	pip install -r requirements.txt 

bucket:
	./1-create-bucket.sh

build:
	./2-build-layer.sh

deploy: 
	./3-deploy.sh

data:
	./4-init-data.sh

infra: bucket build deploy data

teardown:
	./5-cleanup.sh

env:
	which python3
	python3 --version
	which pytest
	which pylint

lint:
	pylint --load-plugins pylint_flask --disable=R,C flask_app/*.py nlib csvcli

test:
	@cd tests; pytest -vv --cov-report term-missing --cov=web --cov=nlib test_*.py

qall: install lint test
