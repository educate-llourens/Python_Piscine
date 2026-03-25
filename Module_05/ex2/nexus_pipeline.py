#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Union, Dict
from collections import defaultdict


class ProcessingStage(Protocol):
    """
    Interface for stages using duck typing. Any class with process() can act
    as a stage

    Args:
        Protocol (_type_): _description_
    """
    def process(self, data: Any) -> Any: ...


# CREATING THE PIPELINE *******************************************************
class ProcessingPipeline(ABC):
    """
    Abstract base managing stages. contains a list of stages and orchestrates
    data flow
    """
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


# STAGE CLASSES ***************************************************************
class InputStage:
    def process(self, data: Any) -> Dict:
        return_dict: dict = {}
        return return_dict


class TransformStage:
    def process(self, data: Any) -> Dict:
        return_dict: dict = {}
        return return_dict


class OutputStage:
    def process(self, data: Any) -> str:
        return_str: str = ""
        return return_str


# ADAPTER CLASSES *************************************************************
class JSONAdapterPipeLine(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        pass


class CSVAdapterPipeLine(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        pass


class StreamAdapterPipeLine(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        pass


# NEXUS MANAGER ***************************************************************
class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)


# PRINT EXAMPLE ***************************************************************
def main() -> None:
    # Variable declarations -----------------------------------------
    nexus_overlord = NexusManager()

    input_stage: InputStage = InputStage()
    transform_stage: TransformStage = TransformStage()
    output_stage: OutputStage = OutputStage()
    json_pipeline: JSONAdapterPipeLine = JSONAdapterPipeLine("JSON_01")
    csv_pipeline: CSVAdapterPipeLine = CSVAdapterPipeLine("CSV_01")
    stream_pipeline: StreamAdapterPipeLine = StreamAdapterPipeLine("STREAM_01")
    stages_list = [input_stage, transform_stage, output_stage]
    adapters_list = [json_pipeline, csv_pipeline, stream_pipeline]

    json_data: dict = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv_data: str = "user,action,timestamp"
    stream_data: str = "Real-time sensor stream"

    # Header --------------------------------------------------------
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    # Initialise NexusManager ---------------------------------------
    if nexus_overlord:
        print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    # Creating a pipeline -------------------------------------------
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    json_pipeline.add_stage(input_stage)
    print("Stage 2: Data transformation and enrichment")
    json_pipeline.add_stage(transform_stage)
    print("Stage 3: Output formatting and delivery\n")
    json_pipeline.add_stage(output_stage)
    nexus_overlord.add_pipeline(json_pipeline)

    # Creating next two pipelines -----------------------------------
    for pipeline in [csv_pipeline, stream_pipeline]:
        pipeline.add_stage(input_stage)
        pipeline.add_stage(transform_stage)
        pipeline.add_stage(output_stage)
        nexus_overlord.add_pipeline(pipeline)

    # Demonstrate pipeline works with any data ----------------------
    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    print('Input: {"sensor": "temp", "value": 23.5, "unit": "C"}')
    print("Transform: Enriched with metadata and validation")
    # Process data and print return string
    print("")
    print("")
    print("Processing CSV data through same pipeline...")
    print('Input: "user,action,timestamp"')
    print("Transform: Parsed and structured data")
    # Process data and print return string
    print("")
    print("Processing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    # Process data and print return string
    print("")
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print("")
    print("Chain result: 100 records processed through 3-stage pipeline")
    print("Performance: 95% efficiency, 0.2s total processing time")
    print("")
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    # Force failures and print errors
    print("")
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
