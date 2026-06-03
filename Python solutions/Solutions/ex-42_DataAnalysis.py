import statistics
def analyze_sales():
    try:
        with open("sales.txt", "r") as file:
            sales = [int(line.strip()) for line in file]
        print("Mean:", statistics.mean(sales))
        print("Median:", statistics.median(sales))
    except FileNotFoundError:
        print("File Not Found")
    except ValueError:
        print("Invalid Data")
analyze_sales()