# Comprehensive Musical Parameters

This document provides detailed descriptions, derivations, and significance for all **37 musical parameters**. Each parameter is classified as **Primary** (directly measurable) or **Secondary** (derived from Primary or other Secondary parameters). 

---

## **1. Pitch Class**

**Definition:**  
The pitch identity of a note without octave information, encoded as integers (C=0, C#=1, ..., B=11).

**Primary/Secondary:**  
**Primary.**

**Derivation:**  
Measured directly from the tonal identity of a note, ignoring registration.

**Musical Context:**  
Pitch class is foundational for tonal and harmonic analysis. It captures the core identity of a note, enabling the study of scales, chords, and melodic patterns independent of octave.

**Relative Importance:**  
**High.** Central to melody, harmony, and key analysis.

---

## **2. Registration**

**Definition:**  
The octave placement of a pitch, expressed as an integer (e.g., C4 = 4).

**Primary/Secondary:**  
**Primary.**

**Derivation:**  
Measured directly from the note’s position in a score or its MIDI value.

**Musical Context:**  
Registration differentiates between pitches of the same class but in different octaves. It influences voice leading, texture, and emotional impact.

**Relative Importance:**  
**High.** Essential for distinguishing between similar pitch classes in different registers.

---

## **3. Intervallic Movement**

**Definition:**  
Sequential pitch differences in semitones, incorporating time ordering and registration shifts.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **1. Pitch Class** (Primary)  
- **2. Registration** (Primary)

**Derivation:**  
Calculated as:
\[
\text{Interval} = \text{Pitch}_{n} - \text{Pitch}_{n-1}
\]
where pitch includes both pitch class and registration.

**Musical Context:**  
Reflects the contour and progression of a melody. Small intervals suggest lyrical smoothness, while large leaps convey drama or excitement.

**Relative Importance:**  
**High.** Crucial for melodic expressiveness and contour.

---

## **4. Range**

**Definition:**  
The span between the highest and lowest pitches in a section or piece.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **2. Registration** (Primary)

**Derivation:**  
Difference between the maximum and minimum registration values:
\[
\text{Range} = \text{Max(Registration)} - \text{Min(Registration)}
\]

**Musical Context:**  
Defines the breadth of a melodic or harmonic structure. Wider ranges often signal emotional intensity or virtuosity.

**Relative Importance:**  
**Moderate.** Influences the scope and drama of a passage but is less detailed than intervallic movement.

---

## **5. Tessitura**

**Definition:**  
The average pitch position within the range of a phrase or section.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **2. Registration** (Primary)

**Derivation:**  
Calculated as:
\[
\text{Tessitura} = \frac{\sum_{i=1}^{n} \text{Registration}_{i}}{n}
\]

**Musical Context:**  
Indicates where most of the notes lie within a performer’s range. High tessitura conveys brightness or tension, while low tessitura suggests warmth or solemnity.

**Relative Importance:**  
**Moderate.** Relevant for performance analysis and expressiveness.

---

## **6. Contour Complexity**

**Definition:**  
A measure of directional changes in a melodic line.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **3. Intervallic Movement** (Secondary)

**Derivation:**  
Count the number of inflection points (changes in direction from ascending to descending or vice versa) and normalize by the total number of notes:
\[
\text{Complexity} = \frac{\text{Inflection Points}}{\text{Total Notes}}
\]

**Musical Context:**  
Captures the shape and complexity of a melody. Simple contours suggest clarity, while complex contours indicate expressiveness or intricacy.

**Relative Importance:**  
**Moderate.** Secondary to intervallic movement.

---

## **7. Ornamentation Density**

**Definition:**  
The frequency of ornamental notes (e.g., trills, grace notes) in a measure or section.

**Primary/Secondary:**  
**Primary.**

**Derivation:**  
Count the number of ornaments per unit of time.

**Musical Context:**  
Ornamentation enriches expressiveness and style. Its density varies by genre and era (e.g., Baroque music is highly ornamented).

**Relative Importance:**  
**Low to Moderate.** Specific to certain styles or periods.

---

## **8. Chord Interval Structure**

**Definition:**  
The intervals (in semitones) between a chord’s root and its other notes, expressed as a stack.

**Primary/Secondary:**  
**Primary.**

**Derivation:**  
Measured directly by comparing each chord tone to the root.

**Musical Context:**  
Defines the chord’s quality (e.g., major, minor, augmented). Essential for harmonic analysis.

**Relative Importance:**  
**High.** Foundational for understanding harmonic relationships.

---

## **9. Fuzzy Chord Classification**

**Definition:**  
Probabilistic assignment of a chord to categories (e.g., major, minor) based on interval structure and context.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **8. Chord Interval Structure** (Primary)

**Derivation:**  
Apply fuzzy logic to chord intervals to assign likelihoods to different chord types.

**Musical Context:**  
Useful for resolving ambiguities in complex or extended harmonies.

**Relative Importance:**  
**High.** Particularly relevant in jazz, modern, and atonal music.

---

## **10. Chord Inversion**

**Definition:**  
The chord member (e.g., root, third, fifth) appearing in the bass.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **8. Chord Interval Structure** (Primary)  
- **11. Bass Note** (Primary)

**Derivation:**  
Determine the interval between the bass note and the chord root to classify the inversion.

**Musical Context:**  
Inversions affect harmonic function and voice leading.

**Relative Importance:**  
**High.** Essential for harmonic and tonal analysis.

---

## **11. Bass Note**

**Definition:**  
The lowest pitch in a chord or passage.

**Primary/Secondary:**  
**Primary.**

**Derivation:**  
Measured directly from the lowest pitch present.

**Musical Context:**  
Anchors harmonic and tonal structures.

**Relative Importance:**  
**High.** Key to understanding harmonic grounding.

---

## **12. Chord Distance**

**Definition:**  
The intervallic similarity or functional relationship between two chords, represented as a numerical score.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **8. Chord Interval Structure** (Primary)

**Derivation:**  
1. Align the interval stacks of two chords.  
2. Compute the weighted difference between intervals:
   \[
   D(C_1, C_2) = \sum_{k=1}^{\max(m, n)} w_k \cdot |i_k - j_k|
   \]
3. Normalize the distance score.

**Musical Context:**  
Highlights functional progressions or chromatic shifts.

**Relative Importance:**  
**High.** Essential for harmonic progressions.

---

## **13. Implied Harmonic Root**

**Definition:**  
The lowest fundamental pitch inferred from simultaneous pitches based on harmonic series.

**Primary/Secondary:**  
**Secondary.**

**Derived From:**  
- **1. Pitch Class** (Primary)  
- **2. Registration** (Primary)

**Derivation:**  
Identify the root aligning with the lowest harmonic numbers:
\[
R_{\text{implied}} = \arg\min_R \frac{1}{k} \sum_{j=1}^{k} n_{jR}
\]

**Musical Context:**  
Determines harmonic stability and tonal grounding.

**Relative Importance:**  
**High.** Central to tonal analysis.

---

The remaining parameters will follow this format. Let me know if you'd like all 37 completed!  
