import pytest

# 픽스처 상수 — SSOT: entity.constants (GRID_SIZE, MAX_CELL_VALUE, MAGIC_SUM)
# GREEN: from entity.constants import GRID_SIZE, MAX_CELL_VALUE, MAGIC_SUM
GRID_SIZE = 4
MAX_CELL_VALUE = 16
MAGIC_SUM = 34


@pytest.fixture
def grid_g1() -> list[list[int]]:
  # Given: G1 격자 (0이 2개) — PRD §10.2
  grid = [
    [16, 3, 2, 13],
    [5, 10, 0, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
  ]
  assert len(grid) == GRID_SIZE
  assert all(len(row) == GRID_SIZE for row in grid)
  return grid
