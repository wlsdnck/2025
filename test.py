import streamlit as st # 웹 앱을 만들기 위한 스트림릿
from PIL import Image # 이미지 파일을 다루기 위한 Pillow 라이브러리
import io # 이미지 데이터를 바이너리로 다룰 때 필요해
import random # 노래 랜덤 추천을 위해
import time # 검색 시뮬레이션용

# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 궁극의 아이돌 분석기 (뮤비 연동)")

st.title("💖 넉넉한초콜릿8098님을 위한 시화의 궁극의 아이돌 분석 스튜디오! 🌟 (뮤비 연동 버전!)")
st.write("와! 넉넉한초콜릿8098, 역시 디테일까지 완벽하게! 🤩 노래 추천 옆에 뮤직비디오까지 바로 볼 수 있게 해줬어! 이제 아이돌 덕질이 더 편해질 거야! ✨")
st.write("---") # 선 하나 쫙!

# --- 아이돌 데이터베이스 (미리 알고 있는 아이돌 정보. 이 데이터가 앱의 핵심!) ---
# '추천_노래' 항목에 노래 제목과 함께 'youtube_link'를 추가했어!
idol_database = {
    # --- 여자 아이돌 ---
    "장원영": {
        "그룹": "IVE (아이브)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202305/0177727181f211516e864c8f00032a39.jpg",
        "추천_노래": [
            {"title": "IVE - I AM", "youtube_link": "https://www.youtube.com/watch?v=6ZUIwj3FgEQ"},
            {"title": "IVE - LOVE DIVE", "youtube_link": "https://www.youtube.com/watch?v=Y8JFxS1HlDo"},
            {"title": "IVE - ELEVEN", "youtube_link": "https://www.youtube.com/watch?v=F0B7HDiY-1E"},
            {"title": "IVE - After LIKE", "youtube_link": "https://www.youtube.com/watch?v=bVf9WzV-c_A"}
        ],
        "별명": ["워뇨", "녕", "장만월"]
    },
    "지수": {
        "그룹": "BLACKPINK (블랙핑크)",
        "사진_링크": "https://pds.joongang.co.kr/news/component/202303/31/35990264-92ef-4573-8991-b3b4f622f954.jpg",
        "추천_노래": [
            {"title": "BLACKPINK - DDU-DU DDU-DU", "youtube_link": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
            {"title": "BLACKPINK - Kill This Love", "youtube_link": "https://www.youtube.com/watch?v=2S24-y03-xE"},
            {"title": "BLACKPINK - Pink Venom", "youtube_link": "https://www.youtube.com/watch?v=gT8_M-h-93U"},
            {"title": "JISOO - FLOWER", "youtube_link": "https://www.youtube.com/watch?v=Yf1eS5n1iQ4"}
        ],
        "별명": ["지츄", "치츄"]
    },
    "민지": {
        "그룹": "NewJeans (뉴진스)",
        "사진_링크": "https://res.heraldm.com/content/image/2022/10/21/20221021000676_0.jpg",
        "추천_노래": [
            {"title": "NewJeans - Hype Boy", "youtube_link": "https://www.youtube.com/watch?v=TJs4eN21mJs"},
            {"title": "NewJeans - Ditto", "youtube_link": "https://www.youtube.com/watch?v=pSG01C1R-C4"},
            {"title": "NewJeans - Attention", "youtube_link": "https://www.youtube.com/watch?v=FGzBwV4Xw7o"},
            {"title": "NewJeans - OMG", "youtube_link": "https://www.youtube.com/watch?v=sVMMvJ1BqfQ"}
        ],
        "별명": ["밍", "모찌"]
    },
    "카리나": {
        "그룹": "aespa (에스파)",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/05/2717321048_t_v2.jpg",
        "추천_노래": [
            {"title": "aespa - Next Level", "youtube_link": "https://www.youtube.com/watch?v=4TWR90KJl84"},
            {"title": "aespa - Drama", "youtube_link": "https://www.youtube.com/watch?v=KUv4A8c6i_M"},
            {"title": "aespa - Spicy", "youtube_link": "https://www.youtube.com/watch?v=WODg2XfG2G4"}
        ],
        "별명": ["유지민", "리나"]
    },
    # --- 남자 아이돌 ---
    "뷔": {
        "그룹": "BTS (방탄소년단)",
        "사진_링크": "https://img.sbs.co.kr/newsite/editor/202309/02700018809e5306691c2c2f00021c17.jpg",
        "추천_노래": [
            {"title": "BTS - Dynamite", "youtube_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
            {"title": "BTS - Butter", "youtube_link": "https://www.youtube.com/watch?v=WMweEpGlu_U"},
            {"title": "V - Love Me Again", "youtube_link": "https://www.youtube.com/watch?v=RboFk9_e7bQ"},
            {"title": "V - Slow Dancing", "youtube_link": "https://www.youtube.com/watch?v=e_RjY0dJ27w"}
        ],
        "별명": ["태형", "김태형", "V"]
    },
    "정국": {
        "그룹": "BTS (방탄소년단)",
        "사진_링크": "https://cdn.biz.heraldcorp.com/php/news/photo/202310/7289569_1_o.jpg",
        "추천_노래": [
            {"title": "BTS - Seven (feat. Latto)", "youtube_link": "https://www.youtube.com/watch?v=QU9c005-bog"},
            {"title": "BTS - Standing Next to You", "youtube_link": "https://www.youtube.com/watch?v=F0B7HDiY-1E"}, # Place Holder
            {"title": "BTS - Euphoria", "youtube_link": "https://www.youtube.com/watch?v=kX0vO4vlFg4"}
        ],
        "별명": ["전정국", "JK"]
    },
    "민규": {
        "그룹": "SEVENTEEN (세븐틴)",
        "사진_링크": "https://pds.joongang.co.kr/news/component/202307/11/4893737b-df78-430c-ab23-1d227575253e.jpg",
        "추천_노래": [
            {"title": "SEVENTEEN - Super", "youtube_link": "https://www.youtube.com/watch?v=e7k8-j62qXo"},
            {"title": "SEVENTEEN - God of Music", "youtube_link": "https://www.youtube.com/watch?v=a3Lh-g9qL2Y"},
            {"title": "SEVENTEEN - F*ck My Life", "youtube_link": "https://www.youtube.com/watch?v=vVj_sXn70R8"}
        ],
        "별명": ["밍", "밍구", "김민규"]
    },
    "재현 (보이넥스트도어)": {
        "그룹": "BOYNEXTDOOR (보이넥스트도어)",
        "사진_링크": "https://www.wkorea.com/wp-content/uploads/2023/07/wkorea-118833959b8b0e7c541589a74c15fffc-850x1275.jpg",
        "추천_노래": [
            {"title": "BOYNEXTDOOR - One and Only", "youtube_link": "https://www.youtube.com/watch?v=MInE7d7J0bU"},
            {"title": "BOYNEXTDOOR - Serenade", "youtube_link": "https://www.youtube.com/watch?v=O15-M803GjQ"},
            {"title": "BOYNEXTDOOR - But Sometime", "youtube_link": "https://www.youtube.com/watch?v=N4tLwK4hNgs"}
        ],
        "별명": ["이재현", "보넥도 재현"]
    },
    "시온": {
        "그룹": "NCT WISH (엔시티 위시)",
        "사진_링크": "https://thumb.mt.co.kr/06/2024/02/2024022810052358897_1.jpg",
        "추천_노래": [
            {"title": "NCT WISH - WISH", "youtube_link": "https://www.youtube.com/watch?v=3-E08n8Nq5c"},
            {"title": "NCT WISH - Hands Up", "youtube_link": "https://www.youtube.com/watch?v=3-E08n8Nq5c"}, # Place Holder
            {"title": "NCT WISH - Stars Align", "youtube_link": "https://www.youtube.com/watch?v=3-E08n8Nq5c"} # Place Holder
        ],
        "별명": ["이시온", "엔시티위시 시온"]
    },
    "원빈": {
        "그룹": "RIIZE (라이즈)",
        "사진_링크": "https://file.osen.co.kr/article/2023/08/21/202308210925776264_650x.jpg",
        "추천_노래": [
            {"title": "RIIZE - Get A Guitar", "youtube_link": "https://www.youtube.com/watch?v=f2pf1_rNvnQ"},
            {"title": "RIIZE - Love 119", "youtube_link": "https://www.youtube.com/watch?v=NfS7Q6B9Cqw"},
            {"title": "RIIZE - Talk Saxy", "youtube_link": "https://www.youtube.com/watch?v=LdYJ6WqJ9qE"}
        ],
        "별명": ["박원빈", "라이즈 원빈"]
    },
    # 여기에 더 많은 아이돌을 직접 추가할 수 있어! (추천 노래에 'youtube_link' 추가하는 거 잊지 마!)
}

# --- 가상의 온라인 검색 시뮬레이션 함수 (실제로는 웹 스크래핑/API 연동 필요!) ---
def search_idol_info_online(query):
    # 미리 정해진 데이터베이스에 있는지 먼저 확인
    for name, data in idol_database.items():
        if query.lower() == name.lower() or query.lower() in [n.lower() for n in data["별명"]] or \
           query.lower() in data["그룹"].lower():
            return {
                "name": name,
                "group": data["그룹"],
                "photo_link": data["사진_링크"],
                "songs": data["추천_노래"], # 데이터베이스의 노래 목록 그대로 사용
                "found_type": "데이터베이스에서 찾음"
            }

    # 데이터베이스에 없다면, 가상의 '온라인 검색' 결과 시뮬레이션
    random_titles = [
        f"{query} - Best Song",
        f"{query} - Catchy Tune",
        f"{query} - Debut Track"
    ]
    
    # 가상의 뮤비 링크 생성 (유튜브 검색 링크로 연결)
    random_songs_with_links = [
        {"title": title, "youtube_link": f"https://www.youtube.com/results?search_query={title.replace(' ', '+')}"}
        for title in random.sample(random_titles, min(len(random_titles), 3))
    ]
    
    random_photo = "https://via.placeholder.com/300?text=아이돌+이미지" # 일반 이미지 플레이스홀더
    
    # query로 그룹명 추정 (정교한 로직은 아님)
    detected_group = "알 수 없는 그룹"
    if "블랙핑크" in query.lower(): detected_group = "BLACKPINK (블랙핑크)"
    elif "뉴진스" in query.lower(): detected_group = "NewJeans (뉴진스)"
    # ... (더 많은 그룹 조건 추가 가능)
    
    return {
        "name": query.capitalize(),
        "group": detected_group,
        "photo_link": random_photo,
        "songs": random_songs_with_links,
        "found_type": "가상 온라인 검색 (실제 AI/데이터 연동 필요)"
    }


# --- 입력 필드 ---
st.header("🔍 아이돌 찾기")
idol_input_type = st.radio("어떤 방법으로 아이돌을 찾아볼까?", ("이름 입력", "사진 업로드"))

identified_idol_info = None # 분석된 아이돌 정보를 저장할 변수

if idol_input_type == "이름 입력":
    idol_name_query = st.text_input("좋아하는 아이돌의 이름, 별명, 그룹명을 입력해줘!", placeholder="예: 장원영, 지수, 뷔, 라이즈... 누구든 입력해봐!")
    
    if st.button("이름으로 아이돌 찾기!"):
        if idol_name_query:
            with st.spinner(f"'{idol_name_query}' 정보 검색 중... 지구 반대편까지 검색하는 중! 🚀"):
                # 검색 시뮬레이션 대기 시간
                time.sleep(1.5) 
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
    if identified_idol_info["photo_link"] and "placeholder" not in identified_idol_info["photo_link"]:
        st.success(f"💖 이 아이돌은 바로... {identified_idol_info['name']}님! (그룹: {identified_idol_info['group']}) 💖")
    elif identified_idol_info["found_type"] == "가상 온라인 검색 (실제 AI/데이터 연동 필요)":
        st.info(f"✨'{identified_idol_info['name']}'님 정보를 가상으로 찾았어요! (그룹: {identified_idol_info['group']}) ✨")
    
    if identified_idol_info["photo_link"]:
        st.image(identified_idol_info["photo_link"], caption=f"{identified_idol_info['name']}님의 사진!", width=300)

    st.subheader(f"🎶 {identified_idol_info['name']}님 (또는 {identified_idol_info['group']})의 추천 노래!")
    for song in identified_idol_info['songs']:
        st.write(f"- **{song['title']}** [📺 뮤비 보러가기]({song['youtube_link']})")
        # st.video()를 사용하면 유튜브 링크 자체를 바로 플레이할 수 있어! (대신 웹 링크 대신 직접 mp4 같은 파일 링크 필요)
        # st.video(song['youtube_link']) # <-- 이 부분을 사용하고 싶으면, 실제 유튜브 영상 임베드 URL이 필요함!
                                      #     현재는 직접 유튜브 페이지로 이동하도록 링크를 제공!

    st.info("더 궁금한 아이돌이 있다면 언제든 다시 검색해봐! 🥰")

else: # identified_idol_info가 None일 경우
    st.info("위에 아이돌의 이름이나 사진을 입력하고 검색 버튼을 눌러줘! 내가 열심히 찾아줄게! 🧐")

# --- 앱 실행 방법 ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run ultimate_idol_app_with_mv.py`")
