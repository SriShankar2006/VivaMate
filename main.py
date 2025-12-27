import customtkinter as ctk
from ui.home import HomeScreen
from ui.question_screen import QuestionScreen  # Your QuestionScreen

class VivaMateApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VivaMate")
        self.geometry("900x700")

        self.frames = {}

        # Initialize HomeScreen
        home = HomeScreen(self, self)
        home.pack(fill="both", expand=True)
        self.frames["Home"] = home

        # QuestionScreen will be initialized on demand with a subject
        self.frames["Question"] = None

        self.show_frame("Home")

    # --------------------- Show Frame ---------------------
    def show_frame(self, frame_name, **kwargs):
        # Hide current frame
        for f in self.frames.values():
            if f is not None:
                f.pack_forget()

        if frame_name == "Question":
            subject = kwargs.get("subject")
            # If frame exists, destroy and recreate with new subject
            if self.frames["Question"] is not None:
                self.frames["Question"].destroy()
            self.frames["Question"] = QuestionScreen(self, self, subject)
            self.frames["Question"].pack(fill="both", expand=True)
        else:
            self.frames[frame_name].pack(fill="both", expand=True)

# --------------------- Run App ---------------------
if __name__ == "__main__":
    app = VivaMateApp()
    app.mainloop()
