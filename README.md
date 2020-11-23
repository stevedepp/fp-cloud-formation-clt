to do:
- [ ] add CLT framework
- [ ] logs
- [ ] flask
- [ ] rename CLI functions
- [ ] rename CloudFormation
- [ ] pip's  --use-feature=2020-resolver **
- [ ] makes sure IAM policies are deleted when teardown occurs
- [ ] avoid screen popups and y/n when tearing down
	
## outline

### ```1-create-bucket.sh```

### ```2-build-layer.sh```

### ```./3-deploy.sh```

### ```4-init-data.sh```

### ```5-cleanip.sh```

### ```cfcli.py```

### ```ddb_init.py```

### ```ddb_items.py```

### ```template.yml```

### ```ServerlessProducer/lambda_function.py```

### ```producerAI/lambda_function.py```


## startup

### source .venv/bin/activate
### follow order of scripts


## architecture

### CLI Python modlue

### shell scripts

### DynamoDB table and items

### EventWatch timer

### Lambda function

### S3 bucket

### IAM role

### SQS queue

### Lambda function

### S3 bucket

### Comprehend

### S3 bucket



** 
ERROR: After October 2020 you may experience errors when installing or updating packages. This is because pip will change the way that it resolves dependency conflicts.

We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default.

requests 2.24.0 requires urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1, but you'll have urllib3 1.26.2 which is incompatible.
