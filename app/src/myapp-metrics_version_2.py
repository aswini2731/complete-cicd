import subprocess
import platform

def open_calculator():
    system = platform.system()
    
    try:
        if system == "Windows":
            # Opens the Windows Calculator app
            subprocess.Popen("calc.exe")
        elif system == "Darwin":  # Darwin is the system name for macOS
            # Opens the macOS Calculator app
            subprocess.Popen(["open", "-a", "Calculator"])
        elif system == "Linux":
            # Linux has different calculators depending on the version (distro)
            # This tries common ones like gnome-calculator or xcalc
            calculators = ["gnome-calculator", "kcalc", "xcalc", "galculator"]
            for calc in calculators:
                try:
                    subprocess.Popen(calc)
                    break
                except FileNotFoundError:
                    continue
        print(f"Success: Calculator opened on {system}.")
    except Exception as e:
        print(f"Error: Could not open calculator. {e}")

if __name__ == "__main__":
    open_calculator()
