# ADK Coding Test Generator Agent

이 프로젝트는 Google Agent Development Kit(ADK)를 활용하여 코딩 테스트 문제를 자동으로 생성, 검증, 해결하고 테스트 케이스까지 만들어주는 AI 에이전트 시스템입니다.

![아키텍처 다이어그램](https://raw.githubusercontent.com/jeyong-shin/adk-codingtest-gen-agent/main/architecture.png)

## 프로젝트 구조

```
.
├── codingtest-generator/
│   ├── agent.py                       # 메인 에이전트 정의
│   ├── prompts.py                     # 메인 에이전트 프롬프트
│   ├── .env.example                   # 환경 변수 예시 파일
│   ├── constants/
│   │   └── constants.py               # 공통 상수 정의
│   └── sub_agents/                    # 하위 에이전트들
│       ├── problem_critic/            # 문제 검토 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       ├── problem_generator/         # 문제 생성 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       ├── problem_loop/              # 문제 생성 루프 관리 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       ├── problem_quality_checker/   # 문제 품질 검사 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       ├── problem_solver/            # 문제 해결 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       ├── test_case_generator/       # 테스트 케이스 생성 에이전트
│       │   ├── agents.py
│       │   └── prompts.py
│       └── topic_finder/              # 문제 주제 탐색 에이전트
│           ├── agents.py
│           └── prompts.py
├── .gitignore                         # Git 무시 파일 설정
├── README.md                          # 프로젝트 설명 문서
├── requirements.txt                   # 필요 패키지 목록
├── LICENSE                            # 라이센스
└── architecture.png                   # 에이전트 구조 다이어그램
```

## 에이전트 아키텍처

이 프로젝트는 하나의 메인 에이전트와 7개의 하위 에이전트로 구성됩니다:

1. **메인 에이전트**: 전체 프로세스를 관리하고 하위 에이전트들을 조정합니다.

2. **Topic Finder**: 코딩 테스트 문제의 주제를 제안하고 선택합니다.

3. **Problem Loop**: 문제 생성 프로세스를 관리하며 다음 세 에이전트를 반복적으로 활용합니다:
   - **Problem Generator**: 지정된 주제에 맞는 코딩 테스트 문제를 생성합니다.
   - **Problem Critic**: 생성된 문제의 품질을 비판적으로 검토합니다.
   - **Problem Quality Checker**: 비판 결과를 바탕으로 문제의 합격/불합격 여부를 결정합니다.

4. **Problem Solver**: 합격된 문제에 대한 해답을 Java, JavaScript, Python으로 제공합니다.

5. **Test Case Generator**: 문제 검증을 위한 테스트 케이스 생성 Python 스크립트를 작성합니다.

## 설치 및 실행 방법

### 필수 요구사항
- Python 3.9 이상
- Google ADK 계정 및 API 키

### 설치 단계

1. 저장소 복제
   ```bash
   git clone https://github.com/jeyong-shin/adk-codingtest-gen-agent.git
   cd adk-codingtest-gen-agent
   ```

2. 가상 환경 설정
   ```bash
   python -m venv venv
   ```

3. 가상 환경 활성화
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     .\venv\Scripts\Activate.bat
     ```

4. 필요한 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```

5. 환경 변수 설정
   ```bash
   cp codingtest-generator/.env.example codingtest-generator/.env
   ```
   `.env` 파일을 편집하여 필요한 API 키와 설정을 입력하세요.

6. ADK 웹 서버 실행
   ```bash
   adk web
   ```

## 사용 방법

1. 브라우저에서 `http://localhost:8000`(또는 ADK가 표시하는 URL)에 접속합니다.
2. 에이전트와 대화를 시작하고 코딩 테스트 문제 생성을 요청합니다.
3. 에이전트는 다음과 같은 과정을 통해 코딩 테스트 문제를 생성합니다:
   - 적절한 주제 제안 및 선택
   - 문제 생성, 비판, 품질 검사의 반복 과정
   - 합격된 문제에 대한 다양한 언어로의 해답 제공
   - 테스트 케이스 생성 스크립트 제공

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
