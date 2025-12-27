import customtkinter as ctk
import json
import os

from audio.recorder import AudioRecorder
from audio.playback import play_audio

from evaluation_engine.speech_to_text import speech_to_text
from evaluation_engine.confidence import confidence_score
from evaluation_engine.fluency import fluency_score
from evaluation_engine.clarity import clarity_score


class QuestionScreen(ctk.CTkFrame):
    def __init__(self, parent, app, subject):
        super().__init__(parent)
        self.app = app
        self.subject = subject

        # Audio
        self.audio_file = "recordings/answer.wav"
        self.recorder = AudioRecorder(self.audio_file)

        # Load questions
        with open(os.path.join("data", "questions.json"), "r") as f:
            self.questions = json.load(f)[subject]

        self.index = 0
        self.remaining_time = 30
        self.timer_id = None

        # ================= BACKGROUND =================
        bg = ctk.CTkFrame(self)
        bg.pack(fill="both", expand=True, padx=20, pady=20)

        self.scroll = ctk.CTkScrollableFrame(bg, corner_radius=20)
        self.scroll.pack(fill="both", expand=True)

        # ================= HEADER =================
        ctk.CTkLabel(
            self.scroll,
            text="🎤 VivaMate – Practice Session",
            font=("Segoe UI", 26, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            self.scroll,
            text=f"Subject: {self.subject}",
            font=("Segoe UI", 16)
        ).pack(pady=5)

        # ================= QUESTION =================
        self.question_label = ctk.CTkLabel(
            self.scroll,
            wraplength=800,
            font=("Segoe UI", 20),
            justify="center"
        )
        self.question_label.pack(pady=25)

        self.timer_label = ctk.CTkLabel(
            self.scroll,
            text="⏱ Time: 30",
            font=("Segoe UI", 14)
        )
        self.timer_label.pack(pady=5)

        # ================= RECORD CONTROLS =================
        rec = ctk.CTkFrame(self.scroll, fg_color="transparent")
        rec.pack(pady=15)

        ctk.CTkButton(rec, text="▶ Start Recording",
                      command=self.start_recording)\
            .grid(row=0, column=0, padx=6)

        ctk.CTkButton(rec, text="⏹ Stop Recording",
                      fg_color="#d9534f",
                      command=self.stop_recording)\
            .grid(row=0, column=1, padx=6)

        ctk.CTkButton(rec, text="🔊 Play Recording",
                      command=self.play_recording)\
            .grid(row=0, column=2, padx=6)

        # ================= ANALYSIS =================
        ctk.CTkButton(
            self.scroll,
            text="📊 Analyze Answer",
            fg_color="#5cb85c",
            command=self.analyze
        ).pack(pady=15)

        self.conf_bar, self.conf_label = self.create_bar("Confidence")
        self.flu_bar, self.flu_label = self.create_bar("Fluency")
        self.cla_bar, self.cla_label = self.create_bar("Clarity")

        # ================= KEYWORDS =================
        self.keyword_title = ctk.CTkLabel(
            self.scroll,
            text="",
            font=("Segoe UI", 16, "bold")
        )
        self.keyword_title.pack(pady=(20, 5))

        self.keyword_label = ctk.CTkLabel(
            self.scroll,
            text="",
            wraplength=800,
            justify="center"
        )
        self.keyword_label.pack()

        # ================= NAVIGATION =================
        nav = ctk.CTkFrame(self.scroll, fg_color="transparent")
        nav.pack(pady=25)

        ctk.CTkButton(
            nav,
            text="🏠 Back to Home",
            fg_color="#3498db",
            hover_color="#217dbb",
            command=lambda: self.app.show_frame("Home")
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            nav,
            text="⬅ Previous",
            command=self.prev_question
        ).grid(row=0, column=1, padx=10)

        ctk.CTkButton(
            nav,
            text="Next ➡",
            command=self.next_question
        ).grid(row=0, column=2, padx=10)

        ctk.CTkButton(
            nav,
            text="❌ Exit",
            fg_color="#8b0000",
            hover_color="#5a0000",
            command=self.app.destroy
        ).grid(row=0, column=3, padx=10)

        self.load_question()

    # ================= TIMER (SAFE) =================
    def start_timer(self):
        if self.remaining_time >= 0:
            self.timer_label.configure(text=f"⏱ Time: {self.remaining_time}")
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.start_timer)

    def stop_timer(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

    # ================= FUNCTIONS =================
    def load_question(self):
        self.stop_timer()
        self.remaining_time = 30
        self.timer_label.configure(text="⏱ Time: 30")

        q = self.questions[self.index]
        self.question_label.configure(
            text=f"Q{self.index + 1}. {q['question']}"
        )

        self.conf_bar.set(0)
        self.flu_bar.set(0)
        self.cla_bar.set(0)

        self.conf_label.configure(text="0%")
        self.flu_label.configure(text="0%")
        self.cla_label.configure(text="0%")

        self.keyword_title.configure(text="")
        self.keyword_label.configure(text="")

    def start_recording(self):
        self.remaining_time = 30
        self.start_timer()
        self.recorder.start()

    def stop_recording(self):
        self.stop_timer()
        self.recorder.stop()

    def play_recording(self):
        if os.path.exists(self.audio_file):
            play_audio(self.audio_file)

    def analyze(self):
        text = speech_to_text(self.audio_file)

        conf = int(confidence_score(text) * 20)
        flu = int(fluency_score(text) * 20)
        cla = int(clarity_score(text) * 20)

        self.conf_bar.set(conf / 100)
        self.flu_bar.set(flu / 100)
        self.cla_bar.set(cla / 100)

        self.conf_label.configure(text=f"{conf}%")
        self.flu_label.configure(text=f"{flu}%")
        self.cla_label.configure(text=f"{cla}%")

        keywords = self.questions[self.index].get("keywords", [])
        self.keyword_title.configure(text="🔑 Expected Keywords")
        self.keyword_label.configure(text=", ".join(keywords))

    def next_question(self):
        if self.index < len(self.questions) - 1:
            self.index += 1
            self.load_question()

    def prev_question(self):
        if self.index > 0:
            self.index -= 1
            self.load_question()

    def create_bar(self, name):
        ctk.CTkLabel(self.scroll, text=name,
                     font=("Segoe UI", 14)).pack(pady=(15, 5))

        bar = ctk.CTkProgressBar(self.scroll, width=520)
        bar.set(0)
        bar.pack()

        percent = ctk.CTkLabel(self.scroll, text="0%")
        percent.pack()

        return bar, percent
