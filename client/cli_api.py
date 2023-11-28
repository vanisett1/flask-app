import inquirer
import subprocess

BASE_URL = "https://ufoalienwebapp.azurewebsites.net"  # Base URL for the API

def run_curl_command(curl_cmd):
    try:
        response = subprocess.check_output(curl_cmd, shell=True, text=True)
        print("\nResponse:\n" + response)
    except subprocess.CalledProcessError as e:
        print("\nError occurred:", e.output)

def create_user(auth_token):
    print("\n--- Create User ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    curl_cmd = f"curl -X POST {BASE_URL}/v1/user -H 'Authorization: Bearer {auth_token}' -H 'Content-Type: application/json' -d '{{\"username\": \"{username}\", \"password\": \"{password}\"}}'"
    run_curl_command(curl_cmd)

def update_user(auth_token):
    print("\n--- Update User ---")
    user_id = input("Enter user ID: ")
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    curl_cmd = f"curl -X PUT {BASE_URL}/v1/user?user_id={user_id} -H 'Authorization: Bearer {auth_token}' -H 'Content-Type: application/json' -d '{{\"username\": \"{username}\", \"password\": \"{password}\"}}'"
    run_curl_command(curl_cmd)

def get_user(auth_token):
    print("\n--- Get User ---")
    user_id = input("Enter user ID to retrieve (leave blank for all users): ")
    url = f"{BASE_URL}/v1/user?user_id={user_id}" if user_id else f"{BASE_URL}/v1/user"
    curl_cmd = f"curl -X GET {url} -H 'Authorization: Bearer {auth_token}'"
    run_curl_command(curl_cmd)

def delete_user(auth_token):
    print("\n--- Delete User ---")
    user_id = input("Enter user ID to delete: ")
    curl_cmd = f"curl -X DELETE {BASE_URL}/v1/user?user_id={user_id} -H 'Authorization: Bearer {auth_token}'"
    run_curl_command(curl_cmd)

def main():
    print("\nWelcome to the User Management CLI Tool")
    print("This tool interacts with a user management API for creating, updating, retrieving, and deleting user data.")
    auth_token = input("Enter AUTH_TOKEN: ")

    actions = [
        inquirer.List('action',
                      message="Choose action",
                      choices=['Create User', 'Update User', 'Get User', 'Delete User', 'Exit'],
        ),
    ]

    while True:
        answer = inquirer.prompt(actions)
        action = answer['action']

        if action == 'Create User':
            create_user(auth_token)
        elif action == 'Update User':
            update_user(auth_token)
        elif action == 'Get User':
            get_user(auth_token)
        elif action == 'Delete User':
            delete_user(auth_token)
        elif action == 'Exit':
            print("\nExiting the User Management CLI Tool")
            break

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
