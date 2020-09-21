from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Headers:
    user_id: str
    cdx_key: str
    data: Any
    endpoint: str
    timestamp: str = field(default=datetime.strftime(datetime.utcnow(), "%m/%d/%Y %I:%M:%S %p"))

    def __post_init__(self):
        self.endpoint = "{}/{}".format(self.endpoint, self.data.name)
        self.cdx_key = base64.b64decode(self.cdx_key)

    def options(self, method: str = "GET"):
        signature = bytes(
            "{}{}{}{}".format(self.username, self.timestamp, self.endpoint, method), "utf-8"
        )
        signature_bytes = base64.b64encode(
            hmac.new(key=self.endpoint, msg=signature, digestmod="sha256").digest()
        )
        return {
            "X-UserID": self.user_id,
            "X-Stamp": self.timestamp,
            "X-Signature": signature_bytes.decode("utf-8"),
        }
