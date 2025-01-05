#!/usr/bin/env python3
def triple(num):
    return num*3
    
def square(num):
    return num**2

def main():
    for n in range(10):
        n_triple = triple(n+1)
        n_squared = square(n+1)
        if (n_squared > n_triple):
            break
        print(f"triple({n+1})=={n_triple} square({n+1})=={n_squared}")

if __name__ == "__main__":
    main()

