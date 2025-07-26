# Statistical Trajectory Model – Pseudocode Version (Markdown)

## 1. Overview
This pseudocode outlines the high-level logic for extracting musical data from MIDI, performing statistical analysis, and generating a new musical trajectory based on Gaussian sampling.

---

## 2. Pseudocode

### Step 0: Convert MIDI to Vector Representation
FOR each MIDI file IN dataset:
- Parse events using a MIDI library (e.g., `pretty_midi`) to extract NOTE_ON events with non-zero velocity
- Track absolute time of each note event
- Ensure duration is extracted directly from NOTE_ON and NOTE_OFF events (exact, not estimated)
  - Pitch interval from previous note
  - Delta time from previous onset
  - Duration of current note
- Store as a list of (pitch_delta, delta_t, duration)

### Step 1: Compute Statistics Across Phrases
INPUT: List of N phrases, each represented as M time steps with 3D vectors  
FOR each time step j from 1 to M:
- Compute average of x, y, z values across all N phrases
- Compute standard deviation of x, y, z at each time step  
OUTPUT: Mean and std vectors of shape (M, 3)

### Step 2: Generate New Trajectory
FOR each time step j from 1 to M:
- Sample new values x_j, y_j, z_j from Gaussian distributions:
  - Mean = previously computed mean
  - Std = previously computed std  
APPEND each (x_j, y_j, z_j) to new trajectory list

### Step 3: Convert Trajectory to MIDI Format
SET starting pitch (e.g., Middle C)  
FOR each vector in trajectory:
- Add pitch interval to last pitch to get next pitch
- Convert delta_t and duration to MIDI ticks
- Insert NOTE_ON and NOTE_OFF events accordingly  
SAVE final MIDI sequence as a `.mid` file

---

## 3. Notes
- The model assumes a fixed number of time steps for alignment. All phrases must be padded, truncated, or interpolated to conform.
- For this proof-of-concept, we assume minimal variation in phrase shape. In future iterations, more advanced shape-aware alignment may be needed.
- All note durations are extracted exactly using MIDI NOTE_OFF timing, assuming support from the MIDI parsing library.
- Evaluate the capabilities of `pretty_midi` to ensure compatibility with polyphonic input and accurate time/duration capture.
- Gaussian sampling enables stylistic coherence without exact replication.
- This pseudocode abstracts away implementation details for conceptual clarity.

