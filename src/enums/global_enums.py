from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code ip not equal exepted."
    WRONG_ELEMENT_COUNT = "Number of items is not equal exepted."