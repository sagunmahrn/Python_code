# Example 1
# students ={"Hermione":"Gryffindor",
#            "Harry":"Gryffindor",
#            "Ron":"Gryffindor",
#            "Draco":"Slytherin"
#            }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student,students[student],sep=",")

# Example 2
students= [
    {"name":"Hermione","house":"Gryffindor","Patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","Patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","Patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","Patronus":None},
]

for student in students:
    print(student["name"], student["house"],student["Patronus"],sep=",")