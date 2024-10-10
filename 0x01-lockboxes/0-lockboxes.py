#!/usr/bin/python3
"""
Solution to the lockboxes problem.
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Parameters:
    boxes (List[List[int]]): A list of boxes, each containing a list of keys.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    unlocked = [False] * len(boxes)  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is always unlocked
    keys = boxes[0]  # Keys from the first box

    for key in keys:
        if key < len(boxes):
            unlocked[key] = True  # Unlock the box using the key

    for i in range(len(boxes)):
        if unlocked[i]:
            for key in boxes[i]:
                if key < len(boxes):
                    unlocked[key] = True

    return all(unlocked)  # Check if all boxes are unlocked
