#!/usr/bin/env python3
def main():
    
    while True:
        try:
            num_years = int(input("Enter the number of years: "))
            if num_years <= 0:
                print("Please enter a positive number of years.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    
    total_rainfall = 0.0
    total_months = 0
    

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    print(f"\nYou will be entering rainfall data for {num_years} year(s).")
    print("Please enter the rainfall in inches for each month.\n")
    

    for year in range(1, num_years + 1):
        print(f"--- Year {year} ---")

        for month in range(12):
            while True:
                try:
                    rainfall = float(input(f"Enter inches of rainfall for {months[month]}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please enter a valid amount.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            
            total_rainfall += rainfall
            total_months += 1
        
        print()  
    
    average_rainfall = total_rainfall / total_months
    
 
    print("=" * 50)
    print("RAINFALL SUMMARY")
    print("=" * 50)
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    print("=" * 50)

if __name__ == "__main__":
    main()