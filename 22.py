with open('22.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    cards = [int(line) for line in lines if 0 < len(line) < 5][::-1]


def play(cards_a: [], cards_b: [], recursive=False):
    history = []
    while len(cards_a) > 0 and len(cards_b) > 0:
        if recursive:  # maintain the history
            if cards_a in history:
                return 'a'
            else:
                history.append(cards_a.copy())

        a, b, winner = cards_a.pop(), cards_b.pop(), None

        if recursive:
            if len(cards_a) >= a and len(cards_b) >= b:
                winner = play(cards_a[-a:], cards_b[-b:], True)
            elif len(cards_a) < a or len(cards_b) < b:
                winner = 'a' if a > b else 'b'
        else:
            winner = 'a' if a > b else 'b'

        if winner == 'a':
            cards_a.insert(0, a)
            cards_a.insert(0, b)
        else:
            cards_b.insert(0, b)
            cards_b.insert(0, a)
    return 'a' if len(cards_b) == 0 else 'b'


player_b, player_a = cards[:len(cards) // 2], cards[len(cards) // 2:]
play(player_a, player_b)

result = sum([(i + 1) * card for i, card in enumerate(player_a + player_b)])
print(result)  # 35202
assert 35202 == result

player_b, player_a = cards[:len(cards) // 2], cards[len(cards) // 2:]
play(player_a, player_b, True)

result = sum([(i + 1) * card for i, card in enumerate(player_a + player_b)])
print(result)  # 32317
assert 32317 == result
