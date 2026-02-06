import os

current_dir = os.getcwd()
print(f'Current Directory: {current_dir}')

dir_list = os.listdir('.') # '.' --> currently je directory te achi
print(f'Files in current dir: {dir_list}')