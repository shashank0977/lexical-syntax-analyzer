# Compiler Design Lab Experiments (Lab 1 – Lab 15)

## 📌 Project Overview

This project contains the implementation of fundamental **Compiler Design laboratory experiments** using Python.

It covers all major phases of a compiler including:

* Lexical Analysis
* Syntax Analysis
* Intermediate Code Generation
* Optimization Techniques
* Storage Allocation

---

# 📂 Project Structure

```
compiler-design-lab/
│
├── lab1_lexical_analyzer.py
├── lab2_regex_to_nfa.py
├── lab3_nfa_to_dfa.py
├── lab4_left_recursion_factoring.py
├── lab5_first_follow.py
├── lab6_predictive_parsing_table.py
├── lab7_shift_reduce_parsing.py
├── lab8_leading_trailing.py
├── lab9_lr0_items.py
├── lab10_postfix_prefix.py
├── lab11_quadruple_triple.py
├── lab12_simple_code_generator.py
├── lab13_dag.py
├── lab14_data_flow.py
├── lab15_storage_allocation.py
│
└── README.md
```

---

# 🧪 Experiment Details & Implementation

---

## 🔹 Lab 1 – Lexical Analyzer

### Objective

To identify tokens such as keywords, identifiers, numbers, and operators.

### Process

1. Take input code.
2. Split into tokens.
3. Match using:

   * Keywords list
   * Regular expressions
4. Print token type.

---

## 🔹 Lab 2 – Regular Expression to NFA

### Objective

Convert a simple regular expression into NFA.

### Process

1. Create state objects.
2. Define start and accept states.
3. Add transition based on symbol.
4. Display NFA structure.

---

## 🔹 Lab 3 – NFA to DFA

### Objective

Convert NFA into DFA using subset construction.

### Process

1. Represent NFA transitions.
2. Use set of states as DFA state.
3. Compute transitions for each symbol.
4. Store new DFA states.

---

## 🔹 Lab 4 – Left Recursion & Left Factoring

### Objective

Remove ambiguity from grammar.

### Process

1. Identify left recursive productions.
2. Split into α and β rules.
3. Introduce new non-terminal.
4. Rewrite grammar.

---

## 🔹 Lab 5 – FIRST & FOLLOW

### Objective

Compute FIRST and FOLLOW sets.

### Process

1. Define grammar.
2. Recursively compute FIRST.
3. FOLLOW (basic idea).
4. Store in dictionary.

---

## 🔹 Lab 6 – Predictive Parsing Table

### Objective

Construct LL(1) parsing table.

### Process

1. Use FIRST and FOLLOW sets.
2. Create table entries.
3. Map (Non-terminal, Terminal) → Production.

---

## 🔹 Lab 7 – Shift Reduce Parsing

### Objective

Implement bottom-up parsing.

### Process

1. Initialize stack and input buffer.
2. Perform:

   * Shift (push input to stack)
   * Reduce (replace handle)
3. Repeat until accepted.

---

## 🔹 Lab 8 – LEADING & TRAILING

### Objective

Compute LEADING and TRAILING sets.

### Process

1. For each production:

   * LEADING → first symbol
   * TRAILING → last symbol
2. Store results.

---

## 🔹 Lab 9 – LR(0) Items

### Objective

Generate LR(0) items.

### Process

1. Take productions.
2. Insert dot (•) at all positions.
3. Print all items.

---

## 🔹 Lab 10 – Prefix & Postfix

### Objective

Convert infix expression.

### Process

1. Take input expression.
2. Reverse / process stack logic.
3. Generate:

   * Prefix
   * Postfix

---

## 🔹 Lab 11 – Quadruple, Triple, Indirect Triple

### Objective

Generate intermediate code.

### Process

1. Break expression.
2. Use temporary variables.
3. Represent in:

   * Quadruple
   * Triple
   * Indirect Triple

---

## 🔹 Lab 12 – Simple Code Generator

### Objective

Generate simple machine-like instructions.

### Process

1. Parse expression.
2. Identify operators.
3. Generate instructions:

   * ADD
   * SUB

---

## 🔹 Lab 13 – DAG Implementation

### Objective

Optimize expressions using DAG.

### Process

1. Represent expression as graph.
2. Avoid recomputation.
3. Store nodes efficiently.

---

## 🔹 Lab 14 – Global Data Flow Analysis

### Objective

Analyze variable usage.

### Process

1. Identify variables.
2. Track liveness.
3. Print analysis result.

---

## 🔹 Lab 15 – Storage Allocation

### Objective

Implement memory allocation strategy.

### Process

1. Use stack structure.
2. Perform push and pop.
3. Simulate memory allocation.

---

# ⚙️ Requirements

* Python 3.x

---

# ▶️ How to Run

### Step 1: Open terminal

### Step 2: Navigate to project folder

```
cd compiler-design-lab
```

### Step 3: Run any file

```
python lab1_lexical_analyzer.py
```

Run others similarly.

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

* Lexical Analysis
* Finite Automata
* Grammar Transformations
* Parsing Techniques (Top-down & Bottom-up)
* Intermediate Code Generation
* Optimization Techniques
* Memory Management in Compiler

---

# 👨‍💻 Author

Billa Shashank
Computer Science Engineering 
Student
