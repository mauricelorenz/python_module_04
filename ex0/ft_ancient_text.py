#!/usr/bin/env python3

def main() -> None:
    """Run the main program."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        with open(filename) as f:
            print("Connection established...\n\nRECOVERED DATA:")
            print(f.read())
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
