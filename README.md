# Serverless AI Data Engineering Pipeline
building serverless pipeline from dynamo db to lambda to sqs to lambda to aws comprehend to s3 

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/101269508-893de600-373d-11eb-9d52-a393e4070d67.png">

### quickstart commands

- [x] getting coing:

        mkdir folder_name
        cd folder_name
        git clone https://github.com/stevedepp/fp-cloud-formation-clt.git
        cd fp-cloud-formation-clt
        python3 -m venv .venv
        source .venv/bin/activate
        make install
        
- [x] building infrastructure

        ./cfcli.py make-infra


- [x] some database operations

    - [x] adding names
    
        ./cfcli.py add --file ./cos.txt
        ./cfcli.py add -f ./cos.txt  
        ./cfcli.py add -item ibm -item microsoft
        ./cfcli.py add -i ibm -i microsoft

    - [x] removing names
    
        ./cfcli.py remove --file cos.txt
        ./cfcli.py remove --f cos.txt
        ./cfcli.py remove -item amazon -item google
        ./cfcli.py remove -i amazon -i google

    - [x] updating a database name

        ./cfcli.py update -old netflix -new Netflix
        ./cfcli.py update -o netflix -n Netflix

- [x] tearing it down:

        ./cfcli.py teardown 
        
        

## architecture diagram

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
