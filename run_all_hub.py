"""
OASIS INFOBYTE (OIBSIP) - PYTHON INTERNSHIP PROJECT HUB
Author: Gokul K.
Track: Python Programming
Internship Offer: OIB/R2/IP9900
"""

import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = sys.executable

TASKS = [
    {
        "id": "Task 2",
        "name": "Body Mass Index (BMI) Calculator",
        "folder": "Python-Task2-BMICalculator",
        "gui": "bmi_calculator_gui.py",
        "cli": "bmi_calculator_cli.py",
        "desc": "Calculate BMI with WHO categories, SQLite profile storage, and embedded Matplotlib trend graph."
    },
    {
        "id": "Task 3",
        "name": "Random Password Generator",
        "folder": "Python-Task3-PasswordGenerator",
        "gui": "password_generator_gui.py",
        "cli": "password_generator_cli.py",
        "desc": "Cryptographically secure password generation with secrets, strength meter, and clipboard auto-copy."
    },
    {
        "id": "Task 4",
        "name": "Basic Weather App",
        "folder": "Python-Task4-WeatherApp",
        "gui": "weather_app_gui.py",
        "cli": "weather_app_cli.py",
        "desc": "Live global weather data with 5-day forecast, hourly preview, Pillow iconography, and IP auto-detect."
    }
]

class ProjectHubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OIBSIP - Python Programming Track Hub (Gokul K.)")
        self.geometry("720x540")
        self.minsize(650, 480)

        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.configure(bg="#0F172A")
        self.style.configure("TFrame", background="#0F172A")
        self.style.configure("Card.TFrame", background="#1E293B")
        self.style.configure("TLabel", background="#0F172A", foreground="#F8FAFC", font=("Segoe UI", 10))
        self.style.configure("Card.TLabel", background="#1E293B", foreground="#F8FAFC", font=("Segoe UI", 10))

    def _build_ui(self):
        # Header
        hdr = ttk.Frame(self, padding=(25, 20, 25, 10))
        hdr.pack(fill=tk.X)

        title = tk.Label(hdr, text="OASIS INFOBYTE · PYTHON PROGRAMMING", font=("Segoe UI", 16, "bold"),
                         bg="#0F172A", fg="#38BDF8")
        title.pack(anchor="w")

        sub = tk.Label(hdr, text="Intern: Gokul K.  |  Offer ID: OIB/R2/IP9900  |  Tasks 2, 3, 4 Completed ✅",
                       font=("Segoe UI", 10), bg="#0F172A", fg="#94A3B8")
        sub.pack(anchor="w", pady=(2, 0))

        # Task Cards Container
        body = ttk.Frame(self, padding=(25, 10, 25, 20))
        body.pack(fill=tk.BOTH, expand=True)

        for task in TASKS:
            card = ttk.Frame(body, style="Card.TFrame", padding=14)
            card.pack(fill=tk.X, pady=8)

            t_header = ttk.Frame(card, style="Card.TFrame")
            t_header.pack(fill=tk.X)

            badge = tk.Label(t_header, text=task["id"], font=("Segoe UI", 9, "bold"),
                             bg="#0284C7", fg="#FFFFFF", padx=8, pady=2)
            badge.pack(side=tk.LEFT, padx=(0, 10))

            t_name = tk.Label(t_header, text=task["name"], font=("Segoe UI", 12, "bold"),
                              bg="#1E293B", fg="#F8FAFC")
            t_name.pack(side=tk.LEFT)

            desc = tk.Label(card, text=task["desc"], font=("Segoe UI", 9),
                            bg="#1E293B", fg="#94A3B8", justify="left")
            desc.pack(anchor="w", pady=(6, 10))

            btn_row = ttk.Frame(card, style="Card.TFrame")
            btn_row.pack(fill=tk.X)

            gui_btn = tk.Button(btn_row, text="Launch GUI App (Advanced)", font=("Segoe UI", 9, "bold"),
                                bg="#2563EB", fg="#FFFFFF", activebackground="#1D4ED8", activeforeground="#FFFFFF",
                                relief="flat", padx=12, pady=5, cursor="hand2",
                                command=lambda t=task: self._launch_gui(t))
            gui_btn.pack(side=tk.LEFT, padx=(0, 8))

            cli_btn = tk.Button(btn_row, text="Launch CLI (Beginner)", font=("Segoe UI", 9),
                                bg="#334155", fg="#F8FAFC", activebackground="#475569", activeforeground="#FFFFFF",
                                relief="flat", padx=10, pady=5, cursor="hand2",
                                command=lambda t=task: self._launch_cli(t))
            cli_btn.pack(side=tk.LEFT)

    def _launch_gui(self, task):
        script = os.path.join(BASE_DIR, "OIBSIP", task["folder"], task["gui"])
        subprocess.Popen([PYTHON_EXE, script])

    def _launch_cli(self, task):
        script = os.path.join(BASE_DIR, "OIBSIP", task["folder"], task["cli"])
        if sys.platform == "win32":
            subprocess.Popen(f'start cmd /k "{PYTHON_EXE}" "{script}"', shell=True)
        else:
            subprocess.Popen([PYTHON_EXE, script])

if __name__ == "__main__":
    app = ProjectHubApp()
    app.mainloop()
