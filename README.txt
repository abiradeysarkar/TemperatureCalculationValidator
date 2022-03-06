INTRODUCTION TO THE PROJECT

- Rest API for validating student answer are written in python script
- With CloudFormation, EC2 instance, Roles and VPC is created
- Manually create the S3 bucket and Key pair as mentioned below

Pre-Build steps:

Python project TemperatureValidatorAPI.py is in current repo
Buildpspec file i.e, buildspec.yml is also created in this repo
Create a S3 bucket
Create a PAT token for your Github account
Reference link- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
Copy the PAT token to your local and keep it handy
Create the build project

CodeBuild

Search for CodeBuild services
Create a build project
Add proper/relevant project name
In source, choose the source provider as Github from the dropdown
Repository, select the second option “Repository in my GitHub account”
In Github repository, select the appropriate repo
In Primary source web hook events, enabled the “Rebuild every time a code change is pushed to this repository”
Build type as Single and Event type select PUSH
In Environment, choose “Managed image” -> OS: Ubuntu -> Runtime: Standard -> Image: aws/codebuild/standard:5.0
In Service role, select to create a new role, you can add your reference service role name
In Build spec, select the “Use a buildspec file” (already created in the beginning)
In Artifacts, choose type as S3 - > Add the bucket name which you created earlier -> Artifacts packaging set the default setting as None
Click on Create build project
Once the project build successfully, the zip application file will be on the S3 bucket created at the beginning


For creating the VM with security group and VPC, run the script to create a tack in CloudFormation

To create a key pair, go to EC2
Left panel under Network & Security, click on key pair
Add the key pair name as “assignment-keypair”, download the assignment-keypair.pem file
Click on create stack on CloudFormation
Select the Template source “Upload a template file”
Upload the file from local -> Next page add a stack name -> keep the default setting and select Next -> enable the AWS::IAM::Role checkbox
Create the stack
Check the EC2 instance created



CodeDeploy

Create a application with Application name -> Compute platform: EC2/On-premises
Create the deployment group, add name -> Use the service role from dropdown which created while CodeBuild -> Choose Deployment type as “in-place”
Environment configuration as “Amazon EC2 instances” -> Key as “Name” -> Value as “Name of the EC2 instance created using CloudFormation”
You will get this message- 1 unique matched instance.
Disable the Load Balancer section
Create the Deployment -> select the Deployment group name -> Revision type: S3 -> Copy the S3 URL of the zip file

Example - s3://tempconverter-bucket/Temp-Converter-API-build/application-build.zip
7. In “Additional deployment behavior settings”, select the below-
Overwrite the content

CodePipeline

Create the Pipeline with relevant name
Use the new service role/existing service role
Keep all default setting and move to Next
Source provider, select the Github (version 1) - > Connect to Github -> Add the repository and branch -> Next
Skip build stage
Deploy provider, select CodeDeploy -> Add Application Name - > Deployment group name -> Next
Review all the details and select “Create Pipeline”
Once the Pipeline is created, Release the pipeline
Add the build stage, by editing the pipeline
Add a stage by provide the stage name
Add action group - > Name -> Action Provider: CodeBuild -> Input Artifact: SourceArtifact -> build project name -> Done
Save the changes
Release the pipeline with new stage


How to test deployment is done:
Once the all the above steps are successful, login the EC2 instance using SSH connection
Select the instance and click on Connect
Follow the mentioned steps
Run the ssh command from folder where you have saved the pem file assignment-keypair.pem
Run the below command:
      sudo su -
      cd /TemperatureService
      Output: TemperatureValidatorAPI.py Temperature_Validator_API.log


Test the python script using curl command:
Python script should be running after a successful deployment
Run the below command inside EC2 instance
       curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "from":"rankine",
    "to":"kelvin",
    "value": 300,
    "answer": 166.67
}' \
  http://127.0.0.1:5000/convert

Explanation of the Rest API POST payload:
from : source temperature unit
to: target temperature unit
value: given value
answer: student answer to be validated