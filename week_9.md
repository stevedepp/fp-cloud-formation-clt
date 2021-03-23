
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








Working infra

- [x] make S3 bucket
- [x] build lambda layers


<img width="682" alt="Collecting boto3" src="https://user-images.githubusercontent.com/38410965/112215687-07dc6780-8bf7-11eb-90b5-f91a5833e99c.png">



Working infra

- [x] deploy infrastructure 
- [x] add items to DynamoDB table
- [x] tear down


<img width="682" alt="Successfully packaged artifacts" src="https://user-images.githubusercontent.com/38410965/112215773-23e00900-8bf7-11eb-8df7-1cac2513e03a.png">


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

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/112215857-3d815080-8bf7-11eb-8d5d-e38e067d7f6c.png">



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
