def review_with_ai(data: str) -> str:
    return f"AI suggests: {data.upper()}"

def main():
    print(review_with_ai("example"))

if __name__ == "__main__":
    main()
