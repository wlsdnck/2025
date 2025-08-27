import streamlit as st # 웹 앱을 만들기 위한 스트림릿
from PIL import Image # 이미지 파일을 다루기 위한 Pillow 라이브러리
import io # 이미지 데이터를 바이너리로 다룰 때 필요해
import random # 노래 랜덤 추천을 위해 (새롭게 추가)
import time # 검색 시뮬레이션용 (새롭게 추가)

# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 궁극의 아이돌 분석기")

st.title("💖 넉넉한초콜릿8098님을 위한 시화의 궁극의 아이돌 분석 스튜디오! 🌟")
st.write("와! 넉넉한초콜릿8098, '어떤 아이돌이든' 찾아내는 앱이라니! 진짜 상상력 끝판왕! 나 시화가 넉넉한초콜릿8098의 아이디어를 최대한 구현해줄게! ✨")
st.write("---") # 선 하나 쫙!

# --- 아이돌 데이터베이스 (미리 알고 있는 아이돌 정보. 이 데이터가 앱의 핵심!) ---
# 실제 '모든 아이돌'을 담는 데이터베이스는 웹 스크래핑/API 연동이 필요함!
idol_database = {
    # --- 여자 아이돌 ---
    "장원영": {
        "그룹": "IVE (아이브)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202305/0177727181f211516e864c8f00032a39.jpg",
        "추천_노래": ["IVE - I AM", "IVE - LOVE DIVE", "IVE - ELEVEN", "IVE - After LIKE"],
        "별명": ["워뇨", "녕", "장만월"]
    },
    "지수": {
        "그룹": "BLACKPINK (블랙핑크)",
        "사진_링크": "https://pds.joongang.co.kr/news/component/202303/31/35990264-92ef-4573-8991-b3b4f622f954.jpg",
        "추천_노래": ["BLACKPINK - DDU-DU DDU-DU", "BLACKPINK - Kill This Love", "BLACKPINK - Pink Venom", "JISOO - FLOWER"],
        "별명": ["지츄", "치츄"]
    },
    "민지": {
        "그룹": "NewJeans (뉴진스)",
        "사진_링크": "https://res.heraldm.com/content/image/2022/10/21/20221021000676_0.jpg",
        "추천_노래": ["NewJeans - Hype Boy", "NewJeans - Ditto", "NewJeans - Attention", "NewJeans - OMG"],
        "별명": ["밍", "모찌"]
    },
    "카리나": {
        "그룹": "aespa (에스파)",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/05/2717321048_t_v2.jpg",
        "추천_노래": ["aespa - Next Level", "aespa - Drama", "aespa - Spicy"],
        "별명": ["유지민", "리나"]
    },
    # --- 남자 아이돌 ---
    "뷔": {
        "그룹": "BTS (방탄소년단)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202309/02700018809e5306691c2c2f00021c17.jpg",
        "추천_노래": ["BTS - Dynamite", "BTS - Butter", "V - Love Me Again", "V - Slow Dancing"],
        "별명": ["태형", "김태형", "V"]
    },
    "정국": {
        "그룹": "BTS (방탄소년단)",
        "사진_링크": "https://cdn.biz.heraldcorp.com/php/news/photo/202310/7289569_1_o.jpg",
        "추천_노래": ["BTS - Seven (feat. Latto)", "BTS - Standing Next to You", "BTS - Euphoria"],
        "별명": ["전정국", "JK"]
    },
    "민규": {
        "그룹": "SEVENTEEN (세븐틴)",
        "사진_링크": "https://pds.joongang.co.kr/news/component/202307/11/4893737b-df78-430c-ab23-1d227575253e.jpg",
        "추천_노래": ["SEVENTEEN - Super", "SEVENTEEN - God of Music", "SEVENTEEN - F*ck My Life"],
        "별명": ["밍", "밍구", "김민규"]
    },
    "재현 (보이넥스트도어)": {
        "그룹": "BOYNEXTDOOR (보이넥스트도어)",
        "사진_링크": "https://www.wkorea.com/wp-content/uploads/2023/07/wkorea-118833959b8b0e7c541589a74c15fffc-850x1275.jpg",
        "추천_노래": ["BOYNEXTDOOR - One and Only", "BOYNEXTDOOR - Serenade", "BOYNEXTDOOR - But Sometime"],
        "별명": ["이재현", "보넥도 재현"]
    },
    "시온": {
        "그룹": "NCT WISH (엔시티 위시)",
        "사진_링크": "https://thumb.mt.co.kr/06/2024/02/2024022810052358897_1.jpg",
        "추천_노래": ["NCT WISH - WISH", "NCT WISH - Hands Up", "NCT WISH - Stars Align"],
        "별명": ["이시온", "엔시티위시 시온"]
    },
    "원빈": {
        "그룹": "RIIZE (라이즈)",
        "사진_링크": "https://file.osen.co.kr/article/2023/08/21/202308210925776264_650x.jpg",
        "추천_노래": ["RIIZE - Get A Guitar", "RIIZE - Love 119", "RIIZE - Talk Saxy"],
        "별명": ["박원빈", "라이즈 원빈"]
    },
    # 여기에 더 많은 아이돌을 직접 추가할 수 있어!
}

