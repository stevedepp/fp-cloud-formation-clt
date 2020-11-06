#!/usr/bin/env python

def add_batch(text_file):
    list_add = open(text_file).read().splitlines()
    list_existing = open('conames.txt').read().splitlines()
    list_new = list_existing + list_add
    set_new = set(list_new)
    set_existing = set(list_existing)
    set_increment = set_new - set_existing
    return set_increment
    print(set_increment)
    
if __name__ == "__main__":
    add_batch(text_file)
