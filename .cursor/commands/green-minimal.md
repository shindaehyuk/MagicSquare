# GREEN Minimal — validate_lines

MagicSquare 세션 3 · **ARRR Green** 단계 전용 슬래시 커맨드.
`/green-minimal`만 입력해도 **추가 질문 없이** `src/` 최소 구현으로 Red 테스트를 Green으로 만든다.

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/green-minimal` 만 입력했다. 실패 중인 테스트·Red 원인은 **pytest 출력·tests/·현재 채팅**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `tests/test_validate_lines.py` — 실패 테스트 |
| 4 | `.cursor/commands/red-skeleton.md` · `tdd-red.md` |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: GREEN (Minimal)
```

한 Phase에 **최소 GREEN만** 수행한다. REFACTOR·테스트 assert 변경 금지.

---

## 범위

| 항목 | 내용 |
|------|------|
| 수정 허용 | `src/` **만** (`src/validate_lines.py`) |
| 수정 금지 | `tests/` assert·기대값 (Red 유지) |
| 원칙 | **가장 단순한 코드**로 현재 Red만 Green — YAGNI |
| ECB | Entity/Control에 I/O·print·pytest import 금지 |

---

## Minimal GREEN — 할 일

1. `python -m pytest` 실행 — **현재 Red** 목록 확인
2. Red **1개(또는 동일 원인 묶음)** 에 대해 `src/validate_lines.py` **최소** 수정
3. pytest 재실행 — 해당 테스트 **Green** 확인
4. 아래 **보고 형식**으로 결과 보고
5. **리팩터·일반화·최적화는 하지 않는다** — `/refactor-smell` 이후

---

## 최소 구현 가이드 (우선순위)

| Red 원인 | Minimal 접근 |
|----------|--------------|
| `pass` 미구현 | 10선 합 계산 + 34 비교 **해당 테스트만** 통과하는 분기 |
| `incomplete` | `0` 존재 검사 후 early return |
| `fail` + failed_lines | 틀린 줄만 `{id, sum, expected: 34}` 수집 |
| 줄 ID | R1~R4, C1~C4, D1, D2 (SSOT 통일) |

---

## 보고 형식

```markdown
Phase: GREEN (Minimal)

## 해결한 Red
| 테스트 | Red 원인 | 최소 변경 요약 |
|--------|----------|----------------|
| `test_...` | ... | ... |

## pytest 결과
- 명령: `python -m pytest tests/test_validate_lines.py -v`
- 결과: **n passed**, m failed (남은 Red)
- Green 확인: `test_...` ✅

## 남은 Red (있으면)
| 테스트 | 예상 다음 Minimal |
|--------|-------------------|
| `test_...` | ... |

## 다음 단계 (리팩터 없음)
- Red 남음 → `/green-minimal` 반복
- 전부 Green → `/golden-master` 또는 `/refactor-smell`
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`tests/` assert 변경** | Red를 Green으로 속이기 |
| **과도한 추상화** | Minimal 원칙 |
| **범위 밖 기능** | Solver, UI, 중복 검증 |
| **Phase 혼합** | REFACTOR·새 RED 동시 |
| **git commit/push** | 사용자 명시 요청 시만 |
| **사용자에게 구현 방식 질문** | 무인 실행 |

---

## 완료 보고 (한 줄)

```
GREEN Minimal 완료 — {n} passed / {m} failed → {다음 커맨드}
```
