#!/usr/bin/env python3

def crisis_response() -> None:
    """Demonstrates understanding of how to protect data when
    reading and writing to files
    """
    content: str = ""

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as lost_archive_file:
            print("ROUTINE ACCESS:")
            content = lost_archive_file.read()
        print(f"SUCCESS: Archive recovered - {content}")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print("")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_data.txt", "r") as classified_file:
            print("ROUTINE ACCESS:")
            content = classified_file.read()
        print(f"SUCCESS: Archive recovered - {content}")
        print("STATUS: Normal operations resumed")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print("")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as standard_file:
            content = standard_file.read()
        print(f"SUCCESS: Archive recovered - {content}")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print("")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
