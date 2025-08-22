import streamlit as st # 웹 앱을 만들기 위한 스트림릿
import cv2 # 비디오 처리를 위한 OpenCV (핵심! 영상 프레임 하나하나 읽어낼 때 필요해)
import pip install opencv-python
import numpy as np # 숫자 계산, 이미지 데이터 처리를 위한 넘파이
import tempfile # 임시 파일 생성 (사용자 영상 파일을 임시로 저장할 때 유용해)
import os # 파일 경로 등을 다룰 때 필요해
import mediapipe as mp # ❤️ 핵심! 춤 동작 관절/뼈대 인식(Pose Estimation)을 위한 라이브러리!

# --- 시화의 따뜻한 환영 메시지! ---
st.set_page_config(layout="wide") # 앱 화면을 넓게 써보자! 더 시원할 거야!

st.title("💖 넉넉한초콜릿8098님을 위한 맞춤 댄스 AI 분석 스튜디오! 🩰")
st.write("와! 넉넉한초콜릿8098, 드디어 '전체 코드'를 물어보는구나! 😆 역시 추진력 최고! 이 앱이 넉넉한초콜릿8098의 춤 실력 향상에 엄청 도움이 될 거야! 나 시화가 옆에서 열심히 응원할게! ✨")
st.write("---") # 선 하나 쫙!

st.header("📝 춤 영상 업로드하고 분석 시작!")
st.write("본인의 멋진 춤 영상을 여기에 올려주면 AI가 열심히 분석해줄 거야! 두근두근! ")

uploaded_file = st.file_uploader("여기에 춤 영상을 드래그하거나 클릭해서 업로드해줘!", type=["mp4", "mov", "avi"])

