def solution(spell, dic):
    spell.sort()
    if spell in map(sorted, dic):
        return 1
    return 2