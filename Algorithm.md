# Time Complexity & Space Complexity Notes

## What is an Algorithm?

An algorithm is a **step-by-step procedure** used to solve a problem.

### Example

Finding the largest number in a list:

1. Assume the first element is the largest.
2. Compare it with every other element.
3. Update the largest if needed.
4. Print the result.

---

# What is Time Complexity?

## Definition

Time Complexity measures **how the running time of an algorithm grows as the input size (n) increases.**

It does **NOT** measure actual time in seconds.

### Example

```python
for i in range(n):
    print(i)
```

If

```
n = 5
```

Loop runs 5 times.

If

```
n = 1000
```

Loop runs 1000 times.

Time Complexity:

```
O(n)
```

---

# What is Space Complexity?

## Definition

Space Complexity measures **how much memory an algorithm uses as the input size increases.**

### Example

```python
arr = []

for i in range(n):
    arr.append(i)
```

The list grows with `n`.

Space Complexity:

```
O(n)
```

---

# Big O Notation

Big O describes the **worst-case growth rate** of an algorithm.

| Big O | Name | Performance |
|-------|------|-------------|
| O(1) | Constant | Excellent |
| O(log n) | Logarithmic | Excellent |
| O(n) | Linear | Good |
| O(n log n) | Linearithmic | Good |
| O(n²) | Quadratic | Slow |
| O(n³) | Cubic | Very Slow |
| O(2ⁿ) | Exponential | Extremely Slow |
| O(n!) | Factorial | Worst |

---

# O(1) - Constant Time

The running time does not depend on input size.

### Example

```python
arr = [10,20,30,40]

print(arr[2])
```

Time Complexity:

```
O(1)
```

---

# O(n) - Linear Time

One loop.

### Example

```python
for i in range(n):
    print(i)
```

Time Complexity

```
O(n)
```

---

# O(n²) - Quadratic Time

Nested loops.

### Example

```python
for i in range(n):
    for j in range(n):
        print(i,j)
```

Time Complexity

```
O(n²)
```

---

# O(log n) - Logarithmic Time

Input size is reduced by half each step.

Example:

Binary Search.

```
1000
 ↓
500
 ↓
250
 ↓
125
 ↓
62
```

Time Complexity

```
O(log n)
```

---

# Rules for Finding Time Complexity

## Rule 1: Count Loops

```python
for i in range(n):
    print(i)
```

```
O(n)
```

---

## Rule 2: Nested Loops Multiply

```python
for i in range(n):
    for j in range(n):
        pass
```

```
n × n

O(n²)
```

---

## Rule 3: Consecutive Loops Add

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

```
O(n+n)

↓

O(n)
```

---

## Rule 4: Ignore Constants

```python
for i in range(2*n):
    pass
```

```
O(2n)

↓

O(n)
```

---

## Rule 5: Different Variables Stay Different

```python
for i in range(n):
    pass

for j in range(m):
    pass
```

```
O(n+m)
```

---

# Space Complexity Examples

### Example 1

```python
x = 10
y = 20
```

Space Complexity

```
O(1)
```

---

### Example 2

```python
arr = []

for i in range(n):
    arr.append(i)
```

Space Complexity

```
O(n)
```

---

# Common Mistakes

❌ Measuring time in seconds.

✔ Measure growth with input size.

---

❌ Keeping constants.

```
O(2n)

↓

O(n)
```

---

❌ Thinking two separate loops are O(n²).

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

Correct

```
O(n+n)

↓

O(n)
```

---

# Homework Solution

```python
for i in range(n):
    print(i)

for j in range(n):
    for k in range(n):
        print(j,k)
```

First loop

```
O(n)
```

Nested loop

```
O(n²)
```

Total

```
O(n+n²)

↓

O(n²)
```

Final Answer

```
Time Complexity = O(n²)
```

---

# Quick Revision

- O(1) → Constant
- O(log n) → Divide by 2 each step
- O(n) → Single loop
- O(n²) → Nested loops
- Consecutive loops → Add
- Nested loops → Multiply
- Ignore constants
- Keep the highest-order term only