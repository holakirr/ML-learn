from icecream import ic

print("#" * 100)
print("Cycles")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)


def more_than_n(numbers, n):
    result = []
    for number in numbers:
        if abs(number) > n:
            result.append(number)
    return result


ic(more_than_n([-1, 4, 4.2, 42.2, -3.4, -5.2], 3))
# [4, 4.2, 42.2, -3.4, -5.2]
ic(more_than_n([-1, 4, 4.2, 42.2, -3.4, -5.2], 10))
# [42.2]
ic(more_than_n([], 10))
# []

print("#" * 40, "Task 2", "#" * 40)


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    first_half_sum = 0
    second_half_sum = 0

    for digit in ticket_number[:3]:
        first_half_sum += int(digit)

    for digit in ticket_number[3:]:
        second_half_sum += int(digit)

    return first_half_sum == second_half_sum


ic(lucky_ticket(111111))
# True
ic(lucky_ticket(123456))
# False

print("#" * 40, "Task 3", "#" * 40)


def holes_count(number):
    holes = {"0": 1, "4": 1, "6": 1, "8": 2, "9": 1}
    holes_sum = 0
    for digit in str(number):
        if digit in holes:
            holes_sum += holes[digit]
    return holes_sum


ic(holes_count(8))
# 2
ic(holes_count(146))
# 2
ic(holes_count(84628))
# 6

print("#" * 40, "Task 4", "#" * 40)
matrix_example = [[1, 5, 4], [4, 2, -2], [7, 65, 88]]


def even_numbers_in_matrix(matrix):
    result = 0
    for row in matrix:
        for number in row:
            if number % 2 == 0:
                result += 1
    return result


ic(even_numbers_in_matrix(matrix=matrix_example))
# 5

print("#" * 40, "Task 5", "#" * 40)


def matrix_sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error! Matrices dimensions are different!")
        return None

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[i])):
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result


matrix_example = [[1, 5, 4], [4, 2, -2], [7, 65, 88]]

ic(matrix_sum(matrix1=matrix_example, matrix2=matrix_example))
# [[2, 10, 8], [8, 4, -4], [14, 130, 176]]

matrix1_example = [[1, 5, 4], [4, 2, -2]]

matrix2_example = [[10, 15, 43], [41, 2, -2], [7, 5, 7]]

ic(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# Error! Matrices dimensions are different!
# None

matrix1_example = [[1, 5, 4, 5], [4, 2, -2, -5], [4, 2, -2, -5]]

matrix2_example = [[10, 15, 43], [41, 2, -2], [7, 5, 7]]

ic(matrix_sum(matrix1=matrix1_example, matrix2=matrix2_example))
# Error! Matrices dimensions are different!
# None
