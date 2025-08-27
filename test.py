import streamlit as st # 웹 앱을 만들기 위한 스트림릿

# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 슈퍼 메가 아이돌 가이드")

st.title("💖 넉넉한초콜릿8098님을 위한 슈퍼 메가 아이돌 그룹 가이드! 🌟")
st.write("와! 넉넉한초콜릿8098, 요청한 모든 그룹들을 다 추가해줬어! 이제 원하는 그룹만 쏙쏙 골라서 정보랑 뮤직비디오를 한눈에 볼 수 있어! 😆")
st.write("궁금한 그룹을 선택하면 멤버 정보부터 인기곡 뮤직비디오까지 한눈에 보여줄게! ✨")
st.write("---") # 선 하나 쫙!

# --- 아이돌 그룹 데이터베이스 ---
# 넉넉한초콜릿8098이 원하는 모든 그룹 정보를 여기 추가했어!
group_database = {
    "BTS (방탄소년단)": {
        "멤버": ["RM", "진", "슈가", "제이홉", "지민", "뷔", "정국"],
        "설명": "빅히트 뮤직 소속의 7인조 보이그룹. 'Dynamite', 'Butter' 등으로 전 세계적인 신드롬을 일으키며 K-POP 역사를 새로 쓰고 있는 그룹이에요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2022/06/202206141344405367_t_v2.jpg",
        "인기곡": [
            {"title": "Dynamite", "youtube_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
            {"title": "Butter", "youtube_link": "https://www.youtube.com/watch?v=WMweEpGlu_U"},
            {"title": "Spring Day", "youtube_link": "https://www.youtube.com/watch?v=nM0xHBp_j_Q"}
        ]
    },
    "SEVENTEEN (세븐틴)": {
        "멤버": ["에스쿱스", "정한", "조슈아", "준", "호시", "원우", "우지", "디에잇", "민규", "도겸", "승관", "버논", "디노"],
        "설명": "플레디스 엔터테인먼트 소속의 13인조 보이그룹. '자체 제작돌'로 불리며, 퍼포먼스 팀, 힙합 팀, 보컬 팀으로 나뉘어 다채로운 매력을 선보이고 있어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Seventeen_profile_pic.jpeg",
        "인기곡": [
            {"title": "Super", "youtube_link": "https://www.youtube.com/watch?v=e7k8-j62qXo"},
            {"title": "God of Music", "youtube_link": "https://www.youtube.com/watch?v=a3Lh-g9qL2Y"},
            {"title": "Don't Wanna Cry", "youtube_link": "https://www.youtube.com/watch?v=zEkg4GBQSMc"}
        ]
    },
    "RIIZE (라이즈)": {
        "멤버": ["쇼타로", "은석", "성찬", "원빈", "승한", "소희", "앤톤"],
        "설명": "SM엔터테인먼트 소속의 7인조 보이그룹. 'Realize & Rise'라는 의미를 담고 있으며, 독자적인 장르 '이모셔널 팝'을 추구하는 그룹이에요!",
        "사진_링크": "https://images.fmkorea.com/files/attach/new2/20240113/4688195842/726435308/6567950798/786a3454b51a5c689617300ce4c16a50.jpg",
        "인기곡": [
            {"title": "Get A Guitar", "youtube_link": "https://www.youtube.com/watch?v=f2pf1_rNvnQ"},
            {"title": "Love 119", "youtube_link": "https://www.youtube.com/watch?v=NfS7Q6B9Cqw"},
            {"title": "Talk Saxy", "youtube_link": "https://www.youtube.com/watch?v=LdYJ6WqJ9qE"}
        ]
    },
    "BOYNEXTDOOR (보이넥스트도어)": {
        "멤버": ["성호", "리우", "재현", "태산", "이한", "운학"],
        "설명": "KOZ엔터테인먼트 소속의 6인조 보이그룹. 옆집 소년들처럼 친근하고 유쾌한 매력으로 대중에게 다가가고 있어요!",
        "사진_링크": "https://i.namu.wiki/i/n5D-G3iN4eW1h3Y2d6N9f6G4d4f2G8P5e0e0N8G4b7d5G4a2v9-U_FfU7G_e4L5s2U-9f6B9A3u0v6jF4z2v3S5z5l5P1q1C1g1j1z1h1x1c1e2h2v4l5R9P5B4K6H4F7O4K5J2e.webp",
        "인기곡": [
            {"title": "One and Only", "youtube_link": "https://www.youtube.com/watch?v=MInE7d7J0bU"},
            {"title": "Serenade", "youtube_link": "https://www.youtube.com/watch?v=O15-M803GjQ"},
            {"title": "But Sometime", "youtube_link": "https://www.youtube.com/watch?v=N4tLwK4hNgs"}
        ]
    },
    "NCT WISH (엔시티 위시)": {
        "멤버": ["시온", "리쿠", "유우시", "재희", "료", "사쿠야"],
        "설명": "SM엔터테인먼트 소속의 6인조 보이그룹. 'WISH for OUR WISH'라는 캐치프레이즈로, 음악과 퍼포먼스를 통해 모든 사람들의 '소원'과 '꿈'을 응원하고 있어요!",
        "사진_링크": "https://news.mtn.co.kr/news_content/image_html_dir/2024/02/2024022810052358897_1.jpg",
        "인기곡": [
            {"title": "WISH", "youtube_link": "https://www.youtube.com/watch?v=3-E08n8Nq5c"},
            {"title": "Hands Up", "youtube_link": "https://www.youtube.com/watch?v=P_3yW7mQ3vE"},
            {"title": "Stars Align", "youtube_link": "https://www.youtube.com/watch?v=84VwJbB34y0"}
        ]
    },
    "투모로우바이투게더 (TXT)": {
        "멤버": ["수빈", "연준", "범규", "태현", "휴닝카이"],
        "설명": "빅히트 뮤직 소속의 5인조 보이그룹. 밝고 청량한 매력으로 '성장'과 '청춘'의 서사를 노래하며 많은 사랑을 받고 있어요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/03/2908581024_t_v2.jpg",
        "인기곡": [
            {"title": "Sugar Rush Ride", "youtube_link": "https://www.youtube.com/watch?v=MADXyqR0cQ4"},
            {"title": "Good Boy Gone Bad", "youtube_link": "https://www.youtube.com/watch?v=y_HwJ718pYw"},
            {"title": "Run Away", "youtube_link": "https://www.youtube.com/watch?v=X5MFlG-g3U8"}
        ]
    },
    "TWS (투어스)": {
        "멤버": ["신유", "도훈", "영재", "한진", "지훈", "경민"],
        "설명": "플레디스 엔터테인먼트 소속의 6인조 보이그룹. 보이 넥스트 도어의 동생 그룹이자 세븐틴 동생 그룹으로 2024년 데뷔했어요. 밝고 긍정적인 '보이후드 팝' 장르를 표방해요!",
        "사진_링크": "https://img.osen.co.kr/article/2024/03/14/202403140924773809_650x.jpg",
        "인기곡": [
            {"title": "첫 만남은 계획대로 되지 않아", "youtube_link": "https://www.youtube.com/watch?v=mE9pQvI-iT0"},
            {"title": "BFF", "youtube_link": "https://www.youtube.com/watch?v=p79q6cM28gE"},
            {"title": "unplugged boy", "youtube_link": "https://www.youtube.com/watch?v=0kI4_7_yP-8"}
        ]
    },
    "EXO (엑소)": {
        "멤버": ["수호", "시우민", "백현", "첸", "찬열", "디오", "카이", "세훈"],
        "설명": "SM엔터테인먼트 소속의 보이그룹. '으르렁', 'CALL ME BABY' 등으로 큰 인기를 얻으며 K-POP의 황금기를 이끈 대표적인 그룹이에요!",
        "사진_링크": "https://file.osen.co.kr/article/2023/07/11/202307111059775269_650x.jpg",
        "인기곡": [
            {"title": "으르렁 (Growl)", "youtube_link": "https://www.youtube.com/watch?v=I3dezFzsNig"},
            {"title": "CALL ME BABY", "youtube_link": "https://www.youtube.com/watch?v=yWfsla_Um80"},
            {"title": "Love Shot", "youtube_link": "https://www.youtube.com/watch?v=pX_S4L5wS0g"}
        ]
    },
    "NCT 127": {
        "멤버": ["태일", "쟈니", "태용", "유타", "도영", "재현", "정우", "마크", "해찬"],
        "설명": "SM엔터테인먼트 소속의 보이그룹 NCT의 유닛. 서울(127)을 기반으로 활동하며 'Neo Culture Technology'의 정체성을 보여주는 독특한 음악과 퍼포먼스를 선보여요!",
        "사진_링크": "https://file.osen.co.kr/article/2022/09/20/202209200827774780_650x.jpg",
        "인기곡": [
            {"title": "영웅 (英雄; Kick It)", "youtube_link": "https://www.youtube.com/watch?v=ZfXnL5S8VnU"},
            {"title": "2 Baddies", "youtube_link": "https://www.youtube.com/watch?v=w6J9d-WbFgc"},
            {"title": "Cherry Bomb", "youtube_link": "https://www.youtube.com/watch?v=W_rfP8K5N3c"}
        ]
    },
    "NCT DREAM": {
        "멤버": ["마크", "런쥔", "제노", "해찬", "재민", "천러", "지성"],
        "설명": "SM엔터테인먼트 소속의 보이그룹 NCT의 유닛. 청소년 연합팀으로 시작하여 활발한 활동을 펼치며 밝고 희망찬 에너지를 전달해요!",
        "사진_링크": "https://cdn.asiatoday.co.kr/images/target.jpg?20231201103233",
        "인기곡": [
            {"title": "Candy", "youtube_link": "https://www.youtube.com/watch?v=qCj-mKjKx8I"},
            {"title": "Hot Sauce", "youtube_link": "https://www.youtube.com/watch?v=oT5N08J568g"},
            {"title": "GO", "youtube_link": "https://www.youtube.com/watch?v=0I6HP1QnN0E"}
        ]
    },
    
    # --- 여자 아이돌 ---
    "IVE (아이브)": {
        "멤버": ["안유진", "가을", "레이", "장원영", "리즈", "이서"],
        "설명": "스타쉽엔터테인먼트 소속의 6인조 다국적 걸그룹. 'I HAVE', 'ELEVEN', 'LOVE DIVE' 등 매번 신선하고 중독성 있는 음악으로 큰 사랑을 받고 있어요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/05/2710313176_t_v2.jpg",
        "인기곡": [
            {"title": "I AM", "youtube_link": "https://www.youtube.com/watch?v=6ZUIwj3FgEQ"},
            {"title": "LOVE DIVE", "youtube_link": "https://www.youtube.com/watch?v=Y8JFxS1HlDo"},
            {"title": "ELEVEN", "youtube_link": "https://www.youtube.com/watch?v=F0B7HDiY-1E"}
        ]
    },
    "BLACKPINK (블랙핑크)": {
        "멤버": ["지수", "제니", "로제", "리사"],
        "설명": "YG엔터테인먼트 소속의 4인조 걸그룹. 'DDU-DU DDU-DU', 'Kill This Love' 등 수많은 히트곡을 발표하며 세계적인 영향력을 가진 그룹으로 성장했어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Blackpink_2020.png/1280px-Blackpink_2020.png",
        "인기곡": [
            {"title": "DDU-DU DDU-DU", "youtube_link": "https://www.youtube.com/watch?v=IHNzOHi8sJs"},
            {"title": "Kill This Love", "youtube_link": "https://www.youtube.com/watch?v=2S24-y03-xE"},
            {"title": "Pink Venom", "youtube_link": "https://www.youtube.com/watch?v=gT8_M-h-93U"}
        ]
    },
    "VIVIZ (비비지)": {
        "멤버": ["은하", "신비", "엄지"],
        "설명": "빅플래닛메이드엔터 소속의 3인조 걸그룹. 전 여자친구 멤버들로 구성되어 화려하게 재데뷔했으며, 다양한 콘셉트를 소화하며 팬들의 사랑을 받고 있어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Viviz_%28Big_Planet_Made_Entertainment%29_at_The_Show_on_October_19%2C_2021.jpg/1280px-Viviz_%28Big_Planet_Made_Entertainment%29_at_The_Show_on_October_19%2C_2021.jpg",
        "인기곡": [
            {"title": "BOP BOP!", "youtube_link": "https://www.youtube.com/watch?v=wX-y0M-YqW8"},
            {"title": "LOVEADE", "youtube_link": "https://www.youtube.com/watch?v=S0T0eG_dFk0"},
            {"title": "MANIAC", "youtube_link": "https://www.youtube.com/watch?v=1F_nQ-DqUss"}
        ]
    },
    "aespa (에스파)": {
        "멤버": ["카리나", "지젤", "윈터", "닝닝"],
        "설명": "SM엔터테인먼트 소속의 4인조 걸그룹. '자신의 또 다른 자아인 아바타(ae)를 만나 새로운 세계를 경험한다'는 독특한 세계관과 음악으로 주목받고 있어요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/05/2717321048_t_v2.jpg",
        "인기곡": [
            {"title": "Next Level", "youtube_link": "https://www.youtube.com/watch?v=4TWR90KJl84"},
            {"title": "Drama", "youtube_link": "https://www.youtube.com/watch?v=KUv4A8c6i_M"},
            {"title": "Spicy", "youtube_link": "https://www.youtube.com/watch?v=WODg2XfG2G4"}
        ]
    },
    "BABYMONSTER (베이비몬스터)": {
        "멤버": ["루카", "파리타", "아사", "아현", "라미", "로라", "치키타"],
        "설명": "YG엔터테인먼트 소속의 7인조 다국적 걸그룹. 'Monster'라는 이름처럼 독보적인 재능과 매력을 겸비한 YG의 신인 걸그룹이에요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/BABYMONSTER_231124.jpg/1280px-BABYMONSTER_231124.jpg",
        "인기곡": [
            {"title": "SHEESH", "youtube_link": "https://www.youtube.com/watch?v=sI0C1RjD150"},
            {"title": "BATTER UP", "youtube_link": "https://www.youtube.com/watch?v=WJDNjJ47I_I"},
            {"title": "Stuck In The Middle", "youtube_link": "https://www.youtube.com/watch?v=IeZpI4p_0W8"}
        ]
    },
    "NMIXX (엔믹스)": {
        "멤버": ["릴리", "해원", "설윤", "배이", "지우", "규진"],
        "설명": "JYP엔터테인먼트 소속의 6인조 걸그룹. 'MIXX POP'이라는 독자적인 음악 장르를 개척하며 기존 K-POP에서 볼 수 없었던 새로운 시도를 선보여요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/NMIXX_at_Seoul_Music_Awards_2023.jpg/1280px-NMIXX_at_Seoul_Music_Awards_2023.jpg",
        "인기곡": [
            {"title": "DICE", "youtube_link": "https://www.youtube.com/watch?v=p1gwD_B1QvU"},
            {"title": "O.O", "youtube_link": "https://www.youtube.com/watch?v=3WS_f20W2pM"},
            {"title": "Love Me Like This", "youtube_link": "https://www.youtube.com/watch?v=p4gC2_l_xK4"}
        ]
    },
    "TWICE (트와이스)": {
        "멤버": ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"],
        "설명": "JYP엔터테인먼트 소속의 9인조 다국적 걸그룹. 'CHEER UP', 'TT' 등 수많은 히트곡으로 국민 걸그룹으로 자리매김하며 활발하게 활동하고 있어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Twice_in_2023.png/1280px-Twice_in_2023.png",
        "인기곡": [
            {"title": "CHEER UP", "youtube_link": "https://www.youtube.com/watch?v=c7rCyll5AeY"},
            {"title": "TT", "youtube_link": "https://www.youtube.com/watch?v=ePpPVE-GGJw"},
            {"title": "Feel Special", "youtube_link": "https://www.youtube.com/watch?v=3ymwXLvyuBY"}
        ]
    },
    "Billlie (빌리)": {
        "멤버": ["시윤", "츠키", "문수아", "하람", "수현", "하루나", "시온"],
        "설명": "미스틱스토리 소속의 7인조 걸그룹. 독특하고 신비로운 세계관과 음악으로 팬들에게 깊은 인상을 남기고 있어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Billlie_at_Billlie%27s_Christmas_2022_Event_in_Yeongdeungpo_Times_Square_02.jpg/1280px-Billlie_at_Billlie%27s_Christmas_2022_Event_in_Yeongdeungpo_Times_Square_02.jpg",
        "인기곡": [
            {"title": "RING X RING", "youtube_link": "https://www.youtube.com/watch?v=UqQY9sM_zRk"},
            {"title": "EUNOIA", "youtube_link": "https://www.youtube.com/watch?v=Jm0qJv9wS5k"},
            {"title": "DANG! (hocus pocus)", "youtube_link": "https://www.youtube.com/watch?v=3g51R1t6c0U"}
        ]
    },
}

# --- 그룹 선택 필드 ---
st.header("🎵 어떤 그룹이 궁금해?")

# group_database의 키(그룹 이름)들을 선택지 리스트로 만들어!
group_names = list(group_database.keys())
# 사용자가 선택할 그룹 이름
selected_group_name = st.selectbox("아래 목록에서 궁금한 아이돌 그룹을 선택해줘!", group_names)

# --- 선택된 그룹 정보 표시 ---
if selected_group_name:
    group_info = group_database[selected_group_name]
    
    st.write("---") # 구분선
    st.subheader(f"✨ {selected_group_name} 정보! ✨")
    
    # 그룹 사진 표시
    if group_info["사진_링크"]:
        st.image(group_info["사진_링크"], caption=f"{selected_group_name} 그룹 사진", width=400)
    
    # 멤버 정보
    st.markdown(f"**멤버:** {', '.join(group_info['멤버'])}")
    
    # 그룹 설명
    st.markdown(f"**그룹 설명:** {group_info['설명']}")
    
    st.write("---")
    st.subheader("🎶 이 그룹의 인기곡 뮤직비디오를 감상해봐! 🎶")
    
    # 인기곡 목록과 유튜브 링크 표시
    for song in group_info['인기곡']:
        st.write(f"- **{song['title']}** [📺 뮤비 보러가기]({song['youtube_link']})")
        # st.video(song['youtube_link']) # <-- 이 부분을 사용하면 앱 내에 비디오가 직접 임베드돼!
                                        #      대신 Streamlit Cloud에서는 외부 리소스 임베딩 제한이 있을 수 있고
                                        #      일반적인 유튜브 링크 대신 직접적인 비디오 파일 URL (MP4 등)을 요구하기도 해.
                                        #      그래서 일단은 링크를 클릭해서 새 창으로 열리게 하는 게 편할 거야!

    st.info("다른 그룹 정보도 언제든 선택해서 볼 수 있어! 🥰")

# --- 앱 실행 방법 ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run super_idol_group_app.py`")
