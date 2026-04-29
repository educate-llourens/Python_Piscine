#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from pydantic import (BaseModel, Field,  # type: ignore[import]
                      model_validator, ValidationError)


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True

    @model_validator(mode="after")
    def crew_validator(self) -> "CrewMember":
        if self.is_active is False:
            raise ValueError("Error: All crew members must be active to "
                             "go on missions")
        return self


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list["CrewMember"] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def space_mission_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Error: Space Mission ID must start with 'M'")
        leadership_aboard: bool = False
        for crew_member in self.crew:
            if (crew_member.rank is Rank.commander or
                    crew_member.rank is Rank.captain):
                leadership_aboard = True
        if not leadership_aboard:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        if self.duration_days > 365:
            nbr_experienced_crew: int = 0
            nbr_crew_members: int = len(self.crew)
            for crew_member in self.crew:
                if crew_member.years_experience >= 5:
                    nbr_experienced_crew += 1
            if nbr_experienced_crew < (nbr_crew_members / 2):
                raise ValueError("Error: There are not enough experienced "
                                 "crew members for this mission")
        return self


def space_crew() -> None:
    # Variables ***************************************************************
    s_connor: CrewMember
    j_smith: CrewMember
    a_johnson: CrewMember
    l_grunt: CrewMember
    space_crew: SpaceMission
    invalid_space_crew: SpaceMission

    # Valid Mission Crew Validation *******************************************
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    s_connor = CrewMember(member_id="C4565-F123",
                          name="Sarah Connor",
                          rank=Rank.commander,
                          age=52,
                          specialization="Mission Command",
                          years_experience=32,
                          is_active=True)
    j_smith = CrewMember(member_id="C4583-M741",
                         name="John Smith",
                         rank=Rank.lieutenant,
                         age=36,
                         specialization="Navigation",
                         years_experience=18,
                         is_active=True)
    a_johnson = CrewMember(member_id="C7537-F985",
                           name="Alice Johnson",
                           rank=Rank.officer,
                           age=26,
                           specialization="Engineering",
                           years_experience=8,
                           is_active=True)
    space_crew = SpaceMission(mission_id="M2024_MARS",
                              mission_name="Mars Colony Establishment",
                              destination="Mars",
                              launch_date="2024-04-29",
                              duration_days=900,
                              crew=[s_connor, j_smith, a_johnson],
                              mission_status="Planned",
                              budget_millions=2500.0)
    print(f"Mission: {space_crew.mission_name}")
    print(f"ID: {space_crew.mission_id}")
    print(f"Destination: {space_crew.destination}")
    print(f"Duration: {space_crew.duration_days} days")
    print(f"Budget: ${space_crew.budget_millions}M")
    print(f"Crew size: {len(space_crew.crew)}")
    print("Crew members:")
    for crew_member in space_crew.crew:
        print(f"- {crew_member.name} ({crew_member.rank.value}) - "
              f"{crew_member.specialization}")
    print("")

    # Invalid Mission Crew Validation *****************************************
    print("=========================================")
    print("Expected validation error:")
    l_grunt = CrewMember(member_id="C8985-M782",
                         name="Leroy Grunt",
                         rank=Rank.cadet,
                         age=20,
                         specialization="Operations",
                         years_experience=2,
                         is_active=True)
    try:
        invalid_space_crew = SpaceMission(mission_id="M2025_JUPITER",
                                          mission_name="Jupiter Colony Survey",
                                          destination="Jupiter",
                                          launch_date="2025-04-29",
                                          duration_days=600,
                                          crew=[l_grunt, j_smith, a_johnson],
                                          mission_status="Planned",
                                          budget_millions=2500.0)
        print(invalid_space_crew.launch_date)
    except ValidationError as msg:
        print(msg.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    space_crew()
