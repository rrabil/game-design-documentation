# 12 Audio Requirements

The sound blueprints in the Aurora Toolset are grouped under six major categories: Animals, Civilization, Magical, Nature, People, and Weather. Depending on the mood and tone of each level, the game will draw a variety of blueprints from these categories. The table below lists an initial sampling of relevant people sounds for six of the levels in *Calydon*:

| Level             | Relevant People Sounds from the Aurora Toolset                             |
|-----------------------|--------------------------------------------------------------------------------|
| Prison Darkhenge      | Coughs, crying, crypt moans, pain cries, shrieks, despairing men, etc.         |
| Imperial Palace       | Noble laugh, nobles talk, etc.                                                 |
| City of Romera        | Beggar calls, city yells, customer yells, evangelist calls, rowdy tavern, etc. |
| King’s Dove           | Prostitute calls, laughs, talking nobles                                       |
| Colosseo              | Cheers men, cheers women, shrieks, screams, cheers commoner group, etc.        |
| Light Gate University | Taunting noble group, commoners talk outside, etc.                             |

More detailed audio requirements and decisions will be documented as the game design progresses. Custom sounds may also be developed by adding .wav files or .bmu files to the appropriate file directory and selecting them for use within the module.

## 12.1 Character Sounds

Although voice acting is out of the scope for this game, there are multiple voicesets that come built-in with the Aurora Engine. These include voicesets for males and females from each of the races available in the toolset. A voiceset can be assigned to any given NPC, and the game engine will automatically emit sounds from this set based on triggers within the game, such as when engaging in combat. Such sounds can also be activated when the PC clicks the appropriate buttons in the Radial Menu.

## 12.2 Enemy / NPC Sounds

The enemy and NPC sounds will be similar to the character sounds—i.e., limited to built-in sounds of the Aurora Engine, such as battle cries and cheering.

## 12.3 Music

The Aurora Toolset comes with a wide range of built-in music properties for each tileset. These music files will be leveraged as much as possible to keep the scope of the game manageable. Any custom music created for the game must be in the BioWare Music Unit (BMU) format and then added to the “music” directory under the directory where Neverwinter Nights is installed. Or, .wav files can be created and added to the module using a hak pak.

Custom music will be explored as an option especially for the King’s Dove brothel and the Light Gate University areas, which are a little more unique than the generic areas, groups, and features available in the toolset.

## 12.4 Vocal Recording

This is currently not applicable, since vocal recording is outside the scope and budget of this game. However, the script for *Calydon* will document the intended tone and/or inflection for vocal delivery of each line of dialogue. This is to prepare for the possibility that the game is well received and plans are made to produce it on a more professional scale.
