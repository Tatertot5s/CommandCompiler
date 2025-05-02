function generateCommand() {
    const inputText = document.getElementById("inputCommands").value.trim();
    const isGive = document.getElementById("isGiveCommand").checked;
    const lines = inputText.split('\n').map(line => line.trim().replace(/"/g, '\\"'));

    const start = '/summon falling_block ~ ~1 ~ {BlockState:{Name:"minecraft:redstone_block"},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:activator_rail"},Time:1,Passengers:[{id:"minecraft:command_block_minecart",Command:"';
    const middle = '"},{id:"minecraft:command_block_minecart",Command:"';
    const end = '"}]}]}';

    const commandBody = lines.join(middle);
    const summonCommand = start + commandBody + end;

    let output = "";

    if (isGive) {
      const escaped = summonCommand.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
      output = `/give @p command_block[block_entity_data={id:"command_block", auto:1b, Command:"${escaped}"}] 1`;
    } else {
      output = summonCommand;
    }

    document.getElementById("outputCommand").value = output;
}

document.addEventListener("DOMContentLoaded", () => {
	const inputBox = document.getElementById("inputCommands");
	const checkbox = document.getElementById("isGiveCommand");

	inputBox.addEventListener("input", generateCommand);
	checkbox.addEventListener("change", generateCommand);
});
