with open("02.txt") as f:
    passwords = [a.replace('\n', '').replace('-', ' ').replace(':', '').split(' ') for a in f.readlines()]

count = 0
for password in passwords:
    p1, p2, a, s = int(password[0]), int(password[1]), password[2], password[3]
    if p1 <= s.count(a) <= p2:
        count += 1
print(count)

count = 0
for password in passwords:
    p1, p2, a, s = int(password[0]), int(password[1]), password[2], password[3]
    if s[p1-1] == a and s[p2-1] != a or s[p1-1] != a and s[p2-1] == a:
        count += 1
print(count)
