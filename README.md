# FFIX-Defeat-10.000-Enemies

The objective of this scripts is to help players complete the FFIX Achiviement 'Bloodlust' which requires defeating 10.000 enemies.
Functionally, the script use the library PyAutoGUI to send keystroke to the game's window.


# Instructions

### Requirements
- Python > 3.10
- Windows

### Installation
Create virtual enviroment
```
py -m venv env
```
Activate virtual enviroment 
```
Set-ExecutionPolicy Unrestricted -Scope Process
env/Scripts/activate
```
Install the required libraries
```
pip install requirements.py
```
Now open the game in window mode and:

1. Go in Gizamaluke Grotto and place yourself in the Cavern as seen in the screenshot below

2. Trigger a battle

3. Press `J` to ativate the autobattle feature in the game 

4. Launch the script

```
py autobattler.py
```

The script will automatically focus the game's window and start playing. Since FFIX on PC has the risk of crashing, the script will change room every 10 minutes to autosave the game, this will prevent the loss of hours of farming.

### Parameters

### Why Gizamaluke Grotto

I choose Gizamaluke Grotto because it has been reported has one of the better place to farm, but how long it will take to farm 10.000 enemies?

There are 6 possible combination of enemies encounter, I recorded three batch of 100 encounter and the results are the following

| Encounter | #1 | #2 | #3 |  Total | % | 
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Hornet 4 | 14 | 13 | 11 | 38 | 12.7 % |
| Hornet 2 + Skeleton 1 | 29 | 21 | 26 | 76 | 25.3 % |
| Hornet 3 | 11 | 12 | 11 | 34 | 11.3 % |
| Skeleton 2 | 17 | 26 | 24 | 76 | 22.3 % |
| Hornet 2 | 9 | 11 | 9 |29 | 9.7 % |
| Skeleton 1 | 20 | 17 | 19 | 56 | 18.7 % |

Given this numbers, we can calculate the weight average of enemies per encounter which is 2.43 enemies per encounter

Given an average of 2.3 encounter per minute, the total enemies defeated per hour become 335.34 enemies per hour. To reach 10.000 enemies defeated, we need almost 30 hours of continuos farming.

### Game Settings

### Optimal Team
The optimal team is composed of

| Member | #1 | #2 | #3 |  Total | % | 
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Zidane | eyeXeye | eyes4eyes | always-haste | 38 | 12.7 % |
| Freya | eyeXeye | eyes4eyes | always-haste | 76 | 25.3 % |
| Amourant | eyeXeye | eyes4eyes | always-haste | 34 | 11.3 % |

# Integration with Moguri Mod
Unfortunately I have no clear way to integrate this script with Moguri Mod / Memoria, but there is some work-around that can be done:


