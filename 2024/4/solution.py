import re


def main():
    data = read_input()
    print('total xmas:', count_xmas(data))
    print('total cross-mas:', count_cross_mas(data))


def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()


def count_xmas(data):
    return (
        count_horizontal(data)
        + count_vertical(data)
        + count_diagonal(data)
    )


def count_horizontal(data):
    left_right = sum(len(re.findall(r'XMAS', line)) for line in data)
    right_left = sum(len(re.findall(r'SAMX', line)) for line in data)
    return left_right + right_left


def count_vertical(data):
    data = transpose(data)
    up_down = sum(len(re.findall(r'XMAS', line)) for line in data)
    down_up = sum(len(re.findall(r'SAMX', line)) for line in data)
    return up_down + down_up


def count_diagonal(data):
    diagonals = get_diagonals(data)
    antidiagonals = get_antidiagonals(data)
    df = sum(len(re.findall(r'XMAS', line)) for line in diagonals)
    db = sum(len(re.findall(r'SAMX', line)) for line in diagonals)
    adf = sum(len(re.findall(r'XMAS', line)) for line in antidiagonals)
    adb = sum(len(re.findall(r'SAMX', line)) for line in antidiagonals)
    return df + db + adf + adb


def transpose(data):
    return ["".join(chars) for chars in zip(*data)]


def get_diagonals(data):
    rows = len(data)
    columns = len(data[0])
    diagonals = []
    row = 0
    while row < rows:
        r = row
        c = 0
        diagonal = []
        while c < columns and r > -1:
            diagonal.append(data[r][c])
            r -= 1
            c += 1
        diagonals.append("".join(diagonal))
        row += 1
    row -= 1
    col = 1
    while col < columns:
        r = row
        c = col
        diagonal = []
        while c < columns and r > -1:
            diagonal.append(data[r][c])
            r -= 1
            c += 1
        diagonals.append("".join(diagonal))
        col += 1
    return diagonals


def get_antidiagonals(data):
    rows = len(data)
    columns = len(data[0])
    diagonals = []
    row = rows - 1
    while row > -1:
        r = row
        c = 0
        diagonal = []
        while c < columns and r < rows:
            diagonal.append(data[r][c])
            r += 1
            c += 1
        diagonals.append("".join(diagonal))
        row -= 1
    row += 1
    col = 1
    while col < columns:
        r = row
        c = col
        diagonal = []
        while c < columns and r > -1:
            diagonal.append(data[r][c])
            r += 1
            c += 1
        diagonals.append("".join(diagonal))
        col += 1
    return diagonals


def count_cross_mas(data):
    count = 0
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i]):
            if has_cross_mas(data, i, j):
                count += 1
    return count


def has_cross_mas(data, i, j):
    if data[i][j] != 'A':
        return False
    imax = len(data) - 1
    jmax = len(data[i]) - 1
    if i - 1 < 0:
        return False
    if i + 1 > imax:
        return False
    if j - 1 < 0:
        return False
    if j + 1 > jmax:
        return False

    ul = data[i - 1][j - 1]
    dr = data[i + 1][j + 1]
    if not ((dr == 'M' and ul == 'S') or (dr == 'S' and ul == 'M')):
        return False

    dl = data[i + 1][j - 1]
    ur = data[i - 1][j + 1]
    if not ((dl == 'M' and ur == 'S') or (dl == 'S' and ur == 'M')):
        return False
    return True


if __name__ == '__main__':
    main()
