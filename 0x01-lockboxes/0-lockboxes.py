def canUnlockAll(boxes):
    """
    canUnlockAll checks if it can unlock all boxes
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        for key in keys:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
