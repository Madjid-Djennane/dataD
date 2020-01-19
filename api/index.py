#! /usr/bin/python3

from datetime import datetime
import pytz
import re
import pandas as panda
import io
import requests

def parse_str(x):
    """
    Returns the string delimited by two characters.

    Example:
        `>>> parse_str('[my string]')`
        `'my string'`
    """
    return x[1:-1]

def parse_datetime(x):
    '''
    Parses datetime with timezone formatted as:
        `[day/month/year:hour:minute:second zone]`

    Example:
        `>>> parse_datetime('13/Nov/2015:11:45:42 +0000')`
        `datetime.datetime(2015, 11, 3, 11, 45, 4, tzinfo=<UTC>)`

    Due to problems parsing the timezone (`%z`) with `datetime.strptime`, the
    timezone will be obtained using the `pytz` library.
    '''
    dt = datetime.strptime(x[1:-7], '%d/%b/%Y:%H:%M:%S')
    dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))

# retourne les hits http entre deux dates 'DataFrame'
def entre(data,date1,date2):
    return data[(data['time'] >= date1) & (data['time'] <= date2)]

# retourne la liste des ip de base
def ipBase(data):
    return data['ip'].drop_duplicates()

def main():
    #url="http://www.almhuette-raith.at/apache-log/access.log"
    data = panda.read_csv(
    'access.log',
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
    engine='python',
    na_values='-',
    header=None,
    usecols=[0, 3, 4, 5, 6, 7, 8],
    nrows=600000,
    names=['ip', 'time', 'request', 'status', 'size', 'referer', 'user_agent'],
    converters={'time': parse_datetime,
                'request': parse_str,
                'status': int,
                'size': int,
                'referer': parse_str,
                'user_agent': parse_str})
    
    ##data2 = entre(data, '2015-12-12 19:37:49+01:00', '2015-12-12 19:44:06+01:00')
    
    #data2 = data['ip']
    #data3 = data2.drop_duplicates().to_json()
    #print(data3)
    
    data.info()
    

main()