# title
building ser...

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/101269508-893de600-373d-11eb-9d52-a393e4070d67.png">

### quickstart commands

- [x] **week 4:** cloud9 + aws management console for: 
  - [x] success: sqs queue, dynamo db, lambda, iam policies, s3 bucket 
  - [x] 24 mins 35 seconds
  - [x] challenge is time to build slowing evolution 
  
- [x] **week 5:** AWS serverless application model (SAM) 
  - [x] python SDK for cloud formation
  - [x] sqs queue, dynamo db, lambda, iam policies, s3 bucket 
  - [x] succes: 3 minutes 17 seconds to build
  - [x] challenge: getting one resource to see another
  
- [x] **week 7:** cloud formation via templates
  - [x] success: easier to code and visualize solution structure
  - [x] challenge: lambda dependencies

- [x] **week 8:** lambda layers
  - [x] 4 minutes 45 seconds to build  
  - [x] success: lambda layers for dependencies
  - [x] challenge: 
  
- [x] **week 9** CLT for db operations
  - [x] CLT adds, deletes, updates in item or batch format
  - [x] AWS comprehend has carte blanche priveleges 

## architecture diagram

## evolution
- [x]

## to do:
- [x] encryption in transit
- [x] code in github
- [x] automate dependencies
- [x] principle of least privelege via tightened IAM roles' policies
- [ ] email notifications
- [x] cicd via infrastructure as code
- [x] infrastructure as code logging via aws
- [x] CLT framework
- [x] CF logging via lambda monitoring and cloud watch
- [x] CLT logging via click
- [x] db operations logging via python-json-logger
- [ ] flask to see the output in a webpage with json pretty
- [x] rename CLI functions
- [ ] use CF designer for presentation
- [x] add functionality to append names after cf complete https://stackoverflow.com/questions/47631914/how-to-pass-several-list-of-arguments-to-click-option
- [x] rename CloudFormation from blank-python
- [x] rename LambdaRoles to specific from generic names
- [x] pip's  --use-feature=2020-resolver **
- [x] makes sure IAM policies are deleted when teardown occurs
- [ ] avoid screen popups and y/n when tearing down
- [ ] if add flask, the note below about request lib may cause fail
- [ ] total cost of ownership estimate


Success criteria 

-	DV production standard
-	GitHub professional quality
-	Handoff memoration 
		Presents the project
		Enables 100% client handoff
-	Cohesive quality
		Source code
		Architecture 
		Functionality 
-	MVP checklist
		Application 
		Separate development / production environments
		Comprehensive monitoring and alerts
		Correct Datastore
		Principle of least security enforced
		Data encryption in transit

Deliverables
-	Completed production release in 10 weeks
-	Portfolio of 10 DV 
-	Handoff memorandum

## outline:

Code assumes the environment is equipped with AWS CLI https://aws.amazon.com/cli/

### ```1-create-bucket.sh```
-   random BUCKET_ID
-   BUCKET_NAME = ```lambda-artifacts-[BUCKET_ID]```
-   BUCKET_NAME saved to bucket-name.txt
-   create bucket via ```aws s3 mb```

### ```2-build-layer.sh```
-   remove old layer folders if any
-   ```pip install``` dependencies for lambdas into their layer folders
-   remove ```pandas``` and ```numpy``` from ```ProducerAI``` layer folder; AWS linux requires its flavor of ```pandas``` which is dependent on ```numpy```.
-   curl to ```pandas-0.24.1``` and ```numpy 1.16.1``` for ```manylinux1_x86_64.whl and unzip to ```ProducerAI``` layer folder, deleting ```__pycache__``` and any ```*.dist-info``` files.

### ```3-deploy.sh```
-   employ ```aws cloudformation package``` to package local artifacts of stack, e.g. lambda dependencies, into AWS bucket and via the macro template.yaml return a copy of template ```out.yml``` which replaces references to local artifacts with the S3 location.  
-   employ ```aws cloudformation deploy``` to deploy the stack. 
### ```4-init-data.sh```
-   ```ddb_items_init.py``` initializes ```fang``` table with a list of companies
-   could this be called from python to python without shell script taking either list or file to initialize the fang table?
-   then any list of additions simply adds to the set in dynamo db and we are not dependent on location of execution
-   deletion is next step
-   keep initialization possible in shell by keeing the if main caller at bottom.

### ```5-cleanip.sh```

### ```cfcli.py```

### ```ddb_init.py```

### ```ddb_items.py```

### ```template.yml```

### ```ServerlessProducer/lambda_function.py```

### ```producerAI/lambda_function.py```

### ```make```
-   setup
-   env
-   install
-   bucket
-   build
-   deploy
-   data
-   infra
-   teardown
-   lint
-   test
-   all



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
