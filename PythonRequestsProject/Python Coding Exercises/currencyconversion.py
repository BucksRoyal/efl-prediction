usd_to_eur_rate = 0.92  # example conversion rate: 1 USD = 0.92 EUR

for usd in range(1, 6):  # 1 to 5 USD
    eur = usd * usd_to_eur_rate
    print(f"${usd} = €{eur:.2f}")
else:
    print("Conversion complete for 1–5 USD.")
