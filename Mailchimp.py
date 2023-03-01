from mailchimp_marketing import *
from pprint import pprint

from dotenv import load_dotenv
import os
load_dotenv()
# env variables loaded

Mailchimp = Client() #instantiates a mailchimp client