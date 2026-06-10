# TDD RED — validate_lines

MagicSquare 세션 3 · **`validate_lines` RED 단계 전용** 슬래시 커맨드.
`tests/`만 수정한다. 구현은 GREEN에서 한다.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: RED
```

한 Phase에 RED만 수행한다. GREEN·REFACTOR로 넘어가지 않는다.

---

## 범위

| 항목 | 내용 |
|------|------|
| 대상 API | `validate_lines(grid) -> dict` (`src/validate_lines.py`) |
| 세션 3 | **10선 합 34 판정**만 — Solver · UI · 1~16 중복 검증 제외 |
| 격자 | 4×4, 셀 `0`(빈칸) 또는 1~16, 마법상수 **34** |
| 10선 | R1~R4(행), C1~C4(열), D1(주대각), D2(부대각) |
| R5 | `0`이 하나라도 있으면 `status=incomplete`, 합 계산·34 비교 **생략** |

### API 계약 (Boundary assert 기준)

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": [  # fail일 때만; 틀린 줄만
        {"id": str, "sum": int, "expected": 34},
        ...
    ],
}
```

- **pass**: 10선 모두 합 34, `failed_lines=[]`
- **fail**: 하나 이상 합≠34, `failed_lines`에 해당 줄만
- **incomplete**: `0` 포함, `failed_lines=[]`

---

## AAA 절차

각 테스트는 **Arrange → Act → Assert** 순서로 작성한다.

| 단계 | 내용 |
|------|------|
| **Arrange** | 4×4 `grid` fixture 또는 리터럴 준비. 기대 `status`·`failed_lines`를 주석 또는 변수로 명시 |
| **Act** | `result = validate_lines(grid)` — **한 번만** 호출 |
| **Assert** | API 계약만 검증: `result["status"]`, `result["failed_lines"]` (줄 ID, `sum`, `expected: 34`) |

규칙:

- 테스트 이름: `test_<조건>_<기대_status>` (예: `test_all_lines_sum_34_returns_pass`)
- 한 테스트 = **하나의 행위·하나의 실패 이유** (여러 assert는 같은 Act 결과에 대해서만)
- Entity/Control 로직을 테스트에 복제하지 않는다 — **입·출력 계약**만 assert

---

## RED에서 할 일

1. `.cursorrules`·위 API 계약을 읽고 **아직 없거나 미구현인 동작**에 대한 테스트를 `tests/`에 추가
2. `python -m pytest` 실행 — **새 테스트가 실패(Red)** 하는지 확인
3. 아래 **보고 형식**으로 결과 보고
4. `src/`는 **손대지 않는다** (stub `...` 그대로여도 됨)

---

## pytest 예시

`tests/test_validate_lines.py`:

```python
from validate_lines import validate_lines

# 완성 격자 — 10선 모두 34 (Arrange)
VALID_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]


def test_all_lines_sum_34_returns_pass():
    # Act
    result = validate_lines(VALID_GRID)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_row_sum_not_34_returns_fail_with_failed_lines():
    grid = [row[:] for row in VALID_GRID]
    grid[0][0] = 1  # R1 합 깨짐

    result = validate_lines(grid)

    assert result["status"] == "fail"
    assert len(result["failed_lines"]) >= 1
    failed = result["failed_lines"][0]
    assert failed["expected"] == 34
    assert failed["sum"] != 34
    assert "id" in failed


def test_grid_with_zero_returns_incomplete():
    grid = [row[:] for row in VALID_GRID]
    grid[1][3] = 0  # R5: 빈칸 포함

    result = validate_lines(grid)

    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []
```

실행:

```bash
python -m pytest tests/test_validate_lines.py -v
```

RED 성공 기준: **새로 추가한 테스트가 실패**하고, 실패 원인이 **미구현·미달**이지 assert 오류가 아님.

---

## 보고 형식

RED 작업 후 아래 형식으로만 요약한다.

```markdown
Phase: RED

## 추가한 테스트
| 테스트 | Arrange 요약 | 기대 status | 기대 failed_lines |
|--------|--------------|-------------|-------------------|
| `test_...` | ... | pass/fail/incomplete | ... |

## pytest 결과
- 명령: `python -m pytest ...`
- 결과: **FAILED** (의도된 Red) / n passed, m failed
- 대표 실패 메시지: `...`

## 다음 GREEN 힌트 (구현 없음)
- `src/validate_lines.py`에서 채워야 할 동작 1~3줄
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정** | RED는 테스트만 — 구현은 GREEN |
| **assert 완화** | `==` → `in`, 기대값 변경, 조건 삭제로 통과시키기 |
| **`@pytest.mark.skip` / `xfail`** | 실패를 숨기면 Red가 아님 |
| **`pass` placeholder로 우회** | GREEN 전용 |
| **범위 밖 기능** | Solver, UI, 1~16 중복 검증 |
| **Phase 혼합** | 한 응답에서 GREEN·REFACTOR 동시 수행 |

위반 시: 변경 되돌리고, `Phase: RED`로 다시 시작한다.
