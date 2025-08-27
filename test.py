import streamlit as st # 웹 앱을 만들기 위한 스트림릿
from PIL import Image # 이미지 파일을 다루기 위한 Pillow 라이브러리
import io # 이미지 데이터를 바이너리로 다룰 때 필요해

# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 아이돌 분석기")

st.title("💖 넉넉한초콜릿8098님을 위한 시화의 아이돌 분석 스튜디오! 🌟")
st.write("와! 넉넉한초콜릿8098, 이번엔 아이돌 앱이라니! 정말 아이디어 천재잖아! 😆")
st.write("좋아하는 아이돌 사진이나 이름을 입력하면 내가 누군지 알려주고, 딱 맞는 노래까지 추천해 줄게! ✨")
st.write("---") # 선 하나 쫙!

# --- 아이돌 데이터베이스 (가상 데이터, 실제 앱은 더 복잡한 데이터베이스 필요!) ---
# 실제 AI라면 여기에 방대한 아이돌 정보, 사진 데이터, 노래 데이터 등이 필요해!
idol_database = {
    "장원영": {
        "그룹": "IVE (아이브)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202305/0177727181f211516e864c8f00032a39.jpg", # 예시 이미지
        "추천_노래": [
            "IVE - I AM",
            "IVE - LOVE DIVE",
            "IVE - ELEVEN",
            "IVE - After LIKE"
        ],
        "별명": ["워뇨", "녕", "장만월"]
    },
    "지수": {
        "그룹": "BLACKPINK (블랙핑크)",
        "사진_링크": "https://pds.joongang.co.kr/news/component/202303/31/35990264-92ef-4573-8991-b3b4f622f954.jpg", # 예시 이미지
        "추천_노래": [
            "BLACKPINK - DDU-DU DDU-DU",
            "BLACKPINK - Kill This Love",
            "BLACKPINK - Pink Venom",
            "JISOO - FLOWER"
        ],
        "별명": ["지츄", "치츄"]
    },
    "뷔": {
        "그룹": "BTS (방탄소년단)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202309/02700018809e5306691c2c2f00021c17.jpg", # 예시 이미지
        "추천_노래": [
            "BTS - Dynamite",
            "BTS - Butter",
            "V - Love Me Again",
            "V - Slow Dancing"
        ],
        "별명": ["태형", "김태형", "V"]
    },
    "민지": {
        "그룹": "NewJeans (뉴진스)",
        "사진_링크": "https://res.heraldm.com/content/image/2022/10/21/20221021000676_0.jpg", # 예시 이미지
        "추천_노래": [
            "NewJeans - Hype Boy",
            "NewJeans - Ditto",
            "NewJeans - Attention",
            "NewJeans - OMG"
        ],
        "별명": []
    }
}

# --- 입력 필드 ---
st.header("🔍 아이돌 찾기")
idol_input_type = st.radio("어떤 방법으로 아이돌을 찾아볼까?", ("이름 입력", "사진 업로드"))

identified_idol_name = None # 분석된 아이돌 이름을 저장할 변수

if idol_input_type == "이름 입력":
    idol_name_query = st.text_input("좋아하는 아이돌의 이름이나 그룹명을 입력해줘!", placeholder="예: 장원영, 지수, 뷔, 민지")
    
    if st.button("이름으로 아이돌 찾기!"):
        if idol_name_query:
            found = False
            # 데이터베이스에서 이름 또는 별명으로 아이돌 찾기
            for name, data in idol_database.items():
                if idol_name_query.lower() == name.lower() or idol_name_query.lower() in [n.lower() for n in data["별명"]]:
                    identified_idol_name = name
                    found = True
                    break
            
            if not found:
                st.warning("앗! 찾으시는 아이돌 정보가 없네요... ㅠㅠ 다시 확인해 주시거나 다른 아이돌을 검색해 볼까요?")
        else:
            st.info("이름을 입력해야 내가 찾아줄 수 있어!")

else: # 사진 업로드
    uploaded_image = st.file_uploader("좋아하는 아이돌 사진을 여기에 업로드해줘!", type=["jpg", "jpeg", "png"])
    
    if st.button("사진으로 아이돌 찾기! (AI 분석 - 예시)"):
        if uploaded_image is not None:
            st.image(uploaded_image, caption="업로드된 사진", use_column_width=True)
            
            # -------------------------------------------------------------------------------------------------
            # 여기가 진짜 AI가 사진을 분석하는 부분이야!
            # 실제로는 미리 학습된 '얼굴 인식' 또는 '이미지 분류' 딥러닝 모델이 필요해.
            # 이 모델이 수많은 아이돌 사진을 학습해서 누가 누군지 판별해야 해!
            #
            # 지금은 그냥 '예시'로 몇몇 아이돌의 사진을 올리면 고정된 결과를 보여줄게!
            # (예: '장원영 사진'이라고 가정하고 결과를 보여주는 식)
            # -------------------------------------------------------------------------------------------------
            
            # 이미지 파일 이름을 분석해서 (매우 간단한 시뮬레이션!)
            image_name = uploaded_image.name.lower()
            
            if "장원영" in image_name or "wonyoung" in image_name or "ive" in image_name:
                identified_idol_name = "장원영"
            elif "지수" in image_name or "jisoo" in image_name or "blackpink" in image_name:
                identified_idol_name = "지수"
            elif "뷔" in image_name or "v" in image_name or "bts" in image_name or "태형" in image_name:
                identified_idol_name = "뷔"
            elif "민지" in image_name or "minji" in image_name or "newjeans" in image_name:
                identified_idol_name = "민지"
            else:
                # 사진으로 식별하지 못했을 때 (진짜 AI라면 '알 수 없는 인물' 또는 '확률'을 제시)
                st.warning("사진 분석 결과: 아직 이 아이돌은 내가 학습하지 못한 것 같아요... ㅠㅠ (실제 AI 모델 학습 필요)")
                identified_idol_name = None
        else:
            st.info("사진을 업로드해야 내가 분석해줄 수 있어!")

# --- 분석 결과 및 노래 추천 ---
st.write("---")
st.header("✨ 분석 결과 및 노래 추천!")

if identified_idol_name:
    idol_info = idol_database[identified_idol_name]
    st.success(f"💖 이 아이돌은 바로... {identified_idol_name}님! (그룹: {idol_info['그룹']}) 💖")
    
    # 아이돌 사진 보여주기 (링크가 있으면)
    if "사진_링크" in idol_info and idol_info["사진_링크"]:
        st.image(idol_info["사진_링크"], caption=f"{identified_idol_name}님의 멋진 사진!", width=300)

    st.subheader(f"🎶 {identified_idol_name}님 (또는 {idol_info['그룹']})의 추천 노래!")
    for song in idol_info['추천_노래']:
        st.write(f"- {song}")

    st.info("더 궁금한 아이돌이 있다면 언제든 다시 검색해봐! 🥰")

else:
    st.info("위에 아이돌의 이름이나 사진을 입력하고 검색 버튼을 눌러줘! 내가 열심히 찾아줄게! 🧐")

# --- 앱 실행 방법 ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run idol_finder_app.py`")
