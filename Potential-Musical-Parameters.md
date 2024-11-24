# Comprehensive Musical Parameters

This proposed list of musical parameters, some solid, others perhaps frivolous, provides a detailed framework for analyzing and understanding the diverse components of music. By breaking down music into quantifiable elements, these parameters enable systematic exploration of melody, harmony, rhythm, texture, and timbre. Each parameter is defined with its derivation process and musical significance, offering a structured approach to capture the nuances of musical expression and organization. These parameters are intended as a starting point for further evaluation and refinement. They aim to facilitate deeper investigation into stylistic traits, compositional techniques, and performance practices, with flexibility for adaptation based on specific analytical or generative needs.  Achieving the desired level of generalizability is also of interest: for example will GAI or Quantum solutions mean that we do not need to specify as many parameters. Since many of the listed parameters are "secondary": based on applying some organization to one of the primary parameters, such as pitch or time, it may not be necessary 

If we were to deploy every one of these parameters we would then exist in musical n-space(37).

## 1. Melodic Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 1     | **Pitch class**             | The pitch identity of a note without octave information, encoded as integers (0–11).                             | Primary                                  | N/A                                   |
| 2     | **Registration**            | The octave placement of a pitch, encoded as absolute values or relative to a dataset.                            | Primary                                  | N/A                                   |
| 3     | **Intervallic movement** (Melody)     | Sequential pitch differences in semitones, including time ordering and registration shifts for wide leaps.        | Secondary                                | Pitch class, Registration, Time       |
| 4     | **Range**                    | The span between the highest and lowest pitches in a phrase, section, or piece.                                  | Secondary                                | Registration                          |
| 5     | **Tessitura**                | The average pitch position within the overall range.                                                             | Secondary                                | Registration                          |
| 6     | **Contour complexity**       | A measure of directional changes in a melodic sequence, capturing complexity of shape.                          | Secondary                                | Intervallic movement                   |
| 7     | **Ornamentation density**    | The frequency of ornamentation (e.g., trills, grace notes) within a measure or section.                          | Primary                                  | N/A                                   |

---

## 2. Harmonic Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 8     | **Chord interval structure** | Stacked intervals (in semitones) relative to the root, capturing extended and altered chords.                    | Primary                                  | N/A                                   |
| 9     | **Fuzzy chord classification** | Probabilistic assignment of a chord to multiple categories based on interval structure and context.               | Secondary                                | Chord interval structure, Context     |
| 10    | **Chord inversion**          | Which chord element (root, third, fifth, etc.) is in the bass, represented by an index.                          | Secondary                                | Chord interval structure, Bass note   |
| 11    | **Bass note**               | The lowest pitch in a chord, encoded as a pitch class (0–11).                                                    | Primary                                  | N/A                                   |
| 12    | **Chord distance**           | The intervallic similarity or functional relationship between two chords.                                        | Secondary                                | Chord interval structure              |
| 13    | **Implied harmonic root**    | The fundamental pitch derived from a set of simultaneous pitches using harmonic series relationships.            | Secondary                                | Chord interval structure, Bass note   |

---

## 3. Rhythmic and Metrical Parameters
| **#** | **Parameter**                   | **Definition**                                                                                                   | **Primary/Secondary**                      | **Derived From**                 |
|-------|----------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------|-----------------------------------|
| 14    | **Rhythm**                      | The sequential organization of note durations, including rests and hierarchical patterns.                       | Primary                                    | Note duration, Rests             |
| 15    | **Agogic stress**                | Relative stress implied by note duration; longer durations often receive more emphasis.                         | Secondary                                  | Note duration                     |
| 16    | **Duration density**             | Number of note durations per rhythmic subdivision (e.g., beats, measures).                                      | Secondary                                  | Note duration                     |
| 17    | **Note density per subdivision** | Number of note onsets within each rhythmic subdivision (e.g., per beat or 16th note).                           | Primary                                    | N/A                               |
| 18    | **Periodicity**                  | Repeating patterns in note density or duration across subdivisions, detected via Fourier transform or autocorrelation. | Secondary                                  | Note duration, Note density per subdivision |
| 19    | **Modulo-based periodicity**     | Cyclical patterns of note density or duration using modulo operations over rhythmic subdivisions.               | Secondary                                  | Note duration, Note density per subdivision |
| 20    | **Downbeat weight**              | Relative weight of the first beat of a measure, derived from note density, agogic stress, and rhythmic patterns. | Secondary                                  | Note density, Rhythm, Agogic stress |
| 21    | **Subdivision hierarchy**        | Relative stress distribution across all subdivisions in a measure or phrase.                                    | Secondary                                  | Downbeat weight                   |
| 22    | **Explicit meter**               | The stated meter (e.g., time signature) for the piece or section.                                               | Primary                                    | N/A                               |
| 23    | **Implied meter**                | Inferred meter based on periodicity, stress, and density patterns.                                              | Secondary                                  | Periodicity, Note duration, Downbeat weight |
| 24    | **Implied beat**                 | The basic pulse inferred from note durations or density patterns.                                               | Secondary                                  | Periodicity, Note density         |
| 25    | **Implied subdivision**          | Regular divisions of the beat inferred from density or agogic stress.                                           | Secondary                                  | Implied beat                      |

---

## 4. Textural and Articulative Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 26    | **Articulation ratio**       | Ratio of a note's duration to the inter-onset interval (IOI) for the same instrument.                            | Primary                                  | Note duration, Inter-onset interval   |
| 27    | **Articulation frequency**  | Frequency of articulations (e.g., staccato, marcato) per measure or section.                                     | Secondary                                | Articulation ratio                    |
| 28    | **Polyphonic texture**      | Number of independent voices sounding simultaneously, reflecting polyphonic complexity.                          | Secondary                                | Note density                          |

---

## 5. Structural Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 29    | **Phrase length**           | Duration of a phrase, normalized to the longest phrase in the dataset or measured absolutely.                    | Primary                                  | N/A                                   |
| 30    | **Repetition density**      | Frequency of recurring motifs within a measure or section.                                                       | Secondary                                | Phrase length                         |
| 31    | **Sectional transitions**   | Frequency of transitions between key areas, motifs, or thematic material.                                        | Secondary                                | Phrase length, Harmonic parameters    |

---

## 6. Timbre and Instrumentation Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 32    | **Instrument type**         | Encodes the instrument family (e.g., strings, winds) or specific instrument playing a passage.                   | Primary                                  | N/A                                   |
| 33    | **Orchestration density**   | Number of active instruments in a passage, weighted by note density.                                             | Secondary                                | Instrument type, Note density         |
| 34    | **Timbre changes**          | Frequency of changes in timbral color due to orchestration or instrumentation shifts.                            | Secondary                                | Instrument type                       |

---

## 7. Convex Hull Parameters
| **#** | **Parameter**               | **Definition**                                                                                                    | **Primary/Secondary**                    | **Derived From**                     |
|-------|------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------|
| 35    | **Treble line**             | The highest pitch in a measure, phrase, or section.                                                             | Primary                                  | N/A                                   |
| 36    | **Bass line**               | The lowest pitch in a measure, phrase, or section.                                                              | Primary                                  | N/A                                   |
| 37    | **Convex hull span**        | The pitch span between the treble and bass lines, representing vertical harmonic density.                       | Secondary                                | Treble line, Bass line                |
