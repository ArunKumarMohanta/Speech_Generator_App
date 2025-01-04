import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from plyer import filechooser
from plyer import notification
from gtts import gTTS
import datetime
import requests
from kivy.utils import platform


class SpeechGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(SpeechGenerator, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Text input for user to enter speech text
        self.text_input = TextInput(
            hint_text='Enter your text here',
            font_size=20,
            size_hint=(1, 0.6)
        )
        self.add_widget(self.text_input)

        # Box for Save and Play buttons
        button_box_top = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        # Save button
        save_button = Button(text='Save Speech as MP3', font_size=18)
        save_button.bind(on_press=self.save_mp3)
        button_box_top.add_widget(save_button)

        # Play button
        self.play_button = Button(text='Play Speech', font_size=18, disabled=True)  # Initially disabled
        self.play_button.bind(on_press=self.play_mp3)
        button_box_top.add_widget(self.play_button)

        self.add_widget(button_box_top)

        # Box for Clear and Pause buttons
        button_box_bottom = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        # Clear button
        clear_button = Button(text="Clear Text", font_size=18)
        clear_button.bind(on_press=self.clear_text)
        button_box_bottom.add_widget(clear_button)

        # Pause button
        self.pause_button = Button(text="Pause/Resume", font_size=18, disabled=True)  # Initially disabled
        self.pause_button.bind(on_press=self.pause_resume_mp3)
        button_box_bottom.add_widget(self.pause_button)

        self.add_widget(button_box_bottom)

        # Variable to store the latest generated file path
        self.last_file_path = None
        self.current_sound = None  # Variable to manage the audio object

        # Determine storage folder
        if platform == 'android':
            from android.storage import primary_external_storage_path
            self.speeches_folder = primary_external_storage_path() + '/Download/speeches'
        else:
            self.speeches_folder = os.path.expanduser("~") + '/speeches'

        if not os.path.exists(self.speeches_folder):
            os.makedirs(self.speeches_folder)

    def check_internet(self):
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def save_mp3(self, instance):
        text = self.text_input.text
        if not text.strip():
            self.show_popup('Error', 'Please enter some text')
            return

        if not self.check_internet():
            self.show_popup('Error', 'Internet connection is required for TTS')
            return

        # Generate a filename with timestamp
        filename = f"speech_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        file_path = os.path.join(self.speeches_folder, filename)

        # Generate and save the speech
        try:
            speech = gTTS(text=text, lang='en', slow=False)
            speech.save(file_path)

            # Update the last file path and enable the play and pause buttons
            self.last_file_path = file_path
            self.play_button.disabled = False
            self.pause_button.disabled = False

            # Notify user of success
            self.show_notification("Speech Saved", f"MP3 saved at {file_path}")
        except Exception as e:
            self.show_popup('Error', f'Failed to save MP3: {str(e)}')

    def play_mp3(self, instance):
        if self.last_file_path and os.path.exists(self.last_file_path):
            self.current_sound = SoundLoader.load(self.last_file_path)
            if self.current_sound:
                self.current_sound.play()
            else:
                self.show_popup('Error', 'Failed to play MP3 file.')
        else:
            self.show_popup('Error', 'No file available to play.')

    def pause_resume_mp3(self, instance):
        if self.current_sound:
            if self.current_sound.state == 'play':  # If currently playing
                self.current_sound.stop()  # Pause by stopping (since kivy SoundLoader has no direct pause)
            elif self.current_sound.state == 'stop':  # If paused
                self.current_sound.play()  # Resume by playing again

    def clear_text(self, instance):
        self.text_input.text = ''

    def show_popup(self, title, message):
        # Calculate width dynamically based on the length of the message
        popup_width = max(400, len(message) * 7)  # Each character is roughly 7 pixels wide
        Popup(
            title=title,
            content=Label(text=message, text_size=(popup_width * 0.9, None)),
            size_hint=(None, None),
            size=(popup_width, 150)
        ).open()

    def show_notification(self, title, message):
        if platform == 'android':
            notification.notify(title=title, message=message)
        else:
            self.show_popup(title, message)


class SpeechApp(App):
    def build(self):
        return SpeechGenerator()


if __name__ == '__main__':
    SpeechApp().run()
