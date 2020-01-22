import json
import requests
import base64
import hmac
from datetime import datetime


def wqx_monitoring_locations(orgid: str, pk: str, username: str):
    # handle headers
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/MonitoringLocations"
    params = {"OrganizationIdentifiersCsv": orgid}
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    # prepare the request
    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()
    uri = p.url

    data = "{}{}{}{}".format(username, stamp, uri, "GET")
    # get the byte representation of the data formatted in utf-8
    signature = bytes(data, "utf-8")
    pk_decoded = base64.b64decode(pk)
    signature_bytes = base64.b64encode(hmac.new(key=pk_decoded, msg=signature, digestmod='sha256').digest())
    signature_string = signature_bytes.decode('utf-8')
    headers = {'X-UserID': username, 'X-Stamp': stamp, 'X-Signature': signature_string}
    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    j = json.loads(content)
    r.close()
    return {'status_code': status_code, 'content': j}

