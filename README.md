# Coral
Generic 3-Operand Minecraft CPU Environment.

## Assembler

*Note: Before you try to assemble any code, please configure the* `assembler_tokens.txt` *file.*

To run the Assembler, run `Coral.py` and input `asm [file_name].[file_extension]` and optionally add `~[flag]` at the end.

## Emulator

*Note: Before you try to run / emulate any code, please configure the* `emulator_tokens.txt` *file, and add all functionality into the* `emulator_func.py` *file.*

To run the Assembler, run `Coral.py` and input `emu [file_name].[file_extension]` and optionally add `~[flag` at the end.

#
### Flags
Flags will have the prefix `~` bound to them, unless specified otherwise with the `FLAG_PREFIX` constant in `Coral.py`.

* `nolog`: Actions, Errors and Similar wont be logged.
* `noshow`: Memory wont be shown durring runtime, and will only show once the Emulation is complete.
* `nowarn`: Warning wont get shown to the User. 
* `noerror`: Errors wont get shown to the User, unless they are fatal.

Multiple flags can be used together, by doing `~[flag], ~[flag]`. 

*This project should in no case be affiliated with any trademarked usage of the word 'Coral'.*
