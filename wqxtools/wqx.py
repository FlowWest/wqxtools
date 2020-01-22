import requests
import base64
import hmac
from datetime import datetime


class WQXweb(object):

    def __init__(self, username, pk):
        self.pk = pk
        self.username = username

    def make_hedears(self):
        stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")


    def mon_locations(self, org_id: str):
        return "you made a call to {}".format(org_id)

    def proj_locations(self, org_id: str):

