import json
from dataclasses import dataclass
from typing import Any


def retrieve_data(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_data = f.read()
    return file_data


def import_params(file_id, config_id, params={}):
    return {
        "importConfigurationId": config_id,
        "fileId": file_id,
        "fileType": params.get("fileType", "CSV"),
        "newOrExistingData": params.get("newOrExistingData", "2"),
        "uponCompletion": params.get("uponCompletion", "2"),
        "uponCompletionCondition": params.get("uponCompletionCondition", "2"),
        "worksheetsToImport": params.get("worksheetsToImport", "1"),
        "ignoreFirstRowOfFile": params.get("ignoreFirstRowOfFile", True),
    }


#  TODO remove this logic unless we want to give the user
# an option to pass data directly instead of a file path

# import pandas as pd
# from io import StringIO, BytesIO

# def generate_csv(data):
#     proxy = StringIO()
#     buffer = BytesIO()
#     pd.read_json(json.dumps(data)).to_csv(proxy, index=None)
#     buffer.write(proxy.getvalue().encode("utf-8"))
#     buffer.seek(0)
#     return buffer.read()


# @dataclass
# class ValidData:
#     data: Any
