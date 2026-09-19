import os
import sys
import subprocess

script_path = os.path.join(os.path.dirname(__file__), "OIBSIP", "Python-Task3-PasswordGenerator", "password_generator_gui.py")
subprocess.run([sys.executable, script_path])
