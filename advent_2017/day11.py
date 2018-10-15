from utils import king_distance, origin, add

input1 = 'ne,ne,ne'

headings6 = dict(n=(0, -1), ne=(1, 0), se=(1, 1),
                 s=(0, 1), sw=(-1, 0), nw=(-1, -1))


def follow(input1):
    "Follow each step of the path; return final distance to origin."
    path = input1.rstrip('\n').split(',')
    pos = origin
    maxDistance = 0
    for dir in path:
        pos = add(pos, headings6[dir])
        maxDistance = king_distance(pos) if king_distance(pos) > maxDistance else maxDistance
    return king_distance(pos), maxDistance
