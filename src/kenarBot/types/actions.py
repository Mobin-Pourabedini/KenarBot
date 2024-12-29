from abc import ABC, abstractmethod
from enum import Enum
from typing import Mapping


class ActionType(Enum):
    DIRECT_LINK = "open_direct_link"
    SERVER_LINK = "open_server_link"


class Action(ABC):
    @abstractmethod
    def __init__(self, action_type: ActionType):
        self.type = action_type

    @abstractmethod
    def to_dict(self):
        pass


class OpenDirectLink(Action):
    def __init__(self, url: str):
        super().__init__(ActionType.DIRECT_LINK)
        self.url = url

    def to_dict(self) -> dict:
        return {
            "open_direct_link": self.url
        }


class OpenServerLink(Action):
    def __init__(self, extra_data: Mapping[str, str]):
        super().__init__(ActionType.SERVER_LINK)
        self.extra_data = extra_data

    def to_dict(self):
        return {
            "open_server_link": {
                "data": self.extra_data
            }
        }
