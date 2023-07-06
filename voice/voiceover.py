import pyttsx3

voice = pyttsx3.init()
voice.setProperty("rate", 110)
voice.setProperty("volume", 1)
voice.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")


def vocalize(word):
    voice.say(f"{word}")
    voice.runAndWait()
