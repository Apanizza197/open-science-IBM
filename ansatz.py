from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Parameter

def create_ansatz_1(num_qubits, layers = 1):
    qc = QuantumCircuit(num_qubits)

    for qubit in range(0, num_qubits - (num_qubits % 2), 2):
        qc.h(qubit)
        qc.cnot(qubit, qubit+1)

    j = 0
    for layer in range(layers):
        for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
        for qubit in range(num_qubits - 1):
            qc.cnot(qubit, qubit+1)
    return qc

def create_ansatz_2(num_qubits, layers = 1):
    qc = QuantumCircuit(num_qubits)
    j = 0
    for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
    for layer in range(layers):
        for qubit in range(num_qubits - 1):
            qc.cnot(qubit, qubit+1)
        for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
       
    return qc

def create_ansatz_3(num_qubits, layers = 1):
    qc = QuantumCircuit(num_qubits)
    j = 0
    for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
    for layer in range(layers):
        for qubit in range(0, (num_qubits % 2), 2):
            qc.h(qubit)
            qc.cnot(qubit, qubit+1)
        for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
       
    return qc

def create_ansatz_4(num_qubits, layers = 1):
    qc = QuantumCircuit(num_qubits)
    j = 0
    for layer in range(layers):
        for qubit in range(num_qubits):
            qc.ry(Parameter('θ_' + str(j)), qubit)
            j += 1
        for qubit in range(num_qubits -1):
            qc.cnot(qubit, qubit+1)
        
    return qc


qc = create_ansatz_3(6, 2)
