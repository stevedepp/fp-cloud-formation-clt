# serverless ai data engineering pipeline
building serverless pipeline from dynamo db to lambda to sqs to lambda to aws comprehend to s3 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/38410965/101273547-5529eb80-3764-11eb-9cfa-40ff738a857c.png">

#

## architecture diagram

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/101269508-893de600-373d-11eb-9d52-a393e4070d67.png">

        resource = DynamoDB -> EventBridge -> Lambda -> SQS -> Lambda -> AWS comprehend -> S3  
        name = fang -> 5minutetimer -> serverlessproducer -> producer -> comprehend -> fangsentiment-depp


#

## demo video   
please click the video to hear sound.  additional videos [here](https://github.com/stevedepp/fp-cloud-formation-clt/blob/main/developer_notes.md#evolution-of-development) breadcrumb the path to this solution.

![demo](https://user-images.githubusercontent.com/38410965/111991585-dbd3c000-8aea-11eb-86b2-52f2af0b9a27.mp4)

#

## quickstart commands
(annotated screenshots of all are provided [here](https://github.com/stevedepp/fp-cloud-formation-clt/blob/main/screenshots.md#screenshots))

#

- [x] getting going

        mkdir folder_name
        cd folder_name
        git clone https://github.com/stevedepp/fp-cloud-formation-clt.git
        cd fp-cloud-formation-clt
        python3 -m venv .venv
        source .venv/bin/activate
        make install
        
- [x] building infrastructure

        ./cfcli.py make-infra


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

- [x] tearing it down

        ./cfcli.py teardown 
        
[screenshots](https://github.com/stevedepp/fp-cloud-formation-clt/blob/main/screenshots.md#serverless-ai-data-engineering-pipeline)

## features

- [x] speedy hands-free build in 4 minutes 20 seconds
- [x] speedy hands-free teardown in 2 minutes 30 seconds
- [x] source code in github
- [x] automated dependencies
- [x] encryption in transit
- [x] principle of least privelege via IAM roles' policies
- [x] python based command line tool (CLT) framework
- [x] simple CLT commands
- [x] CLT logging via click
- [x] db operations logging via python-json-logger
- [x] infrastructure as code logging via aws cloud formation (CF) console
- [x] CF logging via lambda monitoring and cloud watch
- [x] CICD via infrastructure as code

## developer comments are [here](https://github.com/stevedepp/fp-cloud-formation-clt/blob/main/developer_notes.md#developer-notes)



