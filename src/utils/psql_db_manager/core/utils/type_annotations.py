from typing import Protocol


class DatabaseConnectionData(Protocol):
    dbname: str
    user: str
    password: str
    host: str
    port: str

    def _asdict(self) -> dict:
        """
        This method converts the namedtuple to a dict.
        """
        ...
