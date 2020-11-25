#!/usr/bin/env python

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fang')

def table_timestamp():
    table_time = table.creation_date_time
    return table_time
    
def items_list():
    items_list = []
    response = table.scan()
    if response['Items'] != []:
        for i in response['Items']:
            items_list.append(i['name'])
        return items_list
    else:
        return "Empty list"

list_items = ['facebook','amazon','netflix', 'google']

def items_add(list_items=list_items):
    if list_items == ['']:
        print("empty")
    else:
        with table.batch_writer() as batch:
            for i in list_items:
                batch.put_item(Item={'name': str(i),})

def items_delete(list_items):
    for i in list_items:
        table.delete_item(Key={'name': i,})

def item_add(item):
    response = table.put_item(Item={'name': item,})
    return response

def item_update(old_item, new_item):
    old_item = [old_item]
    response_delete = items_delete(old_item)
    response_add = item_add(new_item)
    #return response_delete, response_add

if __name__ == '__main__':
    cf_timestamp()
