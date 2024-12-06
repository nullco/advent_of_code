def main():
    data = read_input()
    reports = get_reports(data)
    print('safe_reports:', count_safe(reports))
    print('safe_reports(et=1):', count_safe(reports, error_tolerance=True))


def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()


def get_reports(data):
    return [[int(lvl) for lvl in line.split()] for line in data]


def count_safe(reports, error_tolerance=False):
    return sum([1 for r in reports if is_safe(r, error_tolerance)])


def is_safe(report, error_tolerance):
    def _is_save(levels):
        return (
            test(levels, increasing)
            or test(levels, decreasing)
        )
    if _is_save(report):
        return True
    elif not error_tolerance:
        return False
    for i in range(len(report)):
        if _is_save(report[: i] + report[i + 1:]):
            return True
    return False


def increasing(prev, nxt):
    return nxt > prev and valid_diff(prev, nxt)


def decreasing(prev, nxt):
    return nxt < prev and valid_diff(prev, nxt)


def valid_diff(prev, nxt):
    return 1 <= abs(prev - nxt) <= 3


def test(levels, cond):
    last = None
    for lvl in levels:
        if last is None:
            last = lvl
            continue
        if not cond(last, lvl):
            return False
        last = lvl
    return True


if __name__ == '__main__':
    main()
