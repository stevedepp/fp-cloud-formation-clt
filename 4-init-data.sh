#!/bin/bash

./ddb_init.py
aws dynamodb batch-write-item --request-items file://text.json
