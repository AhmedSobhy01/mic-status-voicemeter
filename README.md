# Voicemeeter Output Channel Tray Status

## Description

This tool displays the mute status of Voicemeeter Banana's output channel in your Windows system tray

## Screenshot

<img width="150" height="51" alt="image" src="https://github.com/user-attachments/assets/7663d043-10db-4214-bec3-96fa11dea5b9" />

## Create an Executable (.exe)

You can package this script as a standalone Windows executable using [PyInstaller](https://pyinstaller.org/):

1. Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2. Build the executable:

    ```bash
    pyinstaller --noconfirm --onefile --windowed --add-data "unmuted.png;." --add-data "muted.png;." --add-data "notfound.png;." voicemeter_tray.py
    ```

## Usage

1. Place `voicemeter_tray.py` and the icon files (`unmuted.png`, `muted.png`, `notfound.png`) in the same folder
2. Run the script:
    ```bash
    python voicemeter_tray.py
    ```
    Or run the generated `.exe` if you built it with PyInstaller
3. The tray icon will show the current mute status of the output channel. Right-click and select "Exit" to close

## Add to System Startup

To start the tray app automatically when you log in:

1. Press `Win + R`, type `shell:startup`, and press Enter
2. In the opened folder, create a shortcut to `voicemeter_tray.py` (or to the `.exe` if you built it)
    - Alternatively, create a batch file like:
        ```
        python "C:\Users\ahmed\Desktop\mic-status-voicemeter\voicemeter_tray.py"
        ```
        and place it in the Startup folder
3. The tray app will now start automatically on login
