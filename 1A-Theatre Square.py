import math

input_string = list(input().split(" "))

n = int(input_string[0])

m = int(input_string[1])

a = int(input_string[2])

flagstones_int = math.ceil(n / a) * math.ceil(m /  a)

print(flagstones_int)