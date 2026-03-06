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
        return (f"Processed {len_list} numeric values,"
                f"sum={total_nbrs}, avg={average_nbrs:.2f}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            print("TextProcessor: data is not a list")
            return False
        for string in data:
            if type(string) is not str:
                print(f"TextProcessor: {string} is not a string")
                return False
        return True


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            print("LogProcessor: data is not a str")
            return False
        if '[ALERT]' in data:
            return True
        if '[INFO]' in data:
            return True
        return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")
    print("Initializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Validation: ", end="")
    nbrs: NumericProcessor = NumericProcessor()
    if nbrs.validate([1, 2, 3, 4, 5]):
        print(" Numeric data verified")
    else:
        print("Numeric data NOT verified")
    print(nbrs.format_output())


if __name__ == "__main__":
    main()
