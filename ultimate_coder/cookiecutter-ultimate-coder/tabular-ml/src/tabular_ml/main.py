def simple_predict(row):
    return 1 if row["feature"] > 0 else 0

def main():
    print(simple_predict({"feature": 1}))

if __name__ == "__main__":
    main()
