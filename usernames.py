#/usr/bin/python3
import sys

def generate_usernames(full_name):
    first_name, last_name = full_name.lower().split()
    return [
        f"{first_name[0]}.{last_name}",
        f"{first_name}.{last_name[0]}",
        f"{first_name}{last_name}"
    ]

if len(sys.argv) != 2:
    print("Usage: python3 usernames.py names.txt")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    for line in file:
        full_name = line.strip()
        if full_name:
            print("\n".join(generate_usernames(full_name)))
