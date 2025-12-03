def main() -> None:
    sentence = input("Enter a sentence: ")

    # Work in lowercase to catch both 'a' and 'A'
    lower = sentence.lower()
    index = lower.find('a')

    if index == -1:
        print("There is no letter 'a' in the sentence.")
    else:
        # +1 to convert from 0-based index to human-readable position
        position = index + 1
        print("There is at least one letter 'a' in the sentence.")
        print(f"The first 'a' is at position {position}.")


if __name__ == "__main__":
    main()
