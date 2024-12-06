from collections import Counter
def main():
    data = read_input()
    la, lb = get_locations(data)
    la, lb = order_locations(la), order_locations(lb)
    print("total_distance:", get_total_distance(la, lb))
    print("similarity_score:", get_similarity_score(la, lb))


def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()


def get_locations(data):
    locations_a = []
    locations_b = []
    for line in data:
        a, b = line.split()
        locations_a.append(int(a))
        locations_b.append(int(b))
    return locations_a, locations_b


def order_locations(locations):
    return sorted(locations)


def get_distances(locations_a, locations_b):
    return [abs(la - lb) for la, lb in zip(locations_a, locations_b)]


def get_total_distance(locations_a, locations_b):
    return sum(get_distances(locations_a, locations_b))


def get_similarity_score(locations_a, locations_b):
    la = set(locations_a)
    lb = Counter(locations_b)
    return sum([le * lb.get(le, 0) for le in la])


if __name__ == '__main__':
    main()
