import base64
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Headers:
    user_id: str
    cdx_key: str
    file_name: str
    timestamp: str = field(default=datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p"))

    def __post_init__(self):
        self.cdx_key = base64.b64decode(self.cdx_key)

    def options(self, method: str = "GET", uri: str ) -> dict:
        signature = bytes(
            "{}{}{}{}".format(self.username, self.timestamp, uri, method), "utf-8"
        )
        signature_bytes = base64.b64encode(
            hmac.new(key=self.cdx_key, msg=signature, digestmod="sha256").digest()
        )
        return {
            "X-UserID": self.user_id,
            "X-Stamp": self.timestamp,
            "X-Signature": signature_bytes.decode("utf-8"),
        }
