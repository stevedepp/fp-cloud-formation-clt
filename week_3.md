
## demo video for week 3: *replicate architecture of project 4*     

please unmute the video to hear sound or follow along with the transcript that's set just below the video.  video resolution improves at full screen.

<video src="https://user-images.githubusercontent.com/38410965/112028923-13546380-8b0f-11eb-88ce-deec20aa2606.mp4" autoplay controls loop muted style="max-width: 730px;">
</video>

#

> Hello everyone this is Steve.  Thank you for watching my video.  This week i spent time reviewing the architecture for my project in detail with hopes to get it running.  As an update I will provide you with a broad overview of the 5 steps needed replicate the architecture.  You will recall my project is modeled after project 4.  To replicate this architecture ...


**Steve Depp**   
**MSDS 498-61**   

### Final project   
### Week 3 update: replicate architecture of project 4   

**186 clicks in week 3**   
step 1: set up & test cloud 9 development environment   
step 2: set up & test SQS queue “producer”    
step 3: set up DynamoDB table “fang”   
step 4: set up serverless application “serverlessproducer”    
step 5: set up serverless application “producerai”   

**next micro steps: week 4**   
**next macro steps: weeks 5 - 9**   
**reach**   

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113616892-b2a34b80-9623-11eb-9fde-4e4e2ff8006a.png">

#

> I first set up a cloud 9 environment.  Then, set up and tested an SQS queue. Then, set up a Dynamo DB table.  And finally
set up 2 serverless applications: ne that gets from DB and puts into SQS; the other that gets from SQS and delivers a transformed version to S3. All in about 186 clicks of the mouse and some typing.  

### Final project   
### Week 3 update:    

### Replicate architecture   

**step 1: set up & test cloud 9 development environment (24 clicks)**   

- set up c9 environment      
- test c9 environment  

**step 2: set up & test SQS queue “producer” (19 clicks)**   

- setup SQS queue      
- test SQS queue    

**step 3: set up DynamoDB table “fang” (13 steps)**

**step 4: set up serverless application “serverlessproducer” (72 clicks)**

- set up lambda function   
- interpret lambda function code   
- install dependencies     
- test locally   
- deploy to AWS   
- test with cloud test event   
- test with cloud trigger event   
	
**step 5: set up serverless application “producerai” (58 clicks)**

- set up lambda function   
- interpret lambda function code   
- install dependencies     
- deploy to AWS   
- test with cloud trigger event   
- verify test in SQS, CloudWatch metrics, CloudWatch logs, S3   

#

> This week i plan to run the template in AWS (probably this afternoon), set up in transit encryption, store the Lambda source code in Github, automate dependencies, and tighten up the role I am using presently to negotiate who Lambda talks with.  I will also do some research in to CICD: specifically what AWS offers and how I might possibly build code outside AWS and have it sourced automatically for monitoring I will look into how I can notify a user with email of important log messages and I will look into total cost of ownership.

### Final project   
### Week 3 update   

### next micro steps: week 4   

**run template in AWS**   

**improvements:**   
- data encryption in transit   
- store code in GitHub instead of copy/paste in code   
- automate dependencies   
- tighten role for “principle of least security”   
	- listen to SQS   
	- call comprehend    
	- write to S3   

**research**   
- CICD   
- email notifications   
- TCO   

#

> In ensuing weeks, I plan to implement CICD and monitoring in week 5 and work on extensions and formal deliverables in the following weeks if things go a bit more speedily, which they never do! 

### Final project
### Week 3 update

### next macro steps: 

**week 5**   
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

> I hope to explore some of my reach goals for this final project.

### Final project   
#### Week 3 update   

### reach:
-	GCP and Azure   
-	Integrating an additional project, e.g. project 1’s Flask app   

# 

thank you for watching   

please let me know any feedback   
