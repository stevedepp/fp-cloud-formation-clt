**@MAIN PHOT0**: hello everyone and thank you for watching this demo video of my final project which MAIN ARCH employs a raspberry pi computer and adafruit weather sensor to collect weather conditions, then publishes those data to google pubsub where a cloud function is triggered that delivers the data to a big query table.

the reason i wanted to employ an IOT data collector is that generally with my degree i want to generate new data for the user 

a device at the edge can not only collect fresh real data but also provide immediate value to nearby users. 
at the same time cloud resources can store and process with greater compute than is available at the edge.   
to me these are the extremes of data science doing what they do best.  
small $10 computer in your house meets tech behemoth in the ether.

the project complex but the process simple **SCROLL TO QUICKSTART**
this was not an easy project. there were many challenges.  
it is however a very simple pipeline -  a sensor collects data and publishes to a query service in the cloud. 

each time that occurs a cloud function is triggered that puts the data into a cloud table 

the challenges are explained in this git repository which provides several resources. 

to make it simple for the user there is quick start on the home page.

There are 5 shell scripts that alternate with 4 manual steps to get the infra up and running.   

So 9 steps in all.  

**CLICK BACK AND FORTH** 

Each quick start step is linked to a page which provides details of the scripts and how to implement them. 

**SCROLL TO HARDWARE PHOTO**      

These 9 steps don’t include the steps of purchasing the edge devices, but included is a shopping list **CLICK PERIOD** from which the user can order the $60 in hardware. 

**CLICK SHOPPING LIST**  

On the same page as the shopping list are a **CLICK BACK** detailed steps for full manual construction of the infrastructure without the shell 5 scripts.  

These 103 manual steps are how I built the first versions of this project.   

**START SCROLLING**   

This manual page helps soldering the parts together, hooking them up and writing each of the 95 command lines to build the gcloud infra.  

From  pubsub, to bigquery  to cloud function.  

From setting up the raspberry pi harddrive on an sd card to setting up communications via wifi defniition and ssh.    

So if a user is stuck on any particular point in the quickstart or wants a more detailed understanding they can refer here.     

Included at the bottom are a few developer notes, but in a third section ...   

**CLICK DEVELOPER NOTES** 

... I provide fulll developer notes with future enhancemens and thoughts on why some features were resjected.  

I have a ton of reosurces that helped me along the way and so I will be filling out the developer notes with more annotated URLs in the future.

Any suggestion you have for new features please let me know.  

**CLICK BACK TO QUICK START**  

The whole process takes 1 script and about 2 minutes to build the gcloud infra in the cloud.  

**CLICK ON FIRST COMMAND**   

**SCROLL DOWN TO RASPBERRY PI**  There are 3 scripts and 4 manual steps build out the gcloud infra on the raspberry pi.  

As mentioned this includes getting the sd card set up, configuring communications via ssh, installing the gcloud on the raspberry pi’s sd card harddrive, and finally running my short python function that collects data from outside and publishes to pubsub.   

Here’s that in action.   

**SCROLL TO TEARDOWN**

Finally, all the infrastrurue including anything left on the raspberry pi is torn down whenever the user executes the one last script.  This takes 30 seconds.   

**GO TO DEVELOPER NOTES** 

Some of more challenging elements were well everything.  Raspberry pi is very manual computer to employ.   I tried many avenues to shorten the construction of the raspberry pi infra including serviice account keys authorizing usage of gcloud from the pi OS and so avoid endless pop ups.   

Employig shell scripts rather than python is very rewarding in terms of comprehending the underlying steps and dependencies for edge and cloud venues but it can also lead to many dead ends. 

This solution would be more fluent in terms of parameterizing the construction were it written in python instead of unix based shell scripting.  As a consequence of using shell rather than python however I did learn how to parameterize basic unix program so the user can specify project name.

In the future, I would enable parameterizing the sensor type and names for all the gloud resources which are currently named for weather related objects.  This would enable the project to have more generic IOT application otther than weather. 

Likely then, I would have mroe than 2 functions and so CICD and linting would take greater prominence in this project.

The shell script is logged by echo and by google logging for the cloud infra.  If genericizing the command line tool went the avenue of python, I would employ a more robust logger like pythonjsonlogger.

Thank you for watching.
