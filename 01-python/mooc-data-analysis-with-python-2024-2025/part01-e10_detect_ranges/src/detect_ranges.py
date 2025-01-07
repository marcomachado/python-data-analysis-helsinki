#!/usr/bin/env python3

def detect_ranges(L):
    L.sort()
    #print(L)
    n = 0
    newList = []
    while n < len(L):
        atual = L[n]
        next = L[n+1] if n < len(L)-1 else L[n]
        if next != atual+1 or atual == next:
            newList.append(L[n])
            n += 1
            
            
        else:
            numInicial = atual
            while next == atual+1 and n < len(L)-1:
                atual = L[n]
                next = L[n+1] if n < len(L)-1 else L[n]
                n += 1
            if next != atual+1:
                #print(f"atual:{atual} --- next:{next} --- n:{n} --- indexInicial:{indexInicial} --- numInicial:{numInicial}")
                #print(f"({numInicial},{atual+1}) --- {L[n]}")
                
                newList.append((numInicial,atual+1))
            else:
                #print(f"atual:{atual} --- next:{next} --- n:{n} --- indexInicial:{indexInicial} --- numInicial:{numInicial}")
                #print(f"({numInicial},{next+1})  --- {L[n]}")
                #print(f"{L[n]}")
                n += 1
                newList.append((numInicial,next+1))
    
    return newList


def main():
    L = [2,5,4,8,12,6,7,10,13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
