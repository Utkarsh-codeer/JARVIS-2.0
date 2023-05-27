import speech_recognition as sr
import openai
import subprocess

# Set up OpenAI API credentials
openai.api_key = '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'

# Function to recognize speech input
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError as e:
        print("Speech recognition service error:", str(e))
        return ""

# Function to send message to OpenAI GPT-3 and get the response
def chat_with_gpt3(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Mapping of application names to executable file paths
# Mapping of application names to executable file paths
# Mapping of application names to executable file paths
app_mapping = {
    "notepad": r"C:\Windows\System32\notepad.exe",
    "paint": r"C:\Windows\System32\mspaint.exe",
    "calculator": r"C:\Windows\System32\calc.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "spotify": r"C:\Users\YourUsername\AppData\Roaming\Spotify\Spotify.exe",
    "vscode": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "audacity": r"C:\Program Files\Audacity\audacity.exe",
    "blender": r"C:\Program Files\Blender Foundation\Blender 3.4\blender.exe",
    "kali linux": r"C:\Users\Radhika lakhotia\OneDrive\Desktop\Kali Linux.Ink",
    "terminal": r"C:\Users\Radhika lakhotia\OneDrive\Desktop\Terminal.lnk",
    "this pc": r"C:\Users\Radhika lakhotia\OneDrive\Desktop\This Pc",
    "virtual box": r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe",
    "downloads": r"D:\Downloads",
    "photoshop": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 2023.lnk",
    "discord": r"C:\Users\Radhika lakhotia\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.exe"
    # Add more mappings as needed
    # Add or Edit them as your system
    
}
 
# Function to handle commands
def handle_command(command):
    if "open" in command:
        app = command.split("open")[1].strip().lower()
        if app in app_mapping:
            try:
                subprocess.Popen(app_mapping[app])
                return f"Opening {app}"
            except FileNotFoundError:
                return f"Sorry, I couldn't find the application {app}."
        else:
            return f"Sorry, I don't know how to open {app}."
    else:
        return chat_with_gpt3([
            {"role": "system", "content": "You are a user."},
            {"role": "user", "content": command}
        ])

# Main loop
while True:
    user_input = recognize_speech()
    if user_input.lower() == "exit":
        break
    response = handle_command(user_input)
    print("AI:", response)
