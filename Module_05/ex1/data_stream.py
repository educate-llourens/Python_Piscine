#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        raise NotImplementedError("Subclass must implement process_batch")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        dictionary: dict = {}
        return dictionary


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            print(f"Error: Stream ID {self.stream_id} has no readings")
            return ""
        return "Sensor analyses: "

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        else:
            data_batch = [item for item in data_batch if item != criteria]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        dictionary: dict = {
            "stream_id": None,
            "type": "Environmental Data"
        }
        return dictionary


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        else:
            data_batch = [item for item in data_batch if item != criteria]
        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        else:
            data_batch = [item for item in data_batch if item != criteria]
        return data_batch


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    print("Initializing Sensor Stream...")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")


if __name__ == "__main__":
    main()
