# MagicSquare ARRR 세션 Checklist

> Phase 완료·Export 전 자체 점검용. `{ }` 항목을 채워 사용.

---

## 메타

| 항목 | 값 |
|------|-----|
| 세션 주제 | {한 줄} |
| Phase | {RED (Plan) / RED (Skeleton) / GREEN / Golden Master / REFACTOR / Export} |
| 날짜 | {YYYY-MM-DD} |

---

## SSOT

- [ ] `.cursorrules` 확인
- [ ] `docs/PRD.md` 확인 (없으면 `.cursorrules`만)
- [ ] 세션 3 범위 준수 (Solver · UI · 1~16 중복 **제외**)

---

## TDD — RED

- [ ] 응답 첫 줄 `Phase: RED (...)` 선언
- [ ] `tests/`만 수정 (Plan 단계는 **수정 없음**)
- [ ] AAA (Arrange → Act → Assert) 준수
- [ ] API 계약만 assert (`status`, `failed_lines`)
- [ ] pytest **의도된 Red** (Plan 제외)
- [ ] assert 완화 · skip · xfail **없음**
- [ ] `src/` 미수정 (Plan·Skeleton)

---

## TDD — GREEN

- [ ] 응답 첫 줄 `Phase: GREEN (Minimal)` 선언
- [ ] `src/`만 수정 — **최소** 구현
- [ ] `tests/` assert **불변**
- [ ] pytest Green (해당 Red 해결)
- [ ] 과도한 추상화 **없음**

---

## Golden Master

- [ ] `Phase: Golden Master` 선언
- [ ] `VALID_GRID` 등 fixture·Golden Output 명시
- [ ] 회귀 없음 (pytest pass)

---

## REFACTOR

- [ ] Smell: `Phase: REFACTOR (Smell)` — **코드 변경 없음**
- [ ] Safe: `Phase: REFACTOR (Safe)` — smell **1건**
- [ ] 리팩터 전후 pytest **전부 pass**
- [ ] API·R1~R5 **동작 동일**

---

## ECB · 도메인

- [ ] 4×4 격자, 셀 `0` 또는 1~16
- [ ] 10선 ID: R1~R4, C1~C4, D1, D2
- [ ] R5: `0` → `incomplete`, 합 검증 생략
- [ ] Entity/Control에 I/O·pytest import **없음**

---

## Docs · Export

- [ ] `/export-session` — 추가 질문 **없음**
- [ ] `Report/NN.REPORT.md` + `Prompting/NN.Export-Transcript.md` **2개**
- [ ] 번호 2자리, **덮어쓰기 없음**
- [ ] Transcript = User/Cursor **전문** (요약 아님)

---

## Git (선택)

- [ ] commit/push — **사용자 명시 요청 시만**

---

## 판정

| 결과 | 조건 |
|------|------|
| ✅ 통과 | 위 해당 Phase 항목 전부 |
| ⚠️ 부분 | 1~2건 미달 — 다음 커맨드 명시 |
| ❌ 재시작 | Phase 혼합 · assert 완화 · 범위 위반 |

**다음 커맨드:** `{ /red-skeleton | /green-minimal | /refactor-safe | /export-session }`
