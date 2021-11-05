import subprocess

source_dirs = "typedweb tests"
subprocess.check_call(f"isort {source_dirs}", shell=True)
subprocess.check_call(f"black {source_dirs}", shell=True)
