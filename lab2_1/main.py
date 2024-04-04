from collections import deque

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def readdict(file_name):
    with open(file_name, "r") as file:
        d = set()
        for line in file:
            word = line.strip()
            if len(word) == 0:
                break
            d.add(word)
    return d


def readwords(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        cases = []
        for line in lines:
            words = line.strip().split()
            if len(words) == 2:  # Проверяем, что строка содержит ровно два слова
                start, end = words
                cases.append((start, end))
    return cases


def word_mods(w, dictionary):
    """Return list of all valid step modifications from a given word"""
    mods = []

    for pos in range(len(w)):
        for c in ALPHABET:
            word = w[:pos] + c + w[(pos + 1) :]
            if word in dictionary and word != w:
                mods.append(word)

    return mods


def find_solution(start, end, dictionary):
    """Use BFS to find shortest path from start to end words"""
    if start == end:
        return [start, end]

    # Add endword to dictionary
    add_end = end not in dictionary
    if add_end:
        dictionary.add(end)

    # BFS Search
    parent = {}
    q = deque([start])

    while q:
        word = q.popleft()

        if word == end:
            break

        # Enqueue word mods that haven't been reached yet.
        for w in word_mods(word, dictionary):
            if w not in parent:
                parent[w] = word
                q.append(w)

    # Restore dictionary to original state
    if add_end:
        dictionary.remove(end)

    if word != end:
        return []

    # Reconstruct modification path
    path = [word]
    while parent[word] != start:
        path.append(parent[word])
        word = parent[word]
    path.append(start)

    return list(reversed(path))


if __name__ == "__main__":
    file = "input3.txt"  # Используем один и тот же файл для чтения словаря и входных данных
    dictionary = readdict(file)
    words = list(reversed(readwords(file)))

    while words:
        start, end = words.pop()

        sequence = find_solution(start, end, dictionary)
        if not sequence:
            print("No solution.")
        else:
            [print(w) for w in sequence]

        if words:
            print()
