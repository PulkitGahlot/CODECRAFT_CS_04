# Python Keystroke Logger

A simple, **Educational keylogger** written in **Python**. This script captures keyboard inputs and saves them to a local log file with timestamps.

---

## ⚠️ Ethical Warning & Disclaimer ⚠️

This project was created for **Educational Purposes** only, to help my cybersecurity career advance and to understand the mechanics of keylogging software for defensive and offensive purposes.

Using a keylogger on any computer you do not own or **NOT** having explicit, **written permission** to monitor is **illegal** and **highly unethical**. Unauthorized surveillance is a serious invasion of privacy and is **punishable by law** in many countries. I am **NOT** responsible for any malicious or illegal use of this code. This to complete the Fourth Task of my Cyber Security Internship at Codecraft Info Tech, which I was asked to upload on github.

By using this code, you **agree** to do so in a **legal** and **ethical manner**.

---

## 📋 Table of Contents

- [Features](#-features)
- How It Works
- Prerequisites
- Installation & Usage
- Log File Format

---

## ✨ Features

- **Keystroke Logging**: Captures both alphanumeric characters and special keys (e.g., [SHIFT], [ENTER], [SPACE]).
- **Word Buffering**: Groups individual characters into words and logs them when a space or enter is pressed, making the log file more readable.
- **Timestamping**: Each logged entry is timestamped (YYYY-MM-DD HH:MM:SS,ms).
- **Local File Storage**: Saves all captured keystrokes to a local file named key_log.txt.
- **Clean Exit**: The logger can be stopped safely by pressing the ```Shift + S``` key combination.

---

## ⚙️ How It Works

The script uses the ```pynput``` library to listen for global keyboard events (key presses and releases).

- A ```Listener``` is set up to monitor all keyboard activity.
- The ```on_press``` function is called every time a key is pressed.
- The script stores typed characters in a temporary buffer.
- When the user presses Space or Enter, the content of the buffer is written to ```key_log.txt``` as a single entry. This makes the log easier to read than logging every single character individually.
- Special keys like ```Shift```, ```Ctrl```, and ```Backspace``` are logged with special tags (e.g., [SHIFT]).
- The ```on_release``` function helps manage the set of currently pressed keys, which is used for the stop-key combination.
- The script terminates when the ```Shift + S``` combination is detected.

---

## 📦 Prerequisites

- Python 3.x
- ```pynput``` Library

---

## 🚀 Installation & Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/PulkitGahlot/CODECRAFT_CS_04.git
   cd CODECRAFT_CS_04
   ```
2. Create an isolated Python Virtual Environment ( Recommended ).
   ```sh
   python -m venv keylogger
   ```
   and activate it with:
   ```sh
   ./keylogger/Scripts/activate
   ```
3. Install the required library:
   ```sh
   pip install pynput
   ```
4. Run the script:
   ```sh
   python keylogger.py
   ```
5. Operation:
   - The terminal will display a "Keylogger Started" message.
   - The script will now run in the background, capturing all keystrokes.
   - All captured data will be saved to ```key_log.txt``` in the same directory.
   - To stop the keylogger, press ```Shift + S```.
  
---

## 📄 Log File Format

The ```key_log.txt``` file contains the captured data. Each entry is on a new line and follows this format:
```YYYY-MM-DD HH:MM:SS,ms: [LOGGED_DATA]```

Example from ```key_log.txt```:
    ```
    2025-07-19 19:30:40,487: This
    2025-07-19 19:30:40,488: [SPACE]
    2025-07-19 19:30:40,847: is
    2025-07-19 19:30:40,848: [SPACE]
    2025-07-19 19:30:41,187: a
    2025-07-19 19:30:41,187: [SPACE]
    2025-07-19 19:30:43,976: test
    2025-07-19 19:30:46,064: [ENTER]
    ```

---

## 👨‍💻 Author

Hi, I'm **Pulkit Gahlot**, a cyber security enthusiast and passionate to be an ethical hacker.

“A good hacker is the one who breaks systems, to build secure ones.”

Feel Free to connect!
- **Linkedin**: [Pulkit Gahlot](https://linkedin.com/in/pulkit-gahlot)
- **X**: [Pulkit_Gahlot_](https://x.com/Pulkit_Gahlot_)
- **GitHub**: [PulkitGahlot](https://github.com/PulkitGahlot)
- **E-Mail**: [pulkitgahlot85@gmail.com](pulkitgahlot85@gmail.com)

Thank you for visiting my GitHub page!
