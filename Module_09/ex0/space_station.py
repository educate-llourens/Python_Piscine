#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError  # type: ignore[import]


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200, default=None)


def main() -> None:
    # Variables ***************************************************************
    space_station: SpaceStation
    invalid_station: SpaceStation

    # Data Validation with valid data *****************************************
    space_station = SpaceStation(station_id="ISS001",
                                 name="International Space Station",
                                 crew_size=6,
                                 power_level=85.5,
                                 oxygen_level=92.3,
                                 last_maintenance="2026-04-28",
                                 is_operational=True)
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size}")
    print(f"Power: {space_station.power_level}")
    print(f"Oxygen: {space_station.oxygen_level}")
    if space_station.is_operational is True:
        print("Status: Operational\n")
    else:
        print("Status: NOT operational\n")

    # Data Validation with invalid data ***************************************

    print("========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(station_id="ISS001",
                                       name="International Space Station",
                                       crew_size=26,
                                       power_level=85.5,
                                       oxygen_level=92.3,
                                       last_maintenance="2026-04-28",
                                       is_operational=True)
        print(invalid_station)
    except ValidationError as msg:
        print(msg.errors()[0]['msg'])
        return


if __name__ == "__main__":
    main()
