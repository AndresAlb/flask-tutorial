# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:45:40 2020

@author: Andres Angeles Albores

App initializer
"""

from flask import Flask 
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