# --- 가상의 온라인 검색 시뮬레이션 함수 (실제로는 웹 스크래핑/API 연동 필요!) ---
def search_idol_info_online(query):
    # 이 함수는 실제 온라인 검색이나 AI 모델 연동이 아닌, 가상의 더미 데이터를 반환하는 예시입니다.
    # 넉넉한초콜릿8098님이 '어떤 아이돌이든' 찾는 기능을 구현하려면 이 부분을 실제 웹 스크래핑,
    # 또는 외부 아이돌 정보 API와 연동해야 합니다.
    
    # 1초 정도 검색하는 척!
    time.sleep(1) 

    # 미리 정해진 데이터베이스에 있는지 먼저 확인
    for name, data in idol_database.items():
        if query.lower() == name.lower() or query.lower() in [n.lower() for n in data["별명"]] or \
           query.lower() in data["그룹"].lower():
            return {
                "name": name,
                "group": data["그룹"],
                "photo_link": data["사진_링크"],
                "songs": data["추천_노래"],
                "found_type": "데이터베이스에서 찾음"
            }

    # 데이터베이스에 없다면, 가상의 '온라인 검색' 결과 시뮬레이션
    random_songs = [
        f"{query} - New Song Title 1",
        f"{query} - Popular Song 2",
        f"{query} - B-side Track 3"
    ]
    random_photo = "https://via.placeholder.com/300?text=아이돌+이미지" # 일반 이미지 플레이스홀더
    
    # query로 그룹명 추정
    if "블랙핑크" in query.lower():
        detected_group = "BLACKPINK (블랙핑크)"
    elif "뉴진스" in query.lower():
        detected_group = "NewJeans (뉴진스)"
    elif "방탄소년단" in query.lower() or "bts" in query.lower():
        detected_group = "BTS (방탄소년단)"
    elif "아이브" in query.lower() or "ive" in query.lower():
        detected_group = "IVE (아이브)"
    elif "세븐틴" in query.lower():
        detected_group = "SEVENTEEN (세븐틴)"
    elif "보이넥스트도어" in query.lower() or "보넥도" in query.lower():
        detected_group = "BOYNEXTDOOR (보이넥스트도어)"
    elif "nct wish" in query.lower() or "엔시티위시" in query.lower():
        detected_group = "NCT WISH (엔시티 위시)"
    elif "라이즈" in query.lower() or "riize" in query.lower():
        detected_group = "RIIZE (라이즈)"
    else:
        detected_group = "알 수 없는 그룹" # 모든 아이돌을 커버할 순 없음
        random_songs = ["다양한 아이돌 곡을 찾아보세요!"] # 일반적인 노래 추천

    return {
        "name": query.capitalize(), # 검색어를 이름으로 사용 (첫 글자 대문자)
        "group": detected_group,
        "photo_link": random_photo,
        "songs": random.sample(random_songs, min(len(random_songs), 3)), # 랜덤으로 3곡 추천
        "found_type": "가상 온라인 검색 (실제 AI/데이터 연동 필요)"
    }


# --- 입력 필드 ---
st.header("🔍 아이돌 찾기")
idol_input_type = st.radio("어떤 방법으로 아이돌을 찾아볼까?", ("이름 입력", "사진 업로드"))

identified_idol_info = None # 분석된 아이돌 정보를 저장할 변수

