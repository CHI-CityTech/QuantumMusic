# Quantum Music Generation Protocol (CLT-Based)

This document summarizes the full pseudocode pipeline for the simplified quantum music experiment, using the Central Limit Theorem to generate new musical content.

---

## Part 1 – Classical Preprocessing (Statistical Trajectory Model)

**Objective:** Extract musical features from MIDI files, convert them into 3D vector trajectories, and generate a new expectation trajectory via Gaussian sampling.

```python
# Step 1: Load MIDI and extract note events (pitch, start time, duration)
import pretty_midi

def load_midi_file(path):
    midi = pretty_midi.PrettyMIDI(path)
    all_notes = []
    for instrument in midi.instruments:
        for note in instrument.notes:
            all_notes.append({
                'pitch': note.pitch,
                'start': note.start,
                'end': note.end,
                'duration': note.end - note.start
            })
    return sorted(all_notes, key=lambda x: x['start'])

# Step 2: Convert notes to (pitch_delta, delta_t, duration) vectors

def convert_to_vectors(note_events):
    vectors = []
    prev_pitch = note_events[0]['pitch']
    prev_start = note_events[0]['start']
    for note in note_events[1:]:
        pitch_delta = note['pitch'] - prev_pitch
        delta_t = note['start'] - prev_start
        duration = note['duration']
        vectors.append((pitch_delta, delta_t, duration))
        prev_pitch = note['pitch']
        prev_start = note['start']
    return vectors

# Step 3: Align time steps (pad shorter phrases to match longest)
def align_time_steps(vectors_list):
    max_length = max(len(v) for v in vectors_list)
    aligned = []
    for vec in vectors_list:
        padded = vec + [(0, 0, 0)] * (max_length - len(vec))
        aligned.append(padded)
    return aligned

# Step 4: Compute expectation (mean) and standard deviation per dimension
import numpy as np

def compute_means_stds(aligned_vectors):
    vectors_np = np.array(aligned_vectors)  # shape: (num_structures, time, 3)
    means = np.mean(vectors_np, axis=0)     # shape: (time, 3)
    stds = np.std(vectors_np, axis=0)       # shape: (time, 3)
    return means, stds

# Step 5: Sample new trajectory using Gaussian sampling

def sample_from_gaussian(mean, std):
    return np.random.normal(loc=mean, scale=std)

new_trajectory = []
for t in range(len(means)):
    point = sample_from_gaussian(mean=means[t], std=stds[t])
    new_trajectory.append(point)
```

---

## Part 2 – Quantum Mapping & Processing (Quantum Component)

**Objective:** Encode the sampled trajectory into a quantum state and apply quantum operations to explore generative transformations.

```python
# Step 1: Normalize vectors to range [0, 1] for encoding

def normalize_vectors(vectors):
    arr = np.array(vectors)
    min_vals = np.min(arr, axis=0)
    max_vals = np.max(arr, axis=0)
    normalized = (arr - min_vals) / (max_vals - min_vals + 1e-9)
    return normalized, min_vals, max_vals

normalized_vector, min_vals, max_vals = normalize_vectors(new_trajectory)

# Step 2: Encode vector as quantum state

def encode_to_quantum_state(vector):
    # Placeholder: Replace with Qiskit amplitude encoding
    # vector must be normalized to unit length (L2 norm = 1)
    pass

# Step 3: Apply quantum operations

def apply_quantum_operations(circuit):
    # Add Hadamard, RX, RY, entanglement gates
    pass

# Step 4: Measure circuit

def measure_quantum_state(circuit):
    # Simulate measurement and extract classical values
    pass

# Step 5: Convert quantum outputs to vector trajectory

def postprocess_measurements(measurements):
    # Inverse transform to original scale (denormalize)
    pass
```

---

## Part 3 – MIDI Reconstruction

**Objective:** Convert the final sampled trajectory into a playable MIDI file using the `pretty_midi` library.

```python
# Step 1: De-normalize vector (if normalization was used)
def denormalize_vectors(vectors, min_vals, max_vals):
    return vectors * (max_vals - min_vals) + min_vals

# Step 2: Reconstruct MIDI

def create_note_event(pitch, start, duration):
    note = pretty_midi.Note(velocity=100, pitch=int(pitch), start=start, end=start+duration)
    return note

def create_instrument_with_notes(note_sequence):
    instrument = pretty_midi.Instrument(program=0)
    instrument.notes.extend(note_sequence)
    return instrument

# Convert vector to MIDI
note_sequence = []
current_time = 0
for pitch_delta, delta_t, duration in denormalized_vectors:
    pitch = 60 + pitch_delta  # assuming C4 as base
    note = create_note_event(pitch, current_time, duration)
    note_sequence.append(note)
    current_time += delta_t

midi = pretty_midi.PrettyMIDI()
midi.instruments.append(create_instrument_with_notes(note_sequence))
midi.write("generated_output.mid")
```

---

## Notes
- `pretty_midi` is used for all MIDI I/O and parsing.
- Quantum simulation assumes future integration with Qiskit.
- Time step alignment allows uniform sampling across variable-length phrases.
- Helper functions now expanded for better clarity and implementation support.
