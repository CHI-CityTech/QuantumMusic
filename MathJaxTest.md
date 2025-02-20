# MathJax Formula Test

This document contains a variety of formulas to test **MathJax** rendering on GitHub Pages.  These are useful in generating documents etc.

---

## **Inline Math Examples**

1. Pythagorean Theorem: \( a^2 + b^2 = c^2 \)  
2. Einstein's Mass-Energy Equivalence: \( E = mc^2 \)  
3. Quadratic Formula: \( x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \)

---

## **Block Math Examples**

### **1. Pythagorean Theorem**
$$
a^2 + b^2 = c^2
$$

### **2. Quadratic Formula**
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### **3. Summation Formula**
$$
S = \sum_{i=1}^{n} i = \frac{n(n + 1)}{2}
$$

### **4. Integral Example**
$$
\int_0^1 x^2 \, dx = \frac{1}{3}
$$

### **5. Fourier Transform**
$$
\hat{f}(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi i x \xi} \, dx
$$

### **6. Matrix Example**
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

---

## **Testing Instructions**

1. Upload this Markdown file to your GitHub repository.
2. Verify the formatting on your GitHub Pages site.
3. If formulas do not render, ensure that:
   - The MathJax script is included in your layout or Markdown files:
     ```html
     <script type="text/javascript" async
         src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
     </script>
     ```
   - Jekyll is enabled with the appropriate `_config.yml` settings:
     ```yaml
     markdown: kramdown
     kramdown:
       input: GFM
     ```

If these steps do not work, let me know the results, and we’ll troubleshoot further!
