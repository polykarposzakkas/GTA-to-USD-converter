def gta_to_usd(gta_amount):
    conversion_rate = 0.00003
    usd_amount = gta_amount * conversion_rate
    return usd_amount

def usd_to_gta(usd_amount):
    conversion_rate = 1 / 0.00003
    gta_amount = usd_amount * conversion_rate
    return gta_amount

def main():
    print("Currency Converter")
    print("1. GTA$ to USD")
    print("2. USD to GTA$")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        gta_amount = float(input("Enter amount in GTA$: "))
        usd_amount = gta_to_usd(gta_amount)
        print(f"The {gta_amount} GTA$ is equal to ${usd_amount:.2f}")
    elif choice == '2':
        usd_amount = float(input("Enter amount in USD: $"))
        gta_amount = usd_to_gta(usd_amount)
        print(f"The ${usd_amount} is equal to {gta_amount:.2f} GTA$")
    else:
        print("Invalid choice")
    
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
