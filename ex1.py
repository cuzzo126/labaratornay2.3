def main() -> None:
    text = input("Enter text: ")
    words = text.split()

    lst = []
    for i, word in enumerate(words):
        lst.append(word)

    result = " ".join(lst)
    print(result)


if __name__ == "__main__":
    main()
