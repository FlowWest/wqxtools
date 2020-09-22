from dataclasses import dataclass
from typing import Any


@dataclass
class ValidData:
    data: Any


def import_params(file_id):
    # review params
    return {
        "importConfigurationId": "import_config",
        "fileId": file_id,
        "fileType": "CSV",
        "newOrExistingData": 1,
        "uponCompletion": "0",
        "uponCompletionCondition": "0",
        "worksheetsToImport": "1",
        "ignoreFirstRowOfFile": True,
    }
