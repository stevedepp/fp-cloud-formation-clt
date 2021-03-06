setup:
	python3 -m venv .venv

env:
	which python3
	python3 --version
	which pytest
	which pylint

install:
	python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt

bucket:
	./1-create-bucket.sh

build:
	./2-build-layer.sh

deploy: 
	./3-deploy.sh

data:
	./.unused/4-init-data.sh

infra: install bucket build deploy

teardown:
	./5-cleanup.sh

lint:
	pylint --load-plugins pylint_flask --disable=R,C flask_app/*.py nlib csvcli

test:
	@cd tests; pytest -vv --cov-report term-missing --cov=web --cov=nlib test_*.py

all: install infra lint test
