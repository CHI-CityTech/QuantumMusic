# Comprehensive Musical Parameters
## **Notation**
We adopt the following symbols for musical parameters, derived from musical set theory, harmonic analysis, and time-based analysis:

- $p$: **Pitch**, represented as a numeric value where each octave increment is 12 (e.g., $p = 0, 1, \dots, 11$ for one octave).
- $pc$: **Pitch class**, derived by modulo operation to strip octave information:  $pc \equiv p \pmod{12}$
- $r$: **Registration**, representing the octave of a pitch:  $r = \lfloor p / 12 \rfloor$
- $f_1$: **Fundamental frequency**, the base frequency of a harmonic series, corresponding to $h = 1$ (e.g., $f_1 = 440 \, \text{Hz}$ for A4).
- $h$: **Harmonic number**, an integer identifying the position of a partial in the harmonic series, where:  $h = 1$ is the fundamental, $h = 2$ is the second harmonic (octave), and so on.
- $f_h$: **Harmonic partial frequency**, the frequency of the $h$-th harmonic partial:  
  $f_h = h \times f_1$
- $r_{p_1, p_2}$: **Frequency ratio** between two pitches $p_1$ and $p_2$:  
  $r_{p_1, p_2} = \frac{f(p_1)}{f(p_2)}$
- $S$: **Melodic series**, the ordered sequence of note events:  
  $S = \{n_1, n_2, n_3, \dots, n_k\}$
- $n_i$: **Note event**, the $i$-th element in the melodic series $S$, representing a single note event.
- $t_i$: **Time**, the timestamp of the $i$-th note event in $S$, measured in beats or seconds.



### **Series-Based Representation**

The melodic line can now be expressed as an ordered tuple or set:
$\[
S = \{(p_1, t_1), (p_2, t_2), (p_3, t_3), \dots, (p_k, t_k)\}
\]$
where each element $(p_i, t_i)$ represents the pitch and time of the $i$-th note event.

- **Pitch Series**: $\{p_1, p_2, \dots, p_k\}$
- **Time Series**: $\{t_1, t_2, \dots, t_k\}$

For example, if we have a melodic sequence of four notes:
- Pitches: $\{60, 62, 64, 67\}$
- Times: $\{0, 1, 2, 3\}$ (measured in beats),
The melodic series is:
\[
S = \{(60, 0), (62, 1), (64, 2), (67, 3)\}
\]
---

## **1. Pitch Class**

**Definition:**  
The *Pitch Class* ($pc$) represents the pitch identity of a note without octave information, encoded as integers from $0$ to $11$. Each pitch class corresponds to one of the 12 semitones in an octave:
- $0 = C$, $1 = C\sharp/D\flat$, $2 = D$, $\dots$, $11 = B$.

**Formula:**  
The pitch class is derived using the modulo operation:

$$
pc \equiv p \pmod{12}
$$

**Explanation:**  
- The modulo operation removes octave information, leaving only the pitch within a single octave.
- For example:
  - If $p = 60$ ($C\sharp$), $pc = 60 \pmod{12} = 0$ ($C$).
  - If $p = 61$ ($C\sharp4$), $pc = 61 \pmod{12} = 1$ ($C\sharp$).
  - If $p = 73$ ($C\sharp5$), $pc = 73 \pmod{12} = 1$ ($C\sharp$).

**Musical Context:**  
The concept of pitch class allows for the human perception that a pitch and its octave equivalents share a fundamental commonality. This abstraction simplifies music theory by focusing on pitch identity without considering octave placement. It is central to:
- Analyzing scales and modes.
- Identifying chord qualities and relationships.
- Grouping notes with equivalent pitch identities (e.g., enharmonic equivalents like G$\sharp$ and A$\flat$).

---

## **2. Registration**

**Definition:**  
The *Registration* ($r$) represents the octave placement of a pitch, expressed as an integer. It specifies the vertical position of a pitch on the keyboard or within a musical range.

**Formula:**  
The registration is calculated by dividing the pitch value ($p$) by 12 and taking the floor of the result:

$$
r = \lfloor p / 12 \rfloor
$$

**Explanation:**  
- Each octave spans 12 semitones. Dividing the pitch value by 12 determines its octave, while the floor operation removes any fractional part.
- For example:
  - $p = 60$ (C4): $r = \lfloor 60 / 12 \rfloor = 5$ (5th octave).
  - $p = 72$ (C5): $r = \lfloor 72 / 12 \rfloor = 6$ (6th octave).
  - $p = 59$ (B3): $r = \lfloor 59 / 12 \rfloor = 4$ (4th octave).

