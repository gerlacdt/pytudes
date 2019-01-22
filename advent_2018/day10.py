from utils import Inputstr, Integers


input10 = Inputstr(10)

test_input = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""


def output(stars):
    minx = min([s[0]for s in stars])
    miny = min([s[1]for s in stars])
    maxx = max([s[0]for s in stars])
    maxy = max([s[1]for s in stars])

    height = abs(maxy - miny)
    if height > 10:
        return None

    d = {(s[0], s[1]) for s in stars}

    for i in range(miny-1, maxy+1):
        for j in range(minx-1, maxx+1):
            if (j, i) in d:
                print("#", end="")
            else:
                print(".", end="")
        print("")

    print("")
    return True


def part1(content=test_input):
    lines = content.splitlines()
    stars = []
    for line in lines:
        x, y, vx, vy = Integers(line)
        stars.append((x, y, vx, vy))
    # make the moves
    move = False
    second = 0
    while not move:
        second += 1
        for j, s in enumerate(stars):
            x, y, vx, vy = s
            stars[j] = (x+vx, y+vy, vx, vy)
        move = output(stars)
    return second
