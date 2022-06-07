def main():
    n = int(input())

    while n:
        n -= 1
        x = int(input())
        l = list(map(int, input().split()))
        
        for i in range(x):
            if l[i] < 0:
                l[i] = 0
            l[i] = l[i]**2

        print(sum(l))


if __name__ == "__main__":
    main()