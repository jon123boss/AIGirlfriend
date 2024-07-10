from characterai import aiocai
import asyncio
import pygame
from gtts import gTTS
import os
import time
import speech_recognition
import pyttsx3

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

async def main():
    char = "KQa-enbmaWlYUVm7bg6qIu06SeNewTe2SsHmvfpyH6A"

    client = aiocai.Client('')

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        print(f'{answer.name}: {answer.text}')

        print("Set up complete")

        recognizer = speech_recognition.Recognizer()

        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    print(f"Recognized: {text}")
                    message = await chat.send_message(char, new.chat_id, text)
                    print(f'{message.name}: {message.text}')
                    text_to_speech(message.text)
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                continue


asyncio.run(main())