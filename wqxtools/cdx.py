import requests
import json

from typing import Any
from .headers import Headers
from .helpers import *

BASE_URL = "https://cdx.epa.gov/WQXWeb/api/"


class CDX:
    def __init__(self, user_id: str, cdx_key: str, data: ValidData, file_name: str) -> None:
        self.user_id = user_id
        self.cdx_key = cdx_key
        self.data = data
        self.headers = Headers(user_id, cdx_key, file_name)

    def call(self, endpoint: str, method: str, *args, **kwargs) -> dict:
        url = BASE_URL + endpoint
        session = requests.Session()
        req = requests.Request(
            method, url, kwargs, headers=self.headers.options(method, url)
        ).prepare()
        response = session.send(req)
        content = json.loads(response.content.decode("utf-8"))
        # error logging should happen here
        return {"status_code": response.status_code, "content": content}

    def upload(self) -> dict:
        return self.call("Upload", "POST", data=generate_csv(self.data))

    def start_import(self, file_id: str) -> dict:
        return self.call("StartImport", "GET", params=import_params(file_id))

    def get_status(self, dataset_id: str) -> dict:
        return self.call("GetStatus", "GET", params={"datasetId": dataset_id})

    def submit_to_cdx(self, dataset_id: str) -> dict:
        return self.call("SubmitDatasetToCdx", "GET", params={"datasetId": dataset_id})
