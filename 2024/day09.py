from tqdm import trange

from aoc import *


aoc_setup(2024, 9)
line = list(map(int, day_input(stripped=True)))

disk: list[int | None] = []
pads = []
counts = []
for i in range(0, len(line), 2):
    disk += [i // 2] * line[i]
    counts += [line[i]]
    if i + 1 < len(line):
        ld = len(disk)
        pads += [ld + j for j in range(line[i + 1])]
        disk += [None] * line[i + 1]


def checksum() -> int:
    return sum(i * (v or 0) for i, v in enumerate(disk))


pre = disk.copy()
for i in range(len(disk) - 1, -1, -1):
    c = disk[i]
    if c is None:
        continue

    xd = pads.pop(0)
    if xd > i:
        break

    disk[xd] = c
    disk[i] = None
    pads.append(i)

pt1 = checksum()
disk = pre

for file_id in trange(max(x or 0 for x in disk), -1, -1):
    count = counts[file_id]
    pos = [i for i, x in enumerate(disk) if x == file_id]
    if not pos:
        continue

    gs = None
    gss = 0
    bgs = None
    for i in range(len(disk)):
        if disk[i] is not None:
            gs = None
            gss = 0
            continue

        if gs is None:
            gs = i

        gss += 1
        if gss >= count and i < pos[0]:
            bgs = gs
            break

    if bgs is not None:
        for pos in pos:
            disk[pos] = None
        for i in range(count):
            disk[bgs + i] = file_id

pt2 = checksum()

answer(1, pt1, auto_submit=True)
expect_demo_answer(1, 1928)

answer(2, pt2, auto_submit=True)
expect_demo_answer(2, 2858)
