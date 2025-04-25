# Quantum Music Preprocessing Pipeline (Part 1)

## 1. Human Language Description

The aim of this part of the Quantum Music project is to extract symbolic musical data from classical compositions and transform it into a simplified 3D vector format compatible with quantum algorithms. We focus on three short **phrases** from the exposition sections of the first movements (Sonata-Allegro Form) of Mozart's Piano Sonatas 1, 2, and 3. From each sonata, three phrases will be identified and extracted—yielding a dataset of **nine compositions**. Each phrase is treated as a **complete composition** or **piece** within our model. This segmentation is used to produce a manageable, analytically meaningful dataset suitable for testing and validation. Although each excerpt is taken from a larger sonata, it is treated as a **complete composition** within our model. This is consistent with the understanding that a musical composition can be any self-contained musical statement, even a brief one. The segmentation is used to produce a manageable data set for testing and validation.

Each composition is processed to extract three essential note parameters:
- **x-axis**: pitch **interval** from the previous note (first note is considered relative to tonic or reference pitch)
- **y-axis**: **delta time (Δt)** from the previous note onset
- **z-axis**: duration (in beats)

Each composition is thus represented as a trajectory in three-dimensional space:

$$
\vec{r}_i(t) = (x_i(t), y_i(t), z_i(t))
$$

## 2. Pseudocode

