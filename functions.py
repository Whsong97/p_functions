def max_num(a, b, c):
    return max(a, b, c)

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def rev_string(string):
    return string[::-1]

def num_within(num, start, end):
    return start <= num <= end

def pascal(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(len(prev_row)-1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)
        triangle.append(row)
    for row in triangle:
        print(' '.join(map(str, row)))

print(max_num(10, 5, 8))  # Output: 10

numbers = [2, 3, 4, 5]
print(mult_list(numbers))  # Output: 120

print(rev_string("Hello, World!"))  # Output: "!dlroW ,olleH"

print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5))  # Output: False

pascal(5)
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
