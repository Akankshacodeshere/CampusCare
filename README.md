# 🏫 CampusCare — Complaint Management System

A simple Python-based **Campus Complaint Management System** that allows students to submit complaints, track their complaints, and automatically prioritize issues based on their category, urgency, and waiting time.

## 📌 About the Project

**CampusCare** is a student-focused complaint management module designed to make reporting campus issues more organized and efficient.

Students can:

* Submit a new complaint
* Select a complaint category
* Describe their issue
* Automatically receive a priority level
* View their previously submitted complaints
* Track pending and overdue complaints

The system stores complaint data in a **CSV file**, making it simple to run without requiring a database.

---

## ✨ Features

### 📝 Complaint Submission

Students can submit complaints by providing:

* Student ID
* Complaint title
* Description
* Category

The system validates the input before accepting the complaint.

### 🚦 Automatic Priority Calculation

Each complaint receives a numerical priority score based on:

**Category Priority + Urgent Keywords**

For example, categories such as electricity have a higher base priority.

The system also detects urgent words such as:

* `fire`
* `shock`
* `harassment`
* `unsafe`
* `leak`
* `urgent`
* `no water`
* `broken`
* `not working`

These keywords increase the complaint's priority.

### 🔴 Priority Levels

The numerical score is converted into three levels:

|     Score | Priority  |
| --------: | --------- |
| 8 or more | 🔴 High   |
|       5–7 | 🟡 Medium |
|   Below 5 | 🟢 Low    |

### ⏳ Priority Escalation

Unresolved complaints automatically become more important over time.

For every **3 days** that an unresolved complaint remains pending, its priority score increases by 1.

Example:

```text
Original Priority = 6
Pending for = 10 days

10 // 3 = 3

Current Priority = 6 + 3 = 9
Priority Level = High
```

### 🚨 Overdue Detection

If a complaint:

* is not resolved, and
* has been pending for more than 7 days,

it is automatically marked as:

```text
OVERDUE
```

### 🔍 Duplicate Complaint Detection

The system prevents a student from submitting the same complaint title again while the previous complaint is still unresolved.

### 📊 Priority-Based Sorting

When viewing complaints, they are automatically sorted from **highest current priority to lowest priority**, allowing urgent issues to appear first.

### 💾 CSV Data Storage

All complaints are stored in:

```text
complaints.csv
```

No external database is required.

---

## 🛠️ Technologies Used

* **Python 3**
* `csv` module
* `datetime` module
* File handling
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling

---

## 📂 Project Structure

```text
CampusCare/
│
├── complaints.py
├── complaints.csv
└── README.md
```

### `complaints.py`

Main Python program containing the complete complaint management system.

### `complaints.csv`

Stores submitted complaints and their information.

### `README.md`

Project documentation.

> `complaints.csv` will be created automatically when the first complaint is submitted if it does not already exist.

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-LINK>
```

### 3. Open the Project Folder

```bash
cd CampusCare
```

### 4. Run the Program

```bash
python complaints.py
```

---

## 🖥️ How the Program Works

### Step 1 — Enter Student ID

The program asks for a student ID.

The ID must:

* contain only letters and numbers
* contain between 3 and 15 characters

Example:

```text
Enter your student ID: BT12345
```

### Step 2 — Main Menu

The user sees:

```text
1. Submit complaint
2. View my complaints
3. Exit
```

### Step 3 — Submit Complaint

The user enters:

```text
Title
Description
Category
```

The program validates the information and calculates the priority automatically.

### Step 4 — View Complaints

The program displays complaints belonging to the current student and sorts them by current priority.

Example:

```text
#3 | Electricity | Fan not working | Pending | High
#1 | Hostel | Room cleaning issue | Pending | Medium
#2 | Academics | Assignment issue | Resolved | Low
```

---

## 🧠 Priority Calculation Logic

The priority system follows this basic logic:

```text
Base Category Score
        +
Urgent Keyword Score
        +
Waiting-Time Escalation
        ↓
Current Priority Score
        ↓
High / Medium / Low
```

### Example

Suppose a student submits:

```text
Category: Electricity
Title: Electrical shock
Description: There is an electrical shock from the hostel switch.
```

The calculation could