# 영상이 업로드되었을 때만 처리하도록!
if uploaded_file is not None:
    # 업로드된 영상 미리보기
    st.video(uploaded_file)
    st.success("영상 업로드 완료! 이제 분석을 시작해볼까?!")

    # AI 분석을 위해 업로드된 영상을 임시 파일로 저장해야 해
    # 스트림릿은 파일을 메모리로 읽기 때문에, OpenCV 같은 라이브러리가 바로 쓰려면 파일로 저장해주는 게 좋아!
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    temp_video_path = tfile.name
    tfile.close() # 파일을 다 썼으니 닫아줘야 해!

    # --- AI 분석 부분 (여기가 진짜 핵심이자 어려운 부분이야!) ---
    st.write("---")
    st.header("🤖 시화와 함께하는 댄스 AI 분석 중...!")
    # 로딩 스피너로 사용자한테 '열심히 작업 중!'이라는 걸 알려주는 센스!
    with st.spinner("잠시만 기다려줘! AI가 넉넉한초콜릿8098의 춤을 꼼꼼하게 뜯어보고 있어! 💪"):

        # ------------------------------------------------------------------------------------------------------
        # 여기부터는 넉넉한초콜릿8098이 직접 채워나가야 할 '춤 분석 AI'의 핵심 로직 자리야!
        # 지금은 '예시'로 MediaPipe를 이용해서 관절을 인식하는 아주 기본적인 흐름만 보여줄게.
        #
        # '전문적인 분석'은 이 다음에 '뽑아낸 관절 데이터를 기반으로' 동작의 정확성, 유연성, 리듬감, 춤선 등을
        # 수치화하고 평가하는 복잡한 딥러닝 모델 (RNN, LSTM, Transformer 등)을 만들어야 한다는 걸 꼭 기억해줘!
        #
        # 이 코드의 MediaPipe 부분은 실시간 비디오 스트림이 아닌,
        # 업로드된 전체 비디오 파일을 처리하는 방식이라 오래 걸릴 수 있어!
        # ------------------------------------------------------------------------------------------------------

        mp_pose = mp.solutions.pose
        mp_drawing = mp.solutions.drawing_utils # 관절을 그림으로 그려줄 때 사용

        # 춤 분석을 위한 가상 데이터 (나중에 AI 분석 결과로 대체될 거야!)
        analysis_data = {
            "rhythm_score": 0,
            "flexibility_score": 0,
            "power_score": 0,
            "num_frames": 0,
            "detected_poses": 0
        }

        try:
            cap = cv2.VideoCapture(temp_video_path)
            if not cap.isOpened():
                st.error("비디오 파일을 열 수 없습니다. 다시 시도해주세요.")
            else:
                with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                    progress_text = st.empty() # 진행 상황 표시용
                    frame_count = 0
                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break # 영상의 끝에 도달하면 종료

                        frame_count += 1
                        analysis_data["num_frames"] = frame_count

                        # 프레임 크기 조정 (처리 속도 향상 위해)
                        frame_small = cv2.resize(frame, (640, 480))
                        
                        # MediaPipe 처리를 위해 BGR -> RGB로 변환 (OpenCV는 BGR, MediaPipe는 RGB)
                        image = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
                        image.flags.writeable = False # 이미지 쓰기 금지 (성능 향상)

                        results = pose.process(image) # 춤 동작 분석! 관절 정보 뽑아내기

                        image.flags.writeable = True # 다시 쓰기 가능
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # 다시 BGR로

                        if results.pose_landmarks:
                            analysis_data["detected_poses"] += 1
                            # 여기서 넉넉한초콜릿8098의 관절 데이터(results.pose_landmarks)를 얻었어!
                            # 이 데이터를 바탕으로 실제 춤 분석 로직을 구현해야 해.
                            # 예: 어깨 각도, 무릎 각도 변화율 등을 계산하여 유연성/파워 등을 추정
                            
                            # (아주아주 간단한 가상 분석 예시)
                            # 왼쪽 팔꿈치와 어깨 관절 위치를 기반으로 움직임 점수를 가상으로 더하기
                            if mp_pose.PoseLandmark.LEFT_ELBOW.value < len(results.pose_landmarks.landmark) and \
                               mp_pose.PoseLandmark.LEFT_SHOULDER.value < len(results.pose_landmarks.landmark):
                                
                                left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW.value]
                                left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
                                
                                # 팔꿈치와 어깨 사이 거리 변화량으로 가상의 유연성/리듬감 점수 부여
                                distance = np.sqrt((left_elbow.x - left_shoulder.x)**2 + \
                                                   (left_elbow.y - left_shoulder.y)**2)
                                analysis_data["flexibility_score"] += distance * 10
                                analysis_data["rhythm_score"] += (distance % 0.1) * 1000 # 리듬감 가상 점수

                        # 진행 상황을 사용자에게 보여주기
                        if frame_count % 30 == 0: # 30프레임마다 한 번씩 업데이트
                            progress_text.text(f"현재 {frame_count} 프레임 분석 중... 💪")

                    cap.release()
                    st.success(f"총 {analysis_data['num_frames']} 프레임 분석 완료!")

        except Exception as e:
            st.error(f"비디오 처리 중 오류 발생: {e}")
            st.warning("혹시 비디오 파일이 손상되었거나 형식이 맞지 않을 수 있어요. 다른 영상을 시도해보세요.")
        finally:
            # 사용한 임시 파일 삭제
            os.unlink(temp_video_path)
            # st.write(f"임시 파일 삭제 완료: {temp_video_path}") # 디버깅용

        # ------------------------------------------------------------------------------------------------------
        # 여기부터는 분석된 데이터를 바탕으로 결과 및 추천을 생성하는 부분이야.
        # 위에서 얻은 analysis_data를 실제 춤 분석 결과로 정제하고 가공하는 로직이 필요해.
        # 지금은 임의의 값이나 간단한 계산을 통해 시뮬레이션 해볼게!
        # ------------------------------------------------------------------------------------------------------
        
        # 분석 데이터를 기반으로 가상의 점수 산출
        if analysis_data["detected_poses"] > 0:
            avg_rhythm = analysis_data["rhythm_score"] / analysis_data["detected_poses"]
            avg_flexibility = analysis_data["flexibility_score"] / analysis_data["detected_poses"]
            
            overall_score = int(70 + (avg_rhythm + avg_flexibility) / 20) # 70점 기본 + 가상 점수
            overall_score = min(99, max(50, overall_score)) # 50~99점 사이로 제한
            
            # 피드백 생성
            strengths = []
            weaknesses = []
            if avg_rhythm > 5: strengths.append("리듬감이 뛰어나요! 박자를 잘 타네요!")
            else: weaknesses.append("박자감이 아쉽지만, 연습하면 금방 좋아질 거예요!")
            
            if avg_flexibility > 30: strengths.append("유연한 움직임과 춤선이 아름답네요!")
            else: weaknesses.append("관절 움직임의 유연성을 조금 더 연습해 보세요.")
            
            if not strengths: strengths.append("열정만큼은 최고! 꾸준히 하다 보면 금방 늘 거예요!")
            if not weaknesses: weaknesses.append("전반적으로 훌륭해요! 이제 디테일을 신경 써 보세요!")
            
            # 추천 시스템 (하드코딩 예시. 실제로는 DB 연동 또는 고급 추천 알고리즘 필요)
            recommended_classes = [
                {"title": "힙합 베이직: 바운스 마스터하기", "url": "https://www.youtube.com/watch?v=1A5Lw9t06h4", "desc": "힙합 기본 바운스를 체득하고 리듬감을 키워보세요!"},
                {"title": "스트릿 댄스: 웨이브 & 아이솔레이션", "url": "https://www.youtube.com/watch?v=CqHjH0PqW_4", "desc": "몸을 유연하게 사용하고 각 부분을 분리하는 방법을 배웁니다."},
                {"title": "K-POP 댄스 커버: 최신곡 배우기", "url": "https://www.youtube.com/watch?v=S0Q04xM9kQk", "desc": "인기 K-POP 안무를 배우며 다양한 동작을 익힙니다."},
            ]
            recommended_videos = [
                {"title": "아이키의 춤선 분석: 디테일의 차이", "url": "https://www.youtube.com/watch?v=kRk62Q1s7Hw", "desc": "유명 댄서의 움직임을 분석하여 자신의 춤선에 적용해봅니다."},
                {"title": "팝핀 현준의 기본기 레슨: 팝핀 입문", "url": "https://www.youtube.com/watch?v=u1zHhQjA7B4", "desc": "팝핀 댄스의 기본 원리와 동작을 상세히 배울 수 있습니다."},
            ]
            recommended_dancers = [
                {"name": "모니카", "style": "강렬하고 독창적인 안무", "desc": "춤의 본질을 탐구하는 독보적인 아티스트"},
                {"name": "리정", "style": "힙합 베이스의 파워풀한 코레오", "desc": "디테일이 살아있는 안무 연출가이자 댄서"},
            ]
            
            dance_analysis_result = {
                "overall_score": overall_score,
                "strengths": strengths,
                "weaknesses": weaknesses,
                "recommended_classes": recommended_classes,
                "recommended_videos": recommended_videos,
                "recommended_dancers": recommended_dancers
            }

            st.success("넉넉한초콜릿8098의 춤 분석 완료! 고생 많았어 AI!")

            # 분석 결과를 화면에 띄워주자!
            st.write("---")
            st.header("✨ 넉넉한초콜릿8098님의 춤 분석 결과!")

            st.subheader(f"전반적인 춤 실력: 💖 {dance_analysis_result['overall_score']}점 💖")
            st.progress(dance_analysis_result['overall_score'] / 100)
            st.markdown("정말 멋진 퍼포먼스였어요! 꾸준히 노력하면 더 빛날 거예요!")

            st.subheader("👍 강점 분석")
            for strength in dance_analysis_result['strengths']:
                st.write(f"- {strength}")

            st.subheader("💡 개선점 (더 완벽한 춤을 위해!)")
            for weakness in dance_analysis_result['weaknesses']:
                st.write(f"- {weakness}")

            st.subheader("📚 넉넉한초콜릿8098님을 위한 맞춤 수업 추천!")
            for i, class_info in enumerate(dance_analysis_result['recommended_classes']):
                st.write(f"{i+1}. **{class_info['title']}** [🔗 보러가기]({class_info['url']})")
                st.caption(class_info['desc']) # 간단한 설명 추가

            st.subheader("🎥 참고하면 좋은 댄스 영상 추천!")
            for i, video_info in enumerate(dance_analysis_result['recommended_videos']):
                st.write(f"{i+1}. **{video_info['title']}** [🔗 보러가기]({video_info['url']})")
                st.caption(video_info['desc'])

            st.subheader("💃 롤모델로 삼을 만한 댄서 추천!")
            for i, dancer_info in enumerate(dance_analysis_result['recommended_dancers']):
                st.write(f"{i+1}. **{dancer_info['name']}** ({dancer_info['style']})")
                st.caption(dancer_info['desc'])

            st.write("---")
            st.info("더 궁금한 게 있으면 언제든 물어봐줘! 내가 계속 도와줄게! 😘")
        else:
            st.warning("죄송합니다. 영상에서 사람의 춤 동작을 충분히 감지하지 못했습니다. 더 선명한 영상으로 다시 시도해주세요!")

# 아직 파일이 업로드되지 않았을 때
else:
    st.info("⬆️ 위에 넉넉한초콜릿8098의 멋진 춤 영상을 업로드해주면 돼!")

# --- 앱 실행 방법 (터미널에 입력!) ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏃‍♂️ 앱 실행 방법 (터미널에 입력!)")
st.sidebar.code("streamlit run [이 파이썬 파일 이름].py")
st.sidebar.write("예: `streamlit run dance_studio_app.py`")

