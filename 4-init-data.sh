#!/bin/bash

./ddb_init.py > request.json
aws dynamodb batch-write-item --request-items file://request.json
rm request.json
