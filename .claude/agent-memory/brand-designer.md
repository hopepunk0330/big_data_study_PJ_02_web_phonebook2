# brand-designer 메모리

이 파일은 brand-designer의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **브랜드 결정사항 자체(현재 확정 상태)는 여기 없습니다 — `docs/design/brand-guide.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-29 (4차) — 사용자 지적("1안·2안 컬러톤 같다") 재검증 + Victory Pop 팔레트 계열 자체를 네이비로 교체
- 배경: 3차에서 오브제 방향을 정의했지만 실은 팔레트 자체가 문제였음 — 3개 시안 `use_figma` read-only로 재실측한 결과, Victory Pop(`201:5`)의 dark block `#1f1b17`이 Spotlight(`176:2`)의 dark bg `#1f1b17`/`#2b2621`와 **완전 동일 hex**, Victory Pop의 light panel(`#e4d6c3`/`#ede6dc`/`#f0e6d8`)이 Slow Ritual(`162:2`)의 배경(`#e4d6c3`/`#ede6dc`/`#f3e4ce`)과 **거의 동일 계열**이라 3안 모두가 사실상 "크림/탄 + 차콜" 두 색군을 돌려썼다는 게 실측으로 확인됨.
- **결정**: Victory Pop의 배경/블록/배지 색만 완전히 새 계열(네이비)로 교체 — Dark Navy `#1B2A4A`(구 charcoal `#1f1b17` 대체) / Ink Navy `#12213D`(구 `#2b2621` 배지 채움 대체) / Pale Ice-blue `#E6EBF3`(구 `#ede6dc`/`#f0e6d8` 대체) / Deeper Ice-blue `#D7E0EE`(구 `#e4d6c3` 대체). 헤드라인 강조 골드 `#B8935B`는 copy.md 고정값이라 불변, 배지 스트로크·CTA·메달 골드도 동일 값 유지(네이비와 짝지어 "훈장/졸업 코드/증서" 관용 색조합을 형성해 "증명하고 자랑하는" 퍼스낼리티에 색채심리학적으로 더 맞음). 근거로 2차 재작업 때 이미 무드보드(`49:38`)에서 "네이비/옐로우/핑크/민트 컬러블록"이 관찰됐던 것도 재확인(당시 미채택이었던 네이비를 이번에 채택).
- 오브제 색상 지정 갱신: 메달 리본배지=gold 스트로크(불변)+navy 채움, 스탬프=navy 잉크, 컨페티=navy+ice-blue 교차(gold는 소량 반짝이는 조각만), 체크마크 배지=navy 원+gold 체크, 화살표/트로피=navy 실루엣+gold 하이라이트.
- Figma 쓰기 없음(read-only 재실측만), 정식화·design-qa 진행 안 함. design-pl에게 3안 팔레트 hex 비교표 + Victory Pop 신규 확정 팔레트 보고.

### 2026-08-24 (1차) — mercari 가격 UX 실험 SCR-002/003 1차 톤 라운드, Figma MCP 도구 부재로 착수 불가(차단 보고)
- 배경: mercari 프로젝트(별도 경로 `/Users/aydana/dev/portfolio/bigdata/01-ML_mercari price_2608`) Figma 파일(`SIBLz4S4IZbjabzhMSAgdo`)의 "레퍼런스" 페이지를 직접 열람하고, SCR-002/003 구조(v1.21 194~218줄·358~417줄, 로컬에서 정상 확인함)에 맞는 톤 프레임 3개(당근마켓·토스류 신뢰감 톤, 서로 다른 실제 트렌드 대응)를 `"mercari 가격제안 Concepts"` 페이지에 만드는 작업이었음.
- **차단 사유**: 이번 세션에 배정된 도구 목록에 `use_figma`/`get_metadata`/`get_screenshot` 등 Figma MCP 도구 자체가 없었고(`Skill`/`Read`/`Write`/`Glob`만 존재), `get_metadata` 직접 호출 시 `No such tool available`, `ToolSearch`도 `disabled for this session`으로 확인됨 — 하네스 문서(`figma-file-organization.md` 0.5번)가 말하는 "잘못된 MCP 네임스페이스" 문제가 아니라 이 세션 자체에 Figma 도구가 아예 배정되지 않은 상태.
- 로컬 문서(계획서 v1.21 두 구간, 브랜드 가이드·이전 로그)만 읽었고 Figma 열람·쓰기는 전혀 하지 않음(레퍼런스 페이지 미확인, 프레임 미생성). design-pl에게 이 블로커를 그대로 보고하고, 사용자에게 Figma 도구가 이 세션에 연결되도록 재시도해달라는 확인을 받은 뒤에만 재개해야 함 — 조용히 다른 방법(예: 로컬 추정만으로 팔레트 확정)으로 대체 진행하지 않음.

