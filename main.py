#from APIhandlers import SendInBlue
from APIhandlers import Mailchimp 
from pprint import pprint
# imports above are the modules in this project 
# this file will be used to integrate both apis through each file

audienceID = "775429d360" # list id for MailChimp
listID = 5 # list id for SendInBlue

pprint(Mailchimp.get_members(audienceID, fields=["members.email_address", "total_items"], count = 6)) # command to fetch up to 6 contact emails from the mail chimp list. 
