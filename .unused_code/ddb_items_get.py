#!/usr/bin/env python

import json

def get_items(fn='bob.json', primary_key='name'):
    items_list = []
    with open(fn) as fin:
        doc = json.load(fin)
    for i in doc['Items']:
        items_list.append(i[primary_key]['S'])
    return items_list

if __name__ == '__main__':
    request()
