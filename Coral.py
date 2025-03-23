# Coral.py
from Assembler import entry as A_entry
from Emulator import entry as E_entry
from Constants import FILE_EXTENSION

while True:
  inp = str(input("Please input a valid command: ")).lower()
  print(inp)
  if inp.startswith("asm"):
    entry = A_entry
    inp.removeprefix("asm ")
  elif inp.startswith("emu"): 
    entry = E_entry
    inp.removeprefix("asm")
  else: continue
  
  FileName = f"{inp.split('.')[0]}.{FILE_EXTENSION}"
  inp.removeprefix(f"FileName ")
  
  Flags = inp

  entry(FileName, Flags)
  break