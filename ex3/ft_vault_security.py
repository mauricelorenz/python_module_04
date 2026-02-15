#!/usr/bin/env python3

def main() -> None:
    """Run the main program."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    filename = "classified_data.txt"
    text = "[CLASSIFIED] New security protocols archived"
    try:
        with open(filename, "r+") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f.read())
            print("\nSECURE PRESERVATION:")
            f.write(f"\n{text}")
            print(text)
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
