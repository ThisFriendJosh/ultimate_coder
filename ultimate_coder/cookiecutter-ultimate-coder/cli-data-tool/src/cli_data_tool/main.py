import argparse

def average(numbers):
    return sum(numbers) / len(numbers)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="+", type=float)
    args = parser.parse_args()
    print(average(args.numbers))

if __name__ == "__main__":
    main()
