import re

# build data structures: firewall, packet

input1 = '''0: 3
1: 2
4: 4
6: 4
'''

UP = 'UP'
DOWN = 'DOWN'


EMPTY_LAYER = ('UP', 0, 0)


def toggle(direction):
    d = {
        'UP': 'DOWN',
        'DOWN': 'UP'
    }
    return d[direction]


def tick(layer):
    """Advance one step of the firewall layer. Take current depth and
    increment it or if at the end reverse.
    """
    direction, scanning_range, idx = layer
    if direction == 'UP' and idx < scanning_range - 1:
        idx += 1
        return (direction, scanning_range, idx)
    if direction == "DOWN" and idx > 0:
        idx -= 1
        return (direction, scanning_range, idx)
    if direction == 'UP' and idx == scanning_range - 1:
        idx -= 1
        return (toggle(direction), scanning_range, idx)
    if direction == 'DOWN' and idx == 0:
        idx += 1
        return (toggle(direction), scanning_range, idx)
    raise RuntimeError("Invalid layer: {}".format(layer))


def scanner(content):
    firewall = []
    lines = content.splitlines()
    for line in lines:
        depth, n = re.findall(r'\w+', line)
        # create layer as tuple (direction, range, currentIndex)
        layer = (UP, int(n), 0)
        if int(depth) > len(firewall):
            filler = [EMPTY_LAYER for i in range(len(firewall), int(depth))]
            firewall += filler
        firewall.append(layer)

    # runner
    position = 0
    acc = 0
    for depth, layer in enumerate(firewall):
        _direction, scanning_range, layer_idx = layer
        if position == layer_idx:
            acc += depth * scanning_range
        # tick all
        for i, rlayer in enumerate(firewall):
            if rlayer != EMPTY_LAYER:
                firewall[i] = tick(rlayer)
    return acc
