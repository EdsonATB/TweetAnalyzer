from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

MINIMUN_TWEETS = 10
QUERY = 'chatgpt'

#*Credenciais de login
config = ConfigParser()
config.read('config.ini')
username = config['X'][username]
email = config['X'][email]
password = config['X'][password]

#Waiting on Twitter Unban for further developing and testing :/