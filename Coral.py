# Coral.py, the main entry point.

# (c) JoBe, 2025


from Assembler import entry as A_entry
from Emulator import entry as E_entry
from Constants import FILE_EXTENSION

from logger import *


log = logger()

while True:
    inp = str(input("Please input a valid command: ")).lower()
    log.debug(f"Got input(s): {inp}")
    if inp.startswith("asm"):
        entry = A_entry
        inp.removeprefix("asm ")
    elif inp.startswith("emu"): 
        entry = E_entry
        inp.removeprefix("asm")
    else: 
        log.error("Input is not recognized as valid input, trying again")
        continue

    file_name = f"{inp.split('.')[0]}.{FILE_EXTENSION}"
    inp.removeprefix(f"{file_name} ")
    log.debug(f"Input got converted to {inp}, with file extension {FILE_EXTENSION} being used")

    flags = inp
    log.debug(f"Using {flags}")

    entry(file_name, flags)
    break
