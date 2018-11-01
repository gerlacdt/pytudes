from utils import Integers
from myutils import readFile
from collections import defaultdict


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


def swarm(input1=input1, N=100):
    lines = input1.splitlines()
    particles = [Integers(line) for line in lines]
    distances = [distance((p[0], p[1], p[2])) for p in particles]
    minIndex = -1

    for i in range(N):
        distances = tick(particles)
        minIndex = distances.index(min(distances))

    return minIndex


input2 = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
"""


def destroy(particles):
    # check collisions of particles
    # remove collided particles
    dups = defaultdict(set)
    for i, p in enumerate(particles):
        dups[(p[0], p[1], p[2])].add(i)

    indexToDelete = set()
    for k, v in dups.items():
        l = dups[k]
        if len(l) > 1:
            indexToDelete.update(l)

    clearedParticles = []
    for i, p in enumerate(particles):
        if i in indexToDelete:
            continue
        clearedParticles.append(p)
    return clearedParticles


def collision(input1, N=3):
    lines = input1.splitlines()
    particles = [Integers(line) for line in lines]
    distances = [distance((p[0], p[1], p[2])) for p in particles]
    minIndex = -1

    for i in range(N):
        tick(particles)
        particles = destroy(particles)
    return len(particles)
