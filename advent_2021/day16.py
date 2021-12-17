from utils import cat, Inputstr

from collections import namedtuple
from typing import List, Tuple
from math import prod


def getInput():
    return Inputstr("16")


Bits = str  # a string of '0's and '1's
Packet = namedtuple("Packet", "V, T, contents")  # V is version; T is type ID


def bits_from_hex(hex) -> Bits:
    """Convert a hexadecimal string into a bit string, making sure each hex digit is 4 bits."""
    # I could have used just `bin(int(hex, 16))`, except that wouldn't left-zero-pad when needed.
    return cat(f"{int(x, 16):04b}" for x in hex)


def int2(bits: Bits) -> int:
    """Convert a bit string into an int."""
    return int(bits, 2)


def parse_int(L, bits) -> Tuple[int, Bits]:
    """Parse an integer from the first L bits; return the int and the remaining bits."""
    return int2(bits[:L]), bits[L:]


def parse_packet(bits) -> Tuple[Packet, Bits]:
    """Parse a packet; return it and the remaining bits."""
    V, T, bits = int2(bits[0:3]), int2(bits[3:6]), bits[6:]
    parser = parse_literal_packet if T == 4 else parse_operator_packet
    return parser(V, T, bits)


def parse_literal_packet(V, T, bits) -> Tuple[Packet, Bits]:
    """Build a packet with a literal value; return it and the remaining bits."""
    literal = ""
    while True:
        bit, nibble, bits = bits[0], bits[1:5], bits[5:]
        literal += nibble
        if bit == "0":
            return Packet(V, T, int2(literal)), bits


def parse_operator_packet(V, T, bits) -> Tuple[Packet, Bits]:
    """Build a packet with subpackets; return it and the remaining bits."""
    I, bits = parse_int(1, bits)
    subpackets = []
    if I == 0:
        L, bits = parse_int(15, bits)
        target = len(bits) - L
        while len(bits) > target:
            packet, bits = parse_packet(bits)
            subpackets.append(packet)
    else:
        L, bits = parse_int(11, bits)
        for _ in range(L):
            packet, bits = parse_packet(bits)
            subpackets.append(packet)
    return Packet(V, T, subpackets), bits


def subpackets(packet) -> List[Packet]:
    """The subpackets of a packet."""
    return packet.contents if isinstance(packet.contents, list) else []


def sum_versions(packet) -> int:
    """The sum of the version numbers of this packet and all its subpackets (recursively)."""
    return packet.V + sum(sum_versions(p) for p in subpackets(packet))


def eval_packet(packet) -> int:
    """Evaluate a packet according to the operator rules."""
    if packet.T == 4:
        return packet.contents
    else:
        vals = [eval_packet(p) for p in subpackets(packet)]
        return packet_ops[packet.T](vals)


packet_ops = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda v: int(v[0] > v[1]),
    6: lambda v: int(v[0] < v[1]),
    7: lambda v: int(v[0] == v[1]),
}


def test_decode():
    packet16, _ = parse_packet(bits_from_hex(getInput()))
    actual = sum_versions(packet16)
    assert actual == 951


def test_eval():
    packet16, _ = parse_packet(bits_from_hex(getInput()))
    actual = eval_packet(packet16)

    assert actual == 902198718880