### 2026-08-24 (2차, 재시도) — 동일 작업 재시도에도 Figma MCP 도구 여전히 부재(재차단 보고)
- 배경: design-pl이 "직전 인스턴스가 Figma 도구 부재로 착수 못함, 이번이 재시도"라는 안내와 함께 동일 브리프(mercari SCR-002/003 1차 톤 라운드 3안)를 재할당.
- `figma-use` 스킬을 로드한 뒤 실제 호출 가능한 함수 목록을 확인 — 이번 세션에도 `use_figma`/`get_metadata`/`get_screenshot`/`ToolSearch` 등 Figma MCP 관련 함수가 도구 스키마 자체에 전혀 정의돼 있지 않음(호출 가능한 함수는 `Skill`/`Read`/`Write`/`Glob` 뿐). 1차 시도와 동일한 증상 재확인 — 세션에 Figma MCP 서버 자체가 연결되지 않은 것으로 판단됨.
- 이번에도 Figma 열람·쓰기 전혀 없음(레퍼런스 페이지 미확인, 프레임 미생성). `docs/design/brand-guide.md`는 이번 mercari 작업과 무관한 별개 프로젝트(연락처 관리 웹앱) 문서임을 확인만 하고 손대지 않음. design-pl에게 "세션에 Figma MCP 연결 자체가 빠져 있다"는 점을 정확히 재보고, 사용자에게 MCP 연결 상태 확인/재시작을 요청.

### 2026-08-24 (3차, 재시도 성공) — mercari 가격제안 화면 Concepts 1차 톤 라운드 3안 완성
- 배경: 이번 세션엔 Figma MCP 도구(`mcp__claude_ai_Figma__*`)가 정상 배정돼 착수 가능. `SIBLz4S4IZbjabzhMSAgdo` 파일의 "레퍼런스" 페이지(`0:1`) → "앱 UIUX 레퍼런스" 섹션(`1:58`, 이미지 42장)을 `get_screenshot`(base64)로 직접 열람 — 지그재그·와디즈·카카오페이류 비비드 컬러블록+굵은 잉크 아웃라인+컨페티 장식+범프 코믹 타이포 프로모 클러스터와, 하단의 미니멀 그레이스케일 와이어프레임 실사 UI 클러스터(플레인 리스트/필터/CTA) 두 축을 실측 확인.
- `06_기능정의서_화면정의서_v1.22.md` "-1. UX 패턴 방향"(201~231줄, 다른 프로젝트 폴더라 읽기만) 확인 후, `SIBLz4S4IZbjabzhMSAgdo` 파일에 새 페이지 `"가격제안 화면 Concepts"`(`8:2`)를 생성하고 3개 톤 프레임을 나란히 배치:
  - **Concept A — 미니멀 신뢰형**(`8:3`, 미니멀·스위스 그리드/Toss류): bg `#FFFFFF`/`#F7F8FA`, Primary `#3182F6`, Ink `#1A1D29`. 히어로 가격 Inter Black 48. 카드 radius 16·보더 1px·그림자 미세.
  - **Concept B — 네오팝 브루탈형**(`8:4`, 네오팝·뉴브루탈리즘/지그재그·와디즈류): bg 크림 `#FFF8EF`, Primary/CTA 코랄 `#FF5A36`, Accent 옐로우 `#FFD400`, Secondary 바이올렛 `#7B5CFF`, Ink `#16171A`. 히어로 가격 Inter Black 60 + 옐로우 하이라이터, 카드 2~3px 잉크 보더 + 하드 오프셋(블러 0) 스티커 그림자, 컨페티 별/다이아몬드 장식.
  - **Concept C — 벤토 다크 글로우형**(`8:5`, 벤토 그리드·다크모드 네온 글로우): bg 네이비블랙 `#0F1115`, Surface `#1B1E24`, Primary/Accent 네온민트 `#4DFFC4`, Secondary 네온바이올렛 `#A78BFA`. 히어로 가격 Inter Black 52 + 네온 글로우(blur 24), 상품 카드를 이미지·가격·신뢰배지·스텝인디케이터 4개 벤토 셀로 분리 배치.
  - 3안 모두 3-2절 UX 패턴(카드형 상품 표시, 히어로 타이포 가격, 카드형 선택 버튼, "1/2" 스텝 인디케이터, "🔍 유사 상품 N건 분석" 신뢰 배지)을 동일하게 포함하되 색/타이포/카드처리만 다르게 표현. 팔레트 명도·색상계열 자체가 뚜렷이 갈림(A 밝은 쿨톤, B 밝은 웜 비비드, C 다크 네온) — 사고 재발 방지 규칙 충족.
