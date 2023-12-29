import streamlit as st
import openai

# openai model을 연결하기 위한 정보
openai.api_key = '26bbea817f7749d88cb0e2d8dbd047aa'
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.azure_endpoint = 'https://labuser11openai.openai.azure.com/'

st.header('Welcome to 이력서 생성기',divider='rainbow')
st.write('안녕하세요 반갑습니다. 이력서 생성 서비스 오신것을 환영합니다. ')

name = st.text_input('당신의 이름을 입력해주세요?')
if name:
    st.write(name + '님 반갑습니다.')

job = st.selectbox('지원하려는 분야를 선택하세요',
                       ('회사원','소프트웨어 개발자','군인','공무원','시나리오 작가'))

contact = st.text_area('본인의 연락처를 입력하세요(전화번호, 이메일 등등)')

content = st.text_area('본인의 이력을 입력하세요')

button_click = st.button('Create')

if button_click:
    with st.spinner('please wait...'):
        result = openai.chat.completions.create(
            temperature=1.5,
            model='gpt-35-turbo-dev',
            messages=[
                {'role':'system','content':'You are a helpful assistant.'},
                {'role':'user','content': '내 이름은 ' + name},
                {'role':'user','content': job + ' 업종에 지원하기 위해서 이력서를 쓰고 있다.'},
                {'role':'user','content': '내 연락처 정보는 ' + contact + '이다. 이력서에 포함시켜줘' },
                {'role':'user','content': '상세내용은 ' + content + '이다'},
                {'role':'user','content': '위 내용을 참조해서 이력서를 생성해줘'}
            ]
        )

        st.success('done')

    st.write('## 이력서')
    st.write(result.choices[0].message.content)