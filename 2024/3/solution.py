import re


def main():
    data = read_input()
    muls = extract_muls(data)
    conditional_muls = extract_conditional_muls(data)
    print('mul totals:', calculate(muls))
    print('conditional mul totals:', calculate(conditional_muls))


def read_input():
    with open('input.txt', 'r') as f:
        return f.read()


def extract_muls(data):
    return re.findall(r"mul\((\d+),(\d+)\)", data)


def extract_conditional_muls(data):
    enabled = True
    res = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    muls = []
    for r in res:
        if r == 'do()':
            enabled = True
        elif r == "don't()":
            enabled = False

        if enabled:
            match = re.match(r"mul\((\d+),(\d+)\)", r)
            if match:
                muls.append((match.group(1), match.group(2)))
    return muls


def calculate(ops):
    return sum([int(a) * int(b) for a, b in ops])


if __name__ == '__main__':
    main()
