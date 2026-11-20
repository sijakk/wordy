# 워디(WORDY) 사이트 배포 가이드 — sijakk.com

이 폴더를 그대로 GitHub Pages에 올리면 `https://sijakk.com` 에서 워디가 열립니다.

## 폴더 구성

| 파일 | 설명 |
|---|---|
| `index.html` | 워디 앱 (Lite 기반, 구글 보상형 광고 연동 코드 포함) |
| `privacy.html` | 개인정보처리방침 (애드센스 심사에 필요) |
| `ads.txt` | 애드센스 판매자 인증 파일 (퍼블리셔 ID 입력 필요) |
| `CNAME` | GitHub Pages에 연결할 도메인 (`sijakk.com`) |
| `manifest.json`, `icon-*.png`, `apple-touch-icon.png` | 홈 화면 추가용 앱 아이콘·정보 |

---

## 1단계. GitHub Pages에 올리기 (약 10분)

1. GitHub에서 **New repository** → 이름 예: `wordy` → Public → Create
2. **Add file > Upload files** 로 이 폴더의 파일을 전부 올리고 Commit
3. 저장소 **Settings > Pages**
   - Source: **Deploy from a branch** / Branch: **main** / 폴더: **/(root)** → Save
   - **Custom domain** 에 `sijakk.com` 입력 → Save
4. 몇 분 뒤 `https://<GitHub아이디>.github.io/wordy` 로 열리는지 확인

## 2단계. 도메인 연결 (도메인 구입처 DNS 설정)

도메인을 산 곳(가비아·카페24·후이즈·Cloudflare 등)의 **DNS 관리**에서:

1. 기존 사이트를 가리키던 `@`(루트)의 **A 레코드 / CNAME 레코드를 삭제**
2. 아래 레코드를 추가

| 타입 | 호스트 | 값 |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<GitHub아이디>.github.io` |

3. 반영까지 몇 분~최대 24시간. 이후 GitHub **Settings > Pages** 에서 **Enforce HTTPS** 체크

## 3단계. 애드센스 가입·사이트 승인 (며칠~4주)

1. https://adsense.google.com 가입 → **사이트 > 새 사이트** 에 `sijakk.com` 추가
2. 퍼블리셔 ID(`ca-pub-숫자16자리`)를 확인한 뒤:
   - `ads.txt` 의 `pub-XXXXXXXXXXXXXXXX` → 본인 번호로 변경 (앞의 `ca-` 는 빼고 `pub-`부터)
   - `index.html` 에서 `ADSENSE_CLIENT='ca-pub-XXXXXXXXXXXXXXXX'` → 본인 ID로 변경
   - `privacy.html` 의 `[문의 이메일을 입력하세요]` → 실제 이메일로 변경
3. GitHub에 수정한 파일 다시 업로드 → 애드센스에서 **소유권 확인(ads.txt 또는 코드 스니펫)** → **검토 요청**

## 4단계. 보상형 광고(H5 Games Ads) 신청

1. 애드센스 승인 후 H5 Games Ads 신청 양식 제출 (퍼블리셔 ID 필요, 승인은 구글 심사)
   - 안내: https://developers.google.com/ad-placement/docs/signup
2. 승인 전에는 `ADS_TEST_MODE=true` 상태로 **구글 테스트 광고**가 나옵니다.
3. 승인 후 `index.html` 에서 `ADS_TEST_MODE=false` 로 바꿔 다시 올리면 실제 광고로 전환됩니다.

> 퍼블리셔 ID를 넣기 전까지는 앱 안의 **데모 광고(5초)**로 동작합니다.

## 동작 메모

- **학습 기록 저장**: 실서비스 모드(`TEST_MODE=false`)라 기록·포인트가 기기에 저장됩니다.
- **음성 인식**: Chrome·Safari 내장 음성 인식을 사용합니다 (첫 사용 시 마이크 권한 요청).
- **목소리**: 기기에 설치된 영어 음성을 사용합니다.
- **아이폰에서 앱처럼 쓰기**: Safari로 sijakk.com 접속 → 공유 → **홈 화면에 추가**
- **포인트 보안**: 포인트는 기기에만 저장되어 조작이 가능합니다. 포인트를 현금성 보상으로 확장할 경우 서버 검증이 필요합니다.
