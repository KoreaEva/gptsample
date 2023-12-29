import streamlit as st
import openai

# openai model을 연결하기 위한 정보
openai.api_key = '26bbea817f7749d88cb0e2d8dbd047aa'
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.azure_endpoint = 'https://labuser11openai.openai.azure.com/'

st.header('Welcome to 인공지능 시인',divider='rainbow')
st.write('안녕하세요 반갑습니다. 인공지능 시인에 오신것을 환영합니다. ')

name = st.text_input('작가의 이름은?')
if name:
    st.write(name + '님 반갑습니다.')

subject = st.text_input('시의 주제를 입력하세요')

content = st.text_area('시의 내용을 입력하세요')

button_click = st.button('Create')

if button_click:
    with st.spinner('please wait...'):
        result = openai.chat.completions.create(
            model='gpt-35-turbo-dev',
            messages=[
                {'role':'system','content':'You are an artificial intelligence poet'},
                {'role':'user','content':subject + '를 주제로 한글 시를 지어줘'},
                {'role':'user','content':'시인의 이름은 ' + name + ' 이다.'},
                {'role':'user','content':content + '의 내용을 참조해서 시를 지어줘'}
            ]
        )

        st.success('done')

    st.write('## 시')
    st.write(result.choices[0].message.content)