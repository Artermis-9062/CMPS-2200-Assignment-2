# CMPS 2200 Recitation 02

## Answers

**Name:** Chuong Hoang Pham

---

Place all written answers from `recitation-02.md` here for easier grading.

- **4) (3 points)** Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = n$, and $f(n) = n^2$  with $a=2$ and $b=2$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
 - $f(n) = 1: $

    $$ W(n) = \sum_{i = 0}^{\lg n} 2^{i} = \frac{2^{\lg n + 1} - 1}{2-1} = 2 \cdot n - 1 $$

  - $f(n) = n: $
    
    $$ W(n) = \sum_{i = 0}^{\lg n} (n) = n \cdot (\lg n + 1) $$

  - $f(n) = n^2: $

  $$ W(n) = \sum_{i = 0}{\lg n} (n^2 \cdot \frac{1}{2^{i}}) = n^2 \cdot \frac{1 - \frac{1}{2}^{\lg n + 1}}{0.5} = 2n^2 - n $$

- **5) (4 points)** Now that you have a nice way to empirically 
  generate values of $W(n)$, we can look at the relationship 
  between $a$, $b$, and $f(n)$. If $f(n) = n^c$, we can derive 
  a very nice result.
  
  The Master Method gives an easy formula for solving general 
  recurrences of the form: 

    $$T(n) = aT(n/b) + n^c$$

  Its three cases correspond to the relationship between $\log_b a$ 
  and $c$. Derive the asymptotic behavior of $T(n)$ by solving its 
  general recursion tree for each of the three cases. Show your 
  recursion tree and derivations from it.

  ```text
                             n^c
                          /       \
                         /         \
                        /           \
                       /             \
                 (n/b)^c             (n/b)^c                a branches
                 /     \             /     \
                /       \           /       \
          (n/b^2)^c  (n/b^2)^c (n/b^2)^c  (n/b^2)^c         a^2 branches
          ...
  ```

  General Summation: 

  $$ T(n) = \sum_{i = 0}^{\lg n} a^i * \frac{n}{b^i}^c = n^c \sum_{i = 0}^{\log_b n} \frac{a}{b^c}^i $$
  1. $\log_b a < c$

    Since $\log_b a < c \Rightarrow a < b^c$. Then, the summation converges to 1 as $n$ grows.
    $$ \Rightarrow T(n) = n^c \cdot O(1) \Rightarrow O(n^c) $$
  2. $\log_b a = c$

    Since $\log_b a = c \Rightarrow a = b^c$. Then, the summation equals to $\log_b n + 1$
    $$ \Rightarrow T(n) = n^c \cdot (\log_b n + 1) \Rightarrow O(n^c \log_b n) $$
  3. $\log_b a > c$ 

    Since $\log_b a > c \Rightarrow a > b^c$. Because $\frac{a}{b^c}$ is strictly greater than 1, the series grows exponentially and the work is dominated by the final leaf nodes.
    
    The number of leaves at the bottom of the tree is $a^{\log_b n}$, which mathematically simplifies to $n^{\log_b a}$.
    $$ \Rightarrow O(n^{\log_b a})$$

- **7) (2 points)** Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

  The general recurrence for span becomes: $S(n) = S(n/b) + f(n)$

  Applying this to the recurrences from Problem 4 (where $b = 2$):

  - 1. When $f(n) = 1$
    -   **Recurrence:** $S(n) = S(n/2) + 1$
    -   $$\mathbf{T(n)} = \sum_{i = 1}^{\lg n} (1) \Rightarrow T(N) \in O(\log n)$$

  - 2. When $f(n) = n$
    -   **Recurrence:** $S(n) = S(n/2) + n$
    -   $$\mathbf{T(n)} = \sum_{i = 0}^{\lg n} (\frac{n}{2^i}) = 2n \text{(as $n$ grows to $infty$)} \Rightarrow T(N) \in O(n)$$

  - 3. When $f(n) = n^2$
    -   **Recurrence:** $S(n) = S(n/2) + n^2$
    -   $$\mathbf{T(n)} = \sum_{i = 0}^{\lg n} (\frac{n}{2^i}^2) = \frac{4}{3}n^2 \text{(as $n$ grows to $infty$)} \Rightarrow T(N) \in O(n^2)$$