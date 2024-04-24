def write_from_file_to_file():
    with open('dataset_24465_4.txt', 'r') as file:
        lines = file.readlines()
        inputList = [line.strip() for line in lines]
        print(inputList)
    with open('randomOutput.txt', 'w') as file:
        for line in reversed(inputList):
            file.write(line+ '\n')
        


write_from_file_to_file()
