def add_nums():
    pair = raw_input("Input two numbers: ")
    list_pair = pair.split(" ")
    sum_num = 0

    for number in list_pair:
        sum_num += int(number)

    print sum_num

add_nums()


def sum_nums():
    raw_input("Input number of values: ")
    string_values = raw_input("Input list of values: ")
    list_values = string_values.split(" ")
    sum_num = 0

    for number in list_values:
        sum_num += int(number)

    print sum_num

sum_nums()


def list_sum():
    num_pairs = int(raw_input("Input number of values: "))
    sum_list = []

    while True:
        if num_pairs > 0:
            string_pairs = raw_input("Input pair of numbers: ")
            list_pairs = string_pairs.split(" ")
            num_pairs = num_pairs - 1
            sum_num = 0

            for number in list_pairs:
                sum_num += int(number)

            sum_list.append(sum_num)
        else:
            break

    for number in sum_list:
        print number,

list_sum()


def list_min():
    num_pairs = int(raw_input("Input number of values: "))
    min_list = []

    while True:
        if num_pairs > 0:
            string_pairs = raw_input("Input pair of numbers: ")
            list_pairs = string_pairs.split(" ")
            num_pairs = num_pairs - 1
            minimum = min(int(list_pairs[0]), int(list_pairs[1]))
            min_list.append(minimum)
        else:
            break

    for number in min_list:
        print number,

list_min()


def list_min():
    num_triples = int(raw_input("Input number of values: "))
    min_list = []

    while True:
        if num_triples > 0:
            string_triples = raw_input("Input set of numbers: ")
            list_triples = string_triples.split(" ")
            num_triples = num_triples - 1
            minimum = min(int(list_triples[0]), int(list_triples[1]), int(list_triples[2]))
            min_list.append(minimum)
        else:
            break

    for number in min_list:
        print number,

list_min()


def max_min():
    string_values = raw_input("Input list of values: ")
    list_values = string_values.split(" ")
    list_values = [int(number) for number in list_values]
    max_min_list = []

    maximum = max(list_values)
    max_min_list.append(maximum)

    minimum = min(list_values)
    max_min_list.append(minimum)

    for number in max_min_list:
        print number,

max_min()


def round_div():
    num_pairs = int(raw_input("Input number of values: "))
    round_list = []

    while True:
        if num_pairs > 0:
            string_pairs = raw_input("Input pair of numbers: ")
            list_pairs = string_pairs.split(" ")
            num_pairs = num_pairs - 1
            remainder = (float(list_pairs[0]) / float(list_pairs[1])) % 1
            if remainder >= 0.5:
                division = (int(list_pairs[0]) / int(list_pairs[1])) + 1
            else:
                division = (int(list_pairs[0]) / int(list_pairs[1]))
            round_list.append(division)
        else:
            break

    for number in round_list:
        print number,

round_div()
