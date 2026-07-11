# brand-designer 메모리

이 파일은 brand-designer가 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 브랜드 결정사항 (색상/톤/가이드)

**상태: 확정 — Concept B "Warm Ledger" (design-pl 경유 사용자 확정 완료, Brand Guide 정식화 완료)**

3개 시안(Deskline/Warm Ledger/Gridline) 중 사용자가 **Concept B "Warm Ledger"**를 최종 확정했다. "Brand Guide" 페이지(fileKey `zgGlMBwFglaDlaeyP4CkgR`, pageId `52:2`, 루트 프레임 `52:3`)로 정식화 완료.

| 항목 | 값 |
|---|---|
| 포지셔닝 | 화려한 CRM형 툴/차가운 주소록 유틸리티 대비, "내가 관리하는 사람들과의 관계"라는 정서적 온기로 차별화. 로그인 사용자별 데이터 격리(핵심 신뢰 요소)를 시각적 경계로도 드러냄 |
| 퍼스낼리티 | "다정하지만 칠칠맞지 않은 친구" — 사람과의 관계는 다정하게, 굵은 잉크 아웃라인으로 "내 목록 vs 남의 목록" 데이터 경계를 또렷하게 표현 |
| 주조색 Primary | `#17A398` (틸) — 신뢰+안정, 딥블루 대신 그린 계열로 차갑지 않게 |
| 보조색 Secondary | `#FF5A76` (코랄) — 따뜻함+친밀감, 배지·태그·강조 텍스트에 제한 사용 |
| 강조색 Accent | `#FFCB47` (앰버) — 주의 환기, "지금 봐야 할 지점"에만 신호로 사용 |
| 사용 비율 | 주조 60% (배경·헤더·주요 버튼) : 보조 30% (배지·태그·강조 텍스트) : 강조 10% (알림·선택 상태·CTA) |
| 서체 | Baloo 2(라틴 Display/워드마크, ExtraBold) + Noto Sans KR Black(KR Display) + Noto Sans KR Regular/Medium(Body/Caption) — 최소 3단계 위계(Display Latin/Display KR/Body/Caption) |
| 로고/워드마크 | 원형 배지 심볼 + 워드마크. 파비콘(16px)은 심볼만, 24px 이상부터 워드마크 텍스트 동반. 굵은 잉크 아웃라인은 24px 이상에서만 적용(작은 크기에서 뭉개짐 방지) |
| 일러스트레이션 방향(참고) | 라인+플랫 하이브리드 — 굵은 잉크 아웃라인(3px 내외) + 브랜드색 1~2개 평면 채색, 3D/아이소메트릭 배제(포지셔닝과 상충). 빈 상태 그래픽은 마스코트 대신 로고 심볼 확대 재사용. 실제 에셋은 미제작(design-systems/ui-designer 몫) |

**워드마크 네이밍 미확정 — 중요**: Brand Guide의 "yourbook."은 서체·톤 표현(굵은 잉크 아웃라인, 축소/확대 검토)용 placeholder이며 최종 서비스명이 아니다. Brand Guide 내 "⚠ 제품명 미정" 콜아웃에 명시함. 실제 서비스명 확정 시 design-pl 경유 별도 논의 필요 — 임의로 확정하지 않는다.

**미채택 처리**: "브랜드 컨셉 Concepts" 페이지(`34:2`)의 Concept A(Deskline, `34:3`+`44:2`)와 Concept C(Gridline, `34:5`+`46:2`)는 삭제하지 않고 이름 앞에 `❌ 미채택 — `을 붙여 그대로 보존(의사결정 히스토리). 확정된 Concept B 원본(`34:4`, `45:2`)은 라벨 변경 없이 그대로 둠 — 정식 자산은 별도로 "Brand Guide" 페이지로 이관됨.

**다음 단계(이 에이전트 범위 아님)**: design-systems가 위 컬러/서체를 정식 디자인 토큰·컴포넌트·아이콘 세트로 생성 → ui-designer가 SCREENS 구역에 실제 화면 제작 → design-qa 감사.

## 작업 로그

### 2026-07-12 — Concept B "Warm Ledger" 정식화 (Brand Guide 완성) + 미채택 라벨링
- design-pl로부터 "Concept B 확정, 시안 재제작 아님" 브리프 수신. 컬러/폰트 값은 기존 메모리 표에서 그대로 가져오고 임의 조정하지 않음.
- "Brand Guide" 페이지(`52:2`) 신규 생성(레퍼런스 페이지 `15:2` 바로 다음 순서로 배치), 루트 프레임(`52:3`, 960px 폭)에 7개 섹션 구성: Header(워드마크+태그라인) / Positioning / Personality / Color Palette(3 스와치+색채심리 근거+사용비율) / Typography(4단계 램프) / Logo & Wordmark Usage(파비콘~히어로 4단계 축소·확대 검토 + "제품명 미정" 경고 콜아웃) / Illustration Direction(참고, 간단 방향만).
- 파비콘 카드 라벨 텍스트가 FILL 폭 설정 때문에 세로로 쪼개져 보이는 버그를 발견 → HUG/WIDTH_AND_HEIGHT로 수정 후 스크린샷 재확인.
- "브랜드 컨셉 Concepts" 페이지(`34:2`)에서 미채택 세트(Concept A: `34:3`+`44:2`, Concept C: `34:5`+`46:2`) 이름 앞에 `❌ 미채택 — ` 부여. 프레임 내부 디자인은 건드리지 않음. 확정 세트(`34:4`, `45:2`)는 변경 없음.
- 컬러/폰트 값 조정 없음, 워드마크 placeholder를 최종 네이밍으로 확정하지 않음 — 브리프의 금지사항 준수.

### 2026-07-12 — 레퍼런스 기반 재작업 (버그 수정)
- 배경: 이전 라운드가 최상위 `get_metadata` 페이지 목록만 보고 "레퍼런스 없음"으로 오판한 채 만든 시안이었음이 드러남. `docs/design/figma-file-organization.md`에 0번 항목("Figma 조회 결과를 그대로 믿지 않는다") 신설됨.
- 이번엔 nodeId `15:2`로 직접 `get_metadata` 호출 → "레퍼런스" 페이지의 "컨셉 참고" 섹션(`15:6`) 확인, 내부 이미지 9장을 `get_screenshot`으로 실제 열람(Y2K/레트로팝 톤 무드보드: 두꺼운 아웃라인 배지, 스큐어모픽 Win98 다이얼로그, 픽셀게임 UI, 그리드 UI 키트, 미니멀 SaaS 포스터 등).
- 이를 연락처 관리 앱(멀티유저 로그인+데이터 격리 최중요 평가기준, PC 브라우저) 성격에 맞게 3가지 뚜렷한 축으로 재해석: Concept A(Deskline, 레트로 OS형) / Concept B(Warm Ledger, 네오팝 배지형) / Concept C(Gridline, 그리드 유틸리티형).
- "브랜드 컨셉 Concepts" 페이지(34:2)의 기존 프레임 34:3/34:4/34:5를 새 시안으로 덮어씀(❌ 미채택 표시 없이 완전 교체 — 이전 산출물이 레퍼런스 미확인 상태에서 나온 오작이었기 때문).
- 결정 안 함: 3안 중 채택 여부는 design-pl → 사용자 확정 필요. 다음 단계(design-systems 토큰화, Brand Guide 완성)는 진행하지 않음.
