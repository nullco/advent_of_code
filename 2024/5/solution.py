

def main():
    data = read_input()
    rules, pages = get_print_config(data)
    ordered_pages, unordered_pages = get_pages_to_print(rules, pages)
    medians = get_medians(ordered_pages)
    print('medians sum: ', sum(medians))
    reordered_pages = fix_unordered_pages(rules, unordered_pages)
    medians = get_medians(reordered_pages)
    print('medians sum - fixed ones: ', sum(medians))


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


def get_pages_to_print(ordering_rules, pages):
    ordered = []
    unordered = []
    for p in pages:
        applying_rules = [r for r in ordering_rules if rule_applies(r, p)]
        if all([validate_rule(r, p) for r in applying_rules]):
            ordered.append(p)
        else:
            unordered.append(p)
    return ordered, unordered


def fix_unordered_pages(ordering_rules, unordered_pages):
    result = []
    for p in unordered_pages:
        applying_rules = [r for r in ordering_rules if rule_applies(r, p)]
        pages_after = get_pages_after(p, applying_rules)
        srs = sorted(pages_after.items(), key=lambda item: len(item[1]))
        result.append([k for k, _ in srs])
    return result


def get_pages_after(pages, rules):
    res = {p: set() for p in pages}
    for rb, ra in rules:
        res[ra].add(rb)
    return res


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
