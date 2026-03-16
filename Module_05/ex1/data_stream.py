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
        new_data_batch: List[Any] = []

        if criteria:
            criteria_data = [item for item in data_batch if
                             item != criteria]
            new_data_batch = criteria_data
        else:
            new_data_batch = data_batch
        for item in new_data_batch:
            if not isinstance(item, str):
                continue
            key, value = item.split(":", 1)
            if key == "temp":
                try:
                    temp_readings.append(float(value))
                except ValueError:
                    raise ValueError(f"Error: ValueError. Sensor stream ID: "
                                     f"{self.stream_id} cannot convert"
                                     f"{value} to a float")
            else:
                continue
            if not temp_readings:
                raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} "
                                   "has no temperature readings")
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
        net_flow: int = 0
        return_str: str = ""
        operations_len: int = len(data_batch)

        if not data_batch:
            raise RuntimeError(f"Error: Transaction stream ID {self.stream_id}"
                               " has no transactions")
        net_flow = sum(data_batch)
        if net_flow > 0:
            return_str = (f"{operations_len} operations, net flow "
                          f"+{net_flow} units")
        elif net_flow <= 0:
            return_str = (f"{operations_len} operations, net flow "
                          f"{net_flow} units")
        return return_str

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        transactions_list: List[int] = []
        criteria_data: List[int] = []
        new_transaction_batch: List[Any] = []
        negative: int = 0

        if criteria:
            criteria_data = [item for item in data_batch if item != criteria]
            new_transaction_batch = criteria_data
        else:
            new_transaction_batch = data_batch
        for item in new_transaction_batch:
            if not isinstance(item, str):
                continue
            key, value = item.split(":", 1)
            if key == "buy":
                try:
                    transactions_list.append(int(value))
                except ValueError:
                    raise ValueError(f"Error: ValueError. Transaction stream "
                                     f"ID: {self.stream_id} cannot convert "
                                     f"{value} to an int")
            elif key == "sell":
                try:
                    negative = int(value)
                    transactions_list.append(negative * -1)
                except ValueError:
                    raise ValueError("Error: ValueError. Transaction stream "
                                     f"ID: {self.stream_id} cannot convert "
                                     f"{value} to an int")
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
    sensor_batch: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_filtered_data: List[float] = []
    transaction: TransactionStream = TransactionStream("TRANS_001")
    transactions_batch: List[Any] = ["buy:100", "sell:150", "buy:75"]
    transaction_filtered_data: list[int] = []

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    try:
        sensor_filtered_data = sensor.filter_data(sensor_batch)
        print(f"Sensor analysis: {sensor.process_batch(sensor_filtered_data)}")
    except (RuntimeError, TypeError, ValueError) as msg:
        print(msg)
        return
    print("")
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    try:
        transaction_filtered_data = transaction.filter_data(transactions_batch)
        print("Transaction analysis: "
              f"{transaction.process_batch(transaction_filtered_data)}")
    except (RuntimeError, ValueError) as msg:
        print(msg)
        return


if __name__ == "__main__":
    main()
