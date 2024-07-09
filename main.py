from characterai import aiocai
import asyncio
async def main():
    char = "aLwp_WfJDB9N46gMbvM8pM1682BaKw6BD5ibS-9KZoc"

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