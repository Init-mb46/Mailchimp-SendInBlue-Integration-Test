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

contact = CreateContact(
    email= "test2@gmail.com",
    attributes= {"FIRSTNAME":"James", "LASTNAME":"Zucker"},
    list_ids=[5] #"waiting list"
)
# contact object is created, a template can be found in "SIB_CONTACT_TEMPLATE.json"

# contact = UpdateContact(
#     attributes= {"FIRSTNAME":"JAMES"}
# ) 
# above code can update select attributes of a contact, the update_contact() method requires an id/email parameter and the UpdateContact object

try:
    res = API.create_contact(contact) # creates the contact using the api and stores the response
    pprint(res) 
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e) # prints any errors, will tell if the contact exists already.

