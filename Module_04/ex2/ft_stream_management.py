#!/usr/bin/env python3

import sys


def main() -> None:
    """Demonstrates understanding of stdin, stdout and stderr
    """
    archivist_id: str = ""
    status_report: str = ""

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                     f"{status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication "
                     "channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()
