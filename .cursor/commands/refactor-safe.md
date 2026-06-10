# REFACTOR Safe — validate_lines

MagicSquare 세션 3 · **ARRR Refactor (실행)** 단계 전용 슬래시 커맨드.
`/refactor-safe`만 입력해도 **추가 질문 없이** smell 1건씩 안전 리팩터한다.

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-safe` 만 입력했다. 대상 smell·코드는 **refactor-smell 보고·src/·현재 채팅**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `.cursor/commands/refactor-smell.md` — smell 목록 |
| 4 | `src/validate_lines.py` · `tests/` |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: REFACTOR (Safe)
```

한 Phase에 **smell 1건(또는 동일 추출 1회)** 만 리팩터. RED·GREEN 혼합 금지.

---

## Safe Refactor 규칙

| 규칙 | 내용 |
|------|------|
| **Green 유지** | 리팩터 전후 pytest **전부 pass** |
| **한 번에 하나** | Extract Method / 상수 추출 / id 헬퍼 등 1 smell |
| **테스트 불변** | `tests/` assert·기대값 **변경 금지** (필요 시 Golden Master bug만) |
| **ECB** | Entity/Control에 I/O·pytest import 금지 |
| **동작 동일** | API 계약·R1~R5 불변 |

---

## REFACTOR Safe — 할 일

1. smell 목록(없으면 `src/`에서 **Duplicated Code** 1건 자동 선택)
2. `python -m pytest` — **시작 Green** 확인
3. smell **1건** 리팩터 (`src/` 위주)
4. pytest 재실행 — **회귀 없음** 확인
5. 아래 **보고 형식**으로 결과 보고

---

## 허용 리팩터 패턴

| 패턴 | 예 |
|------|-----|
| Extract Function | `_line_sum(cells) -> int` |
| Named Constant | `MAGIC_SUM = 34` |
| Line ID Map | `ROW_IDS = ["R1","R2","R3","R4"]` |
| Early Return | R5 incomplete 분리 (동작 동일) |

---

## 보고 형식

```markdown
Phase: REFACTOR (Safe)

## 리팩터한 smell
| smell | 변경 | 파일 |
|-------|------|------|
| Duplicated Code | `_sum_row` 추출 | `src/validate_lines.py` |

## pytest 결과
- Before: n passed
- After: n passed (**회귀 없음**)

## 남은 smell
| # | smell | 다음 |
|---|-------|------|
| 2 | Magic Number | `/refactor-safe` 반복 |

## 다음 단계
- smell 남음 → `/refactor-safe`
- 완료 → `/export-session` 세션 Export
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **테스트 assert 변경** | 동작 변경 우회 |
| **한 번에 여러 smell** | 회귀 원인 추적 불가 |
| **기능 추가** | REFACTOR ≠ GREEN |
| **범위 밖** | Solver, UI, 중복 검증 |
| **git commit/push** | 사용자 명시 요청 시만 |
| **Red 상태에서 리팩터** | Green 선행 |

---

## 완료 보고 (한 줄)

```
REFACTOR Safe 완료 — smell "{이름}" → {n} passed, {남은 smell}건
```
