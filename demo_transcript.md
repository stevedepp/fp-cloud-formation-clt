Hello everyone and thank you for watching this demo video of my final project.  

This is not a complex pipeline. 

On a timer, a Lambda function pulls names from a Dynamo DB table and submits them to an SQS queue that triggers another Lambda to pick them up, submit them to AWS Comprehend and send those results to an S3 bucket.

**EVOLUTION**

Where this project was perfect for me is in teaching me the usefulness of development speed.  The faster I can build my code, the more quickly I can develop innovations for it.  So, I started building from the management console and progressed to AWS Serverless Application Model or SAM which allowed me to build in 3 minutes instead of 24.
This allowed me to progress from SAM to Cloud Formation, from Cloud Formation to Lambda layers and from Lambda layers to IAM roles where I tightened policies to their bare minimum. 

If I were building 24 minutes per round trip i would never have gotten this far. 

**TO DO**

And I have a lot left to do.  Loads of great ideas to improve this project further.

**CODE COMMENTS SCROLL TO CFCLI.PY**

For now I have compressed these 4 shell scripts into one command line tool that adds new names, removes existing names and modifies existing names, and of course tears down the whole enchilada.  Now, we are on the development section here.

I havent forgotten about the user.

**CLICK TO HOME**

So, on the home page there are quick start commands, a list of features,
and if the quick start commands aren’t enough, there are screen shots of each in action.

**CLICK TO screenshots**

This is the set up, … infrastructure build, … and then the database operations.

Now since this is a demo, i will quickly demo some of those commands myself. 

Here’s a terminal 

Typically when a model is built, the Dynamo DB table is empty.   So take a look at a file containing Facebook amazon netflix and google.

`nano ./cos.txt`

Use a command to simply add to that.

`./cfcli.py add --file ./cos.txt`

Now, we’ve added those names.  

I can remove 2 names.

`./cfcli.py remove -i amazon -i google`

We can update netflix spelling from lower case n to upper case N.

`./cfcli.py update -o netflix -n Netflix`

And we can remove a file.

`./cfcli.py remove --file ./cos.txt`

Since we changed the spelling of netflix from lower to upper case, the tool removed the lower case and left us with the upper case.  That’s the only one thats left over.

Then of course we can tear down the whole thing so we don’t pay anything. 

`./cfcli.py teardown`

OK its all torn down.  Thank you for watching.  And I really enjoyed spending the quarter with everybody.  Take Care.
