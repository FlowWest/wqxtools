import json
import requests
import base64
import hmac
from datetime import datetime


# construct the header needed for all the api calls
def make_get_header(uri: str, pk: str, username: str, stamp: str, method: str) -> dict:
    data = "{}{}{}{}".format(username, stamp, uri, method)
    # get the byte representation of the data formatted in utf-8
    signature = bytes(data, "utf-8")
    pk_decoded = base64.b64decode(pk)
    signature_bytes = base64.b64encode(hmac.new(key=pk_decoded, msg=signature, digestmod='sha256').digest())
    signature_string = signature_bytes.decode('utf-8')
    return {'X-UserID': username, 'X-Stamp': stamp, 'X-Signature': signature_string}


# all get request share the process, a bit weird but we need the fully constructed url to
# have the correct message for HMAC256  so we need to use the requests API this way
def prepare_and_send_get(api_endpoint: str, params: dict, pk: str, username: str) -> dict:

    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")
    s = requests.Session()
    p = requests.Request("GET", api_endpoint, params=params).prepare()

    headers = make_get_header(p.url, pk, username, stamp, "GET")

    p.prepare_headers(headers=headers)
    r = s.send(p)
    status_code = r.status_code
    content = json.loads(r.content.decode("utf-8"))
    r.close()
    s.close()
    return {"status_code": status_code, "content": content}


def monitoring_locations(org_id: str, pk: str, username: str) -> dict:
    monitoring_locations_endpoint = "https://cdx.epa.gov/WQXWeb/api/MonitoringLocations"
    params = {"OrganizationIdentifiersCsv": org_id}

    return prepare_and_send_get(monitoring_locations_endpoint, params, pk, username)


def projects(org_id: str, pk: str, username: str) -> dict:
    projects_endpoint = "https://cdx.epa.gov/WQXWeb/api/Projects"
    params = {"OrganizationIdentifiersCsv": org_id}

    return prepare_and_send_get(projects_endpoint, params, pk, username)


def upload(filename: str, filepath: str, pk: str, username: str):
    upload_endpoint = "https://cdx.epa.gov/WQXWeb/api/Upload"
    url = "{}/{}".format(upload_endpoint, filename)

    stamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")
    msg_data = "{}{}{}{}".format(username, stamp, url, "POST")
    signature = bytes(msg_data, "utf-8")
    pk_decoded = base64.b64decode(pk)
    signature_bytes = base64.b64encode(hmac.new(key=pk_decoded, msg=signature, digestmod='sha256').digest())
    signature_string = signature_bytes.decode('utf-8')
    headers = {'X-UserID': username, 'X-Stamp': stamp, 'X-Signature': signature_string}

    with open(filepath, "rb") as f:
        file_data = f.read()

    files = {filename: file_data}
    resp = requests.post(url=url, headers=headers, files=files)
    status_code = resp.status_code
    content = json.loads(resp.content.decode("utf-8"))
    return {"status_code": status_code, "content": content}


def start_import(pk: str, username: str, import_config: str, file_id: str, file_type: str,
                 new_or_existing: str, headers: bool = True) -> dict:

    file_cond = {'both': 0, 'new': 1, 'existing': 2}[new_or_existing]
    first_row_is_header = {True: "true", False: "false"}[headers]
    start_import_endpoint = "https://cdx.epa.gov/WQXWeb/api/StartImport"

    params = {
        "importConfigurationId": import_config,
        "fileId": file_id,
        "fileType": file_type,
        "newOrExistingData": file_cond,
        "uponCompletion": '0',
        "uponCompletionCondition": '0',
        "worksheetsToImport": '1',
        "ignoreFirstRowOfFile": first_row_is_header
    }

    return prepare_and_send_get(start_import_endpoint, params, pk, username)


def get_status(dataset_id: str, pk: str, username: str) -> dict:
    status_endpoint = "https://cdx.epa.gov/WQXWeb/api/GetStatus"
    params = {"datasetId": dataset_id}

    return prepare_and_send_get(status_endpoint, params, pk, username)


# TODO: need implementation
def upload_attachment(filename: str, pk: str, username: str):
    pass


# TODO: need implementation
def xml_export(dataset_id: str, upon_completion: int):
    pass


def submit_to_cdx(dataset_id: str, pk: str, username: str):
    submit_cdx_edpoint = "https://cdx.epa.gov/WQXWeb/api/SubmitDatasetToCdx"
    params = {'datasetId': dataset_id}
    return prepare_and_send_get(submit_cdx_edpoint, params, pk, username)


# TODO: need implementation
def submit_file_to_cdx(field: str):
    pass


def get_document_list(dataset_id: str, pk: str, username: str):
    doc_list_endpoint = "https://cdx.epa.gov/WQXWeb/api/GetDocumentList"
    params = {"datasetId": dataset_id}
    return prepare_and_send_get(doc_list_endpoint, params, pk, username)

