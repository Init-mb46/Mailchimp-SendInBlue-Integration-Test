#NOTE: All api client instantiation and list ids should go in the main file, these should be given as parameters to the mailchimp and sendinblue api handler files

from mailchimp_marketing import *
from mailchimp_marketing.api_client import ApiClientError
from pprint import pprint

from dotenv import load_dotenv
import os
load_dotenv()
# env variables loaded

Mailchimp = Client() #instantiates a mailchimp client
Mailchimp.set_config({
    "api_key":f"{os.getenv('MC_API_KEY')}",
    "server": "us21"
})

def get_members(listID:str, fields:list = [], count:int = 1000):
    try: 
        members = Mailchimp.lists.get_list_members_info(listID, fields=fields, count=count)
        return members
    except ApiClientError as e:
        print("Exception when fetching contacts: %s\n" % e)