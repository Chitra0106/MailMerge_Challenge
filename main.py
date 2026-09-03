import os
with open(r"C:\Users\mailc\PythonProject\.venv\StartingLetter\StartingLetter.txt") as data:
    Letter = data.read().strip()


with open(r"C:\Users\mailc\PythonProject\.venv\Names\Names.txt") as namedata:
    Names = namedata.readlines()


for Name in Names:
    #print(Name)
    Name = Name.strip()
    Person_Letter = Letter.replace("name",Name)
    print(Letter)
    output_path = os.path.join(
        r"C:\Users\mailc\PythonProject\.venv\Output",
        Name + ".txt"
    )
    op_doc_path = os.path.join(
        r"C:\Users\mailc\PythonProject\.venv\Output",
        Name + ".docx"
    )
    with open(output_path,"w") as output:
        output.write(Person_Letter)
    with open(op_doc_path, "w") as output:
        output.write(Person_Letter)