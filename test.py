import streamlit as st # 웹 앱을 만들기 위한 스트림릿
import re # 정규표현식 (유튜브 링크에서 동영상 ID를 추출하기 위해)
import streamlit.components.v1 as components # HTML을 직접 삽입하기 위해 필요


# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide", page_title="시화의 슈퍼 익스트림 디테일 아이돌 가이드")

st.title("💖 넉넉한초콜릿8098님을 위한 슈퍼 익스트림 디테일 아이돌 가이드! 🌟")
st.write("와! 넉넉한초콜릿8098, 그룹 정보는 많을수록 좋지! 주요 수상부터 콘셉트까지! 모든 덕질 정보를 한눈에 볼 수 있도록 더 자세한 정보들을 추가해뒀어! 😆")
st.write("궁금한 그룹을 선택하면 데뷔일, 소속사, 팬덤명부터 멤버 정보, 인기곡 뮤직비디오까지 한눈에 보여줄게! ✨")
st.write("---") # 선 하나 쫙!

# --- 유튜브 링크에서 동영상 ID 추출 함수 ---
def get_youtube_video_id(url):
    # 일반적인 유튜브 watch?v= 또는 embed/ 링크에서 동영상 ID를 추출
    match = re.search(r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})', url)
    if match:
        return match.group(1)
    return None

