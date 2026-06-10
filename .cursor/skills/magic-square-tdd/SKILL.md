---
name: magic-square-tdd
description: >-
  MagicSquare 세션 3 validate_lines TDD ARRR 루프를 안내한다. Arrange(Test Plan),
  Red(Skeleton), Green(Minimal), Golden Master, Refactor(Smell/Safe) 슬래시 커맨드
  실행·Phase 선언·금지 사항을 적용할 때 사용. TDD, RED, GREEN, REFACTOR, validate_lines,
  10선, pytest, ARRR 실습 요청 시.
---

# MagicSquare TDD Skill

MagicSquare **세션 3** — `validate_lines` **10선 합 34 판정** TDD 실습 가이드.

---

## SSOT (항상 먼저 읽기)

| 파일 | 용도 |
|------|------|
| `.cursorrules` | 도메인·API·ECB·TDD 금지 |
| `docs/PRD.md` | PRD (없으면 `.cursorrules`만) |
| `.cursor/commands/export-session.md` | 세션 Export |

---

## ARRR 실습 루프

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
       → /refactor-smell → /refactor-safe → /export-session
```

| 단계 | Command | Phase 선언 | 수정 허용 | 산출 |
|------|---------|------------|-----------|------|
| **A**rrange | `/red-test-plan` | `Phase: RED (Test Plan)` | 없음 (계획만) | 테스트 계획표 |
| **R**ed | `/red-skeleton` | `Phase: RED (Skeleton)` | `tests/` | AAA 실패 테스트 |
| **G**reen | `/green-minimal` | `Phase: GREEN (Minimal)` | `src/` | 최소 구현 |
| **Golden** | `/golden-master` | `Phase: Golden Master` | `tests/` fixture | Golden I/O |
| **R**efactor | `/refactor-smell` | `Phase: REFACTOR (Smell)` | 없음 | smell 목록 |
| **R**efactor | `/refactor-safe` | `Phase: REFACTOR (Safe)` | `src/` | smell 1건 제거 |

**레거시:** `/tdd-red` — RED 테스트 추가 (red-skeleton과 유사, Phase: `RED`)

---

## 도메인 요약

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 `list[list[int]]` |
| 셀 | `0`(빈칸) 또는 1~16 |
| 마법상수 | 34 |
| 10선 ID | R1~R4, C1~C4, D1, D2 |
| R5 | `0` 있으면 `incomplete`, 합 검증 생략 |

### API

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": [{"id": str, "sum": int, "expected": 34}, ...],
}
```

---

## Phase 규칙

1. 응답 **첫 줄**에 Phase 선언 (커맨드별 형식 준수)
2. **한 Phase씩** — RED+GREEN+REFACTOR 혼합 금지
3. **슬래시 커맨드 = 무인 실행** — 추가 질문·확인 금지
4. **ECB:** Entity/Control(`src/`)에 I/O·pytest import 금지

---

## TDD 금지 (공통)

| 금지 | 대안 |
|------|------|
| assert 완화 | 구현 또는 계획 수정 |
| skip / xfail | Red 유지 |
| `pass` placeholder (RED) | `/green-minimal` |
| Solver · UI · 1~16 중복 | 세션 3 범위 밖 |
| git commit/push | 사용자 명시 요청 시만 |

---

## pytest

```bash
python -m pytest tests/test_validate_lines.py -v
```

| Phase | 기대 결과 |
|-------|-----------|
| RED | **FAILED** (의도된 Red) |
| GREEN / REFACTOR | **passed** (회귀 없음) |

---

## 커맨드 선택 가이드

| 상황 | Command |
|------|---------|
| 무엇을 테스트할지 모름 | `/red-test-plan` |
| 계획은 있고 테스트 작성 | `/red-skeleton` |
| Red만 있고 구현 필요 | `/green-minimal` |
| fixture·기준값 정리 | `/golden-master` |
| Green 후 코드 지저분 | `/refactor-smell` → `/refactor-safe` |
| 세션 종료 | `/export-session` |

---

## 관련 파일

| 경로 | 설명 |
|------|------|
| `.cursor/commands/red-test-plan.md` | Arrange |
| `.cursor/commands/red-skeleton.md` | Red |
| `.cursor/commands/green-minimal.md` | Green |
| `.cursor/commands/golden-master.md` | Golden Master |
| `.cursor/commands/refactor-smell.md` | Refactor 진단 |
| `.cursor/commands/refactor-safe.md` | Refactor 실행 |
| `.cursor/commands/tdd-red.md` | RED (레거시) |
| `.cursor/skills/magic-square-docs/` | Report·Transcript·Checklist |
