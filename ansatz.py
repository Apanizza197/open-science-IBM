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

# ANSATZ 4 ES EL QUE ESTAMOS USANDO EN EL PRIMER CASO
# RY CX
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

# Controlled RY
num_qubits = 3
layers = 1

def create_ansatz_cry(num_qubits, layers = 1):
    qc = QuantumCircuit(num_qubits)
    j = 0
    for layer in range(layers):
        qc.ry(Parameter('θ_' + str(j)), 0)
        j += 1

        for qubit in range(1, num_qubits):
            qc.cry(Parameter('θ_' + str(j)), qubit - 1, qubit)
            j += 1
    return qc

def create_ansatz(num_qubits, layers):
    qc = QuantumCircuit(num_qubits)
    j = 0
    for layer in range(layers):
        qc.ry(Parameter('θ_' + str(j)), 0)
        j += 1

        for qubit in range(1, num_qubits):
            qc.cry(Parameter('θ_' + str(j)), qubit - 1, qubit)
            qc.cnot(qubit, qubit -1)
            j += 1
    
    return qc


