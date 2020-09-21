# import requests
import json
import base64
import hmac
from typing import Any
from datetime import datetime
from wqxtools.headers import Headers


# class Upload:
#     # upload_endpoint = "https://cdx.epa.gov/WQXWeb/api/Upload"
#     def __init__(self, user_id: str, cdx_key: str, data: Any, endpoint: str) -> None:
#         self.user_id = user_id
#         self.cdx_key = cdx_key
#         self.data = data
#         self.endpoint = endpoint
#         self.timestamp = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p")

#     def send(self):
#         resp = requests.post(url=url, headers=headers, data=file_data)
#         status_code = resp.status_code
#         content = json.loads(resp.content.decode("utf-8"))
#         return {"status_code": status_code, "content": content}

print(Headers())