import csv

student = [
        {
            "ID": 1, 
            "Name": "Shahriar",
            "Roll": 480,
            "Section":"B",
            "Grade": "A+"
            
        },
        {
            "ID": 2, 
            "Name": "Riya", 
            "Roll": 500,
            "Section":"B",
            "Grade": "A"
        },
    ]


with open("grades.csv", "w", newline="") as CSVfile:
    colums = ["ID", "Name", "Roll", "Section",  "Grade"]
    writer = csv.DictWriter(CSVfile, fieldnames=colums)

    writer.writeheader()
    writer.writerows()
