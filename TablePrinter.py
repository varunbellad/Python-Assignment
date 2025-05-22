print("Varun Bellad, 1AY24AI096, Sec-O")
# TablePrinter.py

def print_table(table_data):
    # Calculate max width for each column
    col_widths = [0] * len(table_data[0])
    for row in table_data:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    # Print each row with padding
    for row in table_data:
        row_str = ""
        for i, item in enumerate(row):
            row_str += str(item).ljust(col_widths[i] + 2)
        print(row_str)

def main():
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', '24', 'New York'],
        ['Bob', '19', 'Los Angeles'],
        ['Charlie', '33', 'Chicago'],
        ['David', '45', 'Houston']
    ]

    print_table(data)

if __name__ == "__main__":
    main()
