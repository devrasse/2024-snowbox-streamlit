import streamlit as st

st.set_page_config(layout='wide')
# HTML 파일을 읽어오기
with open("2024_snowbox.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

st.markdown('<div class="centered"><h1 style="text-align:center;">2024년 미추홀구 제설함</h1></div>', unsafe_allow_html=True)

with st.container(border=True,height=740):
    # Stremlit 앱에 HTML 표시
    st.components.v1.html(html_code,  height=700, scrolling=False)

#st.write("참고: 정확한 진료 확인은 방문전 연락하여 확인하여 주시기 바랍니다.")
styled_text = '<p style="font-size: 20px; color: white;">참고: 제설제 관련 문의는 각 동행정복지센터로 연락바랍니다.</p>'
st.write(styled_text, unsafe_allow_html=True)