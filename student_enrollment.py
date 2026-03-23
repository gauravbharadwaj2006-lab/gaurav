course = {
    "python": 0,
    "ai": 0,
    "data science": 0
}

course_alias = {
    "python": "python",
    "py": "python",
    "Python": "python",

    "ai": "ai",
    "a.i": "ai",
    "artificial intelligence": "ai",

    "data science": "data science",
    "ds": "data science"
}

student = []

n = int(input("Enter the number of student: "))

for i in range(n):
    print(f"\nStudent {i+1}")
    
    name = input("Enter the name of student: ")
    print("Available courses: Python, AI, Data Science")
    
    user_input = input("Enter the course: ").strip().lower()
    
    
    if user_input in course_alias:
        selected_course = course_alias[user_input]
        
        course[selected_course] += 1
        student.append({"name": name, "course": selected_course})
    else:
        print("Please select valid course")

print("\nCourse enrollment count:")
for c, count in course.items():
    print(f"{c}: {count} students")

most_popular = max(course, key=course.get)
print("\nMost popular course:", most_popular)
