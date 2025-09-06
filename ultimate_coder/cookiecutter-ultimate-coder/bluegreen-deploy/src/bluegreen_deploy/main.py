def switch_environment(active: str) -> str:
    return "green" if active == "blue" else "blue"

def main():
    print(switch_environment("blue"))

if __name__ == "__main__":
    main()
