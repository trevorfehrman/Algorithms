#!/usr/bin/python
def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    perms = []
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in options]

    def perm(arr, num):
        if num == 0:
            perms.append(arr)

        else:
            for i in options:
                perm(arr + [i], num - 1)
    perm([], n)
    return len(perms)


print(rock_paper_scissors(2))
