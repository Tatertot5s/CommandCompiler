I made a python script to turn a .mcfunction file into a single command block, and then asked ChatGPT to make a HTML version which worked first try. I may go back and rewrite the HTML code to look nicer if I decide to learn HTML, but currentley I don't know how to program in HTML lmao. The python script was created by me though.

The main use case of this is to be able to put a bunch of commands into your saved hotbar to run quickly and easily.

You most likley want to put these two commands at the end of every command:

setblock ~ ~1 ~ command_block{auto:1b,Command:"fill ~ ~ ~ ~ ~-3 ~ air"} replace
kill @e[type=command_block_minecart,distance=..1]

The first one is so the command block stack disapears, but it needs to be delayed 1 tick that way the next command can run, so you place it as a command block.
The second command kills all the command block minecart used.

Example Script:
gamerule doMobSpawning false
tp @e[type=slime] ~ -500 ~
gamerule doWeatherCycle false
gamerule doDaylightCycle false
time set noon
weather clear
gamerule keepInventory true
setblock ~ ~1 ~ command_block{auto:1b,Command:"fill ~ ~ ~ ~ ~-3 ~ air"} replace
kill @e[type=command_block_minecart,distance=..1]

This would be to clear a superflat world.

This works by making an redstone block falling block, with an activator rail falling block riding it, and then a bunch of command block minecarts riding the activator rail, activating them all in order.
