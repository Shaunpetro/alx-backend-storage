#!/usr/bin/env python3
"""Module having a utility func that list all docs
"""
import pymongo


def list_all(mongo_collection):
    """
    List all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
