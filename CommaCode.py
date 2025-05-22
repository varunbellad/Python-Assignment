print("Varun Bellad, 1AY24AI096, Sec-O")
# CommaCode.py

def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"

def main():
    example_list = input("Enter items separated by commas: ").split(',')
    cleaned_list = [item.strip() for item in example_list if item.strip()]
    
    result = comma_code(cleaned_list)
    print("Formatted string:", result)

if __name__ == "__main__":
    main()
