import csv

from io import StringIO, BytesIO
from dataclasses import dataclass
from typing import Any


def generate_csv(data):
    headers = data[0].keys()
    proxy = StringIO()
    writer = csv.writer(proxy)
    writer.writerow(headers)
    new_arr = [row.values() for row in data]
    [writer.writerow(row) for row in new_arr]
    buffer = BytesIO()
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
