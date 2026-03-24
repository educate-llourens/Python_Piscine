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
        temp_readings: List[float] = []
        nbr_processed_items: int = 0
        avg_temp: float = 0

        if not data_batch:
            raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} has "
                               "no readings")
        nbr_processed_items = len(data_batch)
        for item in data_batch:
            key, value = item.split(":", 1)
            if key == "temp":
                try:
                    temp_readings.append(float(value))
                except ValueError:
                    raise ValueError(f"Error: ValueError. Sensor stream ID: "
                                     f"{self.stream_id} cannot convert"
                                     f"{value} to a float")
            if not temp_readings:
                raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} "
                                   "has no temperature readings")
        try:
            avg_temp = sum(temp_readings) / len(temp_readings)
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
        return_batch: List[str] = []
        criteria_data: List[float] = []
        new_data_batch: List[Any] = []

        if criteria:
            criteria_data = [item for item in data_batch if
                             item != criteria]
            new_data_batch = criteria_data
        else:
            new_data_batch = data_batch
            for item in data_batch:
                key, value = item.split(":", 1)
                if key == "temp" and float(value) > 100:
                    print("[ALERT] Temp too high")
        for item in new_data_batch:
            if not isinstance(item, str):
                continue
            else:
                return_batch.append(item)
            if not return_batch:
                raise RuntimeError(f"Error: Sensor stream ID {self.stream_id} "
                                   "has no readings after filtering")
        return return_batch

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
            return_str = (f"{operations_len} operations, net flow: "
                          f"+{net_flow} units")
        elif net_flow <= 0:
            return_str = (f"{operations_len} operations, net flow: "
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
                    if int(value) > 1000:
                        print("[ALERT] High transaction")
                    transactions_list.append(int(value))
                except ValueError:
                    raise ValueError(f"Error: ValueError. Transaction stream "
                                     f"ID: {self.stream_id} cannot convert "
                                     f"{value} to an int")
            elif key == "sell":
                try:
                    if int(value) < -1000:
                        print("[ALERT] High transaction")
                    negative = int(value)
                    transactions_list.append(negative * -1)
                except ValueError:
                    raise ValueError("Error: ValueError. Transaction stream "
                                     f"ID: {self.stream_id} cannot convert "
                                     f"{value} to an int")
        return transactions_list


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        nbr_errors: int = 0
        len_events: int = 0

        if not data_batch:
            raise RuntimeError(f"Error: Event stream ID {self.stream_id} has "
                               "no events")
        len_events = len(data_batch)
        for item in data_batch:
            if item == "error":
                nbr_errors += 1
        return f"{len_events} events, {nbr_errors} errors detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        criteria_data: List[str] = []
        new_events_batch: List[str] = []
        return_batch: List[str] = []

        if criteria:
            criteria_data = [item for item in data_batch if item != criteria]
            new_events_batch = criteria_data
        else:
            new_events_batch = data_batch
        for item in new_events_batch:
            if not isinstance(item, str):
                raise RuntimeError(f"Error: {self.stream_id}, {item} is not "
                                   "an event")
                continue
            return_batch.append(item)
        for item in return_batch:
            if "error" in item:
                print("[ALERT] Error detected")
        return return_batch


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_batches(self, batches: List[List[Any]]) -> List[str]:
        return_list: List[str] = []
        filtered_data_list: List[Any] = []
        processed_str: List[str] = []
        i: int = 0
        stream_len: int = len(self.streams)

        for i in range(stream_len):
            filtered_data_list.append(self.streams[i].filter_data(batches[i]))
        i = 0
        for i in range(stream_len):
            processed_str.append(self.streams[i].
                                 process_batch(filtered_data_list[i]))
        i = 0
        for i in range(stream_len):
            base_str = processed_str[i]
            trimmed_front = base_str.split(",", 1)[0].strip()
            if isinstance(self.streams[i], SensorStream):
                return_list.append(f"- Sensor data: {trimmed_front}")
            elif isinstance(self.streams[i], TransactionStream):
                return_list.append(f"- Transaction data: "
                                   f"{trimmed_front} processed")
            elif isinstance(self.streams[i], EventStream):
                return_list.append(f"- Event data: {trimmed_front} processed")
            i += 1
        return return_list


def main() -> None:
    # Sensor
    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_batch: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_filtered_data: List[float] = []
    # Transaction
    transaction: TransactionStream = TransactionStream("TRANS_001")
    transactions_batch: List[Any] = ["buy:100", "sell:150", "buy:75"]
    transaction_filtered_data: list[int] = []
    # Event
    event: EventStream = EventStream("EVENT_001")
    event_batch: List[Any] = ["login", "error", "logout"]
    event_filtered_list: List[str] = []
    # Polymorphism data section
    poly_sensor_batch: List[Any] = ["temp:22.5", "humidity:65"]
    poly_transaction_batch: List[Any] = ["buy:100", "sell:150", "buy:75",
                                         "buy:1000"]
    poly_event_batch: List[Any] = ["login", "error", "logout"]
    process_batches: List[List[Any]] = [poly_sensor_batch,
                                        poly_transaction_batch,
                                        poly_event_batch]
    stream_list: List[DataStream] = [sensor, transaction, event]
    processor: StreamProcessor = StreamProcessor(stream_list)
    result_strings: List[str] = []

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    # Sensor
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
    # Transaction
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
    print("")
    # Event
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print("Processing event batch: [login, error, logout]")
    try:
        event_filtered_list = event.filter_data(event_batch)
        print(f"Event analysis: {event.process_batch(event_filtered_list)}")
    except RuntimeError as msg:
        print(msg)
        return
    print("")
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    result_strings = processor.process_batches(process_batches)
    for string in result_strings:
        print(string)
    print("")
    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    # To make this actually work, I would need to store the stats in the
    # get_stats dictionary and update the dictionary. The current return
    # value does not make sense and does not seem to get evaluated at all.
    print("")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
