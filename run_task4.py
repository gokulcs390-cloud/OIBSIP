import os
import sys
import subprocess

script_path = os.path.join(os.path.dirname(__file__), "OIBSIP", "Python-Task4-WeatherApp", "weather_app_gui.py")
subprocess.run([sys.executable, script_path])
