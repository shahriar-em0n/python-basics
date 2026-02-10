from pathlib import Path

# set folder and file name
base_path = Path("016_file")
fullPath = base_path / "note.txt"  # (/) operator diye path join kora jay

print(f"PathLib path: {fullPath}")

with open(fullPath, "w") as f:
    f.write("Hello jonogon how are you")