# --- 아이돌 그룹 데이터베이스 ---
# 넉넉한초콜릿8098이 요청한 그룹들만 포함 + 더욱 상세한 정보 추가!
# 모든 '사진_LINK' 키는 통일되어 있습니다.
group_database = {
    "BTS (방탄소년단)": {
        "멤버": ["RM", "진", "슈가", "제이홉", "지민", "뷔", "정국"],
        "설명": "빅히트 뮤직 소속의 7인조 보이그룹. 'Dynamite', 'Butter' 등으로 전 세계적인 신드롬을 일으키며 K-POP 역사를 새로 쓰고 있는 그룹이에요!",
        "사진_LINK": "https://image.ytn.co.kr/image/general/2022/06/202206141344405367_t_v2.jpg",
        "데뷔일": "2013년 6월 13일",
        "활동_기간": "2013년 - 현재", # NEW!
        "소속사": "빅히트 뮤직",
        "팬덤명": "아미 (ARMY)",
        "응원봉_이름": "아미밤 (ARMY BOMB)",
        "공식색": ["보라색 (Purple)"],
        "주요_수상": ["빌보드 뮤직 어워드 톱 소셜 아티스트", "아메리칸 뮤직 어워드 대상", "그래미 어워드 노미네이션"], # NEW!
        "콘셉트_키워드": ["성장", "자유", "청춘", "메시지 전달"], # NEW!
        "대표곡_추가": ["FAKE LOVE", "IDOL", "DNA"], # NEW!
        "최근_활동": "멤버별 솔로 활동 활발, 각자 개성 강한 음악 선보이며 전 세계 차트 석권 중.", # NEW!
        "인기곡": [ # MV 링크용 (이전과 동일)
            {"title": "Dynamite", "youtube_link": "https://www.youtube.com/embed/gdZLi9oWNZg"},
            {"title": "Butter", "youtube_link": "https://www.youtube.com/embed/WMweEpGlu_U"},
            {"title": "Spring Day", "youtube_link": "https://www.youtube.com/embed/nM0xHBp_j_Q"}
        ]
    },
    "SEVENTEEN (세븐틴)": {
        "멤버": ["에스쿱스", "정한", "조슈아", "준", "호시", "원우", "우지", "디에잇", "민규", "도겸", "승관", "버논", "디노"],
        "설명": "플레디스 엔터테인먼트 소속의 13인조 보이그룹. '자체 제작돌'로 불리며, 퍼포먼스 팀, 힙합 팀, 보컬 팀으로 나뉘어 다채로운 매력을 선보이고 있어요!",
        "사진_LINK": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Seventeen_profile_pic.jpeg",
        "데뷔일": "2015년 5월 26일",
        "활동_기간": "2015년 - 현재", # NEW!
        "소속사": "플레디스 엔터테인먼트",
        "팬덤명": "캐럿 (CARAT)",
        "응원봉_이름": "캐럿봉 (CARAT BONG)",
        "공식색": ["로즈쿼츠 (Rose Quartz)", "세레니티 (Serenity)"],
        "주요_수상": ["골든디스크 대상", "MAMA 올해의 앨범상"], # NEW!
        "콘셉트_키워드": ["자체 제작", "청량", "칼군무", "에너지"], # NEW!
        "대표곡_추가": ["아주 NICE", "MANSAE", "CLAP"], # NEW!
        "최근_활동": "연속 앨범 밀리언셀러 달성, 월드투어 진행 중.", # NEW!
        "인기곡": [
            {"title": "Super", "youtube_link": "https://www.youtube.com/embed/e7k8-j62qXo"},
            {"title": "God of Music", "youtube_link": "https://www.youtube.com/embed/a3Lh-g9qL2Y"},
            {"title": "Don't Wanna Cry", "youtube_link": "https://www.youtube.com/embed/zEkg4GBQSMc"}
        ]
    },
    "RIIZE (라이즈)": {
        "멤버": ["쇼타로", "은석", "성찬", "원빈", "승한", "소희", "앤톤"],
        "설명": "SM엔터테인먼트 소속의 7인조 보이그룹. 'Realize & Rise'라는 의미를 담고 있으며, 독자적인 장르 '이모셔널 팝'을 추구하는 그룹이에요!",
        "사진_LINK": "https://images.fmkorea.com/files/attach/new2/20240113/4688195842/726435308/6567950798/786a3454b51a5c689617300ce4c16a50.jpg",
        "데뷔일": "2023년 9월 4일",
        "활동_기간": "2023년 - 현재", # NEW!
        "소속사": "SM엔터테인먼트",
        "팬덤명": "BRIIZE (브리즈)",
        "응원봉_이름": "미정",
        "공식색": ["미정"],
        "주요_수상": ["골든디스크 신인상", "멜론 뮤직 어워드 신인상"], # NEW!
        "콘셉트_키워드": ["이모셔널 팝", "성장", "청춘"], # NEW!
        "대표곡_추가": ["Memories", "Siren"], # NEW!
        "최근_활동": "다양한 시상식에서 신인상 석권, 일본 데뷔 준비 중.", # NEW!
        "인기곡": [
            {"title": "Get A Guitar", "youtube_link": "https://www.youtube.com/embed/f2pf1_rNvnQ"},
            {"title": "Love 119", "youtube_link": "https://www.youtube.com/embed/NfS7Q6B9Cqw"},
            {"title": "Talk Saxy", "youtube_link": "https://www.youtube.com/embed/LdYJ6WqJ9qE"}
        ]
    },
    "BOYNEXTDOOR (보이넥스트도어)": {
        "멤버": ["성호", "리우", "재현", "태산", "이한", "운학"],
        "설명": "KOZ엔터테인먼트 소속의 6인조 보이그룹. 옆집 소년들처럼 친근하고 유쾌한 매력으로 대중에게 다가가고 있어요!",
        "사진_LINK": "https://i.namu.wiki/i/n5D-G3iN4eW1h3Y2d6N9f6G4d4f2G8P5e0e0N8G4b7d5G4a2v9-U_FfU7G_e4L5s2U-9f6B9A3u0v6jF4z2v3S5z5l5P1q1C1g1j1z1h1x1c1e2h2v4l5R9P5B4K6H4F7O4K5J2e.webp",
        "데뷔일": "2023년 5월 30일",
        "활동_기간": "2023년 - 현재",
        "소속사": "KOZ엔터테인먼트",
        "팬덤명": "와이즐리 (Wiseley)",
        "응원봉_이름": "미정",
        "공식색": ["미정"],
        "주요_수상": ["MAMA 남자 신인상", "한터 뮤직 어워즈 신인상"], # NEW!
        "콘셉트_키워드": ["일상", "친근", "힙합", "개구쟁이"], # NEW!
        "대표곡_추가": ["Serenade", "But Sometimes"], # NEW!
        "최근_활동": "미니 2집 'HOW?'로 활발한 활동.", # NEW!
        "인기곡": [
            {"title": "One and Only", "youtube_link": "https://www.youtube.com/embed/MInE7d7J0bU"},
            {"title": "Serenade", "youtube_link": "https://www.youtube.com/embed/O15-M803GjQ"},
            {"title": "But Sometime", "youtube_link": "https://www.youtube.com/embed/N4tLwK4hNgs"}
        ]
    },
    "NCT WISH (엔시티 위시)": {
        "멤버": ["시온", "리쿠", "유우시", "재희", "료", "사쿠야"],
        "설명": "SM엔터테인먼트 소속의 6인조 보이그룹. 'WISH for OUR WISH'라는 캐치프레이즈로, 음악과 퍼포먼스를 통해 모든 사람들의 '소원'과 '꿈'을 응원하고 있어요!",
        "사진_LINK": "https://news.mtn.co.kr/news_content/image_html_dir/2024/02/2024022810052358897_1.jpg",
        "데뷔일": "2024년 2월 21일 (한국)",
        "활동_기간": "2024년 - 현재",
        "소속사": "SM엔터테인먼트",
        "팬덤명": "미정",
        "응원봉_이름": "미정",
        "공식색": ["미정"],
        "주요_수상": [], # NEW!
        "콘셉트_키워드": ["청량", "순수", "희망"], # NEW!
        "대표곡_추가": ["Stars Align"], # NEW!
        "최근_활동": "데뷔 싱글 'WISH' 활동, 일본에서 먼저 데뷔.", # NEW!
        "인기곡": [
            {"title": "WISH", "youtube_link": "https://www.youtube.com/embed/3-E08n8Nq5c"},
            {"title": "Hands Up", "youtube_link": "https://www.youtube.com/embed/P_3yW7mQ3vE"},
            {"title": "Stars Align", "youtube_link": "https://www.youtube.com/embed/84VwJbB34y0"}
        ]
    },
    "투모로우바이투게더 (TXT)": {
        "멤버": ["수빈", "연준", "범규", "태현", "휴닝카이"],
        "설명": "빅히트 뮤직 소속의 5인조 보이그룹. 밝고 청량한 매력으로 '성장'과 '청춘'의 서사를 노래하며 많은 사랑을 받고 있어요!",
        "사진_LINK": "https://image.ytn.co.kr/image/general/2024/03/2908581024_t_v2.jpg",
        "데뷔일": "2019년 3월 4일",
        "활동_기간": "2019년 - 현재",
        "소속사": "빅히트 뮤직",
        "팬덤명": "모아 (MOA)",
        "응원봉_이름": "투바투봉",
        "공식색": ["미정"],
        "주요_수상": ["골든디스크 넥스트 제너레이션", "서울가요대상 본상"], # NEW!
        "콘셉트_키워드": ["성장통", "상상", "판타지", "청춘"], # NEW!
        "대표곡_추가": ["Crown", "Can't You See Me?"], # NEW!
        "최근_활동": "다양한 해외 무대 및 페스티벌 참여, 활발한 앨범 활동.", # NEW!
        "인기곡": [
            {"title": "Sugar Rush Ride", "youtube_link": "https://www.youtube.com/embed/MADXyqR0cQ4"},
            {"title": "Good Boy Gone Bad", "youtube_link": "https://www.youtube.com/embed/y_HwJ718pYw"},
            {"title": "Run Away", "youtube_link": "https://www.youtube.com/embed/X5MFlG-g3U8"}
        ]
    },
    "TWS (투어스)": {
        "멤버": ["신유", "도훈", "영재", "한진", "지훈", "경민"],
        "설명": "플레디스 엔터테인먼트 소속의 6인조 보이그룹. 보이 넥스트 도어의 동생 그룹이자 세븐틴 동생 그룹으로 2024년 데뷔했어요. 밝고 긍정적인 '보이후드 팝' 장르를 표방해요!",
        "사진_LINK": "https://img.osen.co.kr/article/2024/03/14/202403140924773809_650x.jpg",
        "데뷔일": "2024년 1월 22일",
        "활동_기간": "2024년 - 현재",
        "소속사": "플레디스 엔터테인먼트",
        "팬덤명": "42(싸이)",
        "응원봉_이름": "미정",
        "공식색": ["미정"],
        "주요_수상": [], # NEW!
        "콘셉트_키워드": ["소년", "청량", "친구", "첫 만남"], # NEW!
        "대표곡_추가": ["plot twist", "BFF"], # NEW!
        "최근_활동": "데뷔곡 '첫 만남은 계획대로 되지 않아'로 음악 방송 1위 차지.", # NEW!
        "인기곡": [
            {"title": "첫 만남은 계획대로 되지 않아", "youtube_link": "https://www.youtube.com/embed/mE9pQvI-iT0"},
            {"title": "BFF", "youtube_link": "https://www.youtube.com/embed/p79q6cM28gE"},
            {"title": "unplugged boy", "youtube_link": "https://www.youtube.com/embed/0kI4_7_yP-8"}
        ]
    },
    "EXO (엑소)": {
        "멤버": ["수호", "시우민", "백현", "첸", "찬열", "디오", "카이", "세훈"],
        "설명": "SM엔터테인먼트 소속의 보이그룹. '으르렁', 'CALL ME BABY' 등으로 큰 인기를 얻으며 K-POP의 황금기를 이끈 대표적인 그룹이에요!",
        "사진_LINK": "https://file.osen.co.kr/article/2023/07/11/202307111059775269_650x.jpg",
        "데뷔일": "2012년 4월 8일",
        "활동_기간": "2012년 - 현재",
        "소속사": "SM엔터테인먼트",
        "팬덤명": "엑소-엘 (EXO-L)",
        "응원봉_이름": "에리디봉",
        "공식색": ["코스믹 라떼 (Cosmic Latte)"],
        "주요_수상": ["MAMA 올해의 앨범상", "골든디스크 대상", "서울가요대상 대상"], # NEW!
        "콘셉트_키워드": ["초능력", "SF", "웅장", "다크"], # NEW!
        "대표곡_추가": ["Growl", "Overdose", "Monster"], # NEW!
        "최근_활동": "솔로 활동 및 유닛 활동 병행, 멤버별 다양한 분야에서 활약.", # NEW!
        "인기곡": [
            {"title": "으르렁 (Growl)", "youtube_link": "https://www.youtube.com/embed/I3dezFzsNig"},
            {"title": "CALL ME BABY", "youtube_link": "https://www.youtube.com/embed/yWfsla_Um80"},
            {"title": "Love Shot", "youtube_link": "https://www.youtube.com/embed/pX_S4L5wS0g"}
        ]
    },
    "NCT 127": {
        "멤버": ["태일", "쟈니", "태용", "유타", "도영", "재현", "정우", "마크", "해찬"],
        "설명": "SM엔터테인먼트 소속의 보이그룹 NCT의 유닛. 서울(127)을 기반으로 활동하며 'Neo Culture Technology'의 정체성을 보여주는 독특한 음악과 퍼포먼스를 선보여요!",
        "사진_LINK": "https://file.osen.co.kr/article/2022/09/20/202209200827774780_650x.jpg",
        "데뷔일": "2016년 7월 7일",
        "활동_기간": "2016년 - 현재",
        "소속사": "SM엔터테인먼트",
        "팬덤명": "시즈니 (NCTzen)",
        "응원봉_이름": "응원봉",
        "공식색": ["펄 네오 샴페인 (Pearl Neo Champagne)"],
        "주요_수상": ["서울가요대상 본상", "가온차트 뮤직 어워즈 올해의 가수상"], # NEW!
        "콘셉트_키워드": ["힙합", "네오", "시크", "파워풀"], # NEW!
        "대표곡_추가": ["Cherry Bomb", "Regular", "Kick It"], # NEW!
        "최근_활동": "정규 5집 'Fact Check' 활동 및 콘서트 투어.", # NEW!
        "인기곡": [
            {"title": "영웅 (英雄; Kick It)", "youtube_link": "https://www.youtube.com/embed/ZfXnL5S8VnU"},
            {"title": "2 Baddies", "youtube_link": "https://www.youtube.com/embed/w6J9d-WbFgc"},
            {"title": "Cherry Bomb", "youtube_link": "https://www.youtube.com/embed/W_rfP8K5N3c"}
        ]
    },
    
    "IVE (아이브)": {
        "멤버": ["안유진", "가을", "레이", "장원영", "리즈", "이서"],
        "설명": "스타쉽엔터테인먼트 소속의 6인조 다국적 걸그룹. 'I HAVE', 'ELEVEN', 'LOVE DIVE' 등 매번 신선하고 중독성 있는 음악으로 큰 사랑을 받고 있어요!",
        "사진_LINK": "https://image.ytn.co.kr/image/general/2024/05/2710313176_t_v2.jpg",
        "데뷔일": "2021년 12월 1일",
        "활동_기간": "2021년 - 현재", # NEW!
        "소속사": "스타쉽 엔터테인먼트",
        "팬덤명": "다이브 (DIVE)",
        "응원봉_이름": "아이브봉 (IVE BONG)",
        "공식색": ["짙은 남색 (Deep Blue)"],
        "주요_수상": ["골든디스크 대상", "MMA 올해의 베스트송", "MAMA 대상"], # NEW!
        "콘셉트_키워드": ["자기애", "당당함", "우아함", "MZ세대"], # NEW!
        "대표곡_추가": ["ELEVEN", "LOVE DIVE", "After LIKE"], # NEW!
        "최근_활동": "미니 2집 'IVE SWITCH'로 컴백, 다채로운 퍼포먼스 선보임.", # NEW!
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
        "데뷔일": "2016년 8월 8일",
        "활동_기간": "2016년 - 현재", # NEW!
        "소속사": "YG엔터테인먼트",
        "팬덤명": "블링크 (BLINK)",
        "응원봉_이름": "블링크봉 (BLINK BONG)",
        "공식색": ["블랙 (Black)", "핑크 (Pink)"],
        "주요_수상": ["MTV VMAs 올해의 그룹", "아시아 아티스트 어워즈 대상"], # NEW!
        "콘셉트_키워드": ["걸크러쉬", "힙합", "럭셔리", "트렌드세터"], # NEW!
        "대표곡_추가": ["DDU-DU DDU-DU", "How You Like That", "Lovesick Girls"], # NEW!
        "최근_활동": "멤버별 솔로 활동 활발, 글로벌 앰버서더로 패션계 영향력 확대.", # NEW!
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
        "데뷔일": "2020년 11월 17일",
        "활동_기간": "2020년 - 현재", # NEW!
        "소속사": "SM엔터테인먼트",
        "팬덤명": "MY (마이)",
        "응원봉_이름": "마이봉 (MY BONG)",
        "공식색": ["미정"],
        "주요_수상": ["골든디스크 디지털 음원 본상", "서울가요대상 본상"], # NEW!
        "콘셉트_키워드": ["메타버스", "AI", "블랙맘바", "강력함"], # NEW!
        "대표곡_추가": ["Next Level", "Savage", "Girls"], # NEW!
        "최근_활동": "정규 1집 'Armageddon' 발매, 강렬한 콘셉트로 활동.", # NEW!
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
        "데뷔일": "2022년 2월 22일",
        "활동_기간": "2022년 - 현재",
        "소속사": "JYP엔터테인먼트",
        "팬덤명": "엔써 (NSWER)",
        "응원봉_이름": "엔라이트 (Nlight)",
        "공식색": ["미정"],
        "주요_수상": ["서울가요대상 신인상", "MAMA 페이보릿 뉴 아티스트"], # NEW!
        "콘셉트_키워드": ["믹스 팝", "다채로움", "자유", "다인원"], # NEW!
        "대표곡_추가": ["DICE", "O.O", "Love Me Like This"], # NEW!
        "최근_활동": "미니 2집 'Fe3O4: BREAK' 발매, 타이틀곡 'DASH'로 활동.", # NEW!
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
        "데뷔일": "2015년 10월 20일",
        "활동_기간": "2015년 - 현재",
        "소속사": "JYP엔터테인먼트",
        "팬덤명": "원스 (ONCE)",
        "응원봉_이름": "캔디봉 (CANDYBONG)",
        "공식색": ["애프리콧 (Apricot)", "네온 마젠타 (Neon Magenta)"],
        "주요_수상": ["골든디스크 대상", "MAMA 올해의 가수상", "멜론 뮤직 어워드 올해의 노래상"], # NEW!
        "콘셉트_키워드": ["에너지", "큐티", "청량", "글로벌"], # NEW!
        "대표곡_추가": ["CHEER UP", "TT", "Feel Special", "SIGNAL"], # NEW!
        "최근_활동": "미니 13집 'With YOU-th' 발매, 월드투어 진행 중.", # NEW!
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
    if "사진_LINK" in group_info and group_info["사진_LINK"]: # '사진_LINK' 키가 있는지 먼저 확인하고 표시
        st.image(group_info["사진_LINK"], caption=f"{selected_group_name} 그룹 사진", width=400)
    
    # 상세 정보 출력
    st.markdown(f"**데뷔일:** {group_info.get('데뷔일', '정보 없음')}")
    st.markdown(f"**활동 기간:** {group_info.get('활동_기간', '정보 없음')}") # NEW!
    st.markdown(f"**소속사:** {group_info.get('소속사', '정보 없음')}")
    st.markdown(f"**팬덤명:** {group_info.get('팬덤명', '정보 없음')}")
    st.markdown(f"**응원봉 이름:** {group_info.get('응원봉_이름', '정보 없음')}")
    
    # 공식 색상이 리스트일 경우와 아닐 경우 처리
    official_color = group_info.get('공식색', ['정보 없음'])
    if isinstance(official_color, list):
        st.markdown(f"**공식 색상:** {', '.join(official_color)}")
    else:
        st.markdown(f"**공식 색상:** {official_color}")

    # 주요 수상
    main_awards = group_info.get('주요_수상', []) # NEW!
    if main_awards:
        st.markdown(f"**주요 수상:** {', '.join(main_awards)}")
    else:
        st.markdown(f"**주요 수상:** 정보 없음")

    # 콘셉트 키워드
    concept_keywords = group_info.get('콘셉트_키워드', []) # NEW!
    if concept_keywords:
        st.markdown(f"**콘셉트 키워드:** {', '.join(concept_keywords)}")
    else:
        st.markdown(f"**콘셉트 키워드:** 정보 없음")

    # 대표곡 (인기곡 MV와는 별도로 명시)
    top_songs = group_info.get('대표곡_추가', []) # NEW!
    if top_songs:
        st.markdown(f"**대표곡:** {', '.join(top_songs)}")
    else:
        st.markdown(f"**대표곡:** 정보 없음")

    # 최근 활동
    recent_activity = group_info.get('최근_활동', '정보 없음') # NEW!
    st.markdown(f"**최근 활동:** {recent_activity}")

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
st.sidebar.write("예: `streamlit run my_extreme_detail_idol_app.py`")
