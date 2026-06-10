# REFACTOR Smell — validate_lines

MagicSquare 세션 3 · **ARRR Refactor (분석)** 단계 전용 슬래시 커맨드.
`/refactor-smell`만 입력해도 **추가 질문 없이** 코드 smell 목록을 진단한다. **리팩터 실행은 하지 않는다.**

---

## 실행 조건 (필수)

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-smell` 만 입력했다. 대상 코드·테스트 상태는 **src/·tests/·pytest·현재 채팅**에서 자동 추출한다. 추가 질문·확인 요청 금지.

---

## SSOT (먼저 읽을 것)

| 우선순위 | 파일 |
|----------|------|
| 1 | `.cursorrules` |
| 2 | `docs/PRD.md` (없으면 `.cursorrules`만) |
| 3 | `src/validate_lines.py` |
| 4 | `tests/test_validate_lines.py` |

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시:

```
Phase: REFACTOR (Smell)
```

**진단·목록만** 수행. 코드 수정·테스트 변경 금지.

---

## 전제

- pytest **전부 Green** (Red 있으면 smell 진단 전 `/green-minimal` 권고만 보고)
- Golden Master fixture 확정 권장 (없어도 진단 가능)

---

## Smell 체크리스트 (MagicSquare)

| smell | 징후 | validate_lines 예 |
|-------|------|-------------------|
| **Duplicated Code** | 10선 합 계산 copy-paste | 행/열/대각 for 루프 3벌 |
| **Long Method** | `validate_lines` 한 함수에 전부 | 50줄+ 단일 함수 |
| **Magic Number** | `34` 하드코딩 산재 | expected 없이 리터럴 |
| **Primitive Obsession** | 줄 ID 문자열 수동 조립 | `"R" + str(i)` 산재 |
| **Shotgun Surgery** | 줄 ID 변경 시 여러 곳 수정 | id 맵핑 분산 |
| **Dead Code** | Green 후 unreachable 분기 | 사용 안 하는 helper |

---

## REFACTOR Smell — 할 일

1. `src/validate_lines.py`·`tests/` 읽기
2. `python -m pytest` — Green 여부 확인
3. smell **목록·위치·심각도·제안**만 출력 (코드 diff 없음)
4. 아래 **보고 형식** 준수

---

## 보고 형식

```markdown
Phase: REFACTOR (Smell)

## pytest 상태
- 결과: n passed / m failed
- Green 아니면: `/green-minimal` 먼저 (smell 진단 중단)

## Smell 목록
| # | smell | 위치 | 심각도 | 제안 (한 줄) |
|---|-------|------|--------|--------------|
| 1 | Duplicated Code | `validate_lines.py:L10-30` | 높음 | `_sum_line(cells, id)` 추출 |

## 리팩터 후보 (우선순위)
1. ...
2. ...

## 다음 단계 (코드 변경 없음)
- `/refactor-safe` — #1 smell부터 안전 리팩터
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/`·`tests/` 수정** | 분석 Phase |
| **동작 변경** | smell 진단만 |
| **범위 밖 리팩터** | Solver/UI 분리 등 |
| **Phase 혼합** | safe refactor 동시 |
| **사용자에게 smell 질문** | 무인 실행 |

---

## 완료 보고 (한 줄)

```
REFACTOR Smell 완료 — {N}건 → `/refactor-safe`
```
