#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from pydantic import (BaseModel, Field,  # type: ignore[import]
                      model_validator, ValidationError)


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def contact_verification(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Error: Contact ID needs to start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Error: Physical contact must be verified")
        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Error: signal strength over 7 requires "
                             "a message")
        return self


def alian_contact() -> None:
    # Variables ***************************************************************
    alien_contact: AlienContact
    invalid_alien_contact: AlienContact

    # Valid Contact Log Validation ********************************************
    alien_contact = AlienContact(contact_id="AC2024_001",
                                 timestamp="2026-04-29",
                                 location="Area 51, Nevada",
                                 contact_type="radio",
                                 signal_strength=8.5,
                                 duration_minutes=45,
                                 witness_count=5,
                                 message_received=("Greetings from Zeta "
                                                   "Reticuli"),
                                 is_verified=False)
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type.value}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}/10")
    print(f"Duration: {alien_contact.duration_minutes} minutes")
    print(f"Witnesses: {alien_contact.witness_count}")
    print(f"Message: {alien_contact.message_received}\n")

    # Invalid Contact Log Validation ******************************************
    print("======================================")
    print("Expected validation error:")
    try:
        invalid_alien_contact = AlienContact(contact_id="AC_2024_001",
                                             timestamp="2026-04-29",
                                             location="Area 51, Nevada",
                                             contact_type="telepathic",
                                             signal_strength=8.5,
                                             duration_minutes=45,
                                             witness_count=2,
                                             message_received=("Greetings from"
                                                               " Zeta Reticuli"
                                                               ),
                                             is_verified=False)
        print(invalid_alien_contact.timestamp)
    except ValidationError as msg:
        print(msg.errors()[0]['ctx']['error'])
        return


if __name__ == "__main__":
    alian_contact()
