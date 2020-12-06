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


	`#!/bin/bash`  
	`BUCKET_ID=$(dd if=/dev/random bs=8 count=1 2>/dev/null | od -An -tx1 | tr -d ' \t\n')`  
	`BUCKET_NAME=lambda-artifacts-$BUCKET_ID`  
	`echo $BUCKET_NAME > bucket-name.txt`  
	`aws s3 mb s3://$BUCKET_NAME`  

-   random BUCKET_ID
-   BUCKET_NAME = ```lambda-artifacts-[BUCKET_ID]```
-   BUCKET_NAME saved to bucket-name.txt
-   create bucket via ```aws s3 mb```

#

### ```2-build-layer.sh```


	`#!/bin/bash`  

	`set -eo pipefail`  
	
	`rm -rf packageServerlessProducer`  
	`rm -rf packageProducerAI`  
	
	`pip install --target ./packageServerlessProducer/python -r ./ServerlessProducer/requirements.txt --use-feature=2020-resolver`  
	`pip install --target ./packageProducerAI/python -r ./ProducerAI/requirements.txt --use-feature=2020-resolver`  
	
	`rm -rf ./packageProducerAI/python/pandas`  
	`rm -rf ./packageProducerAI/python/numpy`  
	
	`curl -O https://files.pythonhosted.org/packages/e6/de/a0d3defd8f338eaf53ef716e40ef6d6c277c35d50e09b586e170169cdf0d/pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl`  
	`curl -O https://files.pythonhosted.org/packages/f5/bf/4981bcbee43934f0adb8f764a1e70ab0ee5a448f6505bd04a87a2fda2a8b/numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl`  
	
	`unzip pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl -d packageProducerAI/python/`  
	`unzip numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl -d packageProducerAI/python/`  
	
	`rm -r packageProducerAI/python/__pycache__`  
	`rm -r packageProducerAI/python/*.dist-info`  
	
	`rm pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl`  
	`rm numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl`  


-   remove old layer folders if any
-   ```pip install``` dependencies for lambdas into their layer folders
-   remove ```pandas``` and ```numpy``` from ```ProducerAI``` layer folder; AWS linux requires its flavor of ```pandas``` which is dependent on ```numpy```.
-   curl to ```pandas-0.24.1``` and ```numpy 1.16.1``` for ```manylinux1_x86_64.whl and unzip to ```ProducerAI``` layer folder, deleting ```__pycache__``` and any ```*.dist-info``` files.

#

### ```3-deploy.sh```

	`#!/bin/bash`  
	`set -eo pipefail`  
	`ARTIFACT_BUCKET=$(cat bucket-name.txt)`  
	`aws cloudformation package --template-file template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file out.yml`  
	`aws cloudformation deploy --template-file out.yml --stack-name depp-498-fp --capabilities CAPABILITY_NAMED_IAM`  

-   employ ```aws cloudformation package``` to package local artifacts of stack, e.g. lambda dependencies, into AWS bucket and via the macro template.yaml return a copy of template ```out.yml``` which replaces references to local artifacts with the S3 location.  
-   employ ```aws cloudformation deploy``` to deploy the stack. 

#

### ```4-init-data.sh```

	`#!/bin/bash`  
	`./ddb_items_init.py > request.json`  
	`aws dynamodb batch-write-item --request-items file://request.json`  
	`rm request.json`  

-   ```ddb_items_init.py``` initializes ```fang``` table with a list of companies
-   could this be called from python to python without shell script taking either list or file to initialize the fang table?
-   then any list of additions simply adds to the set in dynamo db and we are not dependent on location of execution
-   deletion is next step
-   keep initialization possible in shell by keeing the if main caller at bottom.

#

### ```5-cleanip.sh```

	`#!/bin/bash`  
	`set -eo pipefail`  
	`STACK=depp-498-fp`  

	`if [[ $# -eq 1 ]] ; then`  
	`    STACK=$1`  
	`    echo "Deleting stack $STACK"`  
	`fi`  

	`FUNCTION1=$(aws cloudformation describe-stack-resource --stack-name $STACK --logical-resource-id ServerlessProducer --query 'StackResourceDetail.PhysicalResourceId' --output text)`  

	`FUNCTION2=$(aws cloudformation describe-stack-resource --stack-name $STACK --logical-resource-id ProducerAI --query 'StackResourceDetail.PhysicalResourceId' --output text)`  

	`aws s3 rm s3://fangsentiment-depp --recursive`  

	`aws cloudformation delete-stack --stack-name $STACK`  
	`echo "Deleted $STACK stack."`  

	`if [ -f bucket-name.txt ]; then`  
	`    ARTIFACT_BUCKET=$(cat bucket-name.txt)`  
	`    if [[ ! $ARTIFACT_BUCKET =~ lambda-artifacts-[a-z0-9]{16} ]] ; then`  
	`        echo "Bucket was not created by this application. Skipping."`  
	`    else`  
	`        while true; do`  
	`            read -p "Delete deployment artifacts and bucket ($ARTIFACT_BUCKET)? (y/n)" response`  
	`            case $response in`  
	`                [Yy]* ) aws s3 rb --force s3://$ARTIFACT_BUCKET; rm bucket-name.txt; break;;`  
	`                [Nn]* ) break;;`  
	`                * ) echo "Response must start with y or n.";;`  
	`            esac`  
	`        done`  
	`    fi`  
	`fi`  

	`rm -f out.yml`  
	`rm -f function/*.pyc`  
	`rm -f bucket-name.txt`  
	`rm -rf packageProducerAI`  
	`rm -rf packageServerlessProducer`  
	`rm -rf function/__pycache__`  

	`while true; do`  
	`    read -p "Delete function log group (/aws/lambda/$FUNCTION1)? (y/n)" response`  
	`    case $response in`  
	`        [Yy]* ) aws logs delete-log-group --log-group-name /aws/lambda/$FUNCTION1; break;;`  
	`        [Nn]* ) break;;`  
	`        * ) echo "Response must start with y or n.";;`  
	`    esac`  
	`done`  

	`while true; do`  
	`    read -p "Delete function log group (/aws/lambda/$FUNCTION2)? (y/n)" response`  
	`    case $response in`  
	`        [Yy]* ) aws logs delete-log-group --log-group-name /aws/lambda/$FUNCTION2; break;;`  
	`        [Nn]* ) break;;`  
	`        * ) echo "Response must start with y or n.";;`  
	`    esac`  
	`done`  

