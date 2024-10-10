#!/usr/bin/python3
"""
    Modules thwt check Lockboxes 
"""


def canUnlockAll(boxes):
    """
        To open all boxes in the <F11>arr<F11>ay <F11>and return true if open
    """
    # check if boxes is empty
    if len(boxes) == 0:
        return False

    unlocked_set = set()
    unlocked_set.add(0)

    for index, val in enumerate(boxes):
        # check if index box can't be unlocked
        if index not in unlocked_set:
            return False

        # add key indexes from unlocked box
        for value in val:
            # go to each elem index and update the set
            if value < len(boxes) and value > index:
                unlocked_set.update(boxes[value])
        unlocked_set.update(val)

    return True
