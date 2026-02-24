#!/usr/bin/env python3

def main() -> None:
    """Demonstrates understanding of how to read from a file
    """
    content: str = ""

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print("\nData recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    main()
