import requests
import json

from typing import Any
from .headers import Headers
from .helpers import *

BASE_URL = "https://cdx.epa.gov/WQXWeb/api/"


class CDX:
    def __init__(
        self,
        user_id=None,
        cdx_key=None,
        file_path=None,
        file_name=None,
    ) -> None:
        self.user_id = user_id
        self.cdx_key = cdx_key
        self.file_path = file_path
        self.file_name = file_name
        self.headers = Headers(user_id, cdx_key, file_name)

    def call(self, endpoint: str, method: str, **kwargs) -> str:
        url = BASE_URL + endpoint
        with requests.Session() as session:
            req = requests.Request(method, url, **kwargs).prepare()
            headers = self.headers.options(method, req.url)
            headers.update(req.headers)
            req.prepare_headers(headers=headers)
            response = session.send(req)
            content = json.loads(response.content.decode("utf-8"))
        return content

    def upload(self) -> str:
        return self.call(f"Upload/{self.file_name}", "POST", data=retrieve_data(self.file_path))

    def start_import(self, file_id: str, config_id: int, params: dict = {}) -> str:
        return self.call("StartImport", "GET", params=import_params(file_id, config_id, params))

    def get_status(self, dataset_id: str) -> dict:
        return self.call("GetStatus", "GET", params={"datasetId": dataset_id})

    def submit_to_cdx(self, dataset_id: str) -> dict:
        return self.call("SubmitDatasetToCdx", "GET", params={"datasetId": dataset_id})

    # TODO Create the rest of the endpoints