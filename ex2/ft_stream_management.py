#!/usr/bin/env python3

from sys import stdout, stderr


def main() -> None:
    """Run the main program."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {id}: {status}", file=stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=stderr)
    print("[STANDARD] Data transmission complete", file=stdout)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
