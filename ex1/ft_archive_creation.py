#!/usr/bin/env python3

def main() -> None:
    """Run the main program."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    text = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""
    try:
        with open(filename, "w") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            f.write(text)
            print(text)
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
