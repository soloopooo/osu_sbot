class IDNotFoundException(Exception):
    def __init__(self, reason="Please Give us a valid ID.") -> None:
        self.name = "IDNotFoundException"
        self.reason = reason


class DataNotFoundException(Exception):
    def __init__(
        self, reason="Peppy's server are down again...? OR YOU ARE NOT TRUE..."
    ) -> None:
        self.name = "DataNotFoundException"
        self.reason = reason


class BPNumNotValidException(Exception):
    def __init__(self, reason="Not a valid bp num, 10 or 100.") -> None:
        self.name = "BPNumNotValidException"
        self.reason = reason


class APIGetException(Exception):
    def __init__(
        self, reason="API get failed... Please wait for a while.", code=500
    ) -> None:
        self.name = "APIGetException"
        self.code = code
        self.reason = reason

class NoMoreDataException(Exception):
    def __init__(self, reason = "No more data available...") -> None:
        self.name = "NoMoreDataException"
        self.reason = reason