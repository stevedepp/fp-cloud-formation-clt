#!/usr/bin/env python

import json
import boto3

#SETUP LOGGING
import logging
from pythonjsonlogger import jsonlogger

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
LOG.addHandler(logHandler)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fang')

def table_timestamp():
    table_time = table.creation_date_time
    log_table_time_msg = f'table creation at {table_time}'
    LOG.info(log_table_time_msg)
    return table_time
    
def items_list():
    items_list = []
    response = table.scan()
    if response['Items'] != []:
        for i in response['Items']:
            items_list.append(i['name'])
        log_items_list_msg = f'list of items is: {items_list}'
        LOG.info(log_items_list_msg)
        return items_list
    else:
        log_items_list_msg = f'list of items is empty'
        LOG.info(log_items_list_msg)
        return "Empty list"

list_items = ['facebook','amazon','netflix', 'google']

def items_add(list_items=list_items):
    if list_items == ['']:
        log_add_items_msg = f'list of items is empty'
        LOG.info(log_add_items_msg)
        print("empty")
    else:
        with table.batch_writer() as batch:
            for i in list_items:
                batch.put_item(Item={'name': str(i),})
                log_add_items_msg = f'adding name: {str(i)} to list'
                LOG.info(log_add_items_msg)

def items_delete(list_items):
    for i in list_items:
        table.delete_item(Key={'name': i,})
        log_remove_items_msg = f'removing name: {i} from list'
        LOG.info(log_remove_items_msg)
        
def item_add(item):
    response = table.put_item(Item={'name': item,})
    log_add_item_msg = f'removing name: {item} from list'
    LOG.info(log_add_item_msg)
    return response

def item_update(old_item, new_item):
    old_item = [old_item]
    response_delete = items_delete(old_item)
    response_add = item_add(new_item)
    #return response_delete, response_add
    log_add_item_msg = f'replacing {old_item} with {new_item} in list'
    LOG.info(log_add_item_msg)


if __name__ == '__main__':
    cf_timestamp()
