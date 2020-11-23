## to do:
- [ ] add CLT framework
- [ ] logs
- [ ] flask to see the output in a webpage with json pretty
- [ ] rename CLI functions
- [ ] add functionality to append names after cf complete
- [x] rename CloudFormation from blank-python
- [x] rename LambdaRoles to specific from generic names
- [x] pip's  --use-feature=2020-resolver **
- [x] makes sure IAM policies are deleted when teardown occurs
- [ ] avoid screen popups and y/n when tearing down
- [ ] if add flask, the note below about request lib may cause fail



## outline:

### ```1-create-bucket.sh```

### ```2-build-layer.sh```

### ```3-deploy.sh```

### ```4-init-data.sh```

### ```5-cleanip.sh```

### ```cfcli.py```

### ```ddb_init.py```

### ```ddb_items.py```

### ```template.yml```

### ```ServerlessProducer/lambda_function.py```

### ```producerAI/lambda_function.py```

### ```make```

#### setup
#### install
#### bucket



## startup:

### source .venv/bin/activate
### follow order of scripts



## architecture:

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



## notes:

-   pip message: --use-feature=2020-resolver? error message with jupyter installation on ubuntu
https://stackoverflow.com/questions/63277123/what-is-use-feature-2020-resolver-error-message-with-jupyter-installation-on

-   requests 2.24.0 requires urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1, but you'll have urllib3 1.26.2 which is incompatible.
