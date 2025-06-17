from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace

def server_apply_corrections(b0, b1):
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    if b1 == 1:
        qc.x(2)
    if b0 == 1:
        qc.z(2)

    full_state = Statevector.from_instruction(qc)
    q2_state = partial_trace(full_state, [0, 1])

    return q2_state