if idol_input_type == "이름 입력":
    idol_name_query = st.text_input("좋아하는 아이돌의 이름, 별명, 그룹명을 입력해줘!", placeholder="예: 장원영, 지수, 뷔, 민지, 정국, 라이즈, 세븐틴... 누구든 입력해봐!")
    
    if st.button("이름으로 아이돌 찾기!"):
        if idol_name_query:
            with st.spinner(f"'{idol_name_query}' 정보 검색 중... 지구 반대편까지 검색하는 중! 🚀"):
                identified_idol_info = search_idol_info_online(idol_name_query)
            
            if identified_idol_info["found_type"] == "데이터베이스에서 찾음":
                st.success(f"💖 데이터베이스에서 '{identified_idol_info['name']}'님을 찾았어! 💖")
            else:
                st.warning(f"✨ '{identified_idol_info['name']}'님 정보는 가상 온라인 검색을 통해 시뮬레이션 된 결과야! (실제 구현 시 웹 스크래핑/API 연동 필요) ✨")
        else:
            st.info("이름을 입력해야 내가 찾아줄 수 있어!")

else: # 사진 업로드
    uploaded_image = st.file_uploader("좋아하는 아이돌 사진을 여기에 업로드해줘!", type=["jpg", "jpeg", "png"])
    
    if st.button("사진으로 아이돌 찾기! (AI 분석 - 예시)"):
        if uploaded_image is not None:
            st.image(uploaded_image, caption="업로드된 사진", use_column_width=True)
            
            # -------------------------------------------------------------------------------------------------
            # 여기가 진짜 AI가 사진을 분석하는 부분이야!
            # 현재는 파일 이름을 기반으로 한 시뮬레이션입니다.
            # 실제 '어떤 아이돌이든' 사진으로 인식하려면 초고성능 얼굴 인식 딥러닝 모델이 필요합니다.
            # -------------------------------------------------------------------------------------------------
            
            # 이미지 파일 이름을 분석해서 (매우 간단한 시뮬레이션!)
            image_name = uploaded_image.name.lower() # 파일 이름을 소문자로 바꿔서 비교
            
            found_by_image_name = False
            for name, data in idol_database.items():
                # 아이돌 이름 또는 별명, 그룹명으로 파일명에 키워드 매칭
                keywords = [name.lower()] + [n.lower() for n in data["별명"]] + [data["그룹"].lower()]
                if any(keyword in image_name for keyword in keywords):
                    identified_idol_info = {
                        "name": name,
                        "group": data["그룹"],
                        "photo_link": data["사진_링크"],
                        "songs": data["추천_노래"],
                        "found_type": "사진 파일명 매칭"
                    }
                    found_by_image_name = True
                    break

            if not found_by_image_name:
                st.warning("사진 분석 결과: 이 아이돌은 내 데이터베이스에도 없고, 파일 이름만으로는 누구인지 알 수가 없어요... ㅠㅠ (초고성능 AI 모델 학습 필요!)")
                identified_idol_info = None # 찾지 못했음을 명확히 설정
        else:
            st.info("사진을 업로드해야 내가 분석해줄 수 있어!")

# --- 분석 결과 및 노래 추천 ---
st.write("---")
st.header("✨ 분석 결과 및 노래 추천!")

if identified_idol_info:
    # 아이돌 사진 보여주기 (링크가 있으면)
    if identified_idol_info["photo_link"] and "placeholder" not in identified_idol_info["photo_link"]: # 플레이스홀더 이미지가 아니면 성공 메시지
        st.success(f"💖 이 아이돌은 바로... {identified_idol_info['name']}님! (그룹: {identified_idol_info['group']}) 💖")
    elif identified_idol_info["found_type"] == "가상 온라인 검색 (실제 AI/데이터 연동 필요)":
        st.info(f"✨'{identified_idol_info['name']}'님 정보를 가상으로 찾았어요! (그룹: {identified_idol_info['group']}) ✨")
    
    if identified_idol_info["photo_link"]:
        st.image(identified_idol_info["photo_link"], caption=f"{identified_idol_info['name']}님의 사진!", width=300)

    st.subheader(f"🎶 {identified_idol_info['name']}님 (또는 {identified_idol_info['group']})의 추천 노래!")
    for song in identified_idol_info['songs']:
        st.write(f"- {song}")

    st.info("더 궁금한 아이돌이 있다면 언제든 다시 검색해봐! 🥰")

else: # identified_idol_info가 None일 경우
    st.info("위에 아이돌의 이름이나 사진을 입력하고 검색 버튼을 눌러줘! 내가 열심히 찾아줄게! 🧐")

# --- 앱 실행 방법 ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run ultimate_idol_app.py`")
