#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime, timedelta


def create_demo_entries(directories, khal_configuration_path):
    # Check if directories are empty and create demo entries
    demo_entries_created = False
    for directory in directories:
        # Check if directory exists, if not, create it
        os.makedirs(directory, exist_ok=True)

        # check if directory is empty
        if not os.listdir(directory):
            print(f"Directory: {directory} is empty. Creating demo entries...")
            demo_entries_created = True

            # Extract calendar name from directory path
            calendar_name = directory.split("/")[-1]

            # Get current month and year
            current_year = datetime.now().year
            current_month = datetime.now().month

            # Get next month and year
            next_month = current_month + 1 if current_month < 12 else 1
            next_year = current_year if current_month < 12 else current_year + 1

            # Generate each day of the next month
            day = datetime(next_year, next_month, 1)
            while day.month == next_month:
                # Check if the day is a weekday
                if day.weekday() < 5:
                    # Create two blocks each day from 07.00 - 12.00 and 13:15 - 16:00
                    date_str = day.strftime("%d.%m.%Y")
                    subprocess.run(
                        [
                            "khal",
                            "-c",
                            khal_configuration_path,
                            "new",
                            f"{date_str} 07:00 to {date_str} 12:00",
                            "Demo Morning Block",
                            "-a",
                            calendar_name,
                        ]
                    )
                    subprocess.run(
                        [
                            "khal",
                            "-c",
                            khal_configuration_path,
                            "new",
                            f"{date_str} 13:15 to {date_str} 16:00",
                            "Demo Afternoon Block",
                            "-a",
                            calendar_name,
                        ]
                    )

                # Move to the next day
                day += timedelta(days=1)

    if demo_entries_created:
        print("Demo entries have been created. You may delete them if you wish.")
