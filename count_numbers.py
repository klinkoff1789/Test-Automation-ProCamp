def count_nums():
    # file = open("number.txt", "r").read().splitlines()
    with open("number.txt", "r") as file:
        sum = 0.0
        for num in (line.strip() for line in file):
            if num:
                if not num.startswith("#"):
                    print(num)
                    sum += float(num)
    return sum


print(count_nums())