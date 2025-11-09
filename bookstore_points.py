#!/usr/bin/env python3

def calculate_points(books_purchased):
    if books_purchased == 0:
        return 0
    elif books_purchased == 2:
        return 5
    elif books_purchased == 4:
        return 15
    elif books_purchased == 6:
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        return 0

def main():
    print("=" * 50)
    print("CSU Global Bookstore Book Club Points Calculator")
    print("=" * 50)
    print("\nPoints are awarded as follows:")
    print("0 books = 0 points")
    print("2 books = 5 points")
    print("4 books = 15 points")
    print("6 books = 30 points")
    print("8 or more books = 60 points")
    print("-" * 50)
    
    while True:
        try:
            books = int(input("\nEnter the number of books you purchased this month: "))
            if books < 0:
                print("Number of books cannot be negative. Please enter a valid number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    points = calculate_points(books)
    

    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Books purchased: {books}")
    print(f"Points awarded: {points}")
    print("=" * 50)
    

    if points == 0 and books > 0:
        print("\nNote: You need to purchase 2, 4, 6, or 8+ books to earn points.")
    elif points > 0:
        print(f"\nCongratulations! You earned {points} points this month!")

if __name__ == "__main__":
    main()