import random

def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()


file_path = 'r' 

random_line = get_random_line(file_path)
print(random_line)
