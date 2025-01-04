# Speech Generator App

## Overview
The Speech Generator App is a Python-based application that allows users to:

- Convert text to speech and save it as an MP3 file.
- Play the generated speech directly from the app.
- Pause or resume the playback of speech files.
- Clear text input for easy reuse.
- Save MP3 files in a dedicated folder for easy access.

This app is designed to work on multiple platforms and provides a user-friendly interface built with **Kivy**.

## Features
- **Text-to-Speech Conversion**: Uses the `gTTS` library to generate speech from user-provided text.
- **Save and Play MP3**: Save the generated speech as an MP3 file and play it directly from the app.
- **Clear Input**: Easily clear the input text field for new text entries.
- **Pause/Resume Playback**: Pause or resume playback of speech files.
- **File Management**: Automatically organizes saved MP3 files in a dedicated folder.
- **Cross-Platform Notifications**: Displays success and error messages using popups or native notifications.

## How to Use
1. Launch the app.
2. Enter the text you want to convert to speech in the input box.
3. Click **Save Speech as MP3** to generate and save the speech file.
4. Use the **Play Speech** button to play the generated file.
5. Use the **Pause/Resume** button to pause or resume playback.
6. Use the **Clear Text** button to clear the input field for new entries.

## APK for Android
The app has been converted into an APK using **Buildozer**. You can try the app on your Android device by downloading the APK file available in this repository:

[Download the APK](./SpeechGeneratorApp.apk)

## Dependencies
This project uses the following Python libraries:

- `kivy`: For building the graphical user interface.
- `gTTS`: For generating speech from text.
- `plyer`: For file chooser and notifications.
- `requests`: For checking internet connectivity.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SpeechGeneratorApp.git
   cd SpeechGeneratorApp
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python main.py
   ```

## Notes
- The app requires an active internet connection to generate speech using the `gTTS` library.
- MP3 files are saved in the `speeches` folder inside the user's home directory (on Android, they are saved in the `Download/speeches` directory).

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
Feel free to try the APK or modify the source code for your own use. If you encounter any issues or have suggestions for improvement, please create an issue in the repository!

