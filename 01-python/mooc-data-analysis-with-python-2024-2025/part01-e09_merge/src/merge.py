#!/usr/bin/env python3

def merge(L1, L2):
    indexL1 = 0
    indexL2 = 0
    uniqueList = []
    while(indexL1 < len(L1) and indexL2 < len(L2)):
        numL1 = L1[indexL1] 
        numL2 = L2[indexL2]
        print(f'{numL1} --- {numL2}')
        if numL1 < numL2:
            uniqueList.append(numL1)
            indexL1+=1
        elif numL1 > numL2:
            uniqueList.append(numL2)
            indexL2+=1
        else:
            uniqueList.append(numL1)
            uniqueList.append(numL2)
            indexL1+=1
            indexL2+=1
        print(uniqueList)
    print(f"INDEX {indexL1} ---- {indexL2}")
    if indexL1 < len(L1):
        uniqueList.extend(L1[indexL1:])
    if indexL2 < len(L2):
        uniqueList.extend(L2[indexL2:])

    return uniqueList

def main():
    print(merge([1, 5, 9, 12], [2, 6, 10]))

if __name__ == "__main__":
    main()
