def data_types(input_line, data_line):
    if input_line == "int":
        result = int(data_line) * 2
        print(result)
    elif input_line == "real":
        result = float(data_line) * 1.5
        print(f"{result:.2f}")
    elif input_line == "string":
        result = "$" + data_line + "$"
        print(result)

input_line = input()
data_line = input()
data_types(input_line, data_line)
