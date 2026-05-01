import sys


def main():
    print(f"Program name: {sys.argv[0]}")
    arguments = sys.argv[1:]
    if arguments:
        print(f"Arguments received: {len(sys.argv[1:])}")
        for i, param in enumerate(arguments):
            print(f"Argument {i + 1}: {param}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===\n")
    main()
