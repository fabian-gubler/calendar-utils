# Calendar-Utils

This repository contains utility scripts designed to help you automate and manage your calendar entries more effectively. With Calendar-Utils, you can easily populate your calendar based on whether you have a study or work day and automatically add commute times as necessary. Additionally, the calinfo script provides a summary of your existing scheduled events and helps you keep track of how much time is still available to schedule.

## TODOs

### general
- time estimation: ~ 5 hours
	- first split into must do & extra features

### calinfo:

- Show ration between uni and work in percent
- Allow arguments for period (e.g. 7d)
	- provide error messages
- View a "this month" option to ensure 40% pensum reached

### calpop:

- Choose whether in-person or remote

### finalize project

#### architecture
- Create unit tests
- Merge two projects into one
	- create name 
	- how to module the app?
- Configuration file (sane inputs based on samples)

#### logic
- Decouple from khal
	- create .ics files directly
	- check congruence using .ics (not khal)
- Generalizability to various cases
	- if too hard: create a sample set
- Display calendar function (e.g. using khal)

### documentation
- think about structure (prioritise)
	- provide table of contents
	1. Motivation
	2. Video
	3. Description or Features
	4. Installation
	5. Usage
	6. Configuration
	7. Developers
	8. License
- add / edit entries (refer to khal documentation; my configuration)
- Run on your machine: Dependencies using virtualenv + pip (or exact reproducibilty)
	- requirements or setup.py
	- mention python version & should work on mac / linux
	- khal, icalendar, arrow (with versions)
	- test on both fedora and nix
- synchronize with your web calendar (refer to vdirsyncer; my configuration)
	- ? filetype: ini (python)
	- provide example config
- add motivation / storyline
- developers
	- could show nix here
	- running tests
- pictures for hype
	- meme
	- screenshots / video
- include license

## Features

- Automatically populate your calendar based on your work or study schedule
- Add commute time entries as required
- Generate a summary of your scheduled events
- View time availability and calendar usage statistics

## Scripts
### calpop

The calpop script is used to populate and automate your calendar entries based on whether it is a study or work day. It determines whether to add a commute time and creates a correct entry in the corresponding calendar representing your work schedule.

### calinfo
The calinfo script allows you to create a summary of your already scheduled events. It shows how much time is still available to schedule and provides a breakdown of how many hours each calendar attribute contributes.

## Installation

Follow the instructions below to set up the Python application on your local machine.

### Prerequisites
- Python 3.8 or above should be installed on your system. You can verify your Python version by running `python --version` in the terminal.
- Ensure that `pip` (Python's package installer) is updated. If not, run `python -m pip install --upgrade pip`.

### Steps
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. We recommend using a virtual environment for development to avoid any package conflicts. Install `virtualenv` using `pip` if you haven't already:
    ```bash
    pip install virtualenv
    ```

3. Create a virtual environment in the repository folder:
    ```bash
    virtualenv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

5. Once the virtual environment is activated (you should see `(venv)` before your terminal prompt), install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

Now, you should be ready to run the application!

Note: To deactivate the virtual environment when you're done, simply type `deactivate` in the terminal.

