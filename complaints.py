# complaints.py - CampusCare complaint module (Ronit)
# Students can submit complaints and view them.
# Complaints are saved in complaints.csv
 
import csv
from datetime import datetime
 
FILE_NAME = "complaints.csv"
HEADINGS = ["id", "student_id", "title", "description",
            "category", "priority", "status", "date"]
 
categories = ["Hostel", "Classroom", "Internet", "Electricity",
              "Cleanliness", "Transport", "Academics", "Other"]
 
# base priority points for each category
category_points = {"Hostel": 4, "Classroom": 3, "Internet": 3,
                   "Electricity": 5, "Cleanliness": 2, "Transport": 3,
                   "Academics": 2, "Other": 1}
 
# if these words are in the complaint, priority goes up
urgent_words = {"fire": 5, "shock": 5, "harassment": 5, "unsafe": 4,
                "leak": 3, "urgent": 3, "no water": 3, "broken": 2,
                "not working": 2}
 
 
def load_complaints():
    """Read all complaints from the CSV file and return them as a list."""
    complaints = []
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                complaints.append(row)
    except FileNotFoundError:
        pass  # file does not exist yet, so there are no complaints
    return complaints
 
 
def save_complaints(complaints):
    """Write the whole list of complaints back to the CSV file."""
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADINGS)
        writer.writeheader()
        writer.writerows(complaints)
 
 
def calculate_priority(category, title, description):
    """Priority = category points + points for urgent words."""
    score = category_points[category]
    text = (title + " " + description).lower()
    for word in urgent_words:
        if word in text:
            score = score + urgent_words[word]
    return score
 
 
def priority_label(score):
    """Convert the score into High / Medium / Low."""
    if score >= 8:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"
 
 
def days_pending(date_text):
    """How many days ago the complaint was filed."""
    filed = datetime.strptime(date_text, "%Y-%m-%d")
    return (datetime.now() - filed).days
 
 
def current_score(complaint):
    """Old unresolved complaints get +1 priority for every 3 days."""
    score = int(complaint["priority"])
    if complaint["status"] != "Resolved":
        score = score + days_pending(complaint["date"]) // 3
    return score
 
 
def submit_complaint(student_id):
    complaints = load_complaints()
    print("\n--- Submit Complaint ---")
 
    # take title (input validation)
    while True:
        title = input("Title: ").strip()
        if len(title) >= 5:
            break
        print("Title is too short. Enter at least 5 characters.")
 
    # take description (input validation)
    while True:
        description = input("Description: ").strip()
        if len(description) >= 10:
            break
        print("Description is too short. Enter at least 10 characters.")
 
    # choose category (input validation)
    print("\nCategories:")
    for i in range(len(categories)):
        print(i + 1, ".", categories[i])
    while True:
        choice = input("Enter category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            break
        print("Invalid choice. Enter a number from the list.")
 
    # duplicate check: same student, same title, not resolved yet
    for c in complaints:
        if (c["student_id"] == student_id and
                c["title"].lower() == title.lower() and
                c["status"] != "Resolved"):
            print("\nYou have already submitted this complaint (ID", c["id"], ").")
            return
 
    score = calculate_priority(category, title, description)
    new_complaint = {
        "id": len(complaints) + 1,
        "student_id": student_id,
        "title": title,
        "description": description,
        "category": category,
        "priority": score,
        "status": "Pending",
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    complaints.append(new_complaint)
    save_complaints(complaints)
    print("\nComplaint submitted! ID:", new_complaint["id"],
          "| Priority:", priority_label(score))
 
 
def view_my_complaints(student_id):
    complaints = load_complaints()
    mine = []
    for c in complaints:
        if c["student_id"] == student_id:
            mine.append(c)
 
    print("\n--- Your Complaints ---")
    if len(mine) == 0:
        print("No complaints found.")
        return
 
    # highest priority first
    mine.sort(key=current_score, reverse=True)
 
    for c in mine:
        line = ("#" + c["id"] + " | " + c["category"] + " | " + c["title"] +
                " | " + c["status"] + " | " + priority_label(current_score(c)))
        # overdue if not resolved and older than 7 days
        if c["status"] != "Resolved" and days_pending(c["date"]) > 7:
            line = line + " | OVERDUE"
        print(line)
 
 
# ---------------- main program ----------------
while True:
    student_id = input("Enter your student ID: ").strip().upper()
    if student_id.isalnum() and 3 <= len(student_id) <= 15:
        break
    print("Invalid ID. Use only letters and digits (3-15 characters).")
 
while True:
    print("\n1. Submit complaint")
    print("2. View my complaints")
    print("3. Exit")
    option = input("Choose: ").strip()
 
    if option == "1":
        submit_complaint(student_id)
    elif option == "2":
        view_my_complaints(student_id)
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Enter 1, 2 or 3.")
 