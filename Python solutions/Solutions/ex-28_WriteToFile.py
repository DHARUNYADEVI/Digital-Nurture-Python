def write_file():
    file=open("greetings.txt","w")
    file.write("Hello, world!!")
    file.close()
    print("Data written successfully")
write_file()    