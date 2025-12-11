import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

# STEP 1: Read MIDI file and get all notes


def read_midi(filepath):
    """Read MIDI file and extract notes into array"""
    print(f"Reading MIDI file: {filepath}")

    midi = MidiFile(filepath)
    notes = []
    current_time = 0
    active_notes = {}  # Store notes that are currently playing

    # Save MIDI settings
    tempo = 500000
    ticks_per_beat = midi.ticks_per_beat

    # Look through all tracks
    for track in midi.tracks:
        current_time = 0

        for msg in track:
            current_time += msg.time

            # Get tempo if it exists
            if msg.type == 'set_tempo':
                tempo = msg.tempo

            # Note starts
            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = current_time

            # Note ends
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    start = active_notes[msg.note]
                    duration = current_time - start

                    # Add to array: [pitch, start_time, duration]
                    notes.append([msg.note, start, duration])
                    del active_notes[msg.note]

    # Sort notes by start time
    notes.sort(key=lambda x: x[1])

    print(f"Found {len(notes)} notes")
    return notes, tempo, ticks_per_beat


# STEP 2: Show all notes in the array
def show_notes(notes):
    """Display the notes array"""
    print("\n--- NOTES ARRAY ---")
    print(f"{'#':<5} {'Pitch':<10} {'Start':<10} {'Duration':<10}")
    print("-" * 40)

    for i, note in enumerate(notes):
        pitch, start, duration = note
        print(f"{i:<5} {pitch:<10} {start:<10} {duration:<10}")

    print()


# STEP 3: Write notes back to MIDI file
def write_midi(notes, tempo, ticks_per_beat, output_file):
    """Convert notes array back to MIDI file"""
    print(f"Writing MIDI file: {output_file}")

    # Create new MIDI file
    midi = MidiFile(ticks_per_beat=ticks_per_beat)
    track = MidiTrack()
    midi.tracks.append(track)

    # Add tempo
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

    # Create list of all events (when notes start and stop)
    events = []

    for note in notes:
        pitch, start, duration = note

        # When note starts
        events.append({
            'time': start,
            'type': 'on',
            'pitch': pitch
        })

        # When note stops
        events.append({
            'time': start + duration,
            'type': 'off',
            'pitch': pitch
        })

    # Sort by time
    events.sort(key=lambda x: x['time'])

    # Add events to track
    last_time = 0
    for event in events:
        delta = event['time'] - last_time

        if event['type'] == 'on':
            track.append(
                Message('note_on', note=event['pitch'], velocity=64, time=delta))
        else:
            track.append(
                Message('note_off', note=event['pitch'], velocity=0, time=delta))

        last_time = event['time']

    # End track
    track.append(MetaMessage('end_of_track', time=0))

    # Save file
    midi.save(output_file)
    print("MIDI file saved!")


# STEP 4: Compare original and new file
def compare_files(file1, file2):
    """Check if both MIDI files have the same notes"""
    print("\n--- COMPARING FILES ---")

    # Read both files
    notes1, _, _ = read_midi(file1)
    notes2, _, _ = read_midi(file2)

    # Check if same number of notes
    if len(notes1) != len(notes2):
        print(
            f"FAILED: Different number of notes ({len(notes1)} vs {len(notes2)})")
        return False

    # Check each note
    different = 0
    for i, (n1, n2) in enumerate(zip(notes1, notes2)):
        if n1 != n2:
            different += 1
            print(f"Note {i} is different:")
            print(f"  Original: {n1}")
            print(f"  Exported: {n2}")

    # Show result
    if different == 0:
        print(f"SUCCESS! All {len(notes1)} notes match!")
        return True
    else:
        print(f"FAILED: {different} notes are different")
        return False


# MAIN PROGRAM
if __name__ == "__main__":
    print("=" * 50)
    print("MIDI TEST - Mozart Sonata Measures 1-2")
    print("=" * 50)

    # File paths
    input_file = "assets/midi/mozart_sonata_1_mvt1_m1-2.mid"
    output_file = "assets/midi/mozart_test_output.mid"

    # Step 1: Read MIDI file
    notes, tempo, ticks = read_midi(input_file)

    # Step 2: Show the notes
    show_notes(notes)

    # Step 3: Write back to MIDI
    write_midi(notes, tempo, ticks, output_file)

    # Step 4: Compare files
    success = compare_files(input_file, output_file)

    # Final result
    print("\n" + "=" * 50)
    if success:
        print("TEST PASSED ✓")
    else:
        print("TEST FAILED ✗")
    print("=" * 50)
