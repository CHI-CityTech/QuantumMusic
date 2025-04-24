# Quantum Music: Mapping Vector Expectations to Qiskit

## 1. Context and Purpose

This part builds upon the mathematical structure introduced in [Professor Berman’s Equation Document](https://github.com/CHI-CityTech/QuantumMusic/blob/main/docs/Equations_project_04_20_2025.pdf), where vector expectations are derived from musical data using statistical methods (see Equation 3).

This document expands on the Quantum Music project by describing how classical musical data—specifically, vectorized expectations derived from Equation 3—can be translated into quantum registers using Qiskit. These vectors represent pitch intervals, delta onset times, and durations, averaged across multiple musical compositions. The goal is to use these expectation values as inputs for quantum circuit transformations that encode, manipulate, and ultimately regenerate new musical forms.

## 2. Quantum Process Overview

The following pseudocode outlines the functional implementation of the quantum encoding pipeline using Qiskit:

```python
# Step 1: Normalize expectation vector values
def normalize_expectations(expectations, value_range=(0, 1)):
    min_val, max_val = min(expectations), max(expectations)
    return [(x - min_val) / (max_val - min_val) * (value_range[1] - value_range[0]) + value_range[0] for x in expectations]

# Step 2: Encode into quantum state using Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import RYGate

# Create parameterized circuit based on expectations
def encode_expectations_to_circuit(expectations):
    n = len(expectations)
    qc = QuantumCircuit(n)
    for i, theta in enumerate(expectations):
        qc.ry(theta, i)  # RY gate used for rotation-based encoding
    return qc

# Step 3: Simulate circuit and analyze output
def simulate_circuit(qc):
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    statevector = result.get_statevector()
    return statevector
```

### Note on Amplitudes and Measurement

In quantum computing, the term **amplitude** refers to a complex-valued coefficient associated with each basis state of a quantum system. These amplitudes contain both magnitude and phase information and are fundamentally different from the musical concept of amplitude (which usually refers to volume or loudness).

The **probability** of observing a particular basis state upon measurement is given by squaring the absolute value of its amplitude:

$$
P(x) = |\alpha_x|^2
$$

Where:
- _**P(x)**_ is the probability of observing basis state *x*
- _**αₓ**_ is the complex-valued amplitude associated with that state
- _**|αₓ|²**_ represents the squared magnitude (i.e., αₓ* · αₓ), ensuring the result is real and non-negative

This squaring guarantees that the outcome is a real, non-negative probability, even though the original amplitude may be complex. This operation aligns with probability theory and enables the interpretation of the quantum statevector as a distribution over potential outcomes. 

This is particularly relevant in **Part 3**, where basis states with the highest probabilities will be selected or weighted to regenerate musical trajectories.


## 4. Remaining Pipeline Components

The current quantum phase has implemented all major steps up to the analysis of the quantum statevector. The following components remain to complete the full pipeline:

- 🔜 **Interpret quantum output**: Identify meaningful amplitudes or probabilities from the statevector to guide reconstruction.
- 🔜 **Rescale and recontextualize results**: Convert quantum outputs (typically in [0,1]) back into musical parameter ranges—e.g., pitch intervals, delta-times, and durations.
- 🔜 **Reconstruct musical trajectory**: Assemble the interpreted and rescaled vectors into a complete musical sequence.
- 🔜 **Export to MIDI**: Use a MIDI library (e.g., `mido`) to generate a valid `.mid` file from the reconstructed trajectory.

## 5. Glossary

- **Amplitude (Quantum)**: A complex-valued coefficient representing the probability amplitude of a quantum basis state. The squared magnitude of this value gives the probability of observing that state upon measurement.
- **Amplitude (Musical)**: The perceived loudness or volume of a note, based on the physical energy of its waveform. Not to be confused with quantum amplitude.
- **Qubit**: The basic unit of quantum information, analogous to a classical bit, but capable of existing in superposition.
- **Quantum Statevector**: A vector that describes the full state of a quantum system. It encodes the amplitude for every possible basis state.
- **Expectation Value (Equation 3)**: The average contribution of a characteristic across multiple phrases, serving as the input vector for quantum encoding.
- **Rotation Encoding**: A method of encoding classical values into qubits using parameterized rotation gates, such as RY(θ).
- **Qiskit**: An open-source Python library developed by IBM for working with quantum computers. Used for circuit construction, simulation, and execution.
- **Statevector Simulator**: A backend in Qiskit that computes the quantum state after running a circuit, without measurement noise.
- **Measurement**: The process of collapsing a quantum state to a definite classical output, typically used in quantum sampling or decision making.
- **Normalization (Quantum Context)**: The act of scaling classical values into a fixed range (e.g., [0, 1]) to make them suitable for encoding into quantum states.

---
