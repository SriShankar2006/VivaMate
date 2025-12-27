import customtkinter as ctk

class EvaluationScreen(ctk.CTkFrame):
    def __init__(self, parent, scores):
        super().__init__(parent)
        self.parent = parent

        ctk.CTkLabel(
            self,
            text="Auto Evaluation Result",
            font=("Arial", 26, "bold")
        ).pack(pady=20)

        for key, value in scores.items():
            ctk.CTkLabel(
                self,
                text=f"{key}: {value}/5",
                font=("Arial", 18)
            ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Back to Home",
            command=self.go_home
        ).pack(pady=30)

    def go_home(self):
        self.parent.show_home()
