def read_file():
    try:
        file=open("greetings.txt","r")
        content=file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found")
read_file()            