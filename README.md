# Seonghyeon Lim — Personal Website

영문 연구자 홈페이지입니다. 최신 본문과 다운로드 파일은 `/home/lim/Downloads/seonghyeon_lim_cv.pdf`를 기준으로 2026년 11월 5일 갱신했습니다. [Woogyeol Jin의 홈페이지](https://wls04.github.io/)의 간결한 구성을 참고해 새로 구현했습니다.

## 로컬에서 보기

`index.html`을 브라우저로 직접 열거나, 다음 명령을 실행하세요. Node.js나 패키지 설치가 필요하지 않습니다.

```bash
cd /home/lim/shlim_ws/webpage
python3 -m http.server 8000 --bind 127.0.0.1
```

브라우저에서 <http://localhost:8000>으로 접속합니다.

## 수정할 파일

- `index.html`: 소개, 논문, 학력, 대회, 로봇 플랫폼 및 링크
- `styles.css`: 데스크톱/모바일 레이아웃과 색상
- `script.js`: 현재 섹션 표시
- `assets/seonghyeon-lim.jpg`: 웹용으로 크기를 줄인 프로필 사진
- `assets/Seonghyeon_Lim_CV.pdf`: 다운로드용 CV

Publications는 All 목록으로 논문 8편을 항상 모두 표시합니다. JavaScript를 끄거나 인쇄할 때도 모든 논문이 포함됩니다.

논문 제목, 상태 및 링크는 최신 PDF를 기준으로 반영했습니다. MAPO의 OpenReview/Project 링크와 iGEM Software 링크를 포함하며, ICLR 2027 논문은 Under review로 표시합니다. 공개 링크가 없는 논문에는 임의의 링크를 추가하지 않았습니다. 대회는 최신 CV에 수록된 ICRA 2025와 iGEM 2022 두 항목을 표시합니다.

PDF 교체 시 `assets/Seonghyeon_Lim_CV.pdf`를 새 파일로 덮어쓰면 됩니다. CV의 변경 사항이 웹 본문에 자동으로 반영되지는 않습니다.

## 배포 파일 만들기

```bash
python3 build.py
```

완성된 정적 사이트는 `dist/`에 생성됩니다. Sites 배포 설정은 `.openai/hosting.json`에 있습니다. 서버 기능이나 외부 JavaScript 라이브러리는 사용하지 않습니다.

GitHub Pages에 올리려면 저장소의 웹 루트에 `dist/` 내용 또는 `index.html`, `styles.css`, `script.js`, `assets/`, `.nojekyll`을 배치하세요. 상대 경로를 사용하므로 프로젝트 하위 경로에서도 동작합니다. 다른 도메인으로 옮길 때는 `index.html`의 `og:image` URL도 해당 주소로 바꾸세요.
