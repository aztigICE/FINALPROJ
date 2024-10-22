import os
import group_manager
import team_assignments
import team_tasks

print()
print(r",--------.              ,--.    ,-----.          ,--.                        _ ")
print(r"'--.  .--',--,--. ,---. |  |,-. |  |) /_  ,--,--.|  |-.,--. ,--.           .' '")
print(r"   |  |  ' ,-.  |(  .-' |     / |  .-.  \' ,-.  || .-. '\  '  /       __  /    \ ")
print(r"   |  |  \ '-'  |.-'  `)|  \  \ |  '--' /\ '-'  || `-' | \   '       /.-;|  /'._|_.'#`\ ")
print(r"   `--'   `--`--'`----' `--'`--'`------'  `--`--' `---'.-'  /       ||   |  |  _       |")
print(r"                                                       `---'        \\__/|  \.' ;'-.__/")
print(r"                                                                     '--' \    /")
print(r"                                                                           '._.'")

# Create the users.txt file if it doesn't exist
if not os.path.exists("users.txt"):
    with open("users.txt", "w") as f:
        pass  # Create an empty file

credentials = input("LOGIN/SIGNUP\n\n->")
print()

#login or signup
if credentials == "LOGIN":
    login_user = input("Enter Username: ")
    login_pass = input("Enter Password: ")
    with open("users.txt", "r") as f:
        for line in f:
            existing_user, existing_pass = line.strip().split(":")
            if existing_user == login_user and existing_pass == login_pass:
                print(f"Login success! Welcome, {login_user}")
                logged_in = True
                current_user = login_user
                break
        else:
            print("Invalid username or password. Please try again.")
            logged_in = False
            current_user = None
elif credentials == "SIGNUP":
    while True:
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")
        def check_username(username):
            with open("users.txt", "r") as f:
                for line in f:
                    existing_user, _ = line.strip().split(":")
                    if existing_user == username:
                        return False
            return True

        if check_username(new_user):
            with open("users.txt", "a") as f:
                f.write(f"{new_user}:{new_pass}\n")
            print(f"Signup success! Welcome, {new_user}")
            logged_in = True
            current_user = new_user
            break
        else:
            print("Username already exists. Please choose a different username.")
            logged_in = False
            current_user = None
'''
if logged_in:
    print(f"You are now logged in as {current_user}!\n")
    print("=" * 80 + "\n")
    print("What would you like to do?\n")

    #Create the teams.txt file if it doesn't exist.
    if not os.path.exists("teams.txt"):
        with open("teams.txt", "w") as f:
            pass  # Create an empty file

    action = input("CREATE or JOIN a team.\n\n->")

    #Create or Join a group
    if action == "CREATE":
        new_team_name = input("New team name: ")
        group_manager.create_group(new_team_name)
    elif action == "JOIN":
        team_name = input("Team name: ")
        team_key = input("Team key: ")
        if group_manager.join_group(team_name, team_key):
            print("You are now a member of the team!")
        else:
            print("Failed to join team. Please try again.")
'''

# only run app if logged in
if logged_in:
    print(f"You are now logged in as {current_user}!\n")
    print("=" * 80 + "\n")
    print("What would you like to do?\n")

    # Create or Join a team
    action = input("CREATE or JOIN a team.\n\n->")

    if action == "CREATE":
        new_team_name = input("New team name: ")
        group_manager.create_team(new_team_name, current_user)
        team_name = new_team_name
    elif action == "JOIN":
        team_code = input("Team code: ")
        with open("teams.txt", "r") as f:
            for line in f:
                stored_team_name, stored_team_code = line.strip().split(":")
                if stored_team_code == team_code:
                    team_name = stored_team_name
                    print("You are now a member of the team!")
                    break
            else:
                print("Failed to join team. Please try again.")

    # Team management
    while True:
        print("\nTeam Management Menu:")
        print("1. View team members")
        print("2. View team tasks")
        print("3. View task assignments")
        print("4. Create task")
        print("5. Assign task")
        print("6. Exit")

        team_action = input("Choose an action: ")

        if team_action == "1":
            group_manager.view_team_members(team_name)
        elif team_action == "2":
            team_tasks.view_tasks(team_name)
        elif team_action == "3":
            team_assignments.view_assignments(team_name)
        elif team_action == "4":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            group_manager.create_task(team_name, task_name, task_description)
        elif team_action == "5":
            task_name = input("Enter task name: ")
            member_name = input("Enter member name: ")
            group_manager.assign_task(team_name, task_name, member_name)
        elif team_action == "6":
            break
        else:
            print("Invalid action. Please try again.")
else:
    print("Login or signup failed. Please try again.")