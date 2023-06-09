#!/usr/bin/env python3

import sys
import subprocess

khal_configuration_path = "./config"

def create_commute(time: str, destination: str):
    # TODO: Check if already exists
    if destination == '4':
        timespan, from_, arrival = "06:28 07:16", "St. Gallen", "Zurich Airport"
        print(f"Selection: Zurich Airport\n")
        subprocess.run(["khal", "-c", khal_configuration_path, "new", time, timespan, from_, "to", arrival])

def create_block(time: str, block: str):
    arr = block.split()
    timespan = f"{arr[0]} {arr[1]}"
    result = subprocess.run(["khal", "-c", khal_configuration_path, "at", time, timespan], capture_output=True, text=True)

    if result.stdout.strip() == '':
        # No events for the given time range
        subprocess.run(["khal", "-c", khal_configuration_path, "new", time] + arr)
        result = subprocess.run(["khal", "-c", khal_configuration_path, "at", time, timespan], capture_output=True, text=True)

    lines = result.stdout.splitlines()
    if len(lines) >= 2:
        existing_entry = [line for line in lines if '-' in line]
        if existing_entry:
            print(f"Existing: {existing_entry[0]}")
        else:
            subprocess.run(["khal", "-c", khal_configuration_path, "new", time] + arr)
            result = subprocess.run(["khal", "-c", khal_configuration_path, "at", time, timespan], capture_output=True, text=True)
            print(result.stdout.splitlines()[1])
    else:
        # No events found even after creating a new event
        print("No events found")

    # print(result.stdout.splitlines()[1])

def main():
    if len(sys.argv) > 1:
        time = sys.argv[1]
    else:
        time = input("Please indicate date (e.g. tomorrow): ")

    print()
    print("\033[1mIs it a study day or work day?\033[0m")
    print("1 - Study day")
    print("2 - Work day")

    day_type = input()

    if day_type == '1':
        while True:
            print()
            yn = input("\033[1mGenerate Study Entries\033[0m\nyes or no (y/n): ")
            if yn.lower() == 'y':
                break
            elif yn.lower() == 'n':
                sys.exit()

        blocks = [
            "07:00 12:00 Study -a uni",
            "13:15 16:00 Study -a uni",
        ]

        print("\n\033[1mEntries\033[0m")
        for block in blocks:
            create_block(time, block)

    elif day_type == '2':
        create_commute(time, '4')

        while True:
            yn = input("\033[1mGenerate Work Entries\033[0m\nyes or no (y/n): ")
            if yn.lower() == 'y':
                break
            elif yn.lower() == 'n':
                sys.exit()

        blocks = [
            "07:30 12:00 Work -a work",
            "13:15 16:00 Work -a work",
        ]

        print("\n\033[1mEntries\033[0m")
        for block in blocks:
            create_block(time, block)

    else:
        print("Invalid selection")
        sys.exit()

    print()
    subprocess.run(["khal", "-c", khal_configuration_path, "list", time])

if __name__ == "__main__":
    main()
