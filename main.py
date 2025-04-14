def main():
	if int(input("If you would like to output this to file, press 1: ")) == 1:
		does_output = True
		if int(input("If you would like to specify a file, type 1: ")) == 1:
			input_file = input("Please define an input file: ")
			output_file = input("Please define an output file: ")
		else:
			input_file = "command_in.mcfunction"
			output_file = "command_out.txt"
	else:
		does_output = False
		if int(input("If you would like to specify a file, type 1: ")) == 1:
			input_file = input("Please define an input file: ")
			output_file = ""
		else:
			input_file = "command_in.mcfunction"
			output_file = ""

	#Is it a give command?
	if int(input("If you would like this to be a give command, type 1: ")) == 1:
		is_give_command = True
	else:
		is_give_command = False
	
	print(generate_command(input_file, output_file, is_give_command, does_output))

	print(f"Your file has been written to {output_file}")

def generate_command(input_file: str, output_file: str, is_give_command: bool, does_output: bool):
	file_read = open(input_file, 'r')
	if does_output:
		file_write = open(output_file, 'w')

	start = 'summon falling_block ~ ~1 ~ {BlockState:{Name:"minecraft:redstone_block"},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:activator_rail"},Time:1,Passengers:[{id:"minecraft:command_block_minecart",Command:"'
	middle = '"},{id:"minecraft:command_block_minecart",Command:"'
	end = '"}]}]}'
	command = ""

	lines = file_read.readlines()

	for i in range(len(lines)):
		inputs = lines[i].strip()
		inputs = inputs.replace('"', '\\"')
		if i == len(lines) - 1:
			command = command + inputs
		else:
			command = command + inputs + middle

	summon_command = start + command + end

	if is_give_command:
		escaped_summon_command = summon_command.replace('\\', '\\\\').replace('"', '\\"')
		give_command = f'/give @p command_block[block_entity_data={{id:"command_block", auto:1b, Command:"{escaped_summon_command}"}}] 1'
		if does_output:
			file_write.write(give_command)
		return give_command
	else:
		if does_output:
			file_write.write(summon_command)
		return summon_command

if __name__ == '__main__':
	main()

#	file_read.close()
#	file_write.close()