# Golden Master — validate_lines

MagicSquare 세션 3 · **ARRR Golden Master** 단계 전용 슬래시 커맨드.
`/golden-master`만 입력해도 **추가 질문 없이** 기준 격자(fixture)·기대 출력을 정리한다.

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/golden-master` 만 입력했다. 기존 fixture·테스트·구현 상태는 **tests/·src/·현재 채팅**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `tests/test_validate_lines.py` |
| 4 | `src/validate_lines.py` |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: Golden Master
```

Golden Master **정리·문서화**만 수행. 범위 밖 리팩터·새 기능 금지.

---

## Golden Master란

| 개념 | MagicSquare 적용 |
|------|------------------|
| **Golden Input** | 검증된 4×4 `grid` fixture |
| **Golden Output** | `validate_lines(grid)` 기대 `dict` |
| **용도** | 회귀 방지·테스트 Arrange SSOT·수동 검산 대체 |

---

## 범위

| 항목 | 내용 |
|------|------|
| 권장 수정 | `tests/test_validate_lines.py` — **fixture 상수·주석** 정리 |
| 선택 | `tests/fixtures/golden_grids.py` (없으면 생성 가능) |
| 금지 | `src/` 동작 변경, assert 완화, 범위 밖 격자 |

---

## Golden Master — 할 일

1. SSOT 기준 **표준 fixture 세트** 정의·정리
2. 각 fixture에 **Golden Output** (status, failed_lines) 명시
3. 중복 grid 리터럴 → **공유 상수**로 통합 (동작 변경 없이)
4. 아래 **보고 형식**으로 결과 보고

---

## 표준 Golden Master 세트 (기본)

| fixture | grid 설명 | Golden Output |
|---------|-----------|---------------|
| `VALID_GRID` | 완성 4×4 마방진 (10선=34) | `status=pass`, `failed_lines=[]` |
| `INCOMPLETE_GRID` | `VALID_GRID` + 셀 1개 `0` | `status=incomplete`, `failed_lines=[]` |
| `FAIL_ROW_GRID` | R1 합 깨짐 | `status=fail`, failed_lines에 R1 |
| `FAIL_DIAG_GRID` | D1 또는 D2 합 깨짐 | `status=fail`, failed_lines에 D1/D2 |

### VALID_GRID (SSOT)

```python
VALID_GRID = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]
```

---

## 보고 형식

```markdown
Phase: Golden Master

## Golden Master 목록
| fixture | status | failed_lines (요약) | 사용 테스트 |
|---------|--------|---------------------|-------------|
| `VALID_GRID` | pass | [] | `test_...` |

## 변경 파일
| 파일 | 변경 |
|------|------|
| `tests/...` | fixture 통합 / 주석 |

## pytest 결과 (회귀 확인)
- 명령: `python -m pytest tests/test_validate_lines.py -v`
- 결과: n passed — **회귀 없음**

## 다음 단계
- `/refactor-smell` — 중복· smell 점검
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **Golden Output 임의 변경** | SSOT 위반 |
| **assert 완화** | 회귀 숨김 |
| **범위 밖 격자** | 1~16 중복 검증 등 |
| **Phase 혼합** | REFACTOR 본격 수행 |
| **사용자에게 fixture 질문** | 무인 실행 |

---

## 완료 보고 (한 줄)

```
Golden Master 완료 — {N}개 fixture → `/refactor-smell`
```
