from characterai import aiocai
import asyncio
import pygame
from gtts import gTTS

tts = gTTS('hello', lang='en')
tts.save('hello.mp3')
# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load('hello.mp3')

# Play the audio file
pygame.mixer.music.play()

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

            message = await chat.send_message(
                char, new.chat_id, text
            )

            print(f'{message.name}: {message.text}')


asyncio.run(main())