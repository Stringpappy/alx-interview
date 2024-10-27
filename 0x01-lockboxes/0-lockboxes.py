#!/usr/bin/python3
"""
    the Lockboxes
"""


def canUnlockAll(boxes):
    """
       To  Returns true if all box open
    """
    # check if boxes is empty
    if len(boxes) == 0:
        return False

    open_set = set()
    open_set.add(0)

    for index, val in enumerate(boxes):
        # check if index box can't be unlocked
        if index not in open_set:
            return False

        # add key indexes from unlocked box
        for value in val:
            # go to each elem index and update the set
            if value < len(boxes) and value > index:
                open_set.update(boxes[value])
        open_set.update(val)

    return True
