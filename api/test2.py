#! /usr/bin/python3

#from datetime import datetime
#import pytz
#import re
#import pandas as panda
#import io
#import requests
#import time

from index import *

if __name__ == "__main__":
    data = getDT('../nodeApi/access.log')
    hits = getLogs(data, '2014-12-12 18:25:11+01:00', '2014-12-12 18:31:11+01:00')
    print(hits)