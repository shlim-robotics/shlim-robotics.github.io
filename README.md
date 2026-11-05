# Seonghyeon Lim — Personal Website

영문 연구자 홈페이지입니다. 다운로드용 CV는 `assets/Seonghyeon_Lim_CV.pdf`이며, 2026년 11월 6일 논문 링크를 갱신했습니다. 로컬 LaTeX 원본은 `../CV/main.tex`입니다.

## 로컬에서 보기

다음 명령으로 이미지를 포함한 사이트를 빌드한 뒤 확인하세요. Node.js나 패키지 설치가 필요하지 않습니다. 생성된 `dist/index.html`을 브라우저로 직접 열어도 됩니다.

```bash
cd /home/lim/shlim_ws/webpage
python3 build.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

브라우저에서 <http://localhost:8000>으로 접속합니다.

## 수정할 파일

- `index.html`: 소개, 논문, 학력, 대회, 로봇 플랫폼 및 링크
- `styles.css`: 데스크톱/모바일 레이아웃과 색상
- `script.js`: 현재 섹션 표시
- `assets/seonghyeon-lim.jpg`: 웹용으로 크기를 줄인 프로필 사진
- `assets/Seonghyeon_Lim_CV.pdf`: 다운로드용 CV
- `assets/publications/`: 논문별 썸네일 이미지
- `publication-images.json`: 이미지 설명, 캡션 및 출처 링크

Publications는 All 목록으로 논문 8편을 항상 모두 표시합니다. JavaScript를 끄거나 인쇄할 때도 모든 논문이 포함됩니다.

논문 제목, 상태 및 링크는 최신 CV를 기준으로 반영했습니다. MAPO의 OpenReview/Project 링크와 Modular Robotic Platform의 Paper/Project 링크를 포함하며, Adaptive Value Anchoring는 학회명과 연도 없이 Under review로 표시합니다. 공개 링크가 없는 논문에는 임의의 링크를 추가하지 않았습니다. 대회는 최신 CV에 수록된 ICRA 2025와 iGEM 2022 두 항목을 표시합니다.

PDF 교체 시 `assets/Seonghyeon_Lim_CV.pdf`를 새 파일로 덮어쓰면 됩니다. CV의 변경 사항이 웹 본문에 자동으로 반영되지는 않습니다.

## 논문 사진 추가 및 교체

아래 파일명으로 `assets/publications/`에 이미지를 넣고 `python3 build.py`를 실행하면 해당 논문의 **오른쪽**에 자동으로 표시됩니다. 이미지가 없으면 기존처럼 텍스트만 표시하며 빈 칸을 만들지 않습니다. 화면 폭이 760px 이하이면 이미지를 설명 아래에 배치하고, 원본 비율을 유지하며 논문 영역의 가로폭 전체를 사용합니다. 이미지 클릭 시 큰 원본이 열립니다.

| 논문 | 이미지 파일명 |
| --- | --- |
| Adaptive Value Anchoring | `value-anchoring.webp` |
| MAPO | `mapo.webp` |
| OpenHEART | `openheart.webp` |
| IK Compensation | `ik-compensation.webp` |
| ST-CBS | `st-cbs.webp` |
| Whole-Body Control / Terrain Estimation | `whole-body-control.webp` |
| Modular Robotic Platform | `modular-robot.webp` |
| Spikebot | `spikebot.webp` |

`.png`, `.jpg`, `.jpeg`, `.gif`도 지원합니다. 같은 이름의 이미지가 여러 확장자로 있으면 `.webp`, `.png`, `.jpg`, `.jpeg`, `.gif` 순서로 사용하므로 교체 시 이전 파일을 제거하세요. 다른 그림으로 바꿀 때는 `publication-images.json`의 설명, 캡션, 출처도 함께 수정하세요. 현재 캡처의 출처와 페이지는 `assets/publications/SOURCES.md`에 기록합니다.

## 배포 파일 만들기

```bash
python3 build.py
```

완성된 정적 사이트는 `dist/`에 생성됩니다. Sites 배포 설정은 `.openai/hosting.json`에 있습니다. 서버 기능이나 외부 JavaScript 라이브러리는 사용하지 않습니다.

## GitHub Pages 자동 배포

`.github/workflows/deploy.yml`이 `main`에 push할 때마다 `python3 build.py`를 실행하고 `dist/`를 배포합니다. Actions 탭에서 수동 실행할 수도 있습니다. 원본 `index.html` 대신 빌드 결과를 배포해야 논문 이미지가 포함됩니다.

개인 계정 이름을 유지하면서 별도 주소를 쓰려면 GitHub Free Organization을 만들고, 그 조직 소유의 공개 저장소를 `조직명.github.io`라는 이름으로 만드세요. 주소는 `https://조직명.github.io`입니다. 조직명은 다른 개인 계정 및 조직이 사용하지 않는 이름이어야 합니다. 개인 계정에 배포할 때도 같은 규칙으로 `계정명.github.io` 저장소를 사용합니다.

1. GitHub에서 공개 저장소를 만들고 로컬 저장소를 `origin`으로 연결해 `main`을 push합니다.
2. 저장소의 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 선택합니다.
3. **Actions → Deploy website → Run workflow**에서 `main`을 선택해 첫 배포를 실행합니다. Pages 설정 전에 실행된 작업이 실패한 경우에도 이 순서로 다시 실행하면 됩니다.
4. 배포 작업이 성공하면 **Settings → Pages**에 표시된 주소로 접속합니다. 이후에는 `main`에 push하면 자동 반영됩니다.

워크플로는 실제 Pages 주소를 `SITE_URL`로 전달하므로 공유 미리보기 이미지의 절대 주소도 자동으로 맞춰집니다. 상대 경로를 사용하므로 프로젝트 하위 경로에서도 동작합니다. 다른 호스팅에서 빌드할 때도 `SITE_URL`에 실제 홈페이지 주소를 지정하면 됩니다. 변수를 지정하지 않으면 원본 HTML의 Sites 주소를 유지합니다.

도메인을 별도로 구매했다면 GitHub Pages의 **Custom domain** 설정과 도메인 업체의 DNS를 연결할 수 있습니다. [GitHub 공식 도메인 연결 안내](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)를 참고하세요.
