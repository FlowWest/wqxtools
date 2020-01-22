import json
import requests
import base64
import hmac
from datetime import datetime


# construct the header needed for all the api calls
def make_header(uri: str, pk: str, username: str, stamp: str, method: str) -> dict:
    data = "{}{}{}{}".format(username, stamp, uri, method)
    # get the byte representation of the data formatted in utf-8
    signature = bytes(data, "utf-8")
    pk_decoded = base64.b64decode(pk)
    signature_bytes = base64.b64encode(hmac.new(key=pk_decoded, msg=signature, digestmod='sha256').digest())
    signature_string = signature_bytes.decode('utf-8')
    return {'X-UserID': username, 'X-Stamp': stamp, 'X-Signature': signature_string}

def wqx_monitoring_locations(orgid: str, pk: str, username: str):
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/MonitoringLocations"
    params = {"OrganizationIdentifiersCsv": orgid}
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    # prepare the request
    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()

    headers = make_header(p.url, pk, username, stamp, "GET")

    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    r.close()
    j = json.loads(content)
    return {'status_code': status_code, 'content': j}

