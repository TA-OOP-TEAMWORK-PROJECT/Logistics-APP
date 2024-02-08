from datetime import datetime

class EventLog:

    def __init__(self, description: str):
        if len(description) == 0:
            raise ValueError("Put something in the description mate. Can't have it empty!")

        self._description = description
        self._timestamp = datetime.now().strftime("%Y/%m/%d, %X")


    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        return f'[{self._timestamp}] {self._description}'