- 빌드 중 발견한 버그 1건 자체 수정: Concept C의 레이아웃 전용 auto-layout 래퍼 프레임들이 `createAutoLayout` 기본 흰색 fill을 그대로 가져 다크 배경 위에 흰 박스로 겹쳐 보임 — 17개 프레임 fill을 빈 배열로 정리해 해결(스크린샷으로 재확인 완료).
- SCR-002/003 실제 화면 목업은 만들지 않음(다음 단계 ui-designer 몫), `docs/design/brand-guide.md`는 이 mercari 작업과 무관한 별개 프로젝트 문서라 손대지 않음. design-pl에게 "3안 확정 대기" 상태로 보고, 확정 전까지 정식화·2차 라운드 진행하지 않음.

### 2026-08-24 (4차) — 사용자 중간 피드백: 페이지 리네임 + Concept B 트렌드 전면 교체(팔레트는 그대로)
- 배경: 1차 3안이 아직 최종 확정 전인 상태에서 사용자가 Figma를 직접 보고 중간 피드백 3건 전달 — (1) 페이지 `8:2` 이름을 관례 표기 "브랜드컨셉"으로, (2) Concept B의 5색 팔레트(`#FFF8EF`/`#FF5A36`/`#FFD400`/`#7B5CFF`/`#16171A`)는 검증된 값이라 유지하되 "네오팝·뉴브루탈리즘" 트렌드만 A/C와 안 겹치는 제3의 실제 트렌드로 교체, (3) A/C는 절대 건드리지 않음.
- 절차: 페이지 `8:2` → "브랜드컨셉"으로 리네임, 기존 `8:4`는 내용 무수정 상태로 이름만 `❌ 미채택 — Concept B — 네오팝 브루탈형`으로 라벨링. 레퍼런스 페이지 `1:58`(무드보드 42장)을 `get_screenshot`으로 재열람해 스탬프·쿠폰·티켓 다꾸(다이어리 꾸미기) 클러스터(와디즈 펀딩데이, 리미티드 쿠폰샵, hwahae awards 도장 포스터, Conversation 말풍선 스티커시트)를 근거로 **콜라주 저널링(Collage/Scrapbook Journaling)**을 신규 트렌드로 확정 — A(1px 보더+무그림자)·C(벤토 셀+네온 stroke+glow) 어느 쪽과도 겹치지 않는 제3의 조형 원리로 "다스트 ticket 대시보더 + 소프트 디퓨즈 그림자(blur16, ink14%) + washi tape 오버랩 + 잉크 도장 배지"를 채택.
- 신규 프레임 `28:2`("Concept B — 콜라주 저널링 (Collage Journaling)")를 `8:4` 계열 옆(x=2620, `8:5` 우측)에 신규 생성 — Color Palette(5 hex 스와치 + washi tape 액센트로 실측 대조 가능하게 원색 유지)/Typography(Hero Price를 대시보더 티켓 스텁 + 코랄 잉크스탬프 "OK!" 배지로 표현, Inter Black 56)/Card Components(선택됨=코랄 솔리드+소프트섀도, 미선택=대시 아웃라인, 신뢰배지=영수증 스트립, 스텝=잉크 스탬프 원)/Illustration Direction(washi tape·잉크도장·영수증컷·폴라로이드 선화) 5개 필수 요소 전부 포함. 팔레트 5개 hex를 read-only로 재조회해 브리프 표와 **완전 일치**(FF5A36/FFD400/7B5CFF/FFF8EF/16171A) 확인.
- A(`8:3`/`20:2`/`20:3`)·C(`8:5`/`23:2`/`23:3`) 6개 프레임은 이름·자식 수 재조회로 무변경 확인(직접 수정 없음). SCR-002/003 적용화면(`21:2`/`21:3`)은 손대지 않음(다음 단계 ui-designer 몫). design-pl에게 신규 프레임 nodeId(`28:2`)와 트렌드 선택 근거, 팔레트 hex 동일성 확인 결과 보고.
