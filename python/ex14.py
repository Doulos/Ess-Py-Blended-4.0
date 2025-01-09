import os
import glob
import subprocess

print("list all files in current directory:")
print(os.listdir())

print("\nlist all files with .py extension:")
print(glob.glob("*.py"))

print("\n" + 40 * "~")
print("run zen.py using shell")

"""
on Python >= 3.7, you can replace the 2 parameters 
  stdout = subprocess.PIPE
  stderr = subprocess.PIPE
by: 
  capture_output = True
  
In the case you have both python 2.x and python 3.x installed,
you might need to run the "python3" interpreter to be sure that
Python 3.x is run
"""
out = subprocess.run(
    "python zen.py",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,  # try setting to False
)
print("returned: ", out.returncode)
print("\n" + "--- out.stdout ---")
print(out.stdout, end="")
print("--")
print("\n" + "--- out.stderr:")
print(out.stderr, end="")
print("--")
