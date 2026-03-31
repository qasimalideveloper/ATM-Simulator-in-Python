import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = 'Sample.BMP'

# Run the command
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check the result
if result.returncode == 0:
    print("Command executed successfully")
    print("Output:")
    print(result.stdout)
else:
    print("Command failed")
    print("Error:")
    print(result.stderr)
