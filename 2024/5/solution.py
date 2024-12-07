

def main():
    data = read_input()
    rules, pages = get_print_config(data)
    ordered_pages = detect_correctly_ordered_pages(rules, pages)
    medians = get_medians(ordered_pages)
    print('medians sum: ', sum(medians))


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


def get_print_config(data):
    ordering_rules = []
    pages = []
    section = 'rules'
    for line in data:
        if not line:
            section = 'pages'
        elif section == 'rules':
            ordering_rules.append([int(e) for e in line.split('|')])
        elif section == 'pages':
            pages.append([int(e) for e in line.split(',')])
    return ordering_rules, pages


def detect_correctly_ordered_pages(ordering_rules, pages):
    result = []
    for p in pages:
        applying_rules = [r for r in ordering_rules if rule_applies(r, p)]
        if all([validate_rule(r, p) for r in applying_rules]):
            result.append(p)
    return result


def rule_applies(rule, pages):
    pb, pa = rule
    if pb in pages and pa in pages:
        return True
    return False


def validate_rule(rule, pages):
    pb, pa = rule
    if pages.index(pb) < pages.index(pa):
        return True
    return False


def get_medians(pages):
    res = []
    for p in pages:
        res.append(p[(len(p) // 2)])
    return res


if __name__ == '__main__':
    main()
