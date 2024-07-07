import os

def compare_files(old_file, new_file, output_file):
    with open(old_file, 'r') as f1, open(new_file, 'r') as f2:
        old_lines = set(f1.readlines())
        new_lines = set(f2.readlines())

    diff_lines = old_lines - new_lines

    with open(output_file, 'w') as out:
        out.writelines(diff_lines)

# Get the current logged-in user's home directory
home_dir = os.path.expanduser('~')

# File paths
old_file = os.path.join(home_dir, 'compare', 'old.txt')
new_file = os.path.join(home_dir, 'compare', 'new.txt')
output_file = os.path.join(home_dir, 'compare', 'output.txt')

compare_files(old_file, new_file, output_file)