**Musical Context:**  
Registration provides a way to distinguish between pitches of the same pitch class across different octaves. While pitch class captures the tonal identity, registration determines the pitch’s height, influencing:
- **Timbre:** High notes often sound brighter, while low notes sound darker.
- **Range:** Helps analyze a melody's tessitura (average pitch level) and range.
- **Orchestration:** Determines how instruments with overlapping ranges can interact.
- **Perception of Octave Equivalence:** Registration complements pitch class by showing how octave-related pitches differ in vertical space.


## **3. Intervallic Movement** (Secondary)

**Derived From:**  
- Primary Parameters: Pitch ($p$), Time ($t$).

**Definition:**  
The *Intervallic Movement* describes the pitch changes between consecutive note events in a sequence, based on their timestamps. It encompasses both the direction and magnitude of these changes, making it applicable to single melodic lines (commonly referred to as "Melody") and to aggregate relationships across polyphonic or multi-instrumental contexts.

**Formula:**  
Intervallic Movement is calculated as the difference between the pitches of consecutive note events, ordered by their timestamps:

$$
\text{Intervallic Movement}_{i} = p_{i} - p_{i-1}, \quad \text{where } t_{i} > t_{i-1}
$$

**Explanation:**  
- **Temporal Dependence:** The parameter relies on the timestamps ($t_i$) to establish the order of the note events.
- **Single Line (Melodic Context):**  
  For a single melodic line, this parameter captures both the interval size and direction, forming the basis of melodic contour.
- **Aggregate Context (Polyphony):**  
  When applied to multiple note events occurring simultaneously or near-simultaneously, Intervallic Movement describes the pitch relationships within an ensemble or chordal texture.

- Positive values indicate ascending motion, with the magnitude representing the size of the ascent in semitones.
- Negative values indicate descending motion, with the magnitude representing the size of the descent.
- Zero indicates no pitch movement (static interval).

**Examples (Single Line):**
1. For the pitch sequence $\{60, 62, 64, 64, 61\}$ with timestamps $\{0, 1, 2, 3, 4\}$:
   - $\text{Intervallic Movement: } \{+2, +2, 0, -3\}$.
2. For the pitch sequence $\{72, 70, 69, 69, 71\}$ with timestamps $\{0, 2, 4, 5, 6\}$:
   - $\text{Intervallic Movement: } \{-2, -1, 0, +2\}$.

**Examples (Aggregate Context):**
- For a chord progression $\{\{60, 64, 67\}, \{62, 65, 69\}\}$ (C Major to D Minor) with timestamps $\{0, 1\}$:
  - $\text{Intervallic Movement: } \{+2, +1, +2\}$ (intervals between corresponding pitches in the chords).

**Musical Context:**  
Intervallic Movement is foundational to musical analysis:
- **Melodic Analysis:** For single-line melodies, it defines the contour and structure.
- **Harmonic and Polyphonic Analysis:** Describes relationships between voices or instrument lines, capturing aggregate interval changes over time.
- **Expressive Qualities:** Large intervals may suggest drama or intensity, while small intervals contribute to smoothness or stability.
- **Computational Applications:** Serves as a flexible parameter for analyzing and classifying melodies, harmonies, or polyphonic textures.

---

### **Next Steps**

Let me know if this revision aligns with your expectations. If it’s ready to go, I’ll move on to the next parameter. 








## **3. Intervallic Movement**

**Definition:**  
The *Intervallic Movement* measures the pitch difference in semitones between consecutive notes in a sequence. It represents the melodic or harmonic step size and direction.

**Formula:**  
The interval between two consecutive pitches is calculated as:

$$
\text{Interval} = p_{i} - p_{i-1}
$$

**Explanation:**  
- $p_{i}$ is the pitch of the current note, and $p_{i-1}$ is the pitch of the previous note.
- The result is a signed value:
  - Positive intervals indicate ascending motion.
  - Negative intervals indicate descending motion.
  - Zero indicates no motion (repeated pitch).

**Examples:**
- If $p_{i} = 64$ (E4) and $p_{i-1} = 60$ (C4):  
  $$\text{Interval} = 64 - 60 = 4$$ (a major third ascending).
- If $p_{i} = 55$ (G3) and $p_{i-1} = 59$ (B3):  
  $$\text{Interval} = 55 - 59 = -4$$ (a major third descending).

**Musical Context:**  
Intervallic movement captures melodic and harmonic relationships. It is essential for contextualizing pitch information in relationship to other note events in time:
- **Melodic Shape:** Defines the contour of a melody.
- **Harmonic Analysis:** Helps identify chord progressions and voice leading.
- **Emotional Expression:** Large intervals often create drama or tension, while small intervals suggest smoothness or calm.
- **Perceptual Dynamics:** Ascending intervals often feel uplifting, while descending intervals feel resolving or grounding.

## **4. Range**

**Definition:**  
The *Range* represents the span between the highest and lowest pitches in a musical section or phrase. It quantifies the vertical extent of the pitch content.

**Formula:**  
The range is calculated as:

