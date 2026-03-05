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
        return result
        ...


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            raise TypeError("NumericProcessor: data is not a list")
            return False
        for nbr in data:
            if type(nbr) is not int:
                raise TypeError(f"NumericProcessor: {nbr} is not an int")
                return False
        return True


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            raise TypeError("TextProcessor: data is not a list")
            return False
        for string in data:
            if type(string) is not str:
                print(f"TextProcessor: {string} is not a string")
                return False
        return True


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            raise TypeError("LogProcessor: data is not a str")
        