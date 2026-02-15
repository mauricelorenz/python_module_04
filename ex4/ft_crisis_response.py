#!/usr/bin/env python3

def main() -> None:
    """Run the main program."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = ["lost_archive.txt",
             "classified_vault.txt",
             "standard_archive.txt"]
    for file in files:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        try:
            with open(file) as f:
                f.read()
            print("SUCCESS: Archive recovered - "
                  "``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except Exception:
            print("RESPONSE: Unknown error occured")
            print("STATUS: Continuing anyway\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
