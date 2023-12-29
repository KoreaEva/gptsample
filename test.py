import openai

openai.api_key = '26bbea817f7749d88cb0e2d8dbd047aa'
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.azure_endpoint = 'https://labuser11openai.openai.azure.com/'

question = input("What's your question : ")

result = openai.chat.completions.create(
            model='gpt-35-turbo-dev',
            messages=[
                {'role':'system','content':'You are a helpful assistant.'},
                {'role':'user','content':question}
            ]
        )

print(result.choices[0].message.content)