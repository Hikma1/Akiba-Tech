money_in_USD=float(input("Enter the amount in USD: "))
exchange_rate=float(input("Enter the exchange rate (1 USD = ?): "))

money_in_local_currency = money_in_USD * exchange_rate
print(f"Amount in local currency: {money_in_local_currency}")