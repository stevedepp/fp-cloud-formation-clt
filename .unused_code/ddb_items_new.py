#!/usr/bin/env python

def add_batch(list_add):
    list_existing = open('conames.txt').read().splitlines()
    list_new = list_existing + list_add
    set_new = set(list_new)
    set_existing = set(list_existing)
    set_increment = set_new - set_existing
    return list(set_new), list(set_increment)
    
if __name__ == "__main__":
    add_batch(list_add)
