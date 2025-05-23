# Python MIDI Snippets (Mido)

This file contains Python code snippets using the `mido` library for working with MIDI files.  


# Import the mido library for working with MIDI files
import mido
from mido import MidiFile, MidiTrack, Message

Explanation:  
mido is a lightweight and intuitive library for reading, writing, and manipulating MIDI files and messages.

- MidiFile lets you load and inspect MIDI files.
- MidiTrack handles individual tracks within a MIDI file.
- Message is used to create and inspect MIDI messages.

The **mido** library can be found [here](https://pypi.org/project/mido/).  

---

## 1. Load and Inspect a MIDI File

```python
from mido import MidiFile

mid = MidiFile('example.mid')
print(f'Number of tracks: {len(mid.tracks)}')
for i, track in enumerate(mid.tracks):
    print(f'Track {i}: {track.name}')
```

**Description:**  
Loads a MIDI file using Mido and prints the number of tracks and their names.

---

## 2. Extract Note On Events with Timing

```python
from mido import MidiFile

mid = MidiFile('example.mid')
for track in mid.tracks:
    time = 0
    for msg in track:
        time += msg.time
        if msg.type == 'note_on':
            print(f'Note {msg.note} velocity {msg.velocity} at time {time}')
```

**Description:**  
Accumulates delta times to determine actual time for each note-on event.

---

## 3. Print Controller and Patch Change Messages

```python
from mido import MidiFile

mid = MidiFile('example.mid')
for track in mid.tracks:
    for msg in track:
        if msg.type == 'control_change' or msg.type == 'program_change':
            print(msg)
```

**Description:**  
Prints all control and patch change messages from the file.
