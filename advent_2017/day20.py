from utils import Integers
from myutils import readFile


INPUT1 = readFile("./data/input20.txt")

input1 = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
"""


def distance(pos):
    return sum([abs(x) for x in pos])


def tick(particles):
    for i, p in enumerate(particles):
        px, py, pz, vx, vy, vz, ax, ay, az = p
        vx += ax
        vy += ay
        vz += az
        px += vx
        py += vy
        pz += vz
        p = (px, py, pz, vx, vy, vz, ax, ay, az)
        particles[i] = p
    return [distance((p[0], p[1], p[2])) for p in particles]


def swarm(input1=input1):
    lines = input1.splitlines()
    particles = [Integers(line) for line in lines]
    distances = [distance((p[0], p[1], p[2])) for p in particles]
    minIndex = -1

    for i in range(1000):
        distances = tick(particles)
        minIndex = distances.index(min(distances))

    return minIndex
