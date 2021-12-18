from utils import Integers, Inputstr, nothing, sign, quantify
from collections import namedtuple


def getInput():
    return Inputstr("17")


class Target:
    def __init__(self, a, b, c, d):
        self.Xs = range(a, b + 1)
        self.Ys = range(c, d + 1)

    def __repr__(self):
        return "Xs: {} Ys: {}".format(self.Xs, self.Ys)


Probe = namedtuple(
    "Probe", ["x", "y", "vx", "vy", "hit", "highest"], defaults=(0, 0, 0, 0, False, 0)
)


def probe_step(probe, target) -> Probe:
    """Simulate the physics of the probe for one time step."""
    x, y, vx, vy, hit, highest = probe
    return Probe(
        x=x + vx,
        y=y + vy,
        vx=sign(vx) * (abs(vx) - 1),
        vy=vy - 1,
        hit=hit or (x in target.Xs and y in target.Ys),
        highest=max(highest, y + vy),
    )


def probe_steps(probe, target, do=nothing) -> Probe:
    """Simulate the probe until it passes the target.  You can optionally
    `do` something to the probe on each time step.

    """
    maxx, miny = max(target.Xs), min(target.Ys)
    do(probe)
    while probe.x <= maxx and probe.y >= miny:
        probe = probe_step(probe, target)
        if probe.hit:
            do(probe)
    return probe


def highest_height(vxs, vys, target) -> int:
    """The highest height reached by a probe that hits the target, among all vx and vy values."""
    probes = [
        probe_steps(Probe(vx=vx, vy=vy), target, do=nothing) for vx in vxs for vy in vys
    ]
    return max([probe.highest for probe in probes if probe.hit])


def probe_hits(vxs, vys, target) -> int:
    """How many of these velocities cause the probe to hit the target?"""
    return quantify(
        probe_steps(Probe(vx=vx, vy=vy), target).hit for vx in vxs for vy in vys
    )


example = "target area: x=20..30, y=-10..-5"


def test_shot_example():
    target = Target(*Integers(example))
    probe = Probe(vx=7, vy=2)
    probe_steps(probe, target)


def test_shot():
    target = Target(*Integers(getInput()))

    vxs = [i for i in range(10, 11)]
    vys = [i for i in range(225)]
    actual = highest_height(vxs, vys, target)

    assert actual == 25200


def test_any_hits():
    target = Target(*Integers(getInput()))
    vxs = [i for i in range(5, max(target.Xs) + 1)]
    vys = [i for i in range(min(target.Ys), 250)]
    actual = probe_hits(vxs, vys, target)

    assert actual == 3012
