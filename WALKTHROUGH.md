# Oasis Infobyte (OIBSIP) Python Internship — Tasks 2, 3 & 4 Walkthrough

**Intern Name:** Gokul K.  
**Offer Letter ID:** OIB/R2/IP9900  
**Track:** Python Programming  
**Status:** All 3 Assigned Tasks Completed (Beginner Tier + Advanced Tier) ✅  

---

## 📁 Submission Repository Structure

All project files are organized inside `c:\Users\acer\OneDrive\Desktop\OASIS\` following the strict Oasis Infobyte naming convention:

```text
OASIS/
├── run_all_hub.py                                # 🚀 Unified Graphical Project Hub & Launcher
├── run_task2.py                                  # Direct Launcher for Task 2 GUI
├── run_task3.py                                  # Direct Launcher for Task 3 GUI
├── run_task4.py                                  # Direct Launcher for Task 4 GUI
├── requirements.txt                              # Root environment dependencies
│
└── OIBSIP/                                       # 📂 Primary Repository Folder for GitHub
    ├── README.md                                 # Master Repository Readme & Video Guidelines
    ├── requirements.txt                          # Full dependency specification
    │
    ├── Python-Task2-BMICalculator/
    │   ├── bmi_calculator_gui.py                 # Advanced Tier: Tkinter GUI + SQLite + Matplotlib Trend
    │   ├── bmi_calculator_cli.py                 # Beginner Tier: Interactive CLI Calculator
    │   ├── bmi_records.db                        # SQLite Database with multi-user records
    │   ├── requirements.txt                      # Task 2 requirements
    │   └── README.md                             # Task 2 documentation & feature checklist
    │
    ├── Python-Task3-PasswordGenerator/
    │   ├── password_generator_gui.py             # Advanced Tier: Tkinter GUI + Secrets + Strength Meter
    │   ├── password_generator_cli.py             # Beginner Tier: Interactive CLI Generator
    │   ├── requirements.txt                      # Task 3 requirements
    │   └── README.md                             # Task 3 documentation & security analysis
    │
    └── Python-Task4-WeatherApp/
        ├── weather_app_gui.py                    # Advanced Tier: Tkinter GUI + 5-Day Forecast + IP Geolocation
        ├── weather_app_cli.py                    # Beginner Tier: Interactive CLI Weather Fetcher
        ├── requirements.txt                      # Task 4 requirements
        └── README.md                             # Task 4 documentation & privacy disclosures
