# Coral

Generic 3-Operand Minecraft CPU Environment.

## Assembler

> Note: Before you try to assemble any code, please configure the`assembler_tokens.txt` file.

To run the Assembler, run `Coral.py` and input `asm <file_name>.<file_extension>` and optionally add `~<flag>` at the end.

## Emulator

> Note: Before you try to run / emulate any code, please configure the `emulator_tokens.txt` file, and add all functionality into the `emulator_func.py` file.

To run the Assembler, run `Coral.py` and input `emu <file_name>.<file_extension>` and optionally add `~<flag>` at the end.

##

### Flags

Flags will have the prefix `~` bound to them, unless specified otherwise with the `FLAG_PREFIX` constant in `Coral.py`. <!-- Standart is '--' i suppose-->

* `nolog`: Actions, Errors and Similar won't be logged.
* `noshow`: Memory won't be shown during runtime, and will only show once the Emulation is complete.
* `nowarn`: Warnings won't get shown to the User. 
* `noerror`: Errors won't get shown to the              User, **unless they are fatal**.

Multiple flags can be chained together, by doing something like `~<flag1> ~<flag2>`. 

---

> *This project should **in no case** be affiliated with any trademarked usage of the word 'Coral'.*
