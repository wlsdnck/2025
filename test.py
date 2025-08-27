import streamlit as st # 웹 앱을 만들기 위한 스트림릿
import re # 정규표현식 (유튜브 링크에서 동영상 ID를 추출하기 위해)
import streamlit.components.v1 as components # HTML을 직접 삽입하기 위해 필요


# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 맞춤형 아이돌 컬렉션 (링크 이동 추가)")

st.title("💖 넉넉한초콜릿8098님을 위한 맞춤형 아이돌 컬렉션! 🌟 (링크 이동 추가!)")
st.write("와! 넉넉한초콜릿8098, 앱에서 뮤비 재생이 안 될 때, 이제 바로 유튜브로 넘어갈 수 있게 버튼까지 추가해줬어! 역시 세심한 아이디어가 최고다! 😆")
st.write("궁금한 그룹을 선택하면 멤버 정보부터 인기곡 뮤직비디오까지 한눈에 보여줄게! ✨")
st.write("---") # 선 하나 쫙!

# --- 유튜브 링크에서 동영상 ID 추출 함수 ---
def get_youtube_video_id(url):
    # 일반적인 유튜브 watch?v= 또는 embed/ 링크에서 동영상 ID를 추출
    match = re.search(r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})', url)
    if match:
        return match.group(1)
    return None

