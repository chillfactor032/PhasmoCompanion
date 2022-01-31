# PhasmoCompanion
This application helps you quickly narrow down the ghost type in Phasmophobia. With StreamDeck integration you can quickly enter evidence and not have to switch to your journal. As evidence is entered, it will tell you which possible evidence and ghost types could be left, which evidence types are no longer possible, and traits about the remaining possible ghosts. There is also a panel to view the location of the cursed items for each map.

![alt text](https://chillaspect.com/images/phasmocompanion/pc1.png "PhasmoCompanion")

## Building from Source

PhasmoCompanion releases are compiled from Python to exe using a compiler called Nuitka. To build this projects as I do for releases you will need a Nuitka compatible c language compiler and Python. PhasmoCompanion was developed with Python 3.9.7. For details about Nuitka prerequisites go to the [Nuitka User Manual](https://nuitka.net/doc/user-manual.html). The GUI for PhasmoCompanion is Qt 6.2.2 and PySide6. To install Nuitka, PySide6, and other requirements, use Pip. There is also a build script build.py that compiles Qt UI files, compiles image resource files, and then issues the nuitka compile command. If you wish to use a virtual environment you can do that as well.

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
py build.py
```

## Setting up StreamDeck

PhasmoCompanion uses UDP data to communicate with your StreamDeck. You will need to create actions that can call the PhasmoCompanion.exe with an argument. I used the "Advanced Launcher" from BarRaider. Install the Advanced Launcher plugin and begin dragging and dropping them in whatever configuration you wish. Here is mine for example.

![alt text](https://chillaspect.com/images/phasmocompanion/pc2.png "PhasmoCompanion")

There are 8 actions that can interact with PhasmoCompanion. For each action, drag the "Advanced Launcher" action to the desired location. Set the title to the action name. Set the Application to PhasmoCompanion.exe. Leave the "Start In" setting default. Set the "Arguments" to the corresponding argument in the table below. Optionally turn off "Indicator: Show dot if process is running" for all actions except the one that launches the GUI. Also optionally set the appearence of the actions (e.g. use the Pc logo for the launcher, add a border to the other actions, set the text position and font, etc...)

Action | Argument | Descriptions
--- | --- | ---
Pc Logo | (none) | Call exe with no arguements to launch GUI
E1 | e1 | Cycle Evidence Slot 1
E2 | e2 | Cycle Evidence Slot 2
E3 | e3 | Cycle Evidence Slot 3
Reset | reset | Reset all evidence slots
Info | tabs | Switch between ghost info and map info tabs
&lt; Map | mapL | Cycle maps to the left
Map &gt; | mapR | Cycle maps to the right

## Donations

PhasmoCompanion is provided free and without warranty. If you feel compelled to donated here are my crypto addresses below.

Coin | Address
--- | ---
BTC | 3C7UT1a2Do3LxFvxZt88S7gsNkRyRKXYCw
ETH | 0xc24Fc5E6C2b3E1e1eaE62f59Fab8cFBC87b1FEfc
LTC | MViPMqjn2kdMwbLAbYtgpgnHfzwwpbzUZQ
