def remove_char(word: str, pos: int) -> str:
    """Return word without character at position pos (1-based)."""
    if pos < 1 or pos > len(word):
        return word
    idx = pos - 1
    return word[:idx] + word[idx + 1:]


def main() -> None:
    word = input("Enter a word: ")

    # remove 3rd letter
    without_third = remove_char(word, 3)
    print(f"Without 3rd letter: {without_third}")

    # remove k-th letter
    k = int(input("Enter k (position to remove): "))
    without_k = remove_char(word, k)
    print(f"Without {k}-th letter: {without_k}")


if __name__ == "__main__":
    main()
