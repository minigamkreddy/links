import re
import json
import serial
import sys
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger as logtoconsole
import time
import xmltodict
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import logging


from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC    # To use select
from selenium.webdriver.support.ui import WebDriverWait   # To use select

import subprocess
import ipaddress
from collections import Counter


import functools
