from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import random

def quantum_login_simulation():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)

    state = Statevector.from_instruction(qc)
    measured = random.choice(['00', '01', '10', '11'])
    b0 = int(measured[1])
    b1 = int(measured[0])
    return b0, b1
