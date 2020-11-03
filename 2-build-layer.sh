#!/bin/bash
set -eo pipefail
rm -rf packageServerlessProducer
rm -rf packageProducerAI
pip install --target ./packageServerlessProducer/python -r ./ServerlessProducer/requirements.txt
pip install --target ./packageProducerAI/python -r ./ProducerAI/requirements.txt
