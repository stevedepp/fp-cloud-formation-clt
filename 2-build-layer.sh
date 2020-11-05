#!/bin/bash
set -eo pipefail
rm -rf packageServerlessProducer
rm -rf packageProducerAI
pip install --target ./packageServerlessProducer/python -r ./ServerlessProducer/requirements.txt
pip install --target ./packageProducerAI/python -r ./ProducerAI/requirements.txt


rm -rf ./packageProducerAI/python/pandas
rm -rf ./packageProducerAI/python/numpy

curl -O https://files.pythonhosted.org/packages/e6/de/a0d3defd8f338eaf53ef716e40ef6d6c277c35d50e09b586e170169cdf0d/pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl
curl -O https://files.pythonhosted.org/packages/f5/bf/4981bcbee43934f0adb8f764a1e70ab0ee5a448f6505bd04a87a2fda2a8b/numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl

unzip pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl -d packageProducerAI/python/
unzip numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl -d packageProducerAI/python/

rm -r packageProducerAI/python/__pycache__
rm -r packageProducerAI/python/*.dist-info

rm pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl
rm numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl
