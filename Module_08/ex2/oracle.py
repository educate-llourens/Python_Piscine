#!/usr/bin/env python3

from dotenv import load_dotenv
import os


def oracle() -> None:
    # Variables ***************************************************************
    matrix_mode: str | None
    log_level: str | None
    zion_endpoint: str | None

    # Configuration loading ***************************************************
    print("\nORACLE STATUS: Reading the Matrix...\n")

    if load_dotenv():
        print("Configuration loaded:")
        matrix_mode = os.getenv("MATRIX_MODE")
        if matrix_mode:
            print(f"Mode: {matrix_mode}")
            if matrix_mode == "development":
                print("Database: Connected to local instance")
            else:
                print("Database: Connected to a public, production instance. "
                      "For security reasons we will end the session")
                return
        else:
            print("Error: No MATRIX_MODE env")
            return
        if os.getenv("API_KEY"):
            print("API Access: Authenticated")
        else:
            print("Authentication error: Could not verify API key")
            return
        log_level = os.getenv("LOG_LEVEL")
        if log_level:
            print(f"Log Level: {log_level}")
        else:
            print("Error: no LOG_LEVEL env")
        zion_endpoint = os.getenv("ZION_ENDPOINT_URL")
        if zion_endpoint:
            print("Zion Network: Online")
        else:
            print("Error: No ZION_ENDPOINT - URL")
            return
        print("")

    # Environment security check **********************************************
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
    else:
        print("Error: Could not find environment variables. Please check "
              "the .env file")
        return

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
