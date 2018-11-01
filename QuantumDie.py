from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
import time


def throw_octahedral_die():
    """Throws a fair octahedral die."""
    qvm = QVMConnection(random_seed=int(time.time() * 10000000))
    p = Program(H(0), H(1), H(2)).measure_all()

    result = qvm.run(p)

    return bit_list_to_int(result[0]) + 1


def bit_list_to_int(bit_list: list) -> int:
    """Converts a list of bits to an integer."""
    out = 0
    for bit in bit_list:
        out = (out << 1) | bit

    return out


throws = []
n = 20
i = 0
while i < n:
    throws.append(throw_octahedral_die())
    i += 1


print(throws)

for i in throw:
    print i
