# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daryl"
__date__ ="$Dec 20, 2014 11:17:10 AM$"

import memcache

client = memcache.Client(['localhost:5701'])

def fibonacci(round):
    f = [1, 1, 1]
    
    for i in range(round):
        f[-1] = sum(f[:2])
        f[0], f[1] = f[1], f[2]
        
    return f[2]

def retrievefib(round):
    fib = client.get(str(round))
    if not fib:
        fib = fibonacci(round)
        client.set(str(round), str(fib))
    else:
        print("cached")
        
    return fib

def main():
    store = [ x for x in range(20) if x % 2 == 0]
    for i in store:
        retrievefib(i)
    
    for i in range(20):
        print(retrievefib(i))

if __name__ == "__main__":
    main()