# --- 아이돌 그룹 데이터베이스 ---
# 넉넉한초콜릿8098이 요청한 그룹들만 포함! (이전 코드와 동일)
group_database = {
    "BTS (방탄소년단)": {
        "멤버": ["RM", "진", "슈가", "제이홉", "지민", "뷔", "정국"],
        "설명": "빅히트 뮤직 소속의 7인조 보이그룹. 'Dynamite', 'Butter' 등으로 전 세계적인 신드롬을 일으키며 K-POP 역사를 새로 쓰고 있는 그룹이에요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2022/06/202206141344405367_t_v2.jpg",
        "인기곡": [
            {"title": "Dynamite", "youtube_link": "https://www.youtube.com/embed/gdZLi9oWNZg"},
            {"title": "Butter", "youtube_link": "https://www.youtube.com/embed/WMweEpGlu_U"},
            {"title": "Spring Day", "youtube_link": "https://www.youtube.com/embed/nM0xHBp_j_Q"}
        ]
    },
    "SEVENTEEN (세븐틴)": {
        "멤버": ["에스쿱스", "정한", "조슈아", "준", "호시", "원우", "우지", "디에잇", "민규", "도겸", "승관", "버논", "디노"],
        "설명": "플레디스 엔터테인먼트 소속의 13인조 보이그룹. '자체 제작돌'로 불리며, 퍼포먼스 팀, 힙합 팀, 보컬 팀으로 나뉘어 다채로운 매력을 선보이고 있어요!",
        "사진_링크": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Seventeen_profile_pic.jpeg",
        "인기곡": [
            {"title": "Super", "youtube_link": "https://www.youtube.com/embed/e7k8-j62qXo"},
            {"title": "God of Music", "youtube_link": "https://www.youtube.com/embed/a3Lh-g9qL2Y"},
            {"title": "Don't Wanna Cry", "youtube_link": "https://www.youtube.com/embed/zEkg4GBQSMc"}
        ]
    },
    "RIIZE (라이즈)": {
        "멤버": ["쇼타로", "은석", "성찬", "원빈", "승한", "소희", "앤톤"],
        "설명": "SM엔터테인먼트 소속의 7인조 보이그룹. 'Realize & Rise'라는 의미를 담고 있으며, 독자적인 장르 '이모셔널 팝'을 추구하는 그룹이에요!",
        "사진_링크": "https://images.fmkorea.com/files/attach/new2/20240113/4688195842/726435308/6567950798/786a3454b51a5c689617300ce4c16a50.jpg",
        "인기곡": [
            {"title": "Get A Guitar", "youtube_link": "https://www.youtube.com/embed/f2pf1_rNvnQ"},
            {"title": "Love 119", "youtube_link": "https://www.youtube.com/embed/NfS7Q6B9Cqw"},
            {"title": "Talk Saxy", "youtube_link": "https://www.youtube.com/embed/LdYJ6WqJ9qE"}
        ]
    },
    "BOYNEXTDOOR (보이넥스트도어)": {
        "멤버": ["성호", "리우", "재현", "태산", "이한", "운학"],
        "설명": "KOZ엔터테인먼트 소속의 6인조 보이그룹. 옆집 소년들처럼 친근하고 유쾌한 매력으로 대중에게 다가가고 있어요!",
        "사진_링크": "https://i.namu.wiki/i/n5D-G3iN4eW1h3Y2d6N9f6G4d4f2G8P5e0e0N8G4b7d5G4a2v9-U_FfU7G_e4L5s2U-9f6B9A3u0v6jF4z2v3S5z5l5P1q1C1g1j1z1h1x1c1e2h2v4l5R9P5B4K6H4F7O4K5J2e.webp",
        "인기곡": [
            {"title": "One and Only", "youtube_link": "https://www.youtube.com/embed/MInE7d7J0bU"},
            {"title": "Serenade", "youtube_link": "https://www.youtube.com/embed/O15-M803GjQ"},
            {"title": "But Sometime", "youtube_link": "https://www.youtube.com/embed/N4tLwK4hNgs"}
        ]
    },
    "NCT WISH (엔시티 위시)": {
        "멤버": ["시온", "리쿠", "유우시", "재희", "료", "사쿠야"],
        "설명": "SM엔터테인먼트 소속의 6인조 보이그룹. 'WISH for OUR WISH'라는 캐치프레이즈로, 음악과 퍼포먼스를 통해 모든 사람들의 '소원'과 '꿈'을 응원하고 있어요!",
        "사진_링크": "https://news.mtn.co.kr/news_content/image_html_dir/2024/02/2024022810052358897_1.jpg",
        "인기곡": [
            {"title": "WISH", "youtube_link": "https://www.youtube.com/embed/3-E08n8Nq5c"},
            {"title": "Hands Up", "youtube_link": "https://www.youtube.com/embed/P_3yW7mQ3vE"},
            {"title": "Stars Align", "youtube_link": "https://www.youtube.com/embed/84VwJbB34y0"}
        ]
    },
    "투모로우바이투게더 (TXT)": {
        "멤버": ["수빈", "연준", "범규", "태현", "휴닝카이"],
        "설명": "빅히트 뮤직 소속의 5인조 보이그룹. 밝고 청량한 매력으로 '성장'과 '청춘'의 서사를 노래하며 많은 사랑을 받고 있어요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/03/2908581024_t_v2.jpg",
        "인기곡": [
            {"title": "Sugar Rush Ride", "youtube_link": "https://www.youtube.com/embed/MADXyqR0cQ4"},
            {"title": "Good Boy Gone Bad", "youtube_link": "https://www.youtube.com/embed/y_HwJ718pYw"},
            {"title": "Run Away", "youtube_link": "https://www.youtube.com/embed/X5MFlG-g3U8"}
        ]
    },
    "TWS (투어스)": {
        "멤버": ["신유", "도훈", "영재", "한진", "지훈", "경민"],
        "설명": "플레디스 엔터테인먼트 소속의 6인조 보이그룹. 보이 넥스트 도어의 동생 그룹이자 세븐틴 동생 그룹으로 2024년 데뷔했어요. 밝고 긍정적인 '보이후드 팝' 장르를 표방해요!",
        "사진_링크": "https://img.osen.co.kr/article/2024/03/14/202403140924773809_650x.jpg",
        "인기곡": [
            {"title": "첫 만남은 계획대로 되지 않아", "youtube_link": "https://www.youtube.com/embed/mE9pQvI-iT0"},
            {"title": "BFF", "youtube_link": "https://www.youtube.com/embed/p79q6cM28gE"},
            {"title": "unplugged boy", "youtube_link": "https://www.youtube.com/embed/0kI4_7_yP-8"}
        ]
    },
    "EXO (엑소)": {
        "멤버": ["수호", "시우민", "백현", "첸", "찬열", "디오", "카이", "세훈"],
        "설명": "SM엔터테인먼트 소속의 보이그룹. '으르렁', 'CALL ME BABY' 등으로 큰 인기를 얻으며 K-POP의 황금기를 이끈 대표적인 그룹이에요!",
        "사진_링크": "https://file.osen.co.kr/article/2023/07/11/202307111059775269_650x.jpg",
        "인기곡": [
            {"title": "으르렁 (Growl)", "youtube_link": "https://www.youtube.com/embed/I3dezFzsNig"},
            {"title": "CALL ME BABY", "youtube_link": "https://www.youtube.com/embed/yWfsla_Um80"},
            {"title": "Love Shot", "youtube_link": "https://www.youtube.com/embed/pX_S4L5wS0g"}
        ]
    },
    "NCT 127": {
        "멤버": ["태일", "쟈니", "태용", "유타", "도영", "재현", "정우", "마크", "해찬"],
        "설명": "SM엔터테인먼트 소속의 보이그룹 NCT의 유닛. 서울(127)을 기반으로 활동하며 'Neo Culture Technology'의 정체성을 보여주는 독특한 음악과 퍼포먼스를 선보여요!",
        "사진_링크": "https://file.osen.co.kr/article/2022/09/20/202209200827774780_650x.jpg",
        "인기곡": [
            {"title": "영웅 (英雄; Kick It)", "youtube_link": "https://www.youtube.com/embed/ZfXnL5S8VnU"},
            {"title": "2 Baddies", "youtube_link": "https://www.youtube.com/embed/w6J9d-WbFgc"},
            {"title": "Cherry Bomb", "youtube_link": "https://www.youtube.com/embed/W_rfP8K5N3c"}
        ]
    },
    
    "IVE (아이브)": {
        "멤버": ["안유진", "가을", "레이", "장원영", "리즈", "이서"],
        "설명": "스타쉽엔터테인먼트 소속의 6인조 다국적 걸그룹. 'I HAVE', 'ELEVEN', 'LOVE DIVE' 등 매번 신선하고 중독성 있는 음악으로 큰 사랑을 받고 있어요!",
        "사진_링크": "https://image.ytn.co.kr/image/general/2024/05/2710313176_t_v2.jpg",
        "인기곡": [
            {"title": "I AM", "youtube_link": "https://www.youtube.com/embed/6ZUIwj3FgEQ"},
            {"title": "LOVE DIVE", "youtube_link": "https://www.youtube.com/embed/Y8JFxS1HlDo"},
            {"title": "ELEVEN", "youtube_link": "https://www.youtube.com/embed/F0B7HDiY-1E"}
        ]
    },
    "BLACKPINK (블랙핑크)": {
        "멤버": ["지수", "제니", "로제", "리사"],
        "설명": "YG엔터테인먼트 소속의 4인조 걸그룹. 'DDU-DU DDU-DU', 'Kill This Love' 등 수많은 히트곡을 발표하며 세계적인 영향력을 가진 그룹으로 성장했어요!",
        "사진_LINK": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Blackpink_2020.png/1280px-Blackpink_2020.png",
        "인기곡": [
            {"title": "DDU-DU DDU-DU", "youtube_link": "https://www.youtube.com/embed/IHNzOHi8sJs"},
            {"title": "Kill This Love", "youtube_link": "https://www.youtube.com/embed/2S24-y03-xE"},
            {"title": "Pink Venom", "youtube_link": "https://www.youtube.com/embed/gT8_M-h-93U"}
        ]
    },
    "aespa (에스파)": {
        "멤버": ["카리나", "지젤", "윈터", "닝닝"],
        "설명": "SM엔터테인먼트 소속의 4인조 걸그룹. '자신의 또 다른 자아인 아바타(ae)를 만나 새로운 세계를 경험한다'는 독특한 세계관과 음악으로 주목받고 있어요!",
        "사진_LINK": "https://image.ytn.co.kr/image/general/2024/05/2717321048_t_v2.jpg",
        "인기곡": [
            {"title": "Next Level", "youtube_link": "https://www.youtube.com/embed/4TWR90KJl84"},
            {"title": "Drama", "youtube_link": "https://www.youtube.com/embed/KUv4A8c6i_M"},
            {"title": "Spicy", "youtube_link": "https://www.youtube.com/embed/WODg2XfG2G4"}
        ]
    },
    "NMIXX (엔믹스)": {
        "멤버": ["릴리", "해원", "설윤", "배이", "지우", "규진"],
        "설명": "JYP엔터테인먼트 소속의 6인조 걸그룹. 'MIXX POP'이라는 독자적인 음악 장르를 개척하며 기존 K-POP에서 볼 수 없었던 새로운 시도를 선보여요!",
        "사진_LINK": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/NMIXX_at_Seoul_Music_Awards_2023.jpg/1280px-NMIXX_at_Seoul_Music_Awards_2023.jpg",
        "인기곡": [
            {"title": "DICE", "youtube_link": "https://www.youtube.com/embed/p1gwD_B1QvU"},
            {"title": "O.O", "youtube_link": "https://www.youtube.com/embed/3WS_f20W2pM"},
            {"title": "Love Me Like This", "youtube_link": "https://www.youtube.com/embed/p4gC2_l_xK4"}
        ]
    },
    "TWICE (트와이스)": {
        "멤버": ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"],
        "설명": "JYP엔터테인먼트 소속의 9인조 다국적 걸그룹. 'CHEER UP', 'TT' 등 수많은 히트곡으로 국민 걸그룹으로 자리매김하며 활발하게 활동하고 있어요!",
        "사진_LINK": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Twice_in_2023.png/1280px-Twice_in_2023.png",
        "인기곡": [
            {"title": "CHEER UP", "youtube_link": "https://www.youtube.com/embed/c7rCyll5AeY"},
            {"title": "TT", "youtube_link": "https://www.youtube.com/embed/ePpPVE-GGJw"},
            {"title": "Feel Special", "youtube_link": "https://www.youtube.com/embed/3ymwXLvyuBY"}
        ]
    },
}


