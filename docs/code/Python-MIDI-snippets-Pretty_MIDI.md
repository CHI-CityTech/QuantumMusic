
# Python MIDI Snippets (pretty_midi)

This file contains Python code snippets using the `pretty_midi` library for high-level MIDI analysis.

**Explanation:**  
pretty_midi is a higher-level library that abstracts away much of the MIDI message handling and focuses on musically meaningful constructs like notes, pitch, timing, and instruments. Ideal for tasks like extracting notes, tempo, or converting to piano rolls.  



# Import the pretty_midi library for high-level musical analysis
```python
import pretty_midi  
```


The links to **pretty_midi** can be found [here](https://pypi.org/project/pretty_midi/).  

---

## 1. Load and Analyze Notes

```python
import pretty_midi

midi_data = pretty_midi.PrettyMIDI('example.mid')
for instrument in midi_data.instruments:
    for note in instrument.notes:
        print(f'Pitch: {note.pitch}, Start: {note.start}, End: {note.end}, Velocity: {note.velocity}')
```

**Description:**  
Loads a MIDI file using PrettyMIDI and prints all note information for each instrument.

---

## 2. Get Velocity and Pitch Range

```python
velocities = [note.velocity for instrument in midi_data.instruments for note in instrument.notes]
pitches = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
print(f'Min Velocity: {min(velocities)}, Max Velocity: {max(velocities)}')
print(f'Pitch Range: {min(pitches)} - {max(pitches)}')
```

**Description:**  
Extracts and prints pitch and velocity ranges from all notes.

---

## 3. Print Instrument and Program Numbers

```python
for instrument in midi_data.instruments:
    print(f'Instrument name: {instrument.name}, Program number: {instrument.program}')
```

**Description:**  
Displays each instrument's name and corresponding General MIDI program number.
