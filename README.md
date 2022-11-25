# PhasmoCompanion
This application helps you quickly narrow down the ghost type in Phasmophobia. With StreamDeck integration, you can quickly enter evidence and not have to switch to your journal. As evidence is entered, it will tell you which possible evidence and ghost types could be left, which evidence types are no longer possible, and traits about the remaining possible ghosts. 

![alt text](https://chillaspect.com/images/phasmocompanion/pc_full.png "PhasmoCompanion")

## Building from Source

PhasmoCompanion releases are compiled from Python to exe using a compiler called PyInstaller. 

```bash
git clone https://github.com/chillfactor032/PhasmoCompanion.git
cd PhasmoCompanion
```
Optionally, create a virtual environment
```bash
py -m venv env
.\env\Scripts\activate
```
Install dependencies and build the project
```bash
py -m pip install -r requirements.txt
py build.py partial
pyinstaller --onefile --windowed --name=PhasmoCompanion --icon=./resources/img/pc_icon.png PhasmoCompanion.py
```

## Setting up StreamDeck

PhasmoCompanion uses hot keys to communicate with StreamDeck. You can setup a StreamDeck profile to make setting evidence easy using the built in System > Hoy Keys plugin. Here is how my StreamDeck profile looks:

![alt text](https://chillaspect.com/images/phasmocompanion/sd.png "StreamDeck Profile for PhasmoCompanion")

There are 4 main actions that can interact with PhasmoCompanion. For each action, drag the System > Hotkey action to the desired location. Set the title to the action name. Set the hotkey of the action using the table below. You can also add a launcher button to launch PhasmoCompanion. To do this, add a System > Open action and set the App/File to the PhasmoCompanion.exe. Optionally set the appearence of the actions (e.g. use the PhasmoCompanion logo for the launcher, add a border to the other actions, set the text position and font, etc...)

![alt text](https://chillaspect.com/images/phasmocompanion/sd2.png "StreamDeck Action Setup")

Action | HotKey | Description
--- | --- | ---
E1 | Ctrl+Shift+1 | Cycle Evidence Slot 1
E2 | Ctrl+Shift+2 | Cycle Evidence Slot 2
E3 | Ctrl+Shift+3 | Cycle Evidence Slot 3
Reset | Ctrl+Shift+4 | Reset all evidence slots

## Donations

PhasmoCompanion is provided free and without warranty. If you feel compelled to donated here are my crypto addresses below.

Coin | Address
--- | ---
BTC | 3C7UT1a2Do3LxFvxZt88S7gsNkRyRKXYCw
ETH | 0xc24Fc5E6C2b3E1e1eaE62f59Fab8cFBC87b1FEfc
LTC | MViPMqjn2kdMwbLAbYtgpgnHfzwwpbzUZQ
