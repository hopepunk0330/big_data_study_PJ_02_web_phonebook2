# graphic-designer 메모리

이 파일은 graphic-designer의 최근 작업 로그(휘발성, 5개 캡)만 남깁니다. **그린 그래픽 목록(현재 확정 상태)은 여기 없습니다 — `docs/design/graphic-assets.md`가 그 소스 오브 트루스입니다.** 작업 시작 시 이 로그가 아니라 그 문서를 먼저 읽으세요.

## 작업 로그

### 2026-07-17 — Icon/* 8종 Basic/Visual 트랙 재판정 + Basic 6종 재드로잉 지시 (사용자가 Icon/User를 직접 지적)
- design-pl 브리프: 사용자가 Figma에서 `Icon/User`(`96:45`)를 직접 보고 "라인형이 맞는 아이콘 같다"고 지적 — Icon/* 8종 전부가 `.claude/agents/graphic-designer.md`의 기존 Basic/Visual 트랙 구분(로그아웃=Basic, 카테고리/알림=Visual 예시)을 한 번도 적용받지 못하고 균일하게 teal fill+3px ink stroke로 그려져 있던 것을 재판정.
- `use_figma` 읽기 전용으로 Icon/* 8종 전체 자식 노드(fill/stroke hex·bound 상태·strokeWeight)를 재실측 — 직전 라운드(색상 바인딩 감사)에서 design-systems가 이미 fill(teal/amber)·stroke(ink/900) 재바인딩을 완료해놓은 상태(`bound: true`, `#1a1a1a`)임을 확인. 이번 라운드는 그 색상 정확성 작업을 뒤집는 게 아니라 "그 fill을 애초에 갖고 있어야 하는가"(트랙)라는 다른 층위 질문에 답하는 것 — 인계 문구로 명확히 구분해 문서에 남김.
- 판정 결과: Basic 6종(Search/Add/Edit/Delete/Logout/User) — 범용 기호이거나 실사용에서 이미 얇은 `Pixel/*` 처리로 다뤄지고 있음, 위험/분류 신호는 컨테이너(버튼 보더·경고 박스)가 전담. Visual 2종 유지(Category/Alert) — 색이 분류·상태 의미를 실제로 나르는 자리.
- Avatar(`104:131`) 구조를 `use_figma`로 실측해 "원 배경(자체 fill)"과 "Icon/User 인스턴스(글리프)" 2겹 구조임을 확인. 새 발견: 마스터는 틸(bound)인데 실제 확정 화면 인스턴스(`501:6370`)의 원 배경은 스카이블루 `#1395e6`(unbound 로컬 오버라이드)로 마스터와 달랐다 — 직전 감사 라운드의 "Avatar는 신 세대에도 틸" 결론은 아이콘 글리프 색만 본 것이었고 원 배경 자체는 확인 대상이 아니었음을 정정. 이 색상 불일치는 이번 브리프 범위 밖이라 design-pl에 별도 보고만, 여기서 고치지 않음. Avatar 원 배경 색 채움 자체는 "사용자별 데이터 격리 신뢰 요소"(brand-guide 1번) 근거로 유지 판정, 그 위 사람 실루엣만 Basic(면색 제거) — 모순 아님.
- Basic 6종 재드로잉 지시(design-systems 실행용): 두께 2px 확정(brand-guide 4번 "기본 컴포넌트 보더 2px" 값 재사용, 새 임의값 아님), 색은 이미 바인딩된 `color/ink/900` 그대로(stroke weight만 3→2 변경하면 됨), "주 실루엣" 도형(teal fill 보유)만 fill 제거하고 "디테일" 도형(원래도 ink fill만이던 손잡이·+막대·화살표 등)은 무변경 — 노드 ID 단위로 표 작성. Icon/User는 Avatar 인스턴스 오버라이드가 마스터 변경을 자동 상속하지 않는다는 주의사항 별도 명시.
- `docs/design/graphic-assets.md`에 "Icon/* 8종 Basic/Visual 트랙 재판정 + Basic 6종 재드로잉 지시" 절 신규 append(기존 절 무손실). **전달 대상**: design-systems(재드로잉 실행), design-pl(Avatar 원 배경 색상 불일치 별도 보고).

### 2026-07-17 — Pixel/Search 색상 검증(teal→sky/500), 그리기 작업 아님
- 배경: 메인 세션이 확정 main 프레임 안 `PxSearch`(`501:6390`) 13개 벡터를 직접 실측해 전부 sky `#1395e6`임을 확인, 반면 마스터 `Pixel/Search`(`255:26`)는 위 색상 감사 절에서 teal/500(A그룹, 재해석 불필요)로 이미 판정돼 있어 모순 발견 — 신뢰 형식으로 sky/500 리바인딩 승인, 확인/판정만 수행(벡터 직접 수정 없음).
- `use_figma` 읽기 전용으로 `501:6390`과 `255:26`을 나란히 실측: 13개 벡터 전부 x/y/width/height/vectorPaths 소수점까지 완전 동일(형태 100% 일치, 색상 외 차이 없음). 마스터 13개 전수 `#17a398`+`color/teal/500` 바인딩(예외 없음), 확정 인스턴스 13개 전수 raw `#1395e6`(unbound) 확인.
- 트랙 판정: Pixel/Search는 icon-craft-guide의 Icon/* 24px Basic/Visual(스트로크 유무) 이분법이 아니라 별도의 Pixel/* 마이크로 픽셀 블록-실루엣 트랙(스트로크 개념 없음, 항상 solid fill)에 속함 — 이 트랙 안에서는 fill 유무가 Basic/Visual 구분 신호가 아니므로, teal→sky 색상 토큰 교체는 트랙 규칙(strokeWeight·fill 구성)을 전혀 건드리지 않음. 위반 없음.
- 판정: 순수 오류 정정(브랜드 톤 재해석 아님) — Pixel/NoResult(2026-07-16, 동일 사유)·Icon/Category(같은 날 앞 라운드, "범용 UI 크롬은 sky/500 버킷") 전례와 일치, 신규 토큰 없이 기존 `color/sky/500` 재사용, 다른 아이콘의 teal 사용에 영향 없음.
- `docs/design/graphic-assets.md`에 "Pixel/Search 색상 검증" 절 신규 append, 기존 A/B 분류표의 Pixel/Search 행은 이 절이 대체함을 명시(기존 행 삭제 없음). **결론**: "리바인딩 승인, design-systems 진행 가능." **전달 대상**: design-systems(마스터 `255:26`의 13개 벡터 fill teal/500→sky/500 실제 리바인딩 실행).

### 2026-07-17 — Auth 페이지(`934:2`) BgPixels/ConfettiFooter 컨페티 오브제 불투명도 결함 수정 (사용자 이슈 제보, 직접 수정)
- 사용자 제보: "로그인 화면 뒤에 bg의 블루배경에 있는 오브제들의 컬러가 달라" — 노드 `934:2` 확인 요청("누락 8개 화면 조립"과 무관한 별개 트랙).
- `get_metadata` 조사 결과 `934:2`는 "Auth"라는 이름의 캔버스(페이지)였고, 그 아래 `Join`(`935:33`)/`login`(`936:1042`)/`login-알림창`(`936:1191`) 3개 프레임을 담고 있음 — 확정 원본(nodeId `501:4692`/`501:4940`/`501:5188`, `user-confirmed-final-design.md` 참고)과는 다른 nodeId라 **파생 SCREENS 페이지**로 판단(보호 라벨 대상 아님, 직접 수정 가능).
- `use_figma` 읽기 전용으로 각 프레임의 `BgPixels`(전역 컨페티 14개: 다이아몬드5+십자4+별5)·`ConfettiFooter`(카드 하단 5개: 다이아몬드3+별2) 전체 fill/opacity/boundVariables 실측 — fill은 전부 `color/ink/900`(`#1a1a1a`)에 정확히 바인딩(색상 토큰 문제 아님, **이 결론은 다음 라운드에서 틀린 것으로 정정됨**). 실제 결함은 **opacity**: 별(Pixel/Star 인스턴스)만 brand-guide 7번 스펙대로 0.25~0.4가 걸려 있고, 다이아몬드·십자는 전부 opacity 1(완전 불투명) — 같은 잉크색인데 반투명/불투명이 섞여 사용자에게 "색이 다르다"는 인상을 줌. ConfettiFooter는 스펙(25% 불투명도)과 반대로 5개 전부(별 포함) opacity 1이었음. 3개 프레임 전부 동일 패턴(프레임당 14개, 총 42개).
- `use_figma`로 3개 프레임 총 42개 노드의 opacity 수정: BgPixels 다이아몬드+십자 9개/프레임은 brand-guide 7번 25~40% 범위 내 0.4/0.3/0.35/0.25 순환 배정, ConfettiFooter 5개/프레임은 스펙대로 전부 0.25로 통일. 형태·fill 색·boundVariables는 무변경. **⚠ 후속(다음 항목 참고): "fill 색 자체는 문제 없다"는 이 판단은 틀렸음 — 원본과 직접 대조하지 않고 내린 결론이었다.**
- `docs/design/graphic-assets.md`에 "Auth 페이지 BgPixels/ConfettiFooter 컨페티 오브제 불투명도 결함 수정 완료" 절 신규 append. **전달 대상**: 없음(직접 완료, design-pl 참고 보고) — 단, 컬러 자체는 다음 라운드에서 재작업됨.

### 2026-07-17 — Auth 페이지(`934:2`) BgPixels 컬러 자체 오류 정정 (사용자 3차 재확인, 전수 hex 재실측 → 직접 수정)
- 사용자가 opacity 수정 후에도 "컬러 자체가 여전히 원본과 다르다"고 3차 재확인 요청 — 원본(`501:4940`)과 직접 hex 대조 없이 "ink/900 바인딩이니 정상"이라 판단했던 직전 라운드의 결론이 틀렸음을 확인.
- `use_figma` 읽기 전용으로 확정 login 프레임(`501:4940`) 하위 BgPixels/ConfettiFooter/Divider 전체 vector를 실측한 결과, **원본은 배치 위치에 따라 다른 색 체계를 쓰고 있었다**: BgPixels(블루 배경 위 전역 산포)의 다이아몬드·십자는 **흰색 `#ffffff`**, 별은 **앰버 `#ffce2c`** — ConfettiFooter(흰 카드 안)는 다이아몬드·별 모두 잉크 `#1a1a1a`(이 부분만 934:2와 이미 일치, 재작업 불필요). Divider(or 구분선) 라인도 원본은 `#1a1a1a` opacity 10%(옅은 선)인데 934:2는 opacity 100%(진한 검정 실선)로 달랐다.
- 934:2 페이지 8개 프레임(Join `935:33`/login `936:1042`/login-알림창 `936:1191`/비번재설정 3개 `995:303`,`996:376`,`996:2575`/Join 배너 2개 `996:2713`,`996:3014`) 전체를 `use_figma`로 전수 스캔한 결과 BgPixels 다이아몬드 40개·십자 32개(64 vector)·별 40개 인스턴스(320 vector)가 **전부 예외 없이 잉크 `#1a1a1a`**로 잘못 복제돼 있었음(원본의 흰색/앰버 2색 체계가 반영 안 됨).
- `use_figma`로 8개 프레임 전체 수정: 다이아몬드 40개+십자 64개 vector → 흰색 `#ffffff`(raw, unbound — 원본과 동일하게 토큰 미바인딩), 별 320개 vector(인스턴스 오버라이드) → 앰버 `#ffce2c`, Divider 10개 라인 → stroke opacity 0.1(색은 동일 `#1a1a1a`). 총 수정 112개 shape/instance(색상) + 10개 line(불투명도) = 122개 노드, 8개 프레임 전체. ConfettiFooter(40개)는 이미 원본과 일치해 무변경.
- 부수 발견: `935:33`은 컴포넌트/인스턴스가 아니라 일반 FRAME(8개 프레임이 BgPixels/ConfettiFooter를 독립 복제한 raw 구조, 마스터 공유 안 함) — "935:33만 고치면 전파된다"는 가정 성립 안 해 8개 프레임 전부 개별 수정.
- `get_screenshot`으로 934:2 페이지 전체·개별 프레임(login/Join/995:303) 재검증 완료. `docs/design/graphic-assets.md`에 "BgPixels 컬러 자체 오류 정정 완료" 절 신규 append. **전달 대상**: design-pl(① 이전 라운드의 "색 문제 없음" 결론이 틀렸다는 점, ② 935:33이 공유 컴포넌트가 아니라는 구조적 발견 — 향후 컴포넌트화 권장 — 참고 보고).

### 2026-07-18 — docs/planning 버전 재동기화 (01_구현요구사항 v1.12→v1.13, 02_화면정의서 v1.16→v1.17), 그리기 작업 아님
- 순수 버전 번호 재동기화 요청. `docs/planning/`의 01(구현요구사항서)·02(화면정의서)가 사용자 승인된 별도 라운드(SCR-002 보완)에서 v1.12→v1.13, v1.16→v1.17로 승격되어, `docs/design/graphic-assets.md`가 이 두 문서를 인용하던 부분(146행 "값 출처" 문장)을 최신 버전으로 갱신.
- 파일 전체(553줄)를 재독해 두 버전 문자열(`01_...v1.12`, `02_...v1.16`)이 다른 곳에도 등장하는지 확인 — 146행 1곳뿐임을 확인, 다른 서술·판단은 전혀 건드리지 않음(03_기능정의서_v1.3은 대상 아니라 무변경).
- **전달 대상**: 없음(순수 문서 인용 버전 동기화, 디자인 판단 아님).
