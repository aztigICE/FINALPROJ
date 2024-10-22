import os

def view_assignments(team_name):
    team_dir = os.path.join('teams', team_name)
    assignments_file = os.path.join(team_dir, 'assignments.txt')
    with open(assignments_file, 'r') as f:
        print("Task Assignments:")
        for line in f:
            task_name, member_name = line.strip().split(":")
            print(f"{task_name} - {member_name}")