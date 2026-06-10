# RED Skeleton — validate_lines

MagicSquare 세션 3 · **ARRR Red** 단계 전용 슬래시 커맨드.
`/red-skeleton`만 입력해도 **추가 질문 없이** AAA 스켈레ton 테스트를 `tests/`에 추가한다.

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/red-skeleton` 만 입력했다. 작성할 시나리오는 **Test Plan·현재 채팅·기존 tests/** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `.cursor/commands/red-test-plan.md` — 직전 계획 |
| 4 | `.cursor/commands/tdd-red.md` — API 계약·AAA 규칙 |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: RED (Skeleton)
```

한 Phase에 **스켈레ton RED만** 수행한다. GREEN·REFACTOR 금지.

---

## 범위

| 항목 | 내용 |
|------|------|
| 수정 허용 | `tests/` **만** |
| 수정 금지 | `src/` (stub `...` 유지) |
| 대상 API | `validate_lines(grid) -> dict` |
| 테스트 이름 | `test_<조건>_<기대_status>` |

### API 계약 (Assert 기준)

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": [  # fail일 때만
        {"id": str, "sum": int, "expected": 34},
    ],
}
```

---

## AAA 스켈레ton 규칙

| 단계 | 스켈레ton 작성법 |
|------|------------------|
| **Arrange** | `# Arrange` 주석 + `grid` 리터럴 또는 fixture. 기대값을 주석으로 명시 |
| **Act** | `# Act` + `result = validate_lines(grid)` **한 번만** |
| **Assert** | `# Assert` + API 계약 assert (`status`, `failed_lines` 구조) |

- 한 테스트 = **하나의 행위·하나의 실패 이유**
- Entity/Control 로직을 테스트에 **복제하지 않음**
- `# TODO`로 Act·Assert만 두고 Arrange만 채우는 것 **금지** — AAA **전부** 작성

---

## RED Skeleton — 할 일

1. SSOT·Test Plan(있으면)에서 **다음 1~2개** 미커버 시나리오 선택
2. `tests/test_validate_lines.py`에 AAA 스켈레ton 테스트 추가
3. `python -m pytest` 실행 — **의도된 Red** 확인
4. 아래 **보고 형식**으로 결과 보고
5. `src/`는 **손대지 않는다**

---

## 스켈레ton 예시

```python
def test_all_lines_sum_34_returns_pass():
    # Arrange
    grid = [
        [16,  3,  2, 13],
        [ 5, 10,  11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []
```

---

## 보고 형식

```markdown
Phase: RED (Skeleton)

## 추가한 스켈레ton
| 테스트 | Arrange 요약 | 기대 status | AAA |
|--------|--------------|-------------|-----|
| `test_...` | ... | pass/fail/incomplete | ✅ |

## pytest 결과
- 명령: `python -m pytest tests/test_validate_lines.py -v`
- 결과: **FAILED** (의도된 Red) / n passed, m failed
- 대표 실패: `...`

## 다음 단계 (구현 없음)
- `/green-minimal` — src/ 최소 구현
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정** | RED는 tests/만 |
| **assert 완화·skip·xfail** | Red 숨김 |
| **`pass` placeholder** | GREEN 전용 |
| **범위 밖 기능** | Solver, UI, 중복 검증 |
| **Phase 혼합** | GREEN·REFACTOR 동시 |
| **사용자에게 시나리오 질문** | 무인 실행 |

---

## 완료 보고 (한 줄)

```
RED Skeleton 완료 — {N}개 테스트 Red → `/green-minimal`
```
