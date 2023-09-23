import subprocess
import json

# Define the maximum number of allowed attempts
max_attempts = 3

# Initialize the attempt counter
attempts = 0

while attempts < max_attempts:
    # Define the Termux fingerprint command
    termux_command = "termux-fingerprint"

    try:
        # Execute the Termux fingerprint command and capture the output as text
        result_text = subprocess.check_output(termux_command, shell=True).decode("utf-8")

        # Attempt to parse the result_text as JSON
        try:
            result_json = json.loads(result_text)
            print(result_json)
            result = result_json["auth_result"] 
        except json.JSONDecodeError:
            result_json = None

        if result == "AUTH_RESULT_SUCCESS":
            print("Fingerprint matched. Identity verified.")
            break  # Exit the loop on successful match
        else:
            print("Fingerprint not matched. Please try again.")
            attempts += 1

    except subprocess.CalledProcessError as e:
        # Handle any errors that may occur when executing the command
        print("Error:", e)
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)

if attempts >= max_attempts:
    print(f"Exceeded the maximum number of attempts ({max_attempts}). Access denied.")

