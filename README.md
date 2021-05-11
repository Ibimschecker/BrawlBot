# BrawlBot
A Deep Q Network bot that learns to play Brawlhalla on its own.

## Packages Used
* numpy
* pyautogui
* time

## Strategy
1. Give it the ability to move in all known ways (i.e. 'up', 'right', etc)
2. Build frame by frame analysis
    * Find its position
    * Find other players positions?
    * Platform position?
    * Wall position?
    * Weapon position?
    * Bomb / mine position?
    * Projectile positions and trijectory
3. Reward System
    * Negative reward for getting hit by object (not falling weapon on fire)
    * Negative reward for getting hit by player
    * Positive reward for dodging a hit
    * ...etc