import csv
import subprocess
import os
print("Current PATH:", os.environ.get('PATH'))

def run_gradle_commands(csv_file, base_dir, log_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            component, *commands = row
            component_dir = os.path.join(base_dir, component)

            if os.path.exists(component_dir):
                print(f"Executing commands in {component_dir}:")
                for command in commands:
                    # Strip any leading/trailing whitespace around the command
                    command = command.strip()
                    try:
                        # Execute the command and capture the output and errors
                        result = subprocess.run(command, shell=True, cwd=component_dir, text=True, capture_output=True)
                        if result.returncode != 0:
                            error_message = f"Error in {component} running '{command}': {result.stderr}"
                            print(error_message)
                            with open(log_file, 'a') as log:
                                log.write(error_message + "\n")
                    except Exception as e:
                        # Log any Python exceptions that occur during command execution
                        error_message = f"Exception in {component} running '{command}': {str(e)}"
                        print(error_message)
                        with open(log_file, 'a') as log:
                            log.write(error_message + "\n")
            else:
                print(f"Directory {component_dir} does not exist.")

if __name__ == "__main__":
    base_directory = r'T:\5_repos\sample_java_app_gradle'  # Adjust as necessary
    csv_filepath = os.path.join(base_directory, 'gradle_commands.csv')
    log_filepath = os.path.join(base_directory, 'gradle_commands_errors.log')
    run_gradle_commands(csv_filepath, base_directory, log_filepath)
