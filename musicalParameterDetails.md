


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


## **3. Intervallic Movement**

**Type:** Secondary  
**Derived From:**  
- Primary Parameters: Pitch ($p$), Time ($t$).
- Aggregate, ordered series of pitches based on their time stamp ($t$)

**Definition:**  
The *Intervallic Movement* describes the pitch changes between consecutive note events in a sequence, based on their timestamps. It encompasses both the direction and magnitude of these changes, making it applicable to single melodic lines (commonly referred to as "Melodic Contour") and to aggregate relationships across polyphonic or multi-instrumental contexts.

**Formula:**  
Intervallic Movement is calculated as the difference between the pitches of consecutive note events, ordered by their timestamps:

$$
\text{Intervallic Movement}\_{i} = p_{i} - p_{i-1}, \quad \text{where } t_{i} > t_{i-1}
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
- **Melodic Analysis:** For single-line melodies, it defines the contour and structure (commonly called "Melodic Contour").
- **Harmonic and Polyphonic Analysis:** Describes relationships between voices or instrument lines, capturing aggregate interval changes over time.
- **Expressive Qualities:** Large intervals may suggest drama or intensity, while small intervals contribute to smoothness or stability.
- **Computational Applications:** Serves as a flexible parameter for analyzing and classifying melodies, harmonies, or polyphonic textures.

## **4. Pitch Range**

**Type:** Secondary  
**Derived From:**  
- Aggregate: Time-independent collection of all pitches in the analyzed passage.

**Definition:**  
The *Pitch Range* is the interval spanned by the lowest and highest pitch values in a given passage. It provides a measure of the overall tonal span of the music.

**Formula:**  
The **Pitch Range** is calculated as:

$$
\text{Pitch Range} = p_{\text{max}} - p_{\text{min}}
$$

Where:
- $p_{\text{max}}$: The highest pitch in the passage.
- $p_{\text{min}}$: The lowest pitch in the passage.

**Explanation:**  
- **Time Independence:** Unlike parameters dependent on temporal order (e.g., Intervallic Movement), Pitch Range considers only the absolute extreme values, ignoring frequency of occurrence or distribution.
- **Extremes Matter:** It highlights the outer boundaries of the pitch content, which may or may not align with the central range of activity (Tessitura).

**Examples:**
1. For the pitch sequence $\{60, 62, 64, 64, 67, 72\}$:
   - $p_{\text{max}} = 72$, $p_{\text{min}} = 60$.
   - $\text{Pitch Range: } 72 - 60 = 12$ semitones (1 octave).
2. For the pitch sequence $\{50, 55, 55, 60, 62, 62, 62\}$:
   - $p_{\text{max}} = 62$, $p_{\text{min}} = 50$.
   - $\text{Pitch Range: } 62 - 50 = 12$ semitones (1 octave).

**Musical Context:**  
Pitch Range helps in understanding the registral span of a passage:
- **Expressive Qualities:** A wide pitch range can create contrast or drama, while a narrow range may emphasize intimacy or focus.
- **Instrumental and Vocal Considerations:** Highlights the technical demands on performers by identifying the span of pitches they must navigate.
- **Comparative Analysis:** Useful in evaluating stylistic tendencies, such as comparing the narrower ranges of early music to the broader ranges in Romantic or contemporary compositions.

## **5. Tessitura**

**Type:** Secondary  
**Derived From:**  
- Primary Parameters: Pitch ($p$).  
- Aggregate: Time-independent collection of all pitches in the analyzed passage.

**Definition:**  
The *Tessitura* represents the most frequently used range of pitches in a melodic or harmonic line. It is calculated as the central range of pitches that contains at least half of all note events, providing insight into the tonal or registral "comfort zone" of the music.

**Formula:**  
Let the sorted pitch set be $P = \{p_1, p_2, \dots, p_k\}$, where $p_i \leq p_{i+1}$, and $k$ is the total number of pitches in the passage. The **Tessitura Range** is:

$$
\text{Tessitura Range} = [p_{\text{low}}, p_{\text{high}}]
$$

Where:
- $p_{\text{low}}$: The smallest pitch such that at least $\lceil k/2 \rceil$ pitches are in the range $[p_{\text{low}}, p_{\text{high}}]$.
- $p_{\text{high}}$: The largest pitch in the same range.

To find this range:
1. Sort the pitches in $P$ by ascending order.
2. Identify all possible contiguous subsets of $P$ containing at least $\lceil k/2 \rceil$ elements.
3. Choose the subset with the smallest range $[p_{\text{low}}, p_{\text{high}}]$.

**Explanation:**  
- **Time Independence:** Tessitura aggregates pitch values without regard to their timing.
- **Pitch Aggregation:** It identifies a central subset of pitches rather than focusing on individual note events.
- Unlike the full pitch range (absolute highest to lowest), Tessitura reflects the **core activity zone** of a melodic or harmonic line.

**Examples:**
1. For the pitch sequence $\{60, 62, 64, 64, 64, 67, 72\}$:
   - Sorted pitches: $\{60, 62, 64, 64, 64, 67, 72\}$.
   - $\lceil k/2 \rceil = 4$, so at least 4 pitches must fall within the range.
   - Contiguous subsets containing 4 or more pitches:
     - $\{62, 64, 64, 64\}$ (range $[62, 64]$).
     - $\{64, 64, 64, 67\}$ (range $[64, 67]$).
   - Smallest range: $[62, 64]$.
   - $\text{Tessitura Range: } [62, 64]$.
