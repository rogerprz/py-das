#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is === to y"
    else: 
        result = "x is greater than or equal to y"
    # conditional statements let you use "a if C else b"
    result = "x is < than y" if x < y else "x is >= to y"
    # match-case makes it easy to compare multiple values

    value = "t"
    match value:
        case "one":
           result = "this is one"
        case "two":
           result = "this is two"
        case "three":
           result = "this is three"
        case _:
           result = "this is something else"
    print (result)

if __name__ == "__main__":
    main()
