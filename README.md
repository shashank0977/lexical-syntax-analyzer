# Compiler Design Lab Experiments

## Project Overview

This project implements fundamental **Compiler Design laboratory experiments** using Python.
The aim is to understand the core concepts of compiler construction such as **lexical analysis, automata conversion, grammar transformation, and predictive parsing**.

Each experiment demonstrates one important phase used in building a compiler.

---

# Experiments Implemented

1. Implementation of **Lexical Analyzer**
2. Conversion from **Regular Expression to NFA**
3. Conversion from **NFA to DFA**
4. **Elimination of Ambiguity, Left Recursion, and Left Factoring**
5. **FIRST and FOLLOW Computation**
6. **Predictive Parsing Table Construction**

---

# Project Structure

```
compiler-design-lab/
│
├── lab1_lexical_analyzer.py
├── lab2_regex_to_nfa.py
├── lab3_nfa_to_dfa.py
├── lab4_left_recursion_factoring.py
├── lab5_first_follow.py
├── lab6_predictive_parsing_table.py
│
└── README.md
```

---

# Implementation Details

## Lab 1 – Lexical Analyzer

### Objective

To implement a simple lexical analyzer that identifies tokens such as:

* Keywords
* Identifiers
* Numbers
* Operators

### Implementation Process

1. Read source code input from the user.
2. Split the input into tokens.
3. Compare tokens with predefined keyword list.
4. Use **regular expressions** to detect numbers and identifiers.
5. Classify each token and print its type.

### Output Example

```
Enter code: int a = 5

int -> KEYWORD
a -> IDENTIFIER
= -> OPERATOR
5 -> NUMBER
```

---

# Lab 2 – Regular Expression to NFA

### Objective

To convert a regular expression into an **NFA (Non Deterministic Finite Automaton)**.

### Implementation Process

1. Define a **State class** to represent NFA states.
2. Create a start state and an accept state.
3. Add transition edges based on the regular expression.
4. Return the constructed NFA.
5. Display start and accept states.

### Concept Used

* Finite Automata
* State transitions

---

# Lab 3 – NFA to DFA Conversion

### Objective

Convert a **Non Deterministic Finite Automaton (NFA)** into a **Deterministic Finite Automaton (DFA)**.

### Implementation Process

1. Define NFA transition table.
2. Use **subset construction method**.
3. Start from the initial NFA state.
4. Generate DFA states as sets of NFA states.
5. Compute transitions for each input symbol.
6. Store the DFA transition table.

### Output

The program prints the **DFA states and transitions**.

---

# Lab 4 – Elimination of Left Recursion and Left Factoring

### Objective

To remove grammar ambiguity by eliminating **left recursion** and applying **left factoring**.

### Implementation Process

1. Identify productions with left recursion.
2. Separate productions into:

* Recursive rules
* Non recursive rules

3. Create a new non-terminal symbol.
4. Rewrite grammar without left recursion.

### Example

Original Grammar

```
A → Aα | β
```

Transformed Grammar

```
A → βA'
A' → αA' | ε
```

---

# Lab 5 – FIRST and FOLLOW Computation

### Objective

Compute **FIRST** and **FOLLOW** sets for grammar symbols.

### FIRST Set

The FIRST set contains terminals that appear at the **beginning of strings derived from a non-terminal**.

### FOLLOW Set

The FOLLOW set contains terminals that **can appear immediately after a non-terminal**.

### Implementation Process

1. Define grammar productions.
2. Recursively compute FIRST sets.
3. Store results in a dictionary.
4. Print FIRST sets for each non-terminal.

---

# Lab 6 – Predictive Parsing Table

### Objective

Construct an **LL(1) Predictive Parsing Table**.

### Implementation Process

1. Use grammar productions.
2. Use computed FIRST and FOLLOW sets.
3. Create parsing table entries.
4. Store entries in a dictionary.
5. Print table in `(NonTerminal, Terminal)` format.

### Example Entry

```
(E , i) → E → TR
```

---

# Requirements

* Python 3.x
* Basic understanding of compiler design concepts

---

# How to Run the Project

### Step 1

Install Python from:

```
https://www.python.org
```

### Step 2

Download the project or clone the repository.

```
git clone <repository-link>
```

### Step 3

Navigate to the project directory.

```
cd compiler-design-lab
```

### Step 4

Run any experiment.

Example:

```
python lab1_lexical_analyzer.py
```

Run others similarly:

```
python lab2_regex_to_nfa.py
python lab3_nfa_to_dfa.py
python lab4_left_recursion_factoring.py
python lab5_first_follow.py
python lab6_predictive_parsing_table.py
```

---

# Learning Outcomes

After completing these experiments, the following concepts are understood:

* Tokenization and lexical analysis
* Automata construction
* Grammar transformations
* Parsing techniques
* Compiler front-end design

---

# Author
Shashank Billa
Compiler Design Laboratory Project
Computer Science Engineering
