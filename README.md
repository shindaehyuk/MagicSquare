# MagicSquare

작성자 : 신대혁, 리뷰어 : 홍길동

4×4 부분 마방진 프로젝트. 세션 3은 `validate_lines`(10선 합 34 판정), 세션 4 Entity Track B는 빈칸 좌표 탐색 등 도메인 로직을 TDD(ARRR)로 진행한다.

상세 요구사항: [`docs/PRD.md`](docs/PRD.md)

---

## 테스트 플랜 — G1 격자 SSOT (PRD §10.2)

PRD [`§10.2 G1 격자 SSOT`](docs/PRD.md) 를 기준으로 한 **공통 픽스처·검증 계획**이다. G1은 이후 `D-MIS-01`, `D-SOL-01` 등 Track B 테스트의 **입력 SSOT**로 재사용한다.

### G1 SSOT 정의

| 항목 | 값 |
|------|-----|
| 격자 (0-index `grid[row][col]`) | 아래 4×4 |
| 빈칸 0-index | `(1, 2)`, `(3, 3)` |
| 빈칸 **1-index row-major** | `(2, 3)`, `(4, 4)` |
| 픽스처 | `tests/conftest.py` → `grid_g1` |
| 상수 (구현 예정) | `src/entity/constants.py` |

```text
[[16,  3,  2, 13],
 [ 5, 10,  0,  8],
 [ 9,  6,  7, 12],
 [ 4, 15, 14,  0]]
```

### 연결 요구사항

| 항목 | 내용 |
|------|------|
| FR | **FR-LOC-01** — 4×4 격자에서 빈칸(0) 좌표를 **1-index row-major** 순으로 반환 |
| 판단 문구 | 격자에 빈칸이 **정확히 2개**일 때, 좌표 목록이 **row-major 오름차순**으로 반환된다 |
| 대상 함수 | `find_blank_coords(grid) -> list[tuple[int, int]]` |
| Test ID | **D-LOC-01** (G1이 Given SSOT) |
| Invariant | **I6** row-major |

### G1 기반 테스트 계획

| Test ID | 테스트명(안) | Given | When | Then | 상태 |
|---------|--------------|-------|------|------|------|
| D-LOC-01-1 | `test_d_loc_01_blank_coords_row_major` | `grid_g1` fixture (PRD §10.2) | `find_blank_coords(grid_g1)` | `[(2, 3), (4, 4)]` | RED (스켈레ton 작성됨) |

**AAA 분해 (D-LOC-01-1)**

| 단계 | 내용 |
|------|------|
| **Arrange** | `grid_g1` — 0-index 빈칸 `(1,2)`, `(3,3)` |
| **Act** | `result = find_blank_coords(grid_g1)` |
| **Assert** | `result == [(2, 3), (4, 4)]` (1-index, row-major) |

### 픽스처·파일

| 파일 | 역할 |
|------|------|
| `tests/conftest.py` | `grid_g1` — G1 격자 리터럴 (로직 없음) |
| `tests/entity/test_d_loc_01.py` | D-LOC-01 RED 테스트 |
| `src/entity/loc.py` | `find_blank_coords` 구현 (GREEN 단계) |

### pytest

```bash
# G1 SSOT 단일 테스트
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v

# D-LOC-01 묶음 전체
python -m pytest tests/entity/test_d_loc_01.py -v
```

### ECB·Mock 점검

| 항목 | 규칙 |
|------|------|
| Logic Track | 도메인 로직 **Mock 금지** — `grid_g1` 데이터 + 실제 `find_blank_coords` 호출 |
| Entity | boundary/control import 금지 |
| E001~E005 | entity에서 에러 코드 emit 금지 |

### TDD 진행

| Phase | G1 관련 산출 |
|-------|--------------|
| RED (Test Plan) | 본 섹션 — G1 SSOT·D-LOC-01-1 계획 |
| RED (Skeleton) | `test_d_loc_01_blank_coords_row_major` + `grid_g1` fixture |
| GREEN | `find_blank_coords` 최소 구현 → G1 assert 통과 |
| Golden Master | `grid_g1` / `[(2,3),(4,4)]` 기준값 고정 |

---

## 실행 (세션 3)

```bash
python -m pytest tests/test_validate_lines.py -v
```
