def fib(n):
    f1, f2 = 1, 1
    with open("fib.txt", "w") as f:
        for i in range(n):
            yield f1
            f.write(f"{f1}\n")
            f1, f2 = f2, f1 + f2

for num in fib(200):
    print(num)