"""Demo module containing a simple hello function."""

def hello() -> str:
    """
    Return a friendly greeting.
    """
    return "Hello dosto"


def main() -> None:
    """Main execution function."""
    print(hello())


if __name__ == "__main__":
    main()

