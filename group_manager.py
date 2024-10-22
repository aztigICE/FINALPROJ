import os
import secrets
import string

# Create Team
def create_team(team_name, creator):
    team_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
    with open("teams.txt", "a") as f:
        f.write(f"{team_name}:{team_key}\n")
    team_dir = os.path.join('teams', team_name)
    if not os.path.exists(team_dir):
        os.mkdir(team_dir)

    # Create file for listing team member and roles
    members_file = os.path.join(team_dir, 'members.txt')
    with open(members_file, 'w') as f:
        f.write(f"{creator}:admin\n")

    # Create a new file for team tasks
    tasks_file = os.path.join(team_dir, 'tasks.txt')
    with open(tasks_file, 'w') as f:
        pass

    # Create a new file for team task assignments
    assignments_file = os.path.join(team_dir, 'assignments.txt')
    with open(assignments_file, 'w') as f:
        pass

    print(f"Team '{team_name}' created successfully! Team key: {team_key}")

def join_team_by_key(team_key, member):
    for team_name in os.listdir('teams'):
        team_dir = os.path.join('teams', team_name)
        members_file = os.path.join(team_dir, 'members.txt')
        with open(members_file, 'r') as f:
            for line in f:
                existing_member, role = line.strip().split(":")
                if existing_member == member:
                    print("You are already a member of this team.")
                    return False

        team_key_file = os.path.join(team_dir, 'team_key.txt')
        with open(team_key_file, 'r') as f:
            existing_key = f.read().strip()
            if existing_key == team_key:
                with open(members_file, 'a') as f:
                    f.write(f"{member}:member\n")
                print(f"Joined team '{team_name}' successfully!")
                return True

    print("Invalid team key. Please try again.")
    return False

def view_team_members(team_name):
    team_dir = os.path.join('teams', team_name)
    members_file = os.path.join(team_dir, 'members.txt')
    with open(members_file, 'r') as f:
        print("Team Members:")
        for line in f:
            member, role = line.strip().split(":")
            print(f"{member} ({role})")

def create_task(team_name, task_name, task_description):
    team_dir = os.path.join('teams', team_name)
    tasks_file = os.path.join(team_dir, 'tasks.txt')
    with open(tasks_file, 'a') as f:
        f.write(f"{task_name}:{task_description}\n")
    print(f"Task '{task_name}' created successfully!")

def assign_task(team_name, task_name, member_name):
    team_dir = os.path.join('teams', team_name)
    assignments_file = os.path.join(team_dir, 'assignments.txt')
    with open(assignments_file, 'a') as f:
        f.write(f"{task_name}:{member_name}\n")
    print(f"Task '{task_name}' assigned to {member_name} successfully!")