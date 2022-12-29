#!python3

from collections import defaultdict, deque


class Component(object):
    def __init__(self, line):
        self.ports = list(map(int, line.split('/')))

    def __repr__(self):
        return '<Component %s>' % self.ports

    def other(self, n):
        """Return the port that's not number n: for 0/2, comp.other(0)
        returns 2; for 2/2, comp.other(2) returns 2."""
        p = self.ports
        return p[1] if p[0] == n else p[0]

    def value(self):
        return sum(self.ports)


with open('input/day24.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

components = [Component(line) for line in input_lines]

# generate a lookup by port
by_port = defaultdict(list)
for c in components:
    for p in c.ports:
        by_port[p].append(c)


strongest = 0
by_len = defaultdict(list)

# start with all the zeros
q = deque()
for comp in by_port[0]:
    q.append(([comp], comp.other(0)))

# process the queue until we're done
while len(q) > 0:
    bridge, tail = q.popleft()
    total = sum([c.value() for c in bridge])

    strongest = max(strongest, total)
    by_len[len(bridge)].append(total)

    for comp in by_port[tail]:
        if comp in bridge:
            continue
        q.append((bridge + [comp], comp.other(tail)))

# do part two bookkeeping
longest = max(by_len.keys())
strong_long = max(by_len[longest])

print(f"part 1: {strongest}")
print(f"part 2: {strong_long}")
