#!/usr/bin/env python

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fang')

def hello():
    table_time = table.creation_date_time
    return table_time
    
def item_add(item):
    response = table.put_item(Item={'company': item,})
    return response

list_items = ['facebook','amazon','netflix', 'google']

def batch_add(list_items=list_items):
    with table.batch_writer() as batch:
        for i in list_items:
            batch.put_item(Item={'company': str(i),})

def item_delete(item):
    table.delete_item(Key={'company': item,})

def item_update(old_item, new_item):
    response_delete = item_delete(old_item)
    response_add = item_add(new_item)
    return response_delete, response_add
    
def items_list():
    items_list = []
    response = table.scan()
    for i in response['Items']:
        items_list.append(i['company'])
    return items_list, response
    
if __name__ == '__main__':
    hello()
