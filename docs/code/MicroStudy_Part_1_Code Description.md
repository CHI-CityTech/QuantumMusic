# Quantum Music Preprocessing Pipeline (Up to Equation 3)

## 1. Human Language Description

The aim of this part of the Quantum Music project is to extract symbolic musical data from classical compositions 
and transform it into a simplified 3D vector format compatible with quantum algorithms. We focus on three phrases, 
one each from the exposition sections of the first movements (Sonata-Allegro Form) of Mozart's Piano Sonatas 1, 2, and 3. 
These phrases will be treated as individual musical pieces for the analysis.

Each phrase is processed to extract three essential note parameters:
- **x-axis**: pitch (MIDI note number)
- **y-axis**: onset time (in beats)
- **z-axis**: duration (in beats)

Each phrase is thus represented as a trajectory in three-dimensional space: \(\vec{r}_i(t) = (x_i(t), y_i(t), z_i(t))\).

Equation (1) describes how each coordinate of the trajectory is a weighted sum of characteristic features \(C_l\), 
with weights \(p_{ilx}, p_{ily}, p_{ilz}\) representing how much each feature contributes to the dimensions x, y, and z.

Equation (2) defines a **new trajectory** \(\vec{r}_R(t)\) as the **expectation** (in the statistical sense) over all input trajectories.
This means for each coordinate and feature, we average the corresponding weight across all phrases. This is formalized
in Equation (3), where:

```math
P^R_{lx}(t_{Rj}) = \frac{1}{N} \sum_{i=1}^{N} p_{ilx}(t_{ij})
```

In this context, **expectation** means the most probable or average configuration of musical parameter contributions 
based on the three input examples. This representation reflects the probabilistic foundation of quantum mechanics, 
where outcomes are computed not as fixed values but as statistical expectations over distributions.

Once this average trajectory is computed, we convert it back into a MIDI file for auditory evaluation. This allows us 
to hear the structure and stylistic tendencies common to all three phrases—effectively a musically meaningful "average."

## 2. Pseudocode

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

# Step 2: Convert Note Events into 3D Trajectories
def note_events_to_3D_trajectories(data):
    trajectories = []
    for piece in data:
        trajectory = []
        for note in piece:
            x = note.pitch          # MIDI number
            y = note.onset_time     # in beats
            z = note.duration       # in beats
            trajectory.append((x, y, z))
        trajectories.append(trajectory)
    return trajectories

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

## 3. Glossary

- **Expectation**: In this context, it refers to the statistical average of a musical parameter across multiple phrases. It represents the most typical or probable value observed—similar to the expected value in probability theory.
- **Trajectory**: A path through 3D space defined by note-level events, where each event is a point with pitch, time, and duration coordinates. A musical phrase becomes a trajectory when mapped this way.
- **Vector**: An ordered set of numbers used to describe a single note in space. Here, each note becomes a 3D vector \((x, y, z)\), corresponding to pitch, onset time, and duration.

---

**End of Document**
