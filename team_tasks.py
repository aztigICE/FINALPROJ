import os

def view_tasks(team_name):
    team_dir = os.path.join('teams', team_name)
    tasks_file = os.path.join(team_dir, 'tasks.txt')
    with open(tasks_file, 'r') as f:
        print("Team Tasks:")
        for line in f:
            task_name, task_description = line.strip().split(":")
            print(f"{task_name} - {task_description}")