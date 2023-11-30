import random

def create_file(amount):
    file = open('number.txt', 'w')

    for i in range(amount):
        file.write(str(random.randint(0, 100)))
        file.write(",")

    file.close()
        
def calculate_average():
    file = open('exercicio01/number.txt', 'r')
    line_lines = file.readlines()
    file.close()
    line_lines = line_lines[0]
    line_lines = line_lines.split(",")
    averag = 0

    for number in line_lines:
        averag += int(number)
    averag = averag / len(line_lines)
    return averag
   
def main():
    create_file(5)
    averag = calculate_average()
    print("A media destes numeros no arquivo é ", averag)

main()
