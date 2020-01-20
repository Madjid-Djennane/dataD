#! /usr/bin/python3
from datetime import datetime
import pytz
import re
import pandas as panda


"""
Retourne une chaine de caractère délimitée par deux caractères
Example:
    `>>> parse_str('[my string]')`
    `'my string'`
"""
def parse_str(x):
    return x[1:-1]



'''
Parse la date de type datetime (avec une timezone)
    `[day/month/year:hour:minute:second zone]`

Example:
    `>>> parse_datetime('22/Dec/2018:14:21:read log file python pandas35 +0100')`
    `2018-12-22:14:21:35 01:00`
'''
def parse_datetime(x):
    dt = datetime.strptime(x[1:-7], '%d/%b/%Y:%H:%M:%S')
    dt_tz = int(x[-6:-3])*60+int(x[-3:-1])
    return dt.replace(tzinfo=pytz.FixedOffset(dt_tz))


'''
Retourne un dataFrame contenant quatres colonnes (qui nous intéressent)
['ip', 'time', 'requête', 'referer']

prend en paramètres le path vers le fichier log  
'''
def getDT(file):
    data = panda.read_csv(
        file,
        sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])', # regex qui repère les espaces pour découper une ligne
        engine='python',
        na_values='-',
        header=None,
        usecols=[0, 3, 4, 7], 
        #nrows=1500000,
        names=['ip', 'time', 'request', 'referer'],
        converters={'time': parse_datetime,
                    'request': parse_str,
                    'referer': parse_str})
    
    return data

'''
Retourne les hits HTTP selon une fenêtre de temps 
Prend en paramètres le dataFrame et deux dates
format date : '2015-12-12 18:25:11+01:00'
'''
def getHttpHits(data, date1, date2):
    temp = data[(data['time'] >= date1) & (data['time'] <= date2)]
    return temp['request']

'''
Retourne les lignes du dataFrame selon une fenêtre de temps
'''
def getLogs(data, date1, date2):
    return data[(data['time'] >= date1) & (data['time'] <= date2)]

'''
Retourne toutes les ip (sans les doublons)

Prend en paramètres le dataFrame
'''
def getIpBase(data):
    return data['ip'].drop_duplicates()


'''
Retourne toutes les ip triées par nombre de hits décroissant 
Prend en paramètres le dataFrame
'''
def getIps(data):
    temp = data.groupby(['ip']).size().reset_index(name='counts')
    return temp[['ip','counts']].sort_values(by='counts', ascending=False)