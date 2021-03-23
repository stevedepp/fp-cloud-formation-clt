
demo video for week 9: *IAM roles and policy tightening.  How to understand, do, and keep your hair.*     
please click the video to hear sound.

![demo](https://user-images.githubusercontent.com/38410965/111993516-18082000-8aed-11eb-882c-b870193c33aa.mp4)


IAM roles and policy tightening
How to understand, do, and keep your hair
Steve Depp
MSDS 498 section 61

Demo Video 9

Project 4

DynamoDB —> EventBridge —>  Lambda —>                   SQS —>         Lambda —>    AWS comprehend —> S3
fang —>              5minutetimer —> serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/112216488-efb91800-8bf7-11eb-8dd0-b8b17eccfc1c.png">







Working infra

- [x] make S3 bucket
- [x] build lambda layers


<img width="682" alt="Collecting boto3" src="https://user-images.githubusercontent.com/38410965/112215687-07dc6780-8bf7-11eb-90b5-f91a5833e99c.png">



Working infra

- [x] deploy infrastructure 
- [x] add items to DynamoDB table
- [x] tear down


<img width="682" alt="Successfully packaged artifacts" src="https://user-images.githubusercontent.com/38410965/112215773-23e00900-8bf7-11eb-8df7-1cac2513e03a.png">


3
Tighten up IAM

ServerlessProducer 
-	gets names from a DynamoDB table
-	puts those names in an SQS Queue

	DynamoDB —> EventBridge —>  Lambda —>                   SQS —>
	fang —>              5minutetimer —> serverlessproducer —> producer —>

ProducerAI
-	gets names from SQS Queue
-	deletes them from the SQS Queue
-	performs some machine learning on them
-	sends that result to S3

	SQS —>         Lambda —>    AWS comprehend —> S3
	producer —> producerai —> comprehend —>            fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/112215930-512cb700-8bf7-11eb-9319-e7868954ceaa.png">



4
ServerlessProducer - IAM - start with code to see permissions needed

ServerlessProducer 
-	gets names from a DynamoDB table:  	scan
-	puts those names in an SQS Queue:		get_queue 	send_message

	DynamoDB —> EventBridge —>  Lambda —>                   SQS —>
	fang —>              5minutetimer —> serverlessproducer —> producer —>

<img width="734" alt="lambda_function py" src="https://user-images.githubusercontent.com/38410965/112215979-61dd2d00-8bf7-11eb-9f78-1e0bfb090f08.png">


5.1
ServerlessProducer - LambdaExecutionRole2 role name

- [x] click on role name “LambdaExecutionRole2”

<img width="984" alt="ServerlessProducer" src="https://user-images.githubusercontent.com/38410965/112216074-7a4d4780-8bf7-11eb-9afd-d6e77e7d1f42.png">



5.2
ServerlessProducer - LambdaExecutionRole2 role - AdministrativeAccess policy

ServerlessProducer in the role of “LambdaExecutionRole2” 
has permissions under “AdministrativeAccess” policy
- [x] do anything on anything:   Allow Action * on Resource *
- [x] delete via “x” on LHS

<img width="984" alt="Pasted Graphic 9" src="https://user-images.githubusercontent.com/38410965/112216194-98b34300-8bf7-11eb-8eee-d702adfd42d8.png">




5.3
ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] Detach


<img width="984" alt="Summary" src="https://user-images.githubusercontent.com/38410965/112216799-4cb4ce00-8bf8-11eb-975b-63f674554a62.png">



5.4
ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] click on “Add inline policy”

<img width="984" alt="Summary" src="https://user-images.githubusercontent.com/38410965/112216850-5c341700-8bf8-11eb-9894-2582294c40b8.png">



5.5 ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] click on “Choose a service”


<img width="984" alt="Create policy" src="https://user-images.githubusercontent.com/38410965/112216906-6d7d2380-8bf8-11eb-9f0d-35d142611e39.png">



5.6.0 
ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] start typing “dyn” and click DynamoDB

<img width="984" alt="Create policy" src="https://user-images.githubusercontent.com/38410965/112216959-7ff75d00-8bf8-11eb-9bb6-98e2ad66346e.png">


5.6.1

ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] click on the arrow “Read” and 



<img width="984" alt="Create policy" src="https://user-images.githubusercontent.com/38410965/112217084-a1584900-8bf8-11eb-9029-23af7fd35e80.png">


5.6.2
ServerlessProducer - LambdaExecutionRole2 role - new policy

- [x] click on “scan” 
- [x] notice the warnings in orange and click on arrow “Resources” to investigate


<img width="984" alt="Pasted Graphic 17" src="https://user-images.githubusercontent.com/38410965/112217164-b339ec00-8bf8-11eb-859d-1ffdc7022856.png">




