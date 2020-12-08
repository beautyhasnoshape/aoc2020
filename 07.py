import re

with open("07.txt") as f:
    lines = [a.replace('\n', '') for a in f.readlines()]

bags = {
    bag: [(b, int(a)) for a, b in re.findall(r"([0-9]+) ([a-z]+ [a-z]+) bag[s]?[\,\.]", bags)]
    for (bag, bags) in [txt.split(' bags contain ') for txt in lines]
}

# non-regex version:
#
# bags = {}
# for line in lines:
#     e = line.split(' ')
#     bag = e[0] + ' ' + e[1]
#     if bag not in bags:
#         bags[bag] = []
#     if e[4] != 'no':
#         for i in range((len(e)-4) // 4):
#             a, b = e[4+i*4+0], e[4+i*4+1] + ' ' + e[4+i*4+2]
#             bags[bag].append((b, a))


def traverse(bag: str, top_bag: str, result: set):
    if bag not in bags:
        return
    for child in bags[bag]:
        if child[0] == 'shiny gold':
            result.add(top_bag)
            break

        traverse(child[0], top_bag, result)


result = set()
for bag in bags:
    traverse(bag, bag, result)
print(len(result))

assert 222 == len(result)


def traverse2(bag: str, result: list, m: int):
    if bag not in bags:
        return
    for child in bags[bag]:
        result.append(m * int(child[1]))

        traverse2(child[0], result, m * int(child[1]))


result = list()
traverse2('shiny gold', result, 1)
print(sum(result))

assert 13264 == sum(result)
