#!/bin/bash
set -eo pipefail
STACK=blank-python

if [[ $# -eq 1 ]] ; then
    STACK=$1
    echo "Deleting stack $STACK"
fi

FUNCTION1=$(aws cloudformation describe-stack-resource --stack-name $STACK --logical-resource-id ServerlessProducer --query 'StackResourceDetail.PhysicalResourceId' --output text)

FUNCTION2=$(aws cloudformation describe-stack-resource --stack-name $STACK --logical-resource-id ProducerAI --query 'StackResourceDetail.PhysicalResourceId' --output text)

aws cloudformation delete-stack --stack-name $STACK
echo "Deleted $STACK stack."

if [ -f bucket-name.txt ]; then
    ARTIFACT_BUCKET=$(cat bucket-name.txt)
    if [[ ! $ARTIFACT_BUCKET =~ lambda-artifacts-[a-z0-9]{16} ]] ; then
        echo "Bucket was not created by this application. Skipping."
    else
        while true; do
            read -p "Delete deployment artifacts and bucket ($ARTIFACT_BUCKET)? (y/n)" response
            case $response in
                [Yy]* ) aws s3 rb --force s3://$ARTIFACT_BUCKET; rm bucket-name.txt; break;;
                [Nn]* ) break;;
                * ) echo "Response must start with y or n.";;
            esac
        done
    fi
fi

while true; do
    read -p "Delete function log group (/aws/lambda/$FUNCTION1)? (y/n)" response
    case $response in
        [Yy]* ) aws logs delete-log-group --log-group-name /aws/lambda/$FUNCTION1; break;;
        [Nn]* ) break;;
        * ) echo "Response must start with y or n.";;
    esac
done

while true; do
    read -p "Delete function log group (/aws/lambda/$FUNCTION2)? (y/n)" response
    case $response in
        [Yy]* ) aws logs delete-log-group --log-group-name /aws/lambda/$FUNCTION2; break;;
        [Nn]* ) break;;
        * ) echo "Response must start with y or n.";;
    esac
done


rm -f out.yml out.json function/*.pyc
rm -rf packageProducerAI packageServerlessProducer function/__pycache__
