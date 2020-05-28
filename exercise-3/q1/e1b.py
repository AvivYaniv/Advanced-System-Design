def dfs(tree):
    thislevel = [tree]    
    while thislevel:
        n = thislevel.pop()
        father, sons = n[0], n[1]
        yield father
        left, right = None, None
        if 0 < len(sons):
            left = sons[0]
            if 2 == len(sons):
                right = sons[1]
        if right: thislevel.append(right)        
        if left: thislevel.append(left)

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
    
    for value in dfs(tree):
        print(value)
  
if __name__== "__main__":
    main()
  