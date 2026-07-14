# design-systems 메모리

이 파일은 design-systems의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **State Ledger(토큰/컴포넌트/아이콘의 현재 확정 상태) 자체는 여기 없습니다 — `docs/design/design-system.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-14 — design-qa LOW 감사 정정: 8절 "페이지 순서" 표의 `15:3` 페이지 이름 오기(문서 텍스트만)

- design-qa가 발견한 LOW 1건: 8절 "페이지 순서" 표에서 `15:3` 페이지 이름이 `UI-design`(공백 없음)으로 기재돼 있었으나, 실제 Figma 페이지 이름은 끝에 공백 1칸이 포함된 `"UI-design "`(트레일링 스페이스)이다.
- Figma 자체는 건드리지 않음(요청 범위가 순수 문서 텍스트 정정이라 Figma 조회/수정 없이 진행). `docs/design/design-system.md` 8절 표의 해당 행 name 컬럼을 `` `UI-design ` `` (코드 스팬으로 트레일링 스페이스 보존)로 정정하고, 비고 컬럼에 "실제 페이지 이름은 끝에 공백 1칸 포함(트레일링 스페이스)"이라는 각주를 추가했다.
- 다른 표 내용(idx/pageId/나머지 28개 페이지명)은 무수정.

### 2026-07-14 — 페이지(canvas) 레벨 구조 재정렬: 구분 페이지 6개 신설 + 전체 순서 재배열 (design-pl 실행 브리프, 페이지 내부 콘텐츠 무수정)

- 사용자가 `docs/harness/design-team/figma-file-organization.md` 1번 항목의 구역 구분 스타일(`--- BRAND ---` 등)을 실제 Figma 파일 페이지 목록에도 반영해달라고 요청. 작업 시작 전 `use_figma` 읽기 전용 스크립트로 기존 23개 페이지가 브리프대로 실제 존재함을 재확인(불일치 없음).
- **1단계**: 빈 구분 페이지 6개 생성 — `--- BRAND ---`(`364:2`) `--- FOUNDATIONS ---`(`364:3`) `--- COMPONENT SPECS ---`(`364:4`) `--- CONCEPTS ---`(`364:5`) `--- COMPONENTS ---`(`364:6`) `--- SCREENS ---`(`364:7`). 아직 실제 구역이 없는 `--- GRAPHIC ASSETS ---`/`--- MOTION ASSETS ---`/`--- MARKETING ---`는 스킵.
- **2단계**: `figma.root.insertChild(index, pageNode)`로 전체 29개 페이지를 목표 순서(레퍼런스→BRAND→Brand Guide→FOUNDATIONS→Colors/Typography/Spacing/Elevation/Icons→COMPONENT SPECS→Component Specs→CONCEPTS→브랜드 컨셉 Concepts→COMPONENTS→Button~Link 11개→SCREENS→파일럿→old-사용하지말것→UI-design)로 재배열 — 페이지 노드 자체만 이동, 내부 콘텐츠는 전혀 건드리지 않음.
- **자체 재검증(design-systems 규칙)**: 재조회한 최종 순서가 목표와 정확히 일치함을 확인. 파일럿 페이지(`222:524`)는 위치만 이동했고 내부는 열지 않음 — `childrenCount: 10`(변경 없음)과 확정 디자인 섹션(`248:11689`)의 `childrenCount: 8`(사용자 확정 8개 프레임 손상 없음)만 딱 한 번 가볍게 확인.
- `docs/design/design-system.md`에 0-8절 신설 + 8절 "페이지 순서" 표를 29개 최종 순서(신규 구분 페이지 포함)로 전면 갱신, 기존 "표와 실제 파일이 어긋난다"는 알려진 이슈 해소로 갱신. `docs/harness/design-team/figma-file-organization.md` 1번 항목 뒤에 "실제 Figma 파일이 이 구조를 그대로 반영한다"는 확인 문구만 추가(구조 자체는 재작성하지 않음).

### 2026-07-14 — Legacy Table Row(`103:7`) 최종 해제 완료 — 사용자 재확정 (design-pl 실행 브리프, 원본 확정 프레임 무수정)
- 배경: 직전 라운드(0-5절)에서 격리 테스트 복제본으로 `103:7`의 COMPONENT→FRAME 전환 위험성(기존 INSTANCE 7개가 빈 박스로 깨짐)을 실증 검증했고, 실제 `103:7`은 인스턴스 7개가 남아있어 그때는 전환하지 않고 보류했다. design-pl이 이 검증 결과를 사용자에게 보고했고, **사용자가 인스턴스가 깨지는 걸 알면서도 "해제해줘"라고 명시적으로 재확인·재승인**했다.
- **전환 실행**: 0-3절에서 나머지 7개 legacy 컴포넌트에 적용한 것과 동일한 절차 — `103:7`(variant 없는 단일 COMPONENT, HORIZONTAL auto-layout, 700×62)의 시각 속성을 그대로 복제한 새 FRAME을 만들고, 자식 노드 6개(name/phone/address/category/edit-action/delete-action)를 이동(move, 동일 ID 유지)한 뒤 원래 COMPONENT 노드를 제거. 신규 FRAME `357:303`, 이름/위치 동일 유지. `get_screenshot`으로 마스터 콘텐츠 무손실 이전 확인.
- **인스턴스 깨짐 실측 관찰**: 7개 인스턴스 전부 `childrenCount: 0`. `103:77`(Table Row 페이지)은 완전히 빈 흰 박스. 파일럿 페이지(`222:524`)의 `❌ 폐기 —` 프레임 안 6개(`110:220`/`110:234`/`110:248`/`110:262`/`110:276`/`110:290`)는 부모 프레임(`110:201`) 스크린샷 기준 테이블 헤더/타이틀은 정상, 그 아래 6개 데이터 행은 전부 완전히 빈 상태(텍스트/배지/아이콘 전혀 없음, 얇은 구분선만 남음) — 0-5절 예측과 정확히 일치. 되돌리지 않음(지시대로).
- `docs/design/design-system.md` 0-3/0-6(신설)/7-2/8절(Legacy 표 + 갭 목록) 갱신 — 8개 legacy 컴포넌트(Avatar 제외) 전부 등록 해제 완료 상태로 최종화, 인스턴스 깨짐은 신규 결함이 아니라 사용자 승인된 트레이드오프로 명시.

### 2026-07-14 — Contact Row 컴포넌트 조립 + Legacy Table Row 해제 위험성 검증 + Link 문서 정리 4작업 (design-pl 실행 브리프, 원본 확정 프레임 무수정)
- **Contact Row 조립**: Table Row 페이지(`103:3`)에 실제 조립 컴포넌트가 없던 갭을 메움. main 확정 프레임 첫 행(`214:573`)을 `get_design_context`로 재실측 — 이름은 Noto Sans KR Bold 14px `#1a1a1a`로 기존 `Body/Button` 텍스트 스타일과 정확히 일치함을 직접 관찰로 최종 확정(design-prompter의 문서 대조 가설을 실측으로 검증). 전화번호=`Body/Regular`+`color/text-muted-strong`(#555), 주소=`Body/Regular`+`color/text-muted`(#777). 구분선 `#ede6d8`이 미등록임을 재확인 → 신규 primitive `color/beige/200` + semantic `color/border-divider-warm`(`VariableID:350:3`) 등록. `Contact Row`(`351:299`, 774×47, 단일 컴포넌트) 신규 — name/phone/address TEXT 프로퍼티로 노출, CatBadge(`256:5`)/Table Row Action(`260:96`/`260:98`) 기존 정식 컴포넌트를 그대로 인스턴스화(새로 안 그림). 조립 직후 read-only 스크립트로 fill 바인딩·mainComponent ID를 hex/ID 단위로 재대조(자체 점검 규칙). `Component Specs`(`342:2`)에 `Spec — Contact Row`(`352:726`) 스펙 시트 추가 — 총 11개.
- **Legacy Table Row(`103:7`) 해제 위험성 검증**: 격리된 테스트 복제본(clone → 테스트 인스턴스 → COMPONENT→FRAME 전환)으로 실험한 결과, **전환 시 기존 INSTANCE가 완전히 빈 박스로 깨짐을 실증**(전환 전 정상 텍스트 표시 스크린샷 vs 전환 후 childrenCount 0 + 빈 흰 박스 스크린샷). 0-3절에서 이미 전환한 7개는 인스턴스가 0개라 이 부작용이 드러나지 않았을 뿐이었다는 것을 이번에 확인. 실제 `103:7`은 인스턴스 7개가 남아있어 **전환하지 않음** — 위험 근거와 함께 7-2절에 기록, 최종 판단은 design-pl 경유 사용자에게 위임(→ 이후 라운드에서 사용자가 해제를 재확정, 위 항목 참고). 테스트 산출물(테스트 마스터/인스턴스/전환된 FRAME) 전부 삭제해 실제 파일에는 흔적 없음(재확인 완료).
- **Link 44×44 터치 타겟 미달**: 7-2절에 독립 항목 추가(login `247:6827` 원본 내재값, 7-1 §4와 같은 계열이나 등록 시점 차이로 별도 기록). 컴포넌트 크기 변경 없음.
- **Link WCAG 대비 3.12:1**: 사용자가 "이번 프로젝트 범위에서 개선하지 않기로" 확정 → 7-2절 TODO에서 7-1절 RESOLVED(6번 항목)로 이동. 원본 프레임/토큰 값(#17A398) 자체는 무변경, 순수 문서 상태 변경.
- `docs/design/design-system.md` 0-5절 신설 + 0-3/1-1/1-2/1-4/1-5/3/5/7-1/7-2/8절 갱신.

### 2026-07-14 — Link 텍스트 링크 신규 등록 + Component Specs 페이지(스펙 시트 10개) 신설 (design-pl 실행 브리프, 원본 확정 프레임 무수정)
- **관찰**: 브리프가 지목한 login(`247:6666`)의 "로그인으로 돌아가기"는 실제로는 Join 프레임(`241:1552`)의 `241:2144`에 있었고, 실측 결과 흰 배경+2px ink 보더+radius10의 **버튼**(Button/Neutral과 동일 구조, 그림자 없음)이었다 — 신규 컴포넌트 대신 기존 Button/Neutral 인스턴스로 커버됨을 확인. 브리프의 "짝을 이루는 유사 보조 텍스트 링크" 예외 조항에 따라 login `247:6827`("비밀번호 찾기", Noto Sans KR Bold 12px, `#17A398`=기존 teal/500, underline, 그림자 없음)을 진짜 텍스트 링크로 채택.
- **토큰**: 신규 semantic `color/text-link`(→teal/500, `VariableID:340:3`, scope TEXT_FILL). 기존 `color/text-accent`(레거시 teal/700 별칭)는 실측값과 달라 재사용 안 함. 신규 primitive는 불필요.
- **텍스트 스타일**: `Body/Link`(Noto Sans KR Bold 12px, letterSpacing 0, lineHeight 18px, underline) 신규.
- **컴포넌트**: "Link" 전용 페이지(`341:2`) + `Link` 컴포넌트(`341:3`, 69×18, TEXT 프로퍼티 `Label#341:0`) 신규. Default 상태만(hover 등은 7-2절 TODO로 기록).
- **WCAG 신규 발견**: `color/text-link`(#17A398) on 흰 배경 = 3.12:1로 AA 4.5:1 미달(12px Bold는 큰 텍스트 예외도 미적용). 원본 확정 실측값 그대로라 임의로 진하게 바꾸지 않고 7-2절에 TODO로 기록 — **이후 라운드(0-5절)에서 사용자 확정으로 RESOLVED 전환됨, 위 항목 참고**.
- **Component Specs 페이지**(`342:2`, Icons 바로 뒤): 기존 9개 컴포넌트(NeoBtn 48/Button 18/Icon Button 5/Row Action Button 10/Table Row Action 10/Sidebar Nav Item 4/TypeSelector 16/NeoInput 2/CornerInput 2) + Link 1 = 총 10개 스펙 시트 프레임(각 `Spec — {이름}`, 제목+설명+실제 컴포넌트 인스턴스 그리드+상태 라벨)을 생성, 전체 스크린샷으로 variant 피커 없이 한눈에 보임을 검증. 프레임 ID: NeoBtn `342:3`, Button `343:50`, Icon Button `343:653`, Row Action Button `343:697`, Table Row Action `343:1044`, Sidebar Nav Item `343:1106`, TypeSelector `343:1146`, NeoInput `344:721`, CornerInput `344:740`, Link `344:759`.
- `docs/design/design-system.md` 0-4절 신설 + 1-2/1-5/3/5/7-2/8절 갱신.