#

### ```cfcli.py```

	#!/usr/bin/env python3
	import click
	import lib
	import sys
	import subprocess
	from ddb_ops import table_timestamp, item_add, items_add, items_delete, item_update, items_list

	@click.version_option(lib.__version__)
	@click.group()
	def cli():
	    '''greetings'''

	@cli.command("make-infra")
	def hello():
	    # change to make infra and save/publish time
	    subprocess.run(['make', 'infra'])

	@cli.command("add")
	@click.option('--file', help='File containig a column of names')
	@click.option('--item', '-i', multiple=True, help='One item via --item or several separated by -i')
	def add(file, item):
	    if not file and not item:
		click.echo("--file or --items is required")
	    elif file and item:
		click.echo("--file or --items but not both please")
	    else:
		items_list_before = items_list()
		click.echo(f"Current items in DynamoDB are: {items_list_before}")
		if file:
		    with open(file) as fin:
			list_to_add = fin.read().splitlines()
		elif item:
		    list_to_add = list(item)
		    file = 'list'
		click.echo(f"Adding these items from {file} to DynamoDB: {list_to_add}")
		items_add(list_to_add)
		items_list_after = items_list()
		items_added = list(set(items_list_after) - set(items_list_before))
		click.echo(f"Net, processing batch from {file}. \n-> adding: {items_added}")
		click.echo(f"full list will be {items_list_after}")

	@cli.command("remove")
	@click.option('--file', help='File containig a column of names')
	@click.option('--item', '-i', multiple=True, help='One item via --item or several separated by -i')
	def delete(file, item):
	    if not file and not item:
		click.echo("--file or --item is required")
	    elif file and item:
		click.echo("--file or --item but not both please")
	    else:
		items_list_before = items_list()
		click.echo(f"Current items in DynamoDB are: {items_list_before}")
		if file:
		    with open(file) as fin:
			list_to_delete = fin.read().splitlines()
		elif item:
		    list_to_delete = list(item)
		    file = 'list'
		click.echo(f"Deleting these items from {file} from DynamoDB: {list_to_delete}")
		items_delete(list_to_delete)
		items_list_after = items_list()
		items_deleted = list(set(items_list_before)-set(items_list_after))
		click.echo(f"Net, processing batch from {file}. \n-> deleting: {items_deleted}")
		click.echo(f"full list will be {items_list_after}")
		subprocess.run(['aws', 's3', 'rm', 's3://fangsentiment-depp', '--recursive'])

	@cli.command("update")
	@click.option('--old', '-o', help='Item that needs updating; use --old or -o')
	@click.option('--new', '-n', help='Items new value; use --new or -n')
	def update(old, new):
	    if not old and not new:
		click.echo("--old AND --new is required")
	    else:
		items_list_before = items_list()
		click.echo(f"Current items in DynamoDB are: {items_list_before}")
		click.echo(f"Update from {old} to {new}")
		item_update(old, new)
		items_list_after = items_list()
		click.echo(f"full list will be {items_list_after}")
		subprocess.run(['aws', 's3', 'rm', 's3://fangsentiment-depp', '--recursive'])

	@cli.command("teardown")
	def end():
	    # change to make infra and save/publish time
	    subprocess.run(['make','teardown'])

	if __name__ == "__main__":
	    cli()

-	click library employed for command line tool menus and logging
-	./cfcli.py make-infra  --> install requirements, builds and deploys aws resources from cloud formation template
-	./cfcli.py add 
	-	takes 1 of 2 both not both arguments as names to add
		-	--file or -f will take a text file containing a column of names
		-	--item or -i will take a single name in-line folling --item or -i
	-	finds names currently in table 
	-	from current names + new names, computes unique total set 
	-	adds the net difference unique total set - current names
	- 	reports back the old table form, new table form and table transaction
	
-	./cfcli.py remove
	-	takes 1 of 2 both not both arguments as names to add
		-	--file or -f will take a text file containing a column of names
		-	--item or -i will take a single name in-line folling --item or -i
	-	finds names currently in table
	-	ignores a name to be removed if not in table
	-	removes names
	- 	reports back the old table form, new table form and table transaction

-	./cfcli.py update
	-	takes 2 arguments
		-	--old or -o will take a current name to be changed
		-	--new or -n will take the replacement for old name
	- 	reports back the old table form, new table form and table transaction

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
