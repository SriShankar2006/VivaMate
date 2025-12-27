# VivaMate
VivaMate is a desktop application designed to help students practice viva and interview questions effectively. It offers course-wise question practice, voice-based answering, and self-evaluation to improve confidence, clarity, fluency, and technical accuracy. Ideal for exam preparation and interview readiness.


🎓 VivaMate – Smart Viva Practice Application

VivaMate is a desktop-based viva and interview practice application designed to help students improve their speaking confidence, clarity, and technical accuracy. It simulates real viva conditions by providing timed questions, voice recording, playback, and automated self-analysis.

🚀 Features
🏠 Home Screen

Clean and simple UI

Course selection (e.g., C Programming, DBMS, etc.)

One-click Start Practice

Designed for distraction-free preparation

🧠 Practice Session Screen

Displays subject name and question

Countdown timer to simulate real viva pressure

Voice-based interaction:

▶ Start Recording

⏹ Stop Recording

🔊 Play Recorded Answer

Automated answer analysis

Progress indicators for:

Confidence

Fluency

Clarity

Displays expected keywords for self-evaluation

Easy navigation:

Previous / Next question

Back to Home

Exit application

🎯 Purpose of VivaMate

Many students understand theory but struggle during viva or interviews due to:

Nervousness

Lack of speaking practice

Poor time management

VivaMate addresses these issues by providing a safe practice environment where students can rehearse answers, listen to themselves, and track improvement over time.

🛠️ Technologies Used

Python

Tkinter / CustomTkinter for UI

Audio recording & playback

JSON-based question bank

Logic-based auto evaluation (confidence, fluency, clarity)

📸 Application Screens
Home Screen

Course selection

Start practice option

Clean and minimal interface

Practice Session

Question display with timer

Voice recording controls

Auto-analysis with progress bars

Expected keywords for guidance

📌 Ideal For

Engineering students

Viva & practical exam preparation

Interview practice

Communication skill improvement

Self-paced learning

🔮 Future Enhancements

AI-based speech evaluation

More subjects and question banks

Mobile version

Export performance reports

Keyword-based technical accuracy scoring

VivaMate/
│
├── main.py                 # App entry point
│
├── ui/
│   ├── home.py             # Home screen UI
│   ├── question_screen.py  # Question + timer
│   ├── evaluation.py       # Auto-evaluation screen
│
├── audio/
│   ├── recorder.py         # Voice recording logic
│   ├── playback.py         # Audio playback
│
├── evaluation_engine/
│   ├── speech_to_text.py   # Voice → Text
│   ├── confidence.py       # Confidence score
│   ├── fluency.py          # Fluency score
│   ├── clarity.py          # Clarity score
│   ├── keywords.py         # Keyword matching
│
├── data/
│   ├── questions.json      # Viva questions + keywords
│   └── vivamate.db         # SQLite database
│
├── recordings/             # Saved audio files
│
└── utils/
    ├── timer.py            # Countdown timer
    └── db.py               # Database handling