```

---

## 🚀 Interactive Project Hub (`run_all_hub.py`)

A centralized, dark-themed GUI control panel was created at the root of `OASIS`. It allows you to preview, demo, and launch any of the 3 tasks (both GUI and CLI modes) with a single click.

```powershell
python run_all_hub.py
```

---

## 🔍 Task Deep-Dive & Implemented Features

### Task 2: BMI Calculator (`Python-Task2-BMICalculator`)

- **Objective:** Calculate Body Mass Index ($BMI = weight / height^2$) and categorize according to WHO standards.
- **Beginner Tier (`bmi_calculator_cli.py`):**
  - Interactive terminal prompts for weight (kg) and height (m or cm).
  - Categorizes into: *Underweight (< 18.5)*, *Normal (18.5–24.9)*, *Overweight (25–29.9)*, and *Obese ($\ge 30$)*.
  - Formatted output rounded to 2 decimal places with personalized health tips.
  - Input validation rejecting negative numbers, zero, or non-numeric strings.
- **Advanced Tier (`bmi_calculator_gui.py`):**
  - Built with `tkinter` and styled `ttk` widgets.
  - Supports both **Metric (kg, cm)** and **Imperial (lbs, ft/in)** inputs.
  - **Dynamic color feedback banner:** Blue (Underweight), Green (Normal), Amber (Overweight), Red (Obese).
  - **Multi-user profile support:** Create, switch, and delete user profiles.
  - **Data Persistence:** SQLite database (`bmi_records.db`) storing historical records with timestamps.
  - **Embedded Matplotlib Trend Chart:** Interactive line chart showing the user's BMI trajectory over time against healthy reference bands.
  - **Records Table:** Treeview table displaying past records with record deletion capability.

---

### Task 3: Random Password Generator (`Python-Task3-PasswordGenerator`)

- **Objective:** Generate cryptographically secure, randomized passwords based on user-defined criteria.
- **Beginner Tier (`password_generator_cli.py`):**
  - Minimum 8-character length enforcement.
  - Prompts for uppercase, lowercase, numbers, and symbols (minimum 2 types enforced).
  - Guaranteed inclusion of at least one character from each chosen pool.
  - Continuous loop without restarting.
- **Advanced Tier (`password_generator_gui.py`):**
  - Powered by Python's **`secrets`** module (Cryptographically Secure Pseudo-Random Number Generator).
  - Interactive slider and synchronized spinbox for lengths 8 to 64.
  - Checkboxes for uppercase, lowercase, digits, and symbols.
  - **Exclude ambiguous characters toggle:** Filters out `0, O, o, 1, l, I, |`.
  - **Live Password Strength Meter:** Visual colored bar and bit-entropy calculations (*Weak*, *Medium*, *Strong*, *Very Strong*).
  - **Clipboard Integration:** One-click copy and automatic copy toggle using `pyperclip` (with Tkinter fallback).
  - **Session History:** Keeps the last 5 generated passwords visible in-memory (never persisted to disk for security).

---

### Task 4: Basic Weather App (`Python-Task4-WeatherApp`)

- **Objective:** Fetch and display live weather conditions and multi-day forecasts for any city or ZIP code.
- **Beginner Tier (`weather_app_cli.py`):**
  - Queries OpenWeatherMap / Open-Meteo APIs.
  - Displays temperature in both °C and °F, humidity, wind speed, pressure, and descriptions.
  - Error handling for invalid cities, timeouts, and missing API keys.
- **Advanced Tier (`weather_app_gui.py`):**
  - Modern dashboard showing city name, date, time, large temperature badge, and conditions.
  - **Weather Iconography:** Uses Pillow to render weather icons with automatic offline fallbacks.
  - **Hourly Forecast:** Shows conditions and temperatures for the next 6 to 12 hours.
  - **5-Day Daily Forecast:** Clean forecast cards with dates, condition summaries, and icons.
  - **Unit Toggle:** Instant switch between Celsius (°C) and Fahrenheit (°F).
  - **Auto-Location Detection:** Automatically detects location via IP on launch using `ipinfo.io` (free tier).
  - **Demo Data Mode:** Built-in "🌟 Demo Data" button to showcase full forecasts even without an internet connection or API key.
  - **API Key Settings:** Modal dialog to enter and save custom OpenWeatherMap API keys.
  - **Asynchronous Threading:** Prevents GUI freezing during network calls.

---

## 🎥 Video Demonstration & LinkedIn Checklist

Per Section 1.2 and 1.3 of the Oasis Infobyte rules:

1. **Title Card (First 2 Seconds of Video):**
   Show a static frame or overlay with:
   - **Full Name:** Gokul K.
   - **Assigned Track:** Python Programming
   - **Task Titles:** Task 2 (BMI Calculator), Task 3 (Password Generator), Task 4 (Weather App)
   - **Cohort / Internship:** Oasis Infobyte SIP (OIBSIP)
2. **Video Walkthrough:**
   - Record screen running `run_all_hub.py` or each GUI application.
   - Show end-to-end functionality (calculating BMI, generating passwords, fetching weather).
3. **LinkedIn Post:**
   - Tag **Oasis Infobyte**.
   - Mandatory Hashtag: `#oasisinfobyte`.
   - Domain Hashtags: `#python #pythonprogramming #internship #datascience #softwaredevelopment #oibsip`.
4. **Peer Evaluation:**
   - Leave substantive comments on at least 2 other interns' LinkedIn demo videos.
