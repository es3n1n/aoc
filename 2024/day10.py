from collections import deque

from aoc import *


aoc_setup(2024, 10)
grid = [list(map(int, line.strip())) for line in day_input_lines()]


def find_bfs(start: tuple[int, int]) -> int:
    queue = deque([(start[0], start[1], 0)])
    seen = {(start[0], start[1])}

    result = set()
    while queue:
        r, c, height = queue.popleft()
        if grid[r][c] == 9 and height == 9:
            result.add((r, c))

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            xd = grid[nr][nc]
            if xd != height + 1:
                continue

            if (nr, nc) in seen:
                continue

            queue.append((nr, nc, xd))
            seen.add((nr, nc))
    return len(result)


def find_dfs(start: tuple[int, int]) -> int:
    result = 0

    def do(r: int, c: int, height: int, seen: set[tuple[int, int]]) -> None:
        nonlocal result

        if grid[r][c] == 9 and height == 9:
            result += 1
            return

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            xd = grid[nr][nc]
            if xd != height + 1:
                continue

            if (nr, nc) in seen:
                continue

            seen.add((nr, nc))
            do(nr, nc, xd, seen)
            seen.remove((nr, nc))

    do(start[0], start[1], 0, {start})
    return result


trailheads = [(r, c) for c in range(len(grid[0])) for r in range(len(grid)) if grid[r][c] == 0]
pt1 = sum(find_bfs(start) for start in trailheads)
pt2 = sum(find_dfs(start) for start in trailheads)

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 36)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 81)
