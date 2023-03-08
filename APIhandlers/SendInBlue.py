#NOTE: All api client instantiation and list ids should go in the main file, these should be given as parameters to the mailchimp and sendinblue api handler files

from sib_api_v3_sdk import *
from pprint import pprint 
from sib_api_v3_sdk.rest import ApiException

from dotenv import load_dotenv
import os
load_dotenv()
# env variables loaded

config = Configuration()
config.api_key['api-key'] = os.getenv('SIB_API_KEY')
API = ContactsApi(ApiClient(config))
# The contacts api client is created

def create_contacts(contacts: list = [], listid: int = None): 
    Contacts = []
    for i in range(len(contacts)):
        fname = ""
        lname = ""

        #NOTE: FIX TO ENABLE FIRSTNAME AND LAST NAME ADDITIONS, find send in blue import limit
        # if (contacts[i]["merge_fields"]):
        #     fname = contacts[i]["merge_fields"] and ["FNAME"] or ""
        #     lname = contacts[i]["merge_fields"]["FNAME"] or ""

        Contacts.append(CreateContact(
            email= contacts[i]['email_address'],
            attributes= {"FIRSTNAME": fname, "LASTNAME": lname},
            list_ids=[listid] 
        ))
    
    for c in Contacts:
        try:
            res = API.create_contact(c) # creates the contact using the api and stores the response
            pprint(res) 
        except ApiException as e:
            print("Exception when calling ContactsApi->create_contact: %s\n" % e) # prints any errors, will tell if the contact exists already.
