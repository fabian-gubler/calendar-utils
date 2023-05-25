# Calendar-Utils

## Project Description
Calendar-Utils is a set of utility scripts designed to automate and manage calendar entries effectively. It offers functionalities to automatically populate your calendar based on your work or study schedule, add commute times as needed, and provide a summary of your existing scheduled events. It also allows you to keep track of how much time is still available to schedule.

## Motivation
Time management is crucial for a successful semester, especially when balancing both university and work commitments. Upon starting to work, it was initially challenging to efficiently allocate time between both workloads. Manually distributing workloads between both areas through time blocking was time-consuming and difficult to visualize in terms of percentage allocation. This script was created to automate the creation of calendar entries and visualize whether current entries are evenly distributed (e.g., 60/40 for a part-time work schedule of 40%).

## Features

- **Automatically populate your calendar**: based on your work or study schedule.
- **Add commute time entries**: as required.
- **Generate a summary of your scheduled events**: helps you keep track of your existing schedule.
- **View time availability and calendar usage statistics**: keeps you informed about how much time is still available to schedule.

## Scripts

### calendar_populate.py
This script is used to automate your calendar entries based on whether it is a study or work day. It determines whether to add a commute time and creates an accurate entry in the corresponding calendar representing your work schedule.

### calendar_info.py
This script allows you to generate a summary of your already scheduled events. It displays how much time is still available to schedule and provides a breakdown of how many hours each calendar attribute contributes.

## Installation

### Prerequisites

- Python 3.8 or above
- pip (Python's package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/fabian-gubler/calendar-utils.git
cd calendar-utils
```

2. We recommend using a virtual environment to avoid package conflicts:
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate  # Unix or MacOS
.\venv\Scripts\activate    # Windows
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Ensure that the required Python packages are installed and your virtual environment is activated before proceeding.

1. Populate your calendars using the `calpop` script:
```bash
python calendar_populate.py
```

2. Generate a summary of your scheduled events and check the available time using the `calinfo` script:
```bash
python calendar_info.py
```

Feel free to explore the scripts and customize them to suit your needs.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the terms of the MIT license.