2. For the pitch sequence $\{50, 52, 55, 55, 55, 60, 62\}$:
   - Sorted pitches: $\{50, 52, 55, 55, 55, 60, 62\}$.
   - $\lceil k/2 \rceil = 4$, so at least 4 pitches must fall within the range.
   - Contiguous subsets containing 4 or more pitches:
     - $\{55, 55, 55, 60\}$ (range $[55, 60]$).
   - $\text{Tessitura Range: } [55, 60]$.

**Musical Context:**  
Tessitura is crucial for understanding the registral tendencies of a melodic or harmonic line:
- **Vocal and Instrumental Writing:** Helps determine the comfort zone for performers, especially in vocal music, where Tessitura affects ease and timbre.
- **Expressive Qualities:** A higher Tessitura conveys brightness or tension, while a lower Tessitura suggests warmth or gravity.
- **Style and Genre:** Different musical styles favor distinct Tessituras (e.g., Baroque music may have a lower Tessitura compared to Romantic-era music).

## **6. Harmonic Root**

**Type:** Secondary  
**Derived From:**  
- Aggregate: Set of simultaneous note events (pitch values).  
- Primary Parameters: Pitch ($p$).

**Definition:**  
The *Harmonic Root* identifies the specific pitch (including registration) that serves as the implied fundamental frequency for a set of simultaneous pitches. It represents the **lowest shared harmonic origin** of the aggregate, even if this root is far below the actual played pitches.  This implies that there will often by integer pitch values that are < 0

**Formula:**  
Let the pitch aggregate be $\{p_1, p_2, \dots, p_k\}$, and their frequencies be $\{f(p_1), f(p_2), \dots, f(p_k)\}$. The **Harmonic Root** is calculated as follows:

1. **Calculate the Harmonic Numbers:**

   For each pitch $p_i$, compute the ratio of its frequency to a candidate root frequency $f_{\text{root}}$:    

$$
h_i = \frac{f(p_i)}{f_{\text{root}}}
$$

   Where $h_i$ should ideally be an integer, corresponding to a position in the harmonic series.
   
3. **Identify the Lowest Shared Root:**  
   Minimize $f_{\text{root}}$ such that:
   - The resulting harmonic numbers $\{h_1, h_2, \dots, h_k\}$ are as close to integers as possible.
   - Use least common multiple (LCM) or other numerical methods to align these harmonics.

4. **Convert Root Frequency to Pitch and Registration:**  
   Given the root frequency $f_{\text{root}}$, convert to pitch and registration:  

$$
   p_{\text{root}} = 12 \cdot \log_2\left(\frac{f_{\text{root}}}{f_1}\right)
$$
   
   Where $f_1 = 16.35 \, \text{Hz}$ (frequency of C0, the lowest possible C in the system).

---

**Explanation:**  
- **Aggregate Dependency:** The Harmonic Root is derived from the entire set of pitches in the aggregate, rather than any single note.
- **Registration Inclusion:** The root specifies not only the pitch (e.g., D) but also the octave (e.g., D1, D2, etc.), which is crucial for harmonic alignment.
- **Harmonic Alignment:** The calculation identifies the **lowest fundamental frequency** consistent with the aggregate, even if that frequency is below the range of played pitches.

---

**Examples:**

1. **C Major Triad (C4, E4, G4):**  
   - Frequencies: $f(C4) = 261.63 \, \text{Hz}$, $f(E4) = 329.63 \, \text{Hz}$, $f(G4) = 392.00 \, \text{Hz}$.  
   - Harmonic alignment:  
     - $C4 = f_{\text{root}} \cdot 1$  
     - $E4 = f_{\text{root}} \cdot 5/4$  
     - $G4 = f_{\text{root}} \cdot 3/2$  
   - $f_{\text{root}} = 130.81 \, \text{Hz}$ (C3).  
   - **Harmonic Root: C3**.

2. **D Minor Triad (D4, F4, A4):**  
   - Frequencies: $f(D4) = 293.66 \, \text{Hz}$, $f(F4) = 349.23 \, \text{Hz}$, $f(A4) = 440.00 \, \text{Hz}$.  
   - Harmonic alignment:  
     - $D4 = f_{\text{root}} \cdot 2$  
     - $F4 = f_{\text{root}} \cdot 6/5$  
     - $A4 = f_{\text{root}} \cdot 3$  
   - $f_{\text{root}} = 146.83 \, \text{Hz}$ (D3).  
   - **Harmonic Root: D3**.

3. **Ambiguous Aggregate (E4, G4, C5):**  
   - Frequencies: $f(E4) = 329.63 \, \text{Hz}$, $f(G4) = 392.00 \, \text{Hz}$, $f(C5) = 523.25 \, \text{Hz}$.  
   - Possible roots:  
     - $f_{\text{root}} = 130.81 \, \text{Hz}$ (C3, assuming a C-based chord).  
     - $f_{\text{root}} = 98.00 \, \text{Hz}$ (G2, assuming G as the root).  
   - Resolution: Root depends on alignment with harmonic series.

---

**Musical Context:**  
The Harmonic Root is critical for:
- **Harmonic Analysis:** Identifying tonal centers in both tonal and atonal contexts.
- **Chord Identification:** Recognizing root notes even in ambiguous or extended aggregates.
- **Generative Music Systems:** Supporting harmonic and tonal generation in computational models.

---

Let me know if this works or if further refinements are needed!


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

 
