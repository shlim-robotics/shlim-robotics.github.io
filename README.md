# Seonghyeon Lim — Personal Website

`../CV/main.tex`의 활성 본문과 `../CV/main.pdf`를 바탕으로 만든 영문 연구자 홈페이지입니다. [Woogyeol Jin의 홈페이지](https://wls04.github.io/)의 간결한 구성을 참고해 새로 구현했습니다.

## 로컬에서 보기

`index.html`을 브라우저로 직접 열거나, 다음 명령을 실행하세요. Node.js나 패키지 설치가 필요하지 않습니다.

```bash
cd /home/lim/shlim_ws/webpage
python3 -m http.server 8000 --bind 127.0.0.1
```

브라우저에서 <http://localhost:8000>으로 접속합니다.

## 수정할 파일

- `index.html`: 소개, 논문, 학력, 수상, 로봇 플랫폼 및 링크
- `styles.css`: 데스크톱/모바일 레이아웃과 색상
- `script.js`: 현재 섹션 표시
- `assets/seonghyeon-lim.jpg`: 웹용으로 크기를 줄인 프로필 사진
- `assets/Seonghyeon_Lim_CV.pdf`: 다운로드용 CV

Publications는 All 목록으로 논문 8편을 항상 모두 표시합니다. JavaScript를 끄거나 인쇄할 때도 모든 논문이 포함됩니다.

CV에 공개 링크가 없는 ICLR 2027 제출 논문과 CoRL 2026 accepted 논문에는 임의의 링크를 추가하지 않았습니다. 제출/게재 상태는 CV에 적힌 그대로 표시하며 자동 갱신하지 않습니다. LaTeX에서 주석 처리된 Research Experience 및 Technical Skills는 포함하지 않았습니다.

PDF 교체 시 `assets/Seonghyeon_Lim_CV.pdf`를 새 파일로 덮어쓰면 됩니다. CV의 변경 사항이 웹 본문에 자동으로 반영되지는 않습니다.

## 배포 파일 만들기

```bash
python3 build.py
```

완성된 정적 사이트는 `dist/`에 생성됩니다. Sites 배포 설정은 `.openai/hosting.json`에 있습니다. 서버 기능이나 외부 JavaScript 라이브러리는 사용하지 않습니다.

GitHub Pages에 올리려면 저장소의 웹 루트에 `dist/` 내용 또는 `index.html`, `styles.css`, `script.js`, `assets/`, `.nojekyll`을 배치하세요. 상대 경로를 사용하므로 프로젝트 하위 경로에서도 동작합니다. 다른 도메인으로 옮길 때는 `index.html`의 `og:image` URL도 해당 주소로 바꾸세요.