# --- 그룹 선택 필드 ---
st.header("🎵 어떤 그룹이 궁금해?")

group_names = list(group_database.keys())
selected_group_name = st.selectbox("아래 목록에서 궁금한 아이돌 그룹을 선택해줘!", group_names)

# --- 선택된 그룹 정보 표시 ---
if selected_group_name:
    group_info = group_database[selected_group_name]
    
    st.write("---") # 구분선
    st.subheader(f"✨ {selected_group_name} 정보! ✨")
    
    # 그룹 사진 표시
    if group_info["사진_LINK"]:
        st.image(group_info["사진_LINK"], caption=f"{selected_group_name} 그룹 사진", width=400)
    
    # 멤버 정보
    st.markdown(f"**멤버:** {', '.join(group_info['멤버'])}")
    
    # 그룹 설명
    st.markdown(f"**그룹 설명:** {group_info['설명']}")
    
    st.write("---")
    st.subheader("🎶 이 그룹의 인기곡 뮤직비디오를 감상해봐! 🎶")
    
    # 인기곡 목록과 유튜브 링크 표시
    for song in group_info['인기곡']:
        st.markdown(f"**{song['title']}**")
        
        video_id = get_youtube_video_id(song['youtube_link'])
        
        # 뮤직비디오가 앱 내에서 재생되는지 시도 (try-except)
        embedded_successfully = False
        if video_id:
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            try:
                components.html(
                    f"""
                    <iframe 
                        width="560" 
                        height="315" 
                        src="{embed_url}" 
                        frameborder="0" 
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen>
                    </iframe>
                    """,
                    height=315
                )
                embedded_successfully = True
            except Exception as e:
                # 에러 발생 시 embedded_successfully는 False로 유지
                st.error(f"뮤직비디오를 앱 내에서 재생할 수 없어요. (오류: {e})")
        
        # 앱 내에서 재생에 실패했거나 (embedded_successfully가 False), video_id를 찾지 못했거나
        if not embedded_successfully:
            # 원본 유튜브 Watch URL 생성 (embed 링크를 watch 링크로 변환)
            original_watch_url = song['youtube_link'].replace("/embed/", "/watch?v=")
            
            # 버튼 클릭 시 유튜브 화면으로 이동 (target="_blank"로 새 탭에서 열리도록)
            st.link_button(f"📺 '{song['title']}' 유튜브에서 바로 보러가기!", original_watch_url)


    st.info("다른 그룹 정보도 언제든 선택해서 볼 수 있어! 🥰")

# --- 앱 실행 방법 ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run my_idol_collection_app.py`")
