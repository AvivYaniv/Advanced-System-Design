def bfs(tree):
    thislevel = [tree]    
    while thislevel:
        n = thislevel.pop(0)
        father, sons = n[0], n[1]
        yield father
        left, right = None, None
        if 0 < len(sons):
            left = sons[0]
            if 2 == len(sons):
                right = sons[1]
        if left: thislevel.append(left)
        if right: thislevel.append(right)        

def main():
    tree = (1, [
        (2, [
            (4, []),
            (5, []),
        ]),
        (3, [
            (6, []),
            (7, []),
        ]),
    ])
    
    for value in bfs(tree):
        print(value)
  
if __name__== "__main__":
    main()
