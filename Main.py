import streamlit as st

# 💖 페이지 설정은 시작부터 화려하게! 🌈
st.set_page_config(
    page_title="✨MBTI 미래 탐험대! 직업 추천 프로젝트!🌟",
    page_icon="🚀", # 앱 아이콘도 귀엽게!
    layout="wide", # 넓은 화면으로 시원하게!
    initial_sidebar_state="expanded" # 사이드바도 열어둘까?
)

# 🎨 눈이 즐거운 CSS 스타일링 추가! (직접 색깔 커스텀 가능해!)
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff; /* 연한 하늘색 배경! 넘 예쁘지? 🌸 */
        padding: 20px;
    }
    .st-emotion-cache-p5mcoo-stButton>button {
        background-color: #ff69b4; /* 버튼도 핑크핑크하게! 🎀 */
        color: white;
        font-weight: bold;
        border-radius: 15px;
        padding: 10px 20px;
        font-size: 1.1em;
        transition: transform 0.2s;
    }
    .st-emotion-cache-p5mcoo-stButton>button:hover {
        transform: scale(1.05); /* 버튼에 마우스 올리면 살짝 커지는 효과! 💫 */
        background-color: #ff1493;
    }
    .st-emotion-cache-1g83s2l { /* selectbox 라벨 */
        font-size: 1.2em;
        font-weight: bold;
        color: #8a2be2; /* 보라색으로 띠용! 💜 */
    }
    .st-emotion-cache-nahz7x { /* selectbox 선택된 값 */
        font-size: 1.1em;
        color: #483d8b;
        font-weight: bold;
    }
    h1 {
        color: #e6e6fa; /* 제목은 연보라! 신비로운 느낌 🔮 */
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2); /* 그림자 효과도 샥! */
        font-family: 'Comic Sans MS', cursive; /* 귀여운 폰트 어때? 😄 */
    }
    h2 {
        color: #ff6347; /* 서브 제목은 오렌지! 생기발랄! 🍊 */
        border-bottom: 2px solid #ffa07a;
        padding-bottom: 5px;
    }
    .result-box {
        background-color: #ffffff; /* 결과 상자는 하얀색으로 깔끔하게! 📝 */
        border-radius: 20px;
        padding: 25px;
        margin-top: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* 부드러운 그림자! ☁️ */
        border: 2px dashed #9370db; /* 점선 테두리도 센스 있게! 🎈 */
    }
    .emoji-explosion {
        font-size: 2.5em; /* 이모지는 왕크게! ✨ */
        animation: pulse 1.5s infinite; /* 둠칫둠칫 애니메이션 추가! 💃 */
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# 🌠 메인 타이틀! 화려함 폭발! 🎇
st.markdown(
    """
    <h1 style='text-align: center;'>
        ✨MBTI별 꿈의 직업 찾기 대작전!🌟<br>
        <span class="emoji-explosion">🚀🌈🔮🔑📚</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("---") # 구분선으로 깔끔하게 나눠주자!

# 🙋‍♀️ 환영 메시지도 상냥하게!
st.info(
    "👋 안녕 넉넉한초콜릿8098! 너의 멋진 미래를 위한 MBTI 진로 탐험 앱에 온 걸 환영해! 🎉 "
    "네 MBTI를 선택하고, 숨겨진 직업의 가능성을 발견해봐! 두근두근 기대되지 않아? 🤩"
)

# 🧑‍💻 MBTI 직업 추천 사전! (최대한 다양하게, 이모지도 팍팍!)
mbti_careers = {
    "ISTJ": {
        "nickname": "🔍 신뢰의 관리자",
        "description": "규칙을 잘 따르고 책임감이 강한 넉넉한초콜릿8098! 꼼꼼함과 신뢰를 바탕으로 일을 멋지게 해낼 거야! 👍",
        "careers": ["회계사 📊", "공무원 🏛️", "경찰 👮‍♂️", "판사 🧑‍⚖️", "데이터 분석가 📈", "프로젝트 매니저 📋"]
    },
    "ISFJ": {
        "nickname": "😇 따뜻한 수호자",
        "description": "타인을 진심으로 배려하고 따뜻한 마음을 가진 넉넉한초콜릿8098! 주변 사람들에게 긍정적인 영향을 줄 거야! 💖",
        "careers": ["간호사 🩺", "유치원 교사 👩‍🏫", "사회복지사 🤝", "심리 상담사 🛋️", "영양사 🥗", "사서 📚"]
    },
    "INFJ": {
        "nickname": "🌟 통찰력 있는 옹호자",
        "description": "이상적이고 통찰력이 뛰어난 넉넉한초콜릿8098! 세상에 긍정적인 변화를 가져올 수 있는 잠재력을 가졌어! ✨",
        "careers": ["심리 상담사 🗣️", "작가 ✍️", "교수 🎓", "예술가 🎨", "비영리 단체 관리자 🌍", "성직자 🙏"]
    },
    "INTJ": {
        "nickname": "🧠 독립적인 전략가",
        "description": "논리적이고 독립적인 사고를 가진 넉넉한초콜릿8098! 복잡한 문제를 해결하고 미래를 설계하는 데 탁월할 거야! 💡",
        "careers": ["과학자 🔬", "IT 개발자 💻", "건축가 🏗️", "대학교수 🧑‍🏫", "경영 컨설턴트 💼", "데이터 과학자 📊"]
    },
    "ISTP": {
        "nickname": "🛠️ 재주 많은 만능 재주꾼",
        "description": "새로운 것을 탐구하고 직접 체험하는 것을 좋아하는 넉넉한초콜릿8098! 현실적인 문제 해결 능력이 뛰어나! 🚀",
        "careers": ["엔지니어 ⚙️", "파일럿 ✈️", "디자이너 🎨", "경찰관 🚓", "소방관 🚒", "운동선수 🏅"]
    },
    "ISFP": {
        "nickname": "🌈 유연한 예술가",
        "description": "따뜻하고 예술적인 감각을 가진 넉넉한초콜릿8098! 아름다움을 창조하고 즐거움을 줄 수 있는 재능이 있어! 🌸",
        "careers": ["패션 디자이너 👗", "플로리스트 💐", "음악가 🎶", "사진작가 📸", "요리사 🧑‍🍳", "미술 치료사 🖼️"]
    },
    "INFP": {
        "nickname": "🕊️ 열정적인 중재자",
        "description": "내면이 풍부하고 조화와 이해를 중요하게 생각하는 넉넉한초콜릿8098! 타인의 성장을 돕고 세상을 따뜻하게 만들 거야! 💖",
        "careers": ["카운슬러 💬", "작가 📜", "일러스트레이터 🎨", "사서 📖", "사회복지사 🫂", "애니메이터 🎬"]
    },
    "INTP": {
        "nickname": "🧐 논리적인 사색가",
        "description": "논리적이고 분석적인 사고가 뛰어난 넉넉한초콜릿8098! 새로운 이론을 탐구하고 혁신적인 아이디어를 만들 수 있어! 🔬",
        "careers": ["연구원 🧪", "프로그래머 🧑‍💻", "대학교수 🧑‍🏫", "발명가 💡", "철학자 📚", "정보 보안 전문가 🔐"]
    },
    "ESTP": {
        "nickname": "🚀 에너제틱한 활동가",
        "description": "활기차고 에너지가 넘치는 넉넉한초콜릿8098! 직접 경험하고 문제를 해결하는 것을 즐길 거야! 🥳",
        "careers": ["스포츠 선수 🏅", "영업원 🤝", "기업가 💡", "경찰관 🚨", "소방관 👨‍🚒", "연예인 🎤"]
    },
    "ESFP": {
        "nickname": "🥳 자유로운 연예인",
        "description": "긍정적이고 사교적인 넉넉한초콜릿8098! 사람들과 어울리고 에너지를 나누는 데 재능이 있어! 🎉",
        "careers": ["배우 🎭", "가수 🎤", "이벤트 기획자 🎊", "승무원 ✈️", "유치원 교사 👨‍🏫", "레크리에이션 강사 🤸"]
    },
    "ENFP": {
        "nickname": "✨ 창의적인 활동가",
        "description": "상상력이 풍부하고 열정적인 넉넉한초콜릿8098! 새로운 가능성을 탐색하고 사람들을 고무시키는 데 능숙해! 💡",
        "careers": ["마케터 📈", "코치 📣", "컨설턴트 🗣️", "홍보 전문가 📢", "크리에이터 🎥", "디자이너 ✍️"]
    },
    "ENTP": {
        "nickname": "💡 똑똑한 발명가",
        "description": "논쟁을 즐기고 새로운 아이디어를 탐구하는 넉넉한초콜릿8098! 혁신적인 해결책을 찾는 데 타고난 재능이 있어! 🧠",
        "careers": ["변호사 🧑‍⚖️", "스타트업 창업가 🚀", "전략 기획자 📝", "벤처 투자가 💰", "컨설턴트 👨‍💼", "발명가 🛠️"]
    },
    "ESTJ": {
        "nickname": "👑 효율적인 경영자",
        "description": "체계적이고 현실적인 넉넉한초콜릿8098! 조직을 효율적으로 이끌고 목표 달성에 능숙할 거야! 🏢",
        "careers": ["기업 경영자 💼", "군 장교 🎖️", "프로젝트 매니저 📋", "은행원 🏦", "행정 전문가 📄", "부동산 전문가 🏘️"]
    },
    "ESFJ": {
        "nickname": "🫂 다정한 외교관",
        "description": "사람들과의 관계를 중요하게 생각하고 협력을 잘하는 넉넉한초콜릿8098! 모두에게 사랑받는 존재가 될 거야! 🥰",
        "careers": ["교사 🧑‍🏫", "승무원 ✈️", "의료 전문가 👩‍⚕️", "웨딩 플래너 👰‍♀️", "고객 서비스 담당자 📞", "영업 관리자 📈"]
    },
    "ENFJ": {
        "nickname": "💖 따뜻한 리더",
        "description": "타인에게 긍정적인 영향을 미치고 리더십을 발휘하는 넉넉한초콜릿8098! 사람들의 잠재력을 끌어내는 데 탁월해! 🤝",
        "careers": ["교육 컨설턴트 📚", "언론인 🎤", "정치인 🏛️", "코치 🗣️", "비영리 단체 관리자 🌿", "인사 담당자 🧑‍💼"]
    },
    "ENTJ": {
        "nickname": "🐅 단호한 지도자",
        "description": "명확한 비전을 가지고 사람들을 이끄는 넉넉한초콜릿8098! 목표를 달성하기 위해 강력하게 추진할 수 있어! 💪",
        "careers": ["CEO 🔝", "변호사 🧑‍⚖️", "정치인 🏛️", "관리 컨설턴트 📊", "사업 개발자 📈", "경영자 🏢"]
    },
}

# 📝 MBTI 선택 상자 (예쁘게 꾸며야지!)
st.subheader("🕵️‍♀️ 너의 MBTI는 무엇이니?")
selected_mbti = st.selectbox(
    "👉 아래에서 너의 MBTI를 선택해봐! (클릭하고 고를 수 있어!)",
    list(mbti_careers.keys()),
    index=None, # 초기에는 아무것도 선택되지 않도록!
    placeholder="🌟 MBTI를 선택해주세요! 🌟"
)

# 💡 선택 결과 보여주기!
if selected_mbti:
    st.markdown("---")
    mbti_info = mbti_careers[selected_mbti]
    st.markdown(f"<div class='result-box'>", unsafe_allow_html=True)
    st.markdown(f"<h2>🎉 넉넉한초콜릿8098의 MBTI는 '{selected_mbti}' 이구나! 🎉</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3>✨ '{mbti_info['nickname']}' ✨</h3>", unsafe_allow_html=True)
    st.write(f"👉 **{mbti_info['description']}**")
    st.write("") # 한 줄 띄우기
    st.markdown("<h3>🎯 넉넉한초콜릿8098에게 추천하는 직업이야!</h3>", unsafe_allow_html=True)
    
    # 📌 직업 리스트도 예쁘게!
    for i, career in enumerate(mbti_info['careers']):
        st.markdown(f"<li>{i+1}. {career}</li>", unsafe_allow_html=True)
    
    st.write("") # 한 줄 띄우기
    st.success(
        "✨ 이 직업들이 넉넉한초콜릿8098에게 딱 맞을 거야! "
        "물론, 이건 추천일 뿐이니까 너의 진짜 꿈과 재능은 네가 제일 잘 알지? "
        "그래도 새로운 가능성을 탐색하는 데 도움이 되었으면 좋겠다! 💖"
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # 🥳 결과 확인 후 터지는 풍선 효과!
    st.balloons()
    
    # 추가 질문 유도!
    st.write("")
    st.write("---")
    st.markdown(
        "### 🌟 어때? 이 직업 중에 혹시 마음에 드는 게 있었어? "
        "아니면 또 궁금한 직업 분야가 있다면 언제든지 말해줘! "
        "넉넉한초콜릿8098의 꿈을 응원한다! 파이팅! 💪😊"
    )
    
else:
    st.info("⬆️ 위에 너의 MBTI를 선택하면 추천 직업이 나타날 거야! 두근두근! 🤩")

# 🎈 페이지 하단에 귀여운 그림이나 메시지 추가
st.write("---")
st.markdown(
    """
    <p style='text-align: center; font-size: 0.9em; color: #a9a9a9;'>
        이 앱은 진로 탐색에 도움을 주기 위해 만들어졌어! 🌈<br>
        모든 가능성은 너에게 달려있다는 걸 잊지 마! ✨<br>
        Created with ❤️ by 시화 & 넉넉한초콜릿8098
    </p>
    """,
    unsafe_allow_html=True
)
