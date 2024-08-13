#!/usr/bin/env python3
"""
module that has the utility func that inserts docs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).insert_id
