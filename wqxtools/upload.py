import requests
import json
import base64
import hmac
from typing import Any
from datetime import datetime
from wqxtools.headers import Headers


class CDX:
    BASE_URL = 'https://cdx.epa.gov/WQXWeb/api/'
        def __init__(self, user_id: str, cdx_key: str, data: Any) -> None:
            self.user_id = user_id
            self.cdx_key = cdx_key
            self.data = data
            self.headers = Headers(user_id, cdx_key, data.get("name"))

    def upload(self):
        uri = BASE_URL + "Upload"
        resp = requests.post(url=uri, headers=self.headers.options("POST", uri), data=self.data)
        content = json.loads(resp.content.decode("utf-8"))
        return {"status_code": resp.status_code, "content": content}

    def start_import(self, file_id) -> dict:
    start_import_endpoint = "https://cdx.epa.gov/WQXWeb/api/StartImport"
    params = {
        "importConfigurationId": import_config,
        "fileId": file_id,
        "fileType": 'CSV',
        "newOrExistingData": 1,
        "uponCompletion": '0',
        "uponCompletionCondition": '0',
        "worksheetsToImport": '1',
        "ignoreFirstRowOfFile": True
    }