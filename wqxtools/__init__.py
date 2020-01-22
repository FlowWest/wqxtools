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


def monitoring_locations(org_id: str, pk: str, username: str):
    """Endpoint to the WQX Monitoring Locations

    Use this function to return data about monitoring locations
    for a given organization.

    Parameters
    ----------
    org_id: organization id
    pk: private key obtained from wqx web
    username: username obtained from wqx web
    """
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/MonitoringLocations"
    params = {"OrganizationIdentifiersCsv": org_id}
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    # prepare the request, we need to use requests in this way since
    # the signature needed in the header needs a fully constructed url
    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()

    headers = make_header(p.url, pk, username, stamp, "GET")

    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    r.close()
    s.close()
    j = json.loads(content)
    return {'status_code': status_code, 'content': j}


def projects(org_id: str, pk: str, username: str):
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/Projects"
    params = {"OrganizationIdentifiersCsv": org_id}
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()
    headers = make_header(p.url, pk, username, stamp, "GET")

    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    r.close()
    s.close()
    j = json.loads(content)
    return {'status_code': status_code, 'content': j}

def upload(filename: str, filepath: str, pk: str, username: str):
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/Upload"
    uri = "{}/{}".format(api_endpoint, filename) # hack
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")
    headers = make_header(uri, pk, username, stamp, "POST")

    with open(filepath, "rb") as f:
        file_data = f.read()

    files = {filename: file_data}
    resp = requests.post(url = uri, headers=headers, files=files)
    return resp.content

def start_import(pk: str, username: str, import_config: str, file_id: str, file_type: str,
                 new_or_existing: str, upon_completion: int = 0,
                 upon_completion_cond: int = 0, headers: bool = True):

    file_cond = {'both': 0, 'new': 1, 'existing': 2}[new_or_existing]
    first_row_is_header = {True: "true", False: "false"}[headers]
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/StartImport"
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    params = {
        "importConfigurationId": import_config,
        "fileId": file_id,
        "fileType": file_type,
        "newOrExistingData": file_cond,
        "uponCompletion": upon_completion,
        "uponCompletionCondition": upon_completion_cond,
        "worksheetsToImport": '1',
        "ignoreFirstRowOfFile": first_row_is_header
    }

    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()
    headers = make_header(p.url, pk, username, stamp, "GET")
    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    r.close()
    s.close()

def upload_attachment(filename: str, pk: str, username: str):
    pass

def xml_export(dataset_id: str, upon_completion: int):
    pass

def submit_to_cdx(dataset_id: str):
    pass

def submit_file_to_cdx(field: str):
    pass

def get_status(dataset_id: str, pk: str, username: str) -> dict:
    api_endpoint = "https://cdx.epa.gov/WQXWeb/api/GetStatus"
    params = {"datasetId": dataset_id}
    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()
    headers = make_header(p.url, pk, username, stamp, "GET")

    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = r.content.decode("utf-8")
    r.close()
    s.close()
    j = json.loads(content)
    return {'status_code': status_code, 'content': j}

def get_document_list(dataset_id: str):
    pass