*Note: This implementation assumes the use of the [**mido**](https://pypi.org/project/mido/) library for MIDI parsing and extraction within Python.*

### Process Overview

The following steps outline the full pipeline process for preparing the musical data:

1. **Identify Phrases**: Identify three distinct phrases from each of Mozart Piano Sonatas 1, 2, and 3 (exposition section, first movement).
2. **Extract Phrases**: Extract each phrase and define it as a standalone composition or 'piece' within the model. This results in nine total compositions.
3. **Convert to MIDI**: Ensure each phrase is encoded as a separate MIDI file.
4. **Parse MIDI**: Extract note-level data—pitch, onset time, and duration.
5. **Convert to 3D Vectors**: Compute pitch intervals and delta-onset-times for each note and assemble them into 3D vectors.
6. **Assign Characteristic Weights**: Associate each data point with mock or actual characteristic weightings.
7. **Compute Mean Contribution**: Average the weights across all compositions to compute the expected profile.
8. **Generate New Composition**: Use the averaged weights to synthesize a new trajectory.
9. **Convert Back to MIDI**: Render the new trajectory into a MIDI file for auditory review.

```python
# Step 1: Import MIDI and Parse
load_midi_files(path_to_mozart_sonatas):
    midi_files = list_midi_files(path)
    data = []
    for file in midi_files:
        midi = parse_midi(file)
        notes = extract_notes(midi)  # pitch, onset_time, duration
        data.append(notes)
    return data

# Step 2: Convert Note Events into 3D Trajectories with Relative Encoding
def note_events_to_relative_3D_trajectories(data):
    trajectories = []
    for piece in data:
        trajectory = []
        prev_pitch = None
        prev_time = None
        for note in piece:
            interval = note.pitch - prev_pitch if prev_pitch is not None else 0
            delta_t = note.onset_time - prev_time if prev_time is not None else 0
            z = note.duration
            trajectory.append((interval, delta_t, z))
            prev_pitch = note.pitch
            prev_time = note.onset_time
        trajectories.append(trajectory)
    return trajectories
```

```python
# Step 3: Assign weights based on musical characteristics (mocked for now)
def assign_characteristic_weights(trajectories):
    # Assume 3 characteristics for now (Cl1, Cl2, Cl3)
    weighted = []
    for traj in trajectories:
        traj_weighted = []
        for x, y, z in traj:
            weights = get_characteristic_weights(x, y, z)  # returns [(p1x, p1y, p1z), ..., (pLx, pLy, pLz)]
            traj_weighted.append(weights)
        weighted.append(traj_weighted)
    return weighted

# Step 4: Compute Mean Contribution for New Composition (Equation 3)
def compute_average_weights(weighted_trajectories):
    M = max(len(traj) for traj in weighted_trajectories)
    L = len(weighted_trajectories[0][0])  # number of characteristics

    average = []
    for j in range(M):
        avg_weights = [(0, 0, 0) for _ in range(L)]
        count = 0
        for traj in weighted_trajectories:
            if j < len(traj):
                count += 1
                for l in range(L):
                    px, py, pz = traj[j][l]
                    old = avg_weights[l]
                    avg_weights[l] = (old[0]+px, old[1]+py, old[2]+pz)
        if count > 0:
            avg_weights = [(px/count, py/count, pz/count) for (px, py, pz) in avg_weights]
        average.append(avg_weights)
    return average

# Step 5: Generate a New Trajectory from Averages (Equation 2)
def generate_new_trajectory(average_weights, Cl):
    trajectory = []
    for weights in average_weights:
        x = sum(px * Cl[l] for l, (px, _, _) in enumerate(weights))
        y = sum(py * Cl[l] for l, (_, py, _) in enumerate(weights))
        z = sum(pz * Cl[l] for l, (_, _, pz) in enumerate(weights))
        trajectory.append((x, y, z))
    return trajectory

# Step 6: Export New Trajectory to MIDI (optional follow-up)
def convert_to_midi(trajectory):
    # Write this later
    pass
```
def convert_to_midi(trajectory):
    # Write this later
    pass

## 3. Glossary

- **MIDI (Musical Instrument Digital Interface)**: A digital encoding standard that allows music data to be shared between instruments and computers. It captures note events such as pitch, velocity, and duration, rather than audio.
- **Onset Time**: The moment in time, usually measured in beats, when a note begins.
- **Duration**: The length of time a note is held or sustained, typically measured in beats.
- **Pitch**: The frequency of a note, typically represented by a MIDI number (e.g., 60 = Middle C).
- **Characteristic Feature**: A quality or dimension of a composition (e.g., rhythmic density, melodic contour) used for modeling or analysis.
- **Weight Coefficient**: A number representing the relative influence of a characteristic feature on a particular musical parameter (pitch, timing, duration).
- **Sampling Step**: A moment in analytical time where musical values are observed or extracted—used as an anchor point in modeling.
- **Trajectory Point**: A 3D coordinate (x, y, z) representing pitch, time, and duration of a note at a given sampling step.
- **Normalization**: The process of adjusting data to a common scale or range, often used to make features comparable.
- **Interpolation**: A method for estimating intermediate values between known data points, often used to align data with regular time steps.
- **Vector Space**: A mathematical model in which musical events are treated as vectors, enabling operations such as averaging and transformation.

## 4. Variable Definitions from Equations

- **i**: Index for each individual composition (each test item is treated as a standalone musical piece).
- **j**: Index of a time step within the i-th composition. Each time step may correspond to a note onset, but multiple notes can occur at the same time (e.g., chords), or there may be rests—so this index refers to discrete sampling points rather than a strict one-note-per-step model. Most music is nonuniform in its timing structure, and these time patterns are essential to a composition’s style and expressive identity.
- **t_ij**: The timestamp (in beats) for the j-th time step in the i-th composition. This may or may not align exactly with a unique note event.
- **x_i(t), y_i(t), z_i(t)**: The x (pitch), y (onset time), and z (duration) values at time t in composition i.
- **r_i(t)**: A 3D vector representing the note event in composition i at time t.
- **L**: Total number of musical characteristics (e.g., interval size, contour shape).
- **C_l**: The l-th characteristic property (shared across all compositions).
- **p_ilx(t_ij)**: The weight/contribution of characteristic C_l to the pitch (x) at time t_ij in composition i.
- **p_ily(t_ij), p_ilz(t_ij)**: Similar weights for time (y) and duration (z).
- **P^R_lx(t_Rj)**: The expectation (average) of p_ilx(t_ij) across all compositions, used for generating new material.
- **r_R(t)**: The generated new trajectory based on the average weights.

## 5. Potential Next Steps for Vector Definitions

As we validate the core pipeline using solo piano phrases, several future enhancements may extend the model’s expressiveness and scope:

### 1. Voice or Stem Separation
- Enable independent modeling of contrapuntal lines, left/right hand material, or instrument voices.
- Provides cleaner interval/Δt sequences and allows for more nuanced analysis.

### 2. Melodic vs. Accompanimental Role Detection
- Develop techniques for identifying melodic contour or structural prominence within lines.
- Useful for weighting or emphasizing certain voices during expectation modeling.

### 3. Expanded Dimensionality
- Introduce additional vector components such as:
  - Articulation (staccato, legato, etc.)
  - Instrument ID (for ensemble modeling)
  - Velocity (when expressive nuance becomes a focus)

### 4. Multi-Instrument Compatibility
- Adapt pipeline to parse and vectorize compositions involving more than one instrument.
- May include synchronized multi-stem analysis, instrument-specific weighting, and channel separation.

### 5. Reconstruction Heuristics
- Refine the rules for reversing vector trajectories back into playable scores:
  - Define starting pitch
  - Handle simultaneous onsets (e.g., chord sequencing)
  - Address instrument-specific constraints (e.g., playable ranges)

---
end of document
