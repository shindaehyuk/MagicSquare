# RED Test Plan — validate_lines

MagicSquare 세션 3 · **ARRR Arrange** 단계 전용 슬래시 커맨드.
`/red-test-plan`만 입력해도 **추가 질문 없이** 테스트 계획표를 작성한다. **코드·파일 수정 금지.**

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/red-test-plan` 만 입력했다. 미커버 시나리오·현재 테스트·대화 맥락은 **현재 채팅·저장소**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `tests/test_validate_lines.py` — 기존 테스트 현황 |
| 4 | `.cursor/commands/tdd-red.md` — RED API 계약 |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: RED (Test Plan)
```

한 Phase에 **계획만** 수행한다. 테스트 코드 작성·`src/` 수정·pytest 실행·GREEN·REFACTOR 금지.

---

## 범위

| 항목 | 내용 |
|------|------|
| 대상 API | `validate_lines(grid) -> dict` |
| 세션 3 | **10선 합 34 판정** — Solver · UI · 1~16 중복 검증 제외 |
| 10선 ID | R1~R4, C1~C4, D1(`diag:main`), D2(`diag:anti`) |
| R5 | `0` 포함 → `status=incomplete`, 합 계산·34 비교 **생략** |
| status | `pass` \| `fail` \| `incomplete` |

---

## Arrange — 할 일

1. SSOT·기존 `tests/`를 읽고 **아직 계획되지 않은 시나리오**를 식별
2. 각 시나리오에 **AAA**(Arrange / Act / Assert) 분해
3. 아래 **보고 형식**으로 테스트 계획표만 출력
4. **파일을 수정하지 않는다** — `/red-skeleton` 또는 `/tdd-red` 전 단계

---

## 시나리오 체크리스트 (기본 커버리지)

| # | 시나리오 | 기대 status | 우선순위 |
|---|----------|-------------|----------|
| T1 | 완성 격자 — 10선 모두 34 | `pass` | P0 |
| T2 | 한 줄 합≠34 (행) | `fail` + failed_lines | P0 |
| T3 | 한 줄 합≠34 (열) | `fail` | P1 |
| T4 | 한 줄 합≠34 (주대각) | `fail` | P1 |
| T5 | 한 줄 합≠34 (부대각) | `fail` | P1 |
| T6 | 복수 줄 동시 fail | `fail` + 여러 failed_lines | P2 |
| T7 | 격자에 `0` 1개 이상 | `incomplete` | P0 |
| T8 | `0`과 합≠34 공존 | `incomplete` (R5 우선) | P1 |

이미 테스트·계획에 있는 항목은 **제외**하고, **다음 1~3개**만 우선 제안.

---

## 보고 형식

```markdown
Phase: RED (Test Plan)

## 현재 커버리지
| 상태 | 테스트/계획 | 비고 |
|------|-------------|------|
| ✅ 커버됨 | `test_...` 또는 (없음) | ... |
| ⬜ 미커버 | ... | ... |

## 다음 테스트 계획 (우선순위순)
| # | 테스트명(안) | Arrange | Act | Assert | 기대 status | failed_lines |
|---|--------------|---------|-----|--------|-------------|--------------|
| 1 | `test_...` | 4×4 grid 설명 | `validate_lines(grid)` | status, failed_lines | pass/fail/incomplete | ... |

## Golden Master 후보
| fixture명 | 용도 | grid 요약 |
|-----------|------|-----------|
| `VALID_GRID` | pass 기준 | 4×4 완성 마방진 |

## 다음 단계 (코드 없음)
- `/red-skeleton` — 위 계획 1번부터 스켈레ton 작성
- `/tdd-red` — 바로 RED 테스트 추가
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`tests/`·`src/` 수정** | Arrange는 계획만 |
| **pytest 실행** | 스켈레ton·구현 전 |
| **assert 완화·범위 확장** | Solver/UI/중복 검증 |
| **Phase 혼합** | skeleton·GREEN·REFACTOR 동시 |
| **사용자에게 시나리오 질문** | 무인 실행 |

---

## 완료 보고 (한 줄)

```
Test Plan 완료 — 다음 {N}개 시나리오 → `/red-skeleton`
```
