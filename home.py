import customtkinter as ctk
import json
import os

class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Title
        ctk.CTkLabel(
            self,
            text="🎓 VivaMate",
            font=("Segoe UI", 32, "bold")
        ).pack(pady=40)

        ctk.CTkLabel(
            self,
            text="Practice Viva • Build Confidence • Improve Speaking",
            font=("Segoe UI", 16)
        ).pack(pady=10)

        # Course selection dropdown
        ctk.CTkLabel(self, text="Select Course:", font=("Segoe UI", 18)).pack(pady=(30, 5))

        # Load courses dynamically from questions.json
        try:
            with open(os.path.join("data", "questions.json"), "r") as f:
                data = json.load(f)
                self.courses = list(data.keys())
        except FileNotFoundError:
            self.courses = []
            print("questions.json not found!")
        except json.JSONDecodeError:
            self.courses = []
            print("Invalid JSON file!")

        self.selected_course = ctk.StringVar(value=self.courses[0] if self.courses else "")

        self.dropdown = ctk.CTkOptionMenu(
            self,
            values=self.courses,
            variable=self.selected_course,
            width=200
        )
        self.dropdown.pack(pady=15)

        # Start practice button
        ctk.CTkButton(
            self,
            text="▶ Start Practice",
            width=240,
            height=45,
            command=self.start_practice
        ).pack(pady=25)

        # Exit button
        ctk.CTkButton(
            self,
            text="❌ Exit",
            fg_color="#8b0000",
            hover_color="#5a0000",
            command=self.app.destroy
        ).pack()

    # --------------------- Start Practice ---------------------
    def start_practice(self):
        course = self.selected_course.get()
        if not course:
            ctk.CTkMessagebox.show_error("Error", "No course selected!")
            return
        # Show QuestionScreen for the selected course
        self.app.show_frame("Question", subject=course)
