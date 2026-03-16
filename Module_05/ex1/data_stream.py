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
        nbr_processed_items: int = 0
        avg_temp: float = 0

        if not data_batch:
            raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} has "
                               "no readings")
        nbr_processed_items = len(data_batch)
        try:
            avg_temp = sum(data_batch) / nbr_processed_items
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Error: ZeroDivision. Sensor stream ID "
                  f"{self.stream_id} could not calculate avg temp")
        except TypeError:
            raise TypeError(f"Error: TypeError. Sensor stream ID "
                  f"{self.stream_id} received unfiltered data")
        return (f"{nbr_processed_items} readings processed, "
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        temp_readings: List[float] = []
        criteria_data: List[float] = []

        for item in data_batch:
            if not isinstance(item, str):
                continue
            key, value = item.split(":", 1)
            if key == "temp":
                temp_readings.append(float(value))
            else:
                continue
            if not temp_readings:
                raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} "
                                   "has no temperature readings")
            if criteria:
                criteria_data = [item for item in data_batch if
                                 item != criteria]
                return criteria_data
        return temp_readings

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        dictionary: dict = {
            "stream_id": self.stream_id
        }
        return dictionary


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            raise RuntimeError(f"Error: Transaction stream ID {self.stream_id} has "
                               "no transactions")
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
        if not data_batch:
            raise RuntimeError(f"Error: Event stream ID {self.stream_id} has "
                               "no events")
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        else:
            data_batch = [item for item in data_batch if item != criteria]
        return data_batch


def main() -> None:
    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_batch: list[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_filtered_data: List[float] = []

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    try:
        sensor_filtered_data = sensor.filter_data(sensor_batch)
        print(f"Sensor analysis: {sensor.process_batch(sensor_filtered_data)}")
    except (RuntimeError, TypeError) as msg:
        print(msg)
        return
    print("")
    print("Initializing Transaction Stream...")


if __name__ == "__main__":
    main()
