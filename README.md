# Python Keystroke Logger

A simple, **Educational keylogger** written in **Python**. This script captures keyboard inputs and saves them to a local log file with timestamps.

---

## ⚠️ Ethical Warning & Disclaimer ⚠️

This project was created for **Educational Purposes** only, to help my cybersecurity career advance and to understand the mechanics of keylogging software for defensive and offensive purposes.

Using a keylogger on any computer you do not own or **NOT** having explicit, **written permission** to monitor is **illegal** and **highly unethical**. Unauthorized surveillance is a serious invasion of privacy and is **punishable by law** in many countries. I am **NOT** be responsible for any malicious or illegal use of this code. This to complete the Fourth Task of my Cyber Security Internship at Codecraft Info Tech, which I was asked to upload on github.

By using this code, you **agree** to do so in a **legal** and **ethical manner**.

---

## 📋 Table of Contents

    - Features
    - How It Works
    - Prerequisites
    - Installation & Usage
    - Log File Format
    - Future Improvements

---

## ✨ Features

    - **Keystroke Logging**: Captures both alphanumeric characters and special keys (e.g., [SHIFT], [ENTER], [SPACE]).
    - **Word Buffering**: Groups individual characters into words and logs them when a space or enter is pressed, making the log file more readable.
    - **Timestamping**: Each logged entry is timestamped (YYYY-MM-DD HH:MM:SS,ms).
    - **Local File Storage**: Saves all captured keystrokes to a local file named key_log.txt.
    - **Clean Exit**: The logger can be stopped safely by pressing the Shift + S key combination.

---

## ⚙️ How It Works

The script uses the ```pynput``` library to listen for global keyboard events (key presses and releases).

    - A ```Listener``` is set up to monitor all keyboard activity.
    - The on_press function is called every time a key is pressed.
    - The script stores typed characters in a temporary buffer.
    - When the user presses Space or Enter, the content of the buffer is written to key_log.txt as a single entry. This makes the log easier to read than logging every single character individually.
    - Special keys like Shift, Ctrl, and Backspace are logged with special tags (e.g., [SHIFT]).
    - The on_release function helps manage the set of currently pressed keys, which is used for the stop-key combination.
    - The script terminates when the Shift + S combination is detected.
