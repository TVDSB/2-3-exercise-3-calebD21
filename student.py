def main():
    #your code goes here
    from re import X


    x = input()
    y = int(x)

    if y%3 == 0 and y%5 == 0:
    print("fizzbuzz")
    elif y%5 == 0:
        print("buzz")
    elif y%3 == 0:
        print("fizz")

if __name__ =='__main__':
    main()
