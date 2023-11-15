import json

file_name = 'data.txt'

def read_file(file_name: str) -> str:
    f = open(file=file_name)
    data = f.read()
    f.close()
    return data

def to_dict(data: str) -> dict:
    try:
        numbers = json.loads(data)
    except json.decoder.JSONDecodeError:
        numbers = {
            "numbers": []
        }

    return numbers

def sum_of_numbers(numbers: dict) -> int:
    s = 0
    for number in numbers['numbers']:
        s += number

    return s

data = read_file(file_name)
numbers = to_dict(data)
s = sum_of_numbers(numbers)

print(s)