import json
import pandas as pd
from io import StringIO, BytesIO
from dataclasses import dataclass
from typing import Any


def generate_csv(data):
    proxy = StringIO()
    buffer = BytesIO()
    pd.read_json(json.dumps(data)).to_csv(proxy, index=None)
    buffer.write(proxy.getvalue().encode("utf-8"))
    buffer.seek(0)
    return buffer.read()


@dataclass
class ValidData:
    data: Any


def import_params(file_id, config_id):
    # review params
    return {
        "importConfigurationId": config_id,
        "fileId": file_id,
        "fileType": "CSV",
        "newOrExistingData": "1",
        "uponCompletion": "0",
        "uponCompletionCondition": "0",
        "worksheetsToImport": "1",
        "ignoreFirstRowOfFile": True,
    }
