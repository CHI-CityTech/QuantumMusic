# Quantum Music Micro-Study: Minimal Proof of Concept

## Overview

This micro-study aims to test the feasibility of using quantum computing to process a reduced musical dataset—specifically, 2–3 Mozart piano sonatas—using only three musical parameters: **pitch**, **duration**, and **location in time**. The goal is to process symbolic data (MIDI) into a mathematical representation amenable to quantum algorithms and convert the quantum-generated output back into MIDI for auditory evaluation.

## Objective

Demonstrate that a simplified musical dataset can be:
- Transformed into quantum-compatible mathematical expressions.
- Processed using a basic quantum algorithm.
- Reconstructed into a playable musical form.

## Data

- **Dataset**: 2–3 Mozart Piano Sonatas in **MIDI** format.
- **Tracks**: Must verify whether each file contains a single piano track or separate tracks for left and right hands.
- **Parameters extracted**:
  - Pitch (as MIDI note number or pitch class)
  - Duration (in terms of quarter notes)
  - Time (beat-relative timestamp, using extracted meter)

## Methodology

### Step 1: Data Acquisition
- Download MIDI files from reputable repositories (e.g., Kunst der Fuge, Classical Archives, MuseScore).
- Use a MIDI parsing tool (e.g., `mido`, `music21`) to examine structure:
  - Number of tracks
  - Track separation by hand
  - Presence of non-note events (controllers, program changes)

### Step 2: Preprocessing
- Normalize timing to **quarter note resolution** using tempo and time signature metadata.
- Extract note events into a CSV-like format with fields:
  ```
  Time (beats), Pitch, Duration (beats)
  ```

### Step 3: Quantum-Compatible Transformation
- Map events to vectors or tuples suitable for quantum encoding.
- Encode basic state representations with quantum libraries (Qiskit, Pennylane, etc.)
- Optionally simulate via classical computer if no QPU access is available.

### Step 4: Output and Evaluation
- Generate modified output using simple quantum operations or samplers.
- Convert back to MIDI.
- Auditory and visual inspection of result (via DAW or MIDI player).
- Log results and observations.

## Expected Outcome

A minimal, testable pipeline demonstrating:
- That symbolic musical data can be encoded and processed with quantum representations.
- That even low-level quantum logic can manipulate musically meaningful data.
- A proof-of-concept musical output that retains structure and intent from the original data.

## Notes

- Velocity, articulation, orchestration, and other higher-level features are deliberately omitted in this minimal test.
- This phase focuses on infrastructure, pipeline validity, and basic parameter encoding.

## Tools

- **Python** with:
  - `mido` or `music21` for MIDI parsing
  - `qiskit`, `pennylane`, or `braket` for quantum encoding
- **GitHub** for version control
- **Zotero** for documentation
- **Discord** for communication
- **DAW** or MIDI player for output review

---
