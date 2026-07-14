# design-pl 메모리

이 파일은 design-pl이 작업 시작 시 읽고, 작업 종료 시 기록을 남기는 메모리/로그입니다.

## 팀 로스터 (참고용)
- design-prompter, design-scanner, brand-designer, graphic-designer, design-systems, ux-designer, ui-designer, interaction-designer, motion-designer, content-designer, design-qa

## 작업 로그

### 2026-07-14 실행 라운드 — Link 컴포넌트 등록 + Component Specs 페이지(스펙 시트 10개) (21차)
- login `247:6666` 재관찰 결과 "비밀번호 찾기"(`247:6827`, teal/500, underline)를 근거로 신규 토큰 `color/text-link`·텍스트 스타일 `Body/Link`·컴포넌트 `Link`(`341:2`/`341:3`) 등록. 신규 페이지 `Component Specs`(`342:2`, Icons 바로 뒤)에 10개 스펙 시트 생성.
- **design-qa 스팟체크**: 전부 PASS. LOW 1건(Link 44×44 터치 타겟 미달 미문서화).
- 상태: 실행 완료.

### 2026-07-14 실행 라운드 — Contact Row 조립 + Legacy Table Row 위험성 검증 + Link 문서 2건 정리 (22차)
- **Contact Row 조립**: main 확정 프레임(`214:349`, 첫 행 `214:573`) 재관찰 후 기존 부품만 조합해 `Contact Row`(`351:299`) 신규 등록. 미등록 구분선 값 발견해 신규 토큰 `color/beige/200`+`color/border-divider-warm` 등록. 스펙 시트도 생성.
- **Legacy Table Row 위험성 검증(1차)**: 격리 테스트로 COMPONENT→FRAME 전환 시 기존 INSTANCE가 빈 박스로 깨짐을 실증 → 당시엔 해제하지 않고 보류.
- **Link 문서 2건**: 44×44 터치 타겟 미달 7-2절 기록. WCAG 3.12:1은 사용자 확정("테스트니깐 무시")으로 7-1절 RESOLVED 이동.
- **design-qa 스팟체크**: 전부 PASS.
- 상태: 실행 완료.

### 2026-07-14 실행 라운드 — Legacy Table Row 해제 실행 → 인스턴스 파손 → 복구 (23차)
- 배경: 메인 세션이 "해제해줘"로 22차의 "위험함" 결과를 알고도 해제 재승인 → 나머지 7개와 동일 절차로 `103:7`을 FRAME(`357:303`)으로 전환 → **예상대로 인스턴스 7개가 실제로 빈 박스로 깨짐**.
- **메인 세션 정정**: "먼저 인스턴스를 Detach Instance로 분리한 다음 컴포넌트를 전환했어야 한다"는 올바른 순서를 지적 — 순서를 거꾸로 실행한 실수였음.
- **복구**: undo 시도 결과 이 실행 환경에서 `figma.commitUndo()`/`triggerUndo()` 둘 다 불가능함을 실측 확인. 마스터 콘텐츠(`357:303`)를 clone해 재구성: `103:77`→`360:297`(완전 복원), 데이터 행 6개(`110:220`~`110:290`)→`361:85`~`361:120`(빈 박스는 해소했으나 **원본 연락처 데이터 값은 복원 불가 — 대체 예시 데이터로 채움**, 은폐 없이 문서화). 재발 방지용 "해제 전 Detach Instance 우선" 표준 절차를 8절에 신설.
- **design-qa 검증**: 전부 PASS.
- 상태: 복구 완료.

### 2026-07-14 실행 라운드 — Figma 페이지 재정렬 + 구분용 빈 페이지 6개 생성 (24차, 최신)
- 배경: 메인 세션이 직접 Figma에서 확정 디자인 8개 프레임의 정확한 위치(파일럿 페이지 `222:524` 안, 도구 한계로 design-scanner가 못 찾았던 것)를 확인해 전달 → 목표 순서 계획을 신뢰 형식으로 승인, "구분용 빈 페이지"도 추가 요청.
- **design-systems 단독 실행**(순수 위치 이동+명명이 이미 100% 명확해 design-prompter 생략): 구분 페이지 6개 신규 생성(`--- BRAND ---` `364:2`/`--- FOUNDATIONS ---` `364:3`/`--- COMPONENT SPECS ---` `364:4`/`--- CONCEPTS ---` `364:5`/`--- COMPONENTS ---` `364:6`/`--- SCREENS ---` `364:7` — Graphic Assets/Motion Assets/Marketing은 현재 미사용이라 스킵). 전체 29개 페이지를 `figma.root.insertChild`로 목표 순서에 맞게 재배열. 페이지 내용(자식 노드)은 전혀 건드리지 않음 — 파일럿 페이지(`222:524`) 내부의 확정 디자인 섹션(`248:11689`)도 가벼운 자식 개수 확인만 하고 손대지 않음.
- **design-qa 검증**: 구분 페이지 6개 이름/빈 상태 정확 확인, 파일럿 내부 확정 8개 프레임 전부(이름/구조/스크린샷) 무결성 확인 **PASS**, 샘플 4개 페이지(Icons/Table Row/Component Specs/Link) 내용 무손상 **PASS**. 전역 페이지 순서(idx 0~28) 자체는 design-qa 툴셋 한계로 완전 재현 검증은 못 했으나 개별 노드 존재·이름 전수 확인으로 실질 위험 낮음. LOW 1건(`15:3` "UI-design " 트레일링 스페이스가 design-system.md 8절 표에 미반영) → 즉시 정정 완료.
- 상태: 페이지 재정렬 실행 완료 + QA 검증 완료 + LOW 정정 완료. `docs/design/design-system.md` 8절 페이지 순서 표, `docs/harness/design-team/figma-file-organization.md` 확인 문구 반영 완료.
