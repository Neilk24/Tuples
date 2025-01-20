def palindrome(r):
    e = len(r) - 1
    s = 0

    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

if palindrome(r):
    print('This tuple is a Flip-Flop Palindrome.')

else:
    print('This tuple is not a Flip-Flop Palindrome.')