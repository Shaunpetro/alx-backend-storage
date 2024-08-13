#!/usr/bin/env python3
"""
provide some stats about Nginx logs stored in MongoDB:
logs, collection: nginx, Display same as example
first line: x logs, x num of docs in this collection
2nd line: Methods
5 lines with method = ["Get", "POST", "PUT" PATCH and DELETE]
one line with method=GET, path=/status
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """
    prototype: def logs_stats(mongo_collection, option=none):
    provide some stats about nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
