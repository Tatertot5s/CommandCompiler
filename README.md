I made a python script to turn a .mcfunction file into a single command block, and also made a web version of it.

The main use case of this is to be able to put a bunch of commands into your saved hotbar to run quickly and easily.

You most likley want to put these two commands at the end of every command:

setblock ~ ~1 ~ command_block{auto:1b,Command:"fill ~ ~ ~ ~ ~-3 ~ air"} replace
kill @e[type=command_block_minecart,distance=..1]

The first one is so the command block stack disapears, but it needs to be delayed 1 tick that way the next command can run, so you place it as a command block.
The second command kills all the command block minecart used.

This works by making an redstone block falling block, with an activator rail falling block riding it, and then a bunch of command block minecarts riding the activator rail, activating them all in order.

To use the python script, put it in the same folder as a file with some kind of file that has minecraft commands in it (like a .txt file, or .mcfunction) and then specify the name like "functionname.mcfunction", so with the extention. You can also optionally write the output to file, but the script will overwrite ALL contents of the file it's told to output to.