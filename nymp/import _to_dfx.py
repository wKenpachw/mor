import subprocess


TEIGHA_PATH = r"D:\Program Files\ODA\ODAFileConverter_title 20.12.0\ODAFileConverter.exe"
INPUT_FOLDER = r"./"
OUTPUT_FOLDER = r"./"
OUTVER = "ACAD2018"
OUTFORMAT = "DXF"
RECURSIVE = "0"
AUDIT = "1"
INPUTFILTER = "*.DWG"

# Command to run
cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]

# Run
subprocess.run(cmd, shell=True)