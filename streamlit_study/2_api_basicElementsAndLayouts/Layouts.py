import streamlit as st 
import pandas as pd 
import time 


st.title('Layouts')

side_bar = st.sidebar

side_bar.header('sidebar')
side_bar.write('this it sidebar')

st.write('This is page')

# load df 
df = pd.read_csv('tips.csv')


columns = tuple(df.columns)
st.write(columns)

st.header('Select box')
#  create widget select box 
select_column = side_bar.selectbox(
    'Select the column you wnat to display', 
    columns
)

side_bar.write('You selected the column_name = `{}'.format(select_column) + '`')

st.dataframe( df[[select_column]] , width=500 ) 

st.header('Columns')

col1 , col2, col3 = st.columns(3)
with col1:
    st.subheader('col1')
    st.image('./media/image.jpg')

with col2:
    st.subheader('col2')
    st.dataframe(df)

with col3:
    st.subheader('col3')
    st.dataframe( df[[select_column]]  )

st.header('Expander')

with st.expander('Some Explanation'):
    st.write('''
HTML을 PDF로 변환하는 방법으로 Streamlit 페이지를 PDF로 만들 수 있습니다. 여기에 사용할 수 있는 예시 코드를 보여드리겠습니다:

## code 

```python
import streamlit as st
import pdfkit
import os
from datetime import datetime

def save_streamlit_as_pdf():
    """
    Streamlit 페이지를 PDF로 저장하는 함수
    """
    # PDF 저장 버튼
    if st.button("Save as PDF"):
        # 현재 시간으로 파일명 생성
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"streamlit_page_{timestamp}.pdf"
        
        try:
            # wkhtmltopdf 설정
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Windows
            # Linux/Mac의 경우: config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
            
            # PDF 옵션 설정
            options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None
            }
            
            # 현재 Streamlit 페이지의 URL
            # 로컬호스트 URL (기본 Streamlit 포트 8501 사용)
            url = "http://localhost:8501"
            
            # PDF 생성
            pdfkit.from_url(url, pdf_filename, configuration=config, options=options)
            
            # 생성된 PDF 파일 다운로드 링크 제공
            with open(pdf_filename, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                st.download_button(
                    label="Download PDF",
                    data=PDFbyte,
                    file_name=pdf_filename,
                    mime='application/octet-stream'
                )
            
            # 임시 파일 삭제
            os.remove(pdf_filename)
            
            st.success(f"PDF has been generated successfully!")
            
        except Exception as e:
            st.error(f"Error generating PDF: {str(e)}")

# 메인 Streamlit 앱에서 사용 예시
def main():
    st.title("Streamlit to PDF Example")
    
    # 여기에 PDF로 저장하고 싶은 Streamlit 컨텐츠를 추가
    st.write("This is a sample content that will be saved as PDF")
    
    # PDF 저장 기능 추가
    save_streamlit_as_pdf()

if __name__ == "__main__":
    main()

```

이 코드를 사용하기 위해서는 다음과 같은 준비가 필요합니다:

1. 필요한 라이브러리 설치:
```bash
pip install streamlit pdfkit
```

2. wkhtmltopdf 설치:
   - Windows: https://wkhtmltopdf.org/downloads.html 에서 설치
   - Mac: `brew install wkhtmltopdf`
   - Linux: `sudo apt-get install wkhtmltopdf`

주의사항:
1. 이 코드는 로컬에서 실행 중인 Streamlit 앱을 PDF로 변환합니다.
2. wkhtmltopdf의 경로는 운영체제에 따라 다르므로 적절히 수정해야 합니다.
3. 스타일링이나 인터랙티브 요소는 PDF에서 제대로 표현되지 않을 수 있습니다.

추가로 필요한 기능이나 수정하고 싶은 부분이 있으시다면 말씀해 주세요!
''')

