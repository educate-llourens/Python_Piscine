#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        raise NotImplementedError("Subclasses must implement process()")

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError("Subclasses must implement validate()")

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            print("NumericProcessor: data is not a list")
            return False
        for nbr in data:
            if type(nbr) is not int:
                print(f"NumericProcessor: {nbr} is not an int")
                return False
        return True

    def process(self, data: Any) -> str:
        len_list: int = len(data)
        total_nbrs: int = sum(data)
        average_nbrs: float = total_nbrs / len_list
        return (f"Processed {len_list} numeric values, "
                f"sum={total_nbrs}, avg={average_nbrs:.2f}")

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        split_str: list[str] = data.split(" ")
        if type(data) is not str:
            print("TextProcessor: data is not a str")
            return False
        for item in split_str:
            if type(item) is not str:
                print("TextProcessor: data({item}) is not a string")
                return False
        return True

    def process(self, data: Any) -> str:
        len_characters: int = len(data)
        split_str: list[str] = data.split(" ")
        len_words: int = len(split_str)
        return (f"Processed text: {len_characters} characters, "
                f"{len_words} words")

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            print("LogProcessor: data is not a str")
            return False
        if "INFO" in data:
            return True
        if "ERROR" in data:
            return True
        return False

    def process(self, data: Any) -> str:
        split_list: list[str] = data.split(":", 1)
        alert_type: str = split_list[0]
        alert_msg: str = split_list[1]
        return f"[ALERT] {alert_type} level detected:{alert_msg}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    nbrs: NumericProcessor = NumericProcessor()
    numeric_output_str: str = nbrs.process([1, 2, 3, 4, 5])
    text: TextProcessor = TextProcessor()
    text_output_str: str = text.process("Hello Nexus World")
    log: LogProcessor = LogProcessor()
    log_output_str: str = log.process("ERROR: Connection timeout")
    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    input: Any = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]
    i: int = 1
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")
    print("Initializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Validation: ", end="")
    if nbrs.validate([1, 2, 3, 4, 5]):
        print(" Numeric data verified")
        print(nbrs.format_output(numeric_output_str))
    else:
        print("Numeric data NOT verified")
    print("")
    print("Initializing Text Processor...")
    print("Processing data: 'Hello Nexus World'")
    print("Validation: ", end="")
    if text.validate("Hello Nexus World"):
        print(" Text data verified")
        print(text.format_output(text_output_str))
    else:
        print("Text data NOT verified")
    print("")
    print("Initializing Log Processor...")
    print("Processing data: 'ERROR: Connection timeout'")
    print("Validation: ", end="")
    if log.validate("ERROR: Connection timeout"):
        print("Log entry verified")
        print(log.format_output(log_output_str))
    else:
        print("Log data NOT verified")
    print("")
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    while i <= 3:
        processor = processors[i - 1]
        data = input[i - 1]
        print(f"Result {i}: ", end="")
        try:
            if processor.validate(data):
                print(processor.process(data))
            else:
                print("invalid data")
        except Exception as msg:
            print(f"Polymorphic processing error: {msg}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
