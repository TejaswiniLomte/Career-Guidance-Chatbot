import datetime

def show_welcome():
    print("=" * 60)
    print("      TECH CAREER GUIDANCE CHATBOT")
    print("=" * 60)
    print("Hello! I am your Technical Career Assistant.")
    print("I can help you with:")
    print("• Programming Languages")
    print("• Web Development")
    print("• Career Guidance")
    print("• Interview Preparation")
    print("• Project Ideas")
    print("• Technical Skills")
    print("Type 'help' to see commands.")
    print("Type 'exit' to quit.")
    print("=" * 60)

responses = {
    "hello": "Hello! Welcome to the Tech Career Guidance Chatbot.",
    
    "python": """
Python is one of the best programming languages for beginners.
Career Options:
• Data Science
• Machine Learning
• Web Development
• Automation
• AI Engineering
""",

    "java": """
Java is widely used in:
• Enterprise Applications
• Android Development
• Banking Software
• Backend Systems
""",

    "web development": """
Web Development Roadmap:
1. HTML
2. CSS
3. JavaScript
4. Bootstrap
5. React
6. Node.js
7. Database (MySQL/MongoDB)
""",

    "career": """
Popular IT Career Paths:
• Software Developer
• Full Stack Developer
• Data Analyst
• Data Scientist
• AI/ML Engineer
• Cloud Engineer
• Cyber Security Analyst
""",

    "interview": """
Interview Tips:
• Practice DSA
• Learn OOP Concepts
• Prepare Projects
• Improve Communication
• Revise DBMS, OS, and Networking
""",

    "project": """
Project Ideas:
• Student Management System
• Recipe Sharing Website
• Event Registration System
• Chatbot Application
• Portfolio Website
• Online Quiz System
""",

    "skills": """
Important Technical Skills:
• Python
• SQL
• Git & GitHub
• HTML/CSS/JavaScript
• Problem Solving
• Communication Skills
""",

    "github": """
GitHub Tips:
• Upload projects regularly
• Create proper README files
• Maintain project documentation
• Learn Git commands
""",

    "resume": """
Resume Tips:
• Keep it one page
• Mention projects
• Add technical skills
• Include internship experience
• Add GitHub and LinkedIn links
"""
}

def chatbot():
    show_welcome()

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "exit":
            print("\nBot: Thank you for using Tech Career Guidance Chatbot.")
            print("Bot: Best of luck for your coding journey!")
            break

        elif user_input == "help":
            print("""
Available Topics:
python
java
web development
career
interview
project
skills
github
resume
time
help
exit
""")

        elif user_input == "time":
            current_time = datetime.datetime.now()
            print("Bot:", current_time.strftime("%d-%m-%Y %H:%M:%S"))

        elif user_input in responses:
            print("Bot:", responses[user_input])

        else:
            print("""
Bot: Sorry, I don't understand that.

Try asking about:
• Python
• Career
• Interview
• Resume
• Skills
• GitHub
• Projects
• Web Development
""")

if __name__ == "__main__":
    chatbot()
