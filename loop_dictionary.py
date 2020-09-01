data = [
    {'name': 'foo', 'rank': 3, 'game': 'football', 'total': 1},
    {'name': 'bar', 'rank': 5, 'game': 'hockey', 'total': 0},
    {'name': 'foo', 'rank': 7, 'game': 'tennis', 'total': 0},
    {'name': 'foo', 'rank': 2, 'game': 'cricket', 'total': 2},
    {'name': 'bar', 'rank': 1, 'game': 'cricket', 'total': 8},
]

result = {}

for e in data:
    if e["total"]:
        name = e["name"]
        if name not in result:
            result[name] = []
        result[name].append(e["game"])

print result