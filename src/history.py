from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from src.files import JSONManager


class OperationType(Enum):
    SAVING = "Saving"
    ENCRYPTING = "Encrypting"
    DECRYPTING = "Decrypting"
    LOADING = "Loading"



@dataclass
class Record:
    operation: OperationType
    input_text: str
    output_text: str
    shift: int
    time: datetime = datetime.now()

    def __str__(self):
        message = (
            f"Time: {self.time.strftime("%m/%d/%Y, %H:%M:%S")} \n"
            f"Operation: {self.operation.value} \n"
            f"Original text: {self.input_text}, Result: {self.output_text} shift: {self.shift}\n"
            f"Json: {JSONManager.load_from_json('history.json')}\n"
        )
        return message

    def to_dict(self):
        data = asdict(self)
        data['operation'] = self.operation.value
        data['time'] = self.time.strftime('%Y-%m-%d %H:%M:%S')
        return data
