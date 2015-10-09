def main():
    words = str(input("Enter a English word: ")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()