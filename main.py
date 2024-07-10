from characterai import aiocai
import asyncio
import pygame
from gtts import gTTS
import os
import time
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile('path_to_audio_file.wav')

with audio_file as source:
    # Adjust for ambient noise and record the audio
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Web Speech could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech; {0}".format(e))

def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Save the audio file
    filename = "temp_audio.mp3"
    tts.save(filename)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(filename)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Stop the mixer
    pygame.mixer.quit()

    # Delete the temporary audio file
    os.remove(filename)
    print(f"Deleted temporary file: {filename}")

async def main():
    char = "EEI6sjnddRIJTVC59MODiYjL0-JyDIVI2IEGLkPx2Jk"

    client = aiocai.Client('c3090b0e969ff9aa484638c40ca6459145223959')

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        print(f'{answer.name}: {answer.text}')

        while True:
            text = input('YOU: ')
            while text == "repeat":
                text_to_speech(message.text)
                text = input('YOU: ')


            message = await chat.send_message(char, new.chat_id, text)

            print(f'{message.name}: {message.text}')
            text_to_speech(message.text)


asyncio.run(main())