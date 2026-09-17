# CMPS 2200 Assignment 02
## Answers

**Name:** Chuong Hoang Pham

_________________________


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$

    - $\text{Work at level 0: } 1$

    - $\text{Work at level 1: } 2$

    - $\text{Work at level 2: } 4$ 

    Therefore, $T(n) = \sum_{i=0}^{\log_3 n} 2^{i} = 2^{\log_3 n + 1} - 1 = 2 n^{\log_3 2} - 1 \in O(n^{\log_3 2}) \in O(n)$

    b) $T(n)=5T(n/4)+n$
    
    - $\text{Work at level 0: }n$

    - $\text{Work at level 1: } \frac{5}{4} n$

    Since $\frac{5}{4} > 1$, we know that this recurrence is leaf-dominated.
    
    The number of leaves: $5^{\log_4 n} = n^{\log_4 5}$

    Therefore, $T(n) = n^{\log_4 5} \approx n^{1.16} \in O(n^{1.16})$

    c) $T(n)=7T(n/7)+n$

    - $\text{Work at level 0: }n$

    - $\text{Work at level 1: } \frac{7}{7} n = n$

    Since the amount of work at every level is the same, this recurrence is balanced.

    Therefore, $T(n) = n \log_7 n \in O(n \log n)$

    d) $T(n)=9T(n/3)+n^2$

    - $\text{Work at level 0: }n^2$

    - $\text{Work at level 1: } 9 \frac{n^2}{9} = n^2$

    - $T(2) = 9^2 \frac{n^2}{9^2} = n^2$

    Since the amount of work at every level is the same, this recurrence is balanced.

    Therefore, $T(n) = n^2 \log_3 n \in O(n^2 \log n)$

    e) $T(n)=8T(n/2)+n^3$
    
    - $\text{Work at level 0: }n^3$

    - $\text{Work at level 1: } 8 \frac{n^3}{8} =  n^3$

    Since the amount of work at every level is the same, this recurrence is balanced.

    Therefore, $T(n) = n^3 \log_2 n \in O(n^3 \log n)$

    f) $T(n)=49T(n/25)+n^{3/2}\log n$
    
    - $\text{Work at level 0: }n^{3/2}\log n$

    - $\text{Work at level 1: } 49 \frac{n^{3/2}}{25^{3/2}} \log \frac{n}{25}$

    Since $\frac{49}{125} < 1$ and $\frac{n}{25} < n$, we know that this recurrence is root-dominated.

    Therefore, $T(n) = n^{\frac{3}{2}}\log n \in O(n^{\frac{3}{2}} \log n)$

    g) $T(n)=T(n-1)+2$
    
    - $\text{Work at level 0: }2$
    
    - $\text{Work at level 1: } 2$

    Since the amount of work at every level is the same, this recurrence is balanced.

    Therefore, $T(n) = 2n \in O(n)$

    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$

    Since $c \ge 1, \forall i < n, i^c < n^c$

    $T(n) = \sum_{i=0}^{n} i^c < n \cdot n^{c} = n^{c+1}$

    Therefore, $T(n) \in O(n^{c+1})$
    
    i) $T(n)=T(\sqrt{n})+1$

    - $\text{Work at level 0: } 1$

    - $\text{Work at level 1: } 1$

    - $\text{Work at level 2: } 1$

    Since the amount of work at every level is the same, this recurrence is balanced.

    And the height of the tree is $\log \log n$

    Therefore, $T(n) = O(\log \log n)$
2. **Algorithms Comparison**

- Algorithm A: $T(n) = 5 T(n/2) + n$

    - Work at level 0: $n$

    - Work at level 1: $\frac{5}{2}n$

    Since $\frac{5}{2} > 1$, this recurrence is leaf-dominated.

    The number of leaves: $5^{\log_2 n} = n^{\log_2 5} \approx n^{2.32}$

    $\Rightarrow T(n) = n^{\log_2 5} \in O(n^{2.32})$

- Algorithm B: $T(n) = 2T(n-1) + 1$
    
    - $T(n) = 2T(n-1) + 1 = 2(2T(n-2) + 1) + 1 = 4T(n-2) + 2 + 1 = 4(2T(n-3) + 1) + 2 + 1 = 8T(n-3) + 4 + 2 + 1 = \dots = 2^{n-1} T(1) + \dots + 4 + 2 + 1 = \sum_{i=0}^{n-1} 2^{i} = 2^{n} - 1 = O(2^n)$

- Algorithm C: $T(n) = 9T(n/3) + n^2$
    - $\text{Work at level 0: } n^2$
    
    - $\text{Work at level 1: } 9 \frac{n^2}{9} = n^2$
    
    Since the amount of work at every level is the same, this recurrence is balanced.

    Therefore, $T(n) = n^2 \log_3 n \in O(n^2 \log n)$

- **Conclusion**: Choose algorithm C, where the time complexity is $O(n^2 \log n)$ - the fastest algorithm when $n$ increases.

3. **Comparison Table**

|   Size (n) |   Quadratic (ms) |   Subquadratic (ms) |
|------------|------------------|---------------------|
|          2 |           0.0122 |              0.0096 |
|          4 |           0.0235 |              0.0390 |
|          8 |           0.0768 |              0.1281 |
|         16 |           0.3104 |              0.3931 |
|         32 |           1.2492 |              1.5047 |
|         64 |           5.0236 |              5.7959 |
|        128 |          19.9760 |             22.9653 |
|        256 |          80.6061 |             91.3788 |