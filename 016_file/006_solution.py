import os

cd = os.getcwd()
print(f"Current directory: {cd}")

# cross platfrom path create

folderName = "016_file"
fileName = "notes.txt"

# os.path.join autometic (/ or \) detact kore thik kore nibe
fullPath = os.path.join(cd, folderName, fileName)
print(f"created path: {fullPath}")

with open(fullPath, "w") as f:
    f.write("Hello jonogon how are you")
