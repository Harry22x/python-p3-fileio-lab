def write_file(file_name, file_content):
    pass
    with open(f"{file_name}.txt",mode='a', encoding="utf-8") as file_name:
        file_name.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f"{file_name}.txt",mode='a', encoding="utf-8") as file_name:
        file_name.write(append_content)
def read_file(file_name):
    pass
    with open(f"{file_name}.txt", encoding="utf-8") as file:
       return file.read()