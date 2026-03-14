import os

print("Directory size analyser")
folder = input("Enter folder path: ")

total_size=0

for root, dir, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(root,file)
        if os.path.exists(file_path):
            total_size+=os.path.getsize(file_path)

print(f"\nTotal size of '{folder}' : {total_size / (1024*1024):.2f} MB")
        