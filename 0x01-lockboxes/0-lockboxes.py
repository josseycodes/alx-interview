def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # The first box is always unlocked

    for box in range(num_boxes):
        if unlocked[box]:
            for key in boxes[box]:
                if key < num_boxes and not unlocked[key]:
                    unlocked[key] = True

    return all(unlocked)

