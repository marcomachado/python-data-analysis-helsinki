#!/usr/bin/env python3

def detect_ranges(L):
    L.sort()
    print(L)
    n = 0
    newList = []
    while n < len(L)-1:
        print(f"n={n}")
        atual = L[n]
        next = L[n+1]
        if next != atual+1:            
            newList.append(L[n])
            n += 1
            
            
        else:
            indexInicial = n
            numInicial = atual
            print("else")
            while next == atual+1 and n < len(L)-1:            
                print("while")
                atual = L[n]
                next = L[n+1]
                n += 1
            if next != atual+1:
                #print(f"atual:{atual} --- next:{next} --- n:{n} --- indexInicial:{indexInicial} --- numInicial:{numInicial}")
                print(f"({numInicial},{atual+1})")
                newList.append((numInicial,atual+1))
            else:
                #print(f"atual:{atual} --- next:{next} --- n:{n} --- indexInicial:{indexInicial} --- numInicial:{numInicial}")
                print(f"({numInicial},{next+1})")
                newList.append((numInicial,next+1))
    
    return newList


def main():
    L = [-4, -2, 0, 2]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
