
## demo video for week 4: *replicate the hardware*     

please unmute the video to hear sound or follow along with the transcript that's set just below the video.  Video resolution improves at full screen.

<video src="https://user-images.githubusercontent.com/38410965/112003158-088dd480-8af7-11eb-921a-9a667e4ab2ee.mp4" autoplay controls loop muted style="max-width: 730px;">
</video>

#

> Hello everyone thank you for watching my video.  It is a relief to be here, but i can say that the bare bones of my project can walk and talk as intended.  In case you weren’t aware, this final project mimics project 4 that retrieves companies' names from a Dynamo DB table up top here, performs sentiment analysis on their wiki pages, and drops that analysis into an S3 bucket, where e.g. you can spit it into a spreadsheet or a web page.  The good news is thats largely completed and working.

**steve depp**   
**MSDS 498-61**   

### final project   

### replicate the hardware   

“phew”

<img width="452" alt="console aws amazon com" src="https://user-images.githubusercontent.com/38410965/113622509-18df9c80-962b-11eb-8586-74fa21dfd9f7.png">

<img width="623" alt="00E6 U = (facebook, ibm, 'face" src="https://user-images.githubusercontent.com/38410965/113622488-13825200-962b-11eb-8f45-fae6d8f37fb0.png">

#

> The bad news is that I didn’t get to the improvements I’d intended to, which include encrypting in transit and enforcing principle of least dependency via IAM roles.

### final project   

**micro next steps**   
- [x] run template in AWS   
- [ ] data encryption in transit   
- [ ] store code in GitHub instead of copy/paste in code   
- [ ] automate dependencies   
- [ ] tighten role for “principle of least security”   

**under the hood**    
DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3   
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp   

**Project 4**   

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113622759-652adc80-962b-11eb-921e-414f4e5c95a3.png">

#

> One upside to making and deleting this project from AWS 10-20 times is that now I can build and test the whole project in under 25 minutes.  This has taught me alot. I have learned to be very nimble in cloud 9.  It's taught me to need those monitoring plots in Lambda console and how to read the Cloud Watch logs.  Repeatedly building, tearing down and rebuilding has taught me to appreciate testing inside Cloud9, via SQS and via Lamnda test functions, I've learned to appreciate that a deployed lamnda has different output than one that is still ONLY resident in cloud 9.  And these last few days of hair pulling has taught me to appreciate Cloud Formation, which will help in automating the whole process i hope.

### learned   

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**   

￼<img width="105" alt="2435 60" src="https://user-images.githubusercontent.com/38410965/113622880-8db2d680-962b-11eb-9053-6f3294c310d4.png">

**nimble —> Cloud9**   
 - GitHub   
 - structure of dependencies   
 - lambda venv   

**need —> Lambda monitoring & CloudWatch logs**   
 - structured search   
 - relevancy window   

**appreciate**    
- test    
  - locally inside Cloud9   
  - via SQS   
  - via Lambda   
- deploy   
  - test lambda —> “” if not deployed   
  - test lambda —> null if deployed   
- cloud formation   

<img width="906" alt="Stacks (4)" src="https://user-images.githubusercontent.com/38410965/113622905-960b1180-962b-11eb-93b4-36bf2a4accb3.png">

#

> One goal is learning to comprehend this projects total cost of ownership.  And a first step is knowing the resources i create on my own, such as cloud 9 and ... 

### resources - diy   

**Cloud 9**   
- serverlessproducer   
- producerai   
- venv   
- GitHub integration   

<img width="947" alt="console aws amazon com" src="https://user-images.githubusercontent.com/38410965/113622949-a7ecb480-962b-11eb-9fa3-f3bcbed20134.png">

#

> ... the serverless functions created there and their triggers, such the one ...

### resources - diy   

**Lambda functions**   

- serverlessproducer   
  - SQS trigger   

- producerai   
  - EventBridge trigger   

<img width="502" alt="fina" src="https://user-images.githubusercontent.com/38410965/113623044-ca7ecd80-962b-11eb-8022-79a3d3381f26.png">

<img width="469" alt="cloud9-serverlessproducer-serverlessproducer-TKT5FKM6VTWA" src="https://user-images.githubusercontent.com/38410965/113623059-d1a5db80-962b-11eb-913f-8c4fb9d6f9c2.png">

<img width="510" alt="cloud9-producerai-producerai-WOICONMZITOA" src="https://user-images.githubusercontent.com/38410965/113623084-d8cce980-962b-11eb-8ff0-7e846adc9386.png">

#

> ... that causes an sqs queue to move data from ...

### resources - diy   

**SQS queue**   

<img width="912" alt="console aws amazon com" src="https://user-images.githubusercontent.com/38410965/113623128-eaae8c80-962b-11eb-80b0-ed12424d8cd1.png">

#

> ... a dynamo db table ... 

### resources - diy   

**Dynamo DB**    
- 1 table       
  - 9 items   

<img width="768" alt="console aws amazon com" src="https://user-images.githubusercontent.com/38410965/113623177-fe59f300-962b-11eb-8132-3cadababf8a0.png">

#

> to the s3 bucket, which by the way kept me in a debugging loop for many hours.

### resources - diy   

**S3**    
one bucket each for    
- Cloud 9   
- fangsentiment   

<img width="931" alt="53 buckets" src="https://user-images.githubusercontent.com/38410965/113623254-16317700-962c-11eb-9390-9f076c3320a3.png">

#

> In some ways these resources that I provision are less important than the ones that come included, the resources that AWS provisions for you in the background, and which cost money: such as Cloud Watch and ...

### resources - batteries included   

**CloudWatch**   
- logs for development   
- logs for operation   

<img width="850" alt="CloudW" src="https://user-images.githubusercontent.com/38410965/113623304-2cd7ce00-962c-11eb-8b88-ae205b2810cd.png">

#

> Cloud Formation. Knowing these resources will help me understand what needs documentation in Cloud Formation and what
will affect TCO.

### resources - batteries included   

**Cloud Formation**    
- one for each Lambda   
- one for Cloud 9   

<img width="686" alt="console ans amazon com" src="https://user-images.githubusercontent.com/38410965/113623379-46791580-962c-11eb-8af8-9d882093dd45.png">

#

> So that is done, ... but not without a few mistakes. 

### hiccups

- Git Hub & name / guid   
- installing dependencies into wrong folder   
- bucket writing <— bucket creating   

#

> Next macro steps this week are data encryption in transit, storing build code in GitHub, dependency automation and IAM roles.
   
### Final project   
### Week 4 update      

### next macro steps:    

**week 5**   
- data encryption in transit   
- store code in GitHub instead of copy/paste in code   
- automate dependencies   
- tighten role for “principle of least security”   
- Continuous Integration / Continuous Delivery (CICD)   
- Monitoring (email notification)   
- Total Cost of Ownership (TCO)   

**week 6**   
- Nominate extended features + incremental TCO   
- Nominate domain application   

**week 7**   
- Development release   
- Handoff memorandum - Draft   

**week 8**   
- Production release   
- Handoff memorandum - Final   

**week 9**   
- Demo Video - Final   

#

**thank you**
