def optimize(tasks):
    return sorted(tasks, key=lambda t: t[1])

def main():
    tasks = [("a", 2), ("b", 1)]
    print(optimize(tasks))

if __name__ == "__main__":
    main()