$$
\text{Range} = \text{Max}(p) - \text{Min}(p)
$$

**Explanation:**  
- $\text{Max}(p)$ is the highest pitch in the section.
- $\text{Min}(p)$ is the lowest pitch in the section.
- The difference between these values gives the range in semitones.

**Examples:**
- If the pitches in a melody are $\{60, 62, 64, 67, 69\}$:
  - $\text{Max}(p) = 69$ (A4), $\text{Min}(p) = 60$ (C4).
  - $\text{Range} = 69 - 60 = 9$ semitones.
- For a more extended melody with $\{48, 52, 60, 64, 72\}$:
  - $\text{Max}(p) = 72$ (C5), $\text{Min}(p) = 48$ (C3).
  - $\text{Range} = 72 - 48 = 24$ semitones (two octaves).

**Musical Context:**  
Range defines the breadth of pitch content in a piece or section, influencing:
- **Expressive Scope:** Wider ranges often convey drama or grandeur, while narrow ranges can feel intimate or constrained.
- **Instrumental Writing:** Determines which instruments or voices can perform the material.
- **Tessitura and Texture:** High ranges are typically brighter, while low ranges are darker, shaping the overall character of the music.

## **5. Tessitura**

**Definition:**  
The *Tessitura* represents the central range of pitches where the majority of notes in a musical passage are concentrated. Unlike the overall range, it excludes extreme outliers and focuses on the "comfortable zone" of activity.

