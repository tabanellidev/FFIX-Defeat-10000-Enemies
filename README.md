# FFIX-Defeat-10.000-Enemies

The objective of this scripts is to help players complete the FFIX Achiviement 'Bloodlust' which requires defeating 10.000 enemies.
Functionally, the script use the library PyAutoGUI to send keystroke to the game's window.


## Instructions

### Requirements
- Python > 3.10
- Windows

### Installation
Create and activate the virtual enviroment
```
py -m venv env
Set-ExecutionPolicy Unrestricted -Scope Process
env/Scripts/activate
```

Install the required libraries
```
pip install requirements.py
```
Now open the game in Window Mode and:

1. Go in Gizamaluke Grotto and place yourself in the Cavern as seen in the screenshot below

2. Trigger a battle

3. Press `J` to ativate the autobattle feature in the game 

4. Launch the script

```
py autobattler.py
```

The Autobattler will automatically focus the game's window and start playing. Since FFIX on PC has the risk of crashing, the script will change room every 10 minutes to autosave the game, this will prevent the loss of hours of farming. Additionally it will display an estimation of how many enemies where defeated in the meantime, the calculations will be shown below.

### Parameters

The script can be launched with two additional parameters: `-m` if you want to manually focus the game's window and `-s n` where `n` indicates after how many minutes the script will save the game (and display an estimation of how many enemies where defeated), the default value of `n` is 10. An example is shown below.

```
py autobattler.py -m -s 20
```

## Why Gizamaluke Grotto

I choose Gizamaluke Grotto because it has been reported has one of the better place to farm, but how long it will take to farm 10.000 enemies? There are 6 possible combination of enemies encounter, I recorded 3 batch of 100 encounters each and the results are the following:

| Encounter | #1 | #2 | #3 |  Total | % | 
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Hornet 4 | 14 | 13 | 11 | 38 | 12.7 % |
| Hornet 2 + Skeleton 1 | 29 | 21 | 26 | 76 | 25.3 % |
| Hornet 3 | 11 | 12 | 11 | 34 | 11.3 % |
| Skeleton 2 | 17 | 26 | 24 | 76 | 22.3 % |
| Hornet 2 | 9 | 11 | 9 |29 | 9.7 % |
| Skeleton 1 | 20 | 17 | 19 | 56 | 18.7 % |

Given these results, the weight average of enemies defeated per encounter is `2.43 enemies/encounter` and if we consider an average of `2.3 encounter/minute` the total enemies defeated in 60 minutes is `~335.34 enemies/hour`. 

To reach 10.000 enemies defeated, we need almost 30 hours of continuos farming.

### More Optimization

There are a couples of ways to make the battle even quicker. Regarding the settings we can turn on `Skip Intro Battle` and put the camera on `Fixed`, this will save a couple of seconds per fight. 

As far as team composition I suggest using Zidane, Freya, Amarant and Steiner. Equip Steiner with Alert to prevent back attacks and equip to everyone abilities like Auto-Haste, Counter, Eye 4 Eye and Auto-Haste.

# Integration with Moguri Mod / Memoria

Unfortunately I have no clear way to integrate this script with Moguri Mod / Memoria, but there is some workaround that can be done:

- Use manual focus 
- Set the Game Speed to x4 in the launcher
- Disable the save routine since I think there is no risk of crashig using this Mod.


