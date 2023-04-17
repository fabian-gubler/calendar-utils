# Calendar-Utils

This repository contains utility scripts designed to help you automate and manage your calendar entries more effectively. With Calendar-Utils, you can easily populate your calendar based on whether you have a study or work day and automatically add commute times as necessary. Additionally, the calinfo script provides a summary of your existing scheduled events and helps you keep track of how much time is still available to schedule.

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
```nix develop```

If nix is on your system, this allows you to have the same dependencies and versions as
I do, ensuring compatibility