**Formula:**  
To calculate tessitura:
1. Determine the total number of notes in the passage, $n$.
2. Identify the subset of notes that accounts for at least half ($\geq n / 2$) of all pitches.
3. Define the lowest ($\text{Min}(p_{\text{tessitura}})$ and highest ($\text{Max}(p_{\text{tessitura}})$ pitches in this subset.

$$
\text{Tessitura} = \text{Min}(p_{\text{tessitura}}), \text{Max}(p_{\text{tessitura}})
$$

**Explanation:**  
- The tessitura is a range rather than a single value, defined by the bounds within which more than half of all notes occur.
- Excludes rare extreme pitches that fall outside the central activity zone.

**Examples:**
- For the pitches $\{60, 62, 64, 64, 67, 69, 72\}$:
  - Total notes: $n = 7$.
  - Half of $n$: $7 / 2 = 3.5$ (round up to 4).
  - Majority subset: $\{62, 64, 64, 67\}$ (middle group of pitches).
  - Tessitura: $[\text{Min}(p_{\text{tessitura}}), \text{Max}(p_{\text{tessitura}})] = [62, 67]$ (D4 to G4).
- For a wider set $\{48, 52, 55, 60, 64, 64, 64, 67, 72\}$:
  - Total notes: $n = 9$.
  - Half of $n$: $9 / 2 = 4.5$ (round up to 5).
  - Majority subset: $\{60, 64, 64, 64, 67\}$.
  - Tessitura: $[60, 67]$ (C4 to G4).

**Musical Context:**  
Tessitura describes the "active range" of a part:
- **Vocal Writing:** Indicates the comfortable singing range, essential for evaluating vocal difficulty and strain.
- **Instrumental Music:** Identifies where the bulk of pitches lie in orchestration, influencing tone and texture.
- **Expressive Quality:** A high tessitura conveys intensity and tension, while a low tessitura feels grounded and relaxed.

## **6. Harmonic Partial Frequency**

**Definition:**  
The *Harmonic Partial Frequency* ($f_n$) represents the relationship of a pitch to a reference fundamental frequency ($f(h)$), expressed as a ratio. It is defined as the $n$-th harmonic partial, where $n$ is the multiplier of the fundamental.

**Formula:**  

$$
\text{Harmonic Partial Ratio} = \frac{f(p)}{f(h)}
$$

**Explanation:**  
- $f(h)$ is the reference fundamental frequency.
- $f(p)$ is the frequency of the pitch being analyzed.
- The ratio determines which harmonic partial ($n$) the pitch corresponds to:
  - $n = 1$: The pitch is the fundamental ($f(p) = f(h)$).
  - $n = 2$: The pitch is the second harmonic (an octave above the fundamental).
  - $n = 3$: The pitch is the third harmonic (a fifth above the second harmonic), and so on.

**Examples (using ratios):**
- For a fundamental $f(h) = 130.81 \, \text{Hz}$ (C3):
  - A pitch at $f(p) = 130.81 \, \text{Hz}$ has a ratio of $n = \frac{130.81}{130.81} = 1$ (first harmonic, C3).
  - A pitch at $f(p) = 261.63 \, \text{Hz}$ has a ratio of $n = \frac{261.63}{130.81} = 2$ (second harmonic, C4).
  - A pitch at $f(p) = 392.43 \, \text{Hz}$ has a ratio of $n = \frac{392.43}{130.81} = 3$ (third harmonic, G4).

**Musical Context:**  
Expressing harmonic relationships as ratios:
- **Harmonic Relationships:** Ratios simplify calculations for harmonic structures, avoiding reliance on absolute frequencies.
- **Timbre Analysis:** Harmonic partial ratios highlight the strength and distribution of harmonics that define an instrument's timbre.
- **Musical Intervals:** Directly connect ratios to intervallic relationships (e.g., $n = 2$ is an octave, $n = 3$ is a fifth above).

## **7. Frequency Ratio Between Notes**

**Definition:**  
The *Frequency Ratio Between Notes* ($r_{p_1, p_2}$) describes the relationship between two pitches, $p_1$ and $p_2$, expressed as a ratio relative to their frequencies. This approach avoids relying on specific frequency values and instead focuses on their proportional relationship.

**Formula:**  

$$
r_{p_1, p_2} = \frac{f(p_1)}{f(p_2)}
$$

**Explanation:**  
- $f(p_1)$ and $f(p_2)$ are the frequencies of two pitches, derived relative to a reference fundamental or system.
- The ratio indicates the interval between the pitches:
  - Ratios greater than 1 mean $p_1$ is higher than $p_2$.
  - Ratios less than 1 mean $p_1$ is lower than $p_2$.
  - A ratio of 1 means the two pitches are equivalent (unison).

**Generalized Interpretation:**  
- No explicit frequency calculations are needed if the system is normalized. For example:
  - If pitch $p_1$ is one octave above pitch $p_2$, $r_{p_1, p_2} = 2$ regardless of their absolute frequencies.
  - If pitch $p_1$ is a perfect fifth above $p_2$, $r_{p_1, p_2} \approx 1.5$.

**Examples (using relative ratios):**
- If $p_1$ is one octave above $p_2$:  
  $$r_{p_1, p_2} = \frac{2}{1} = 2 \quad \text{(octave)}.$$
- If $p_1$ is a perfect fifth above $p_2$:  
  $$r_{p_1, p_2} = \frac{3}{2} = 1.5 \quad \text{(perfect fifth)}.$$
- If $p_1$ and $p_2$ are the same pitch:  
  $$r_{p_1, p_2} = \frac{1}{1} = 1 \quad \text{(unison)}.$$

**Musical Context:**  
Frequency ratios provide a universal framework for understanding intervals and tonal relationships:
- **Harmonic Intervals:** Ratios map directly to intervals, independent of tuning system or absolute pitch.
- **Generalization Across Scales:** A normalized system allows consistent comparison across musical systems, such as Western equal temperament or non-Western tuning.
- **Abstract Representation:** Ratios facilitate abstract harmonic analysis, crucial for computational models and cross-cultural music studies.

## **8. Interval Contour**

**Definition:**  
The *Interval Contour* represents the pattern of pitch movement in a sequence, abstracting the directional relationships between consecutive intervals rather than their specific sizes. It provides a symbolic representation of whether a note ascends, descends, or remains the same relative to the previous note.

**Formula:**  
Interval contour is derived as a series of directional indicators based on the intervallic movement between consecutive pitches:  

$$
\text{Contour}\_{i} =
\begin{cases} 
+1, & \text{if } p_{i} > p_{i-1} \, \text{(ascending)} \\
0, & \text{if } p_{i} = p_{i-1} \, \text{(unchanged)} \\
-1, & \text{if } p_{i} < p_{i-1} \, \text{(descending)}
\end{cases}
$$

**Explanation:**  
- $p_{i}$ and $p_{i-1}$ are consecutive pitches in the sequence.
- The resulting sequence of $+1$, $0$, and $-1$ captures the overall shape of the melody or harmonic line without specifying interval sizes.

**Examples:**
1. For the pitch sequence $\{60, 62, 64, 64, 61\}$:
   - $\text{Intervals: } +2, +2, 0, -3$
   - $\text{Contour: } \{+1, +1, 0, -1\}$ (ascending, ascending, unchanged, descending).
2. For the pitch sequence $\{72, 70, 69, 69, 71\}$:
   - $\text{Intervals: } -2, -1, 0, +2$
   - $\text{Contour: } \{-1, -1, 0, +1\}$ (descending, descending, unchanged, ascending).

**Musical Context:**  
Interval contour abstracts the shape of a melody or harmonic movement:
- **Melodic Analysis:** Captures the directional flow of melodies, useful for identifying thematic patterns or gestures.
- **Motivic Development:** Helps compare variations of a theme across different sections of a piece.
- **Cross-Cultural Studies:** Provides a universal representation of melodic motion, independent of specific tuning or tonal systems.
- **Computational Analysis:** Facilitates machine learning models to classify and analyze melodies by reducing pitch data to simpler directional patterns.

---

### Next Steps
Let me know if this aligns with your expectations. If so, I’ll proceed with **Note Density** next!

 
