[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22049940)

# Therapy Planner – End-of-Semester Lab Test (Introduction to Programming)

This repository contains the required structure for the end-of-semester lab assignment.  
Use **`app.py`** for the program logic and **`tests.py`** for unit tests. Additional files may be added if necessary.

---

## 📌 Assignment Overview

Create a Python program that:

- Asks users questions about planning **weekly therapy sessions** for **three clients**.
- Computes **weekly totals** for each therapy type by aggregating all client responses.
- Interprets each total as **Low**, **Moderate**, or **High load**.
- Handles invalid inputs gracefully using exception handling.
- Includes a **unit test** for a calculation or interpretation function.

The objective is to calculate **one weekly total per therapy type**, combining all answers across all three clients.

---

## 🧩 Functional Requirements

### Quiz Structure
- The quiz contains **15 questions**.
- Each question corresponds to one of the following therapy types:
  - **IndividualTherapy**
  - **GroupTherapy**
  - **FamilyTherapy**
  - **CoupleTherapy**
  - **OnlineTherapy**
- Each question asks how many weekly sessions (**0–7**) the user has with:
  - the **first client**
  - the **second client**
  - the **third client**

---

## 🛠️ Scoring

- Each response contributes to the total for one therapy type.
- Weekly totals are computed by **summing all responses** that belong to the same therapy type, **regardless of which client the question refers to**.

**Example:**  
All questions labeled `"IndividualTherapy"` are added together, even if they refer to different clients.

---

## 📊 Interpretation

Interpretation is based on the weekly total:

| Weekly Total | Interpretation |
|--------------|----------------|
| **> 9**      | High load      |
| **5–9**      | Moderate load  |
| **< 5**      | Low load       |

This interpretation must be implemented using a **pure function**, which will be unit tested.

---

## 📤 Output Requirements

Your program must:

- Display the **weekly total sessions** for each therapy type.
- Provide a **descriptive label** (High, Moderate, Low) for each type.

---

## ✔️ Input Validation

If the user provides invalid input:

- If the input is **non-numeric**, ask again.
- If the value is outside the valid range **0–7**, show an error and re-prompt.
- Use `try/except` blocks to prevent program crashes.

---

## 🗂️ Data Structure

You may use a **list of dictionaries** or another suitable data structure.

Each dictionary includes:

- `text`: The question text  
- `therapy`: The therapy type  

**Example:**

```python
items = [
    {"text": "How many Individual Therapy sessions per week do you have with the first client?", "therapy": "IndividualTherapy"},
    {"text": "How many Group Therapy sessions per week do you have with the first client?", "therapy": "GroupTherapy"},
    {"text": "How many Family Therapy sessions per week do you have with the first client?", "therapy": "FamilyTherapy"}
]
````

---

## 🧾 Non-Functional Requirements

Your code must:

* Be **modular**.
* Be **testable**.
* Follow **clean writing and naming conventions**.
* Handle errors robustly, including invalid user input.

---

## 📝 Grading Criteria (Total: 9 points)

To pass, you must score **at least 4 points**.

| Criterion                                                                        | Points |
| -------------------------------------------------------------------------------- | ------ |
| Program runs without errors/warnings                                             | 1      |
| Program produces the expected output                                             | 1      |
| Program includes at least one meaningful unit test                               | 1      |
| Student performs a live modification in ≤5 minutes                               | 3      |
| Student answers questions about their own code (up to 3 questions, 1 point each) | 3      |

Evaluation may take place during the **last lab session** or any **exam session**.

---

## 🧪 Example Input

```
How many Individual Therapy sessions per week do you have with the first client? 2
How many Group Therapy sessions per week do you have with the first client? 1
How many Individual Therapy sessions per week do you have with the second client? 3
How many Online Therapy sessions per week do you have with the third client? 2
How many Family Therapy sessions per week do you have with the third client? 0
...
```

---

## 🧾 Example Output

```
IndividualTherapy: 6 sessions/week → Moderate
GroupTherapy: 1 sessions/week → Low
FamilyTherapy: 0 sessions/week → Low
CoupleTherapy: 10 sessions/week → High
OnlineTherapy: 2 sessions/week → Low
```

---


