input_list = [int(num) for num in input('This is the input file: ').split()]
final_output = []

for start_number in input_list:
    start_n = int(start_number)
    return_n = []

    # turn 1
    while start_n > 3:

        return_n.append(start_n // 3)
        start_n = start_n // 3 + start_n % 3

    # last turn
    # assume borrowing happens at the last turn when lender is running out of budget
    # temperarily ignore on the borrowing amount as it will not be counted in the final return
    if 0 < start_n <= 3:
        borrow = 3 - start_n
        return_n.append(1)

    final_output.append(sum(return_n))

for output in final_output:
    print(output)
