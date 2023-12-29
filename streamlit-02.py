import streamlit as st
import openai

openai.api_key = '26bbea817f7749d88cb0e2d8dbd047aa'
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.azure_endpoint = 'https://labuser11openai.openai.azure.com/'


st.header('Welcome to GPTChatBot', divider='rainbow')
st.write('안녕하세요 GPTChatBot 입니다. 무엇이든 물어보세요')

query = st.text_input('질문을 입력하세요')

button_click = st.button("검색")

if button_click:
    with st.spinner('검색중 입니다.'):
        result = openai.chat.completions.create(
                model='gpt-35-turbo-dev',
                messages=[
                    {'role':'system','content':'You are a helpful assistant.'},
                    {'role':'user','content':query}
                ]
            )
        st.success('done')

    st.write('## 답변')
    st.write(result.choices[0].message.content)

#if query != '':
#    st.write(query + '(이)가 궁금하셨군요')

