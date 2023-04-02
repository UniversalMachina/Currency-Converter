import requests

API_KEY = "V5RSkmjQhih2VaWjWCyAdTvEIBK9sjKq"  # Replace with your API key

def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={base_currency}&symbols={target_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    else:
        raise ValueError(f"Error fetching exchange rate: {response.status_code}")

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == '__main__':
    amount = float(input("Enter the amount: "))
    base_currency = input("Enter the base currency (e.g. USD): ").upper()
    target_currency = input("Enter the target currency (e.g. EUR): ").upper()

    try:
        converted_amount = convert_currency(amount, base_currency, target_currency)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except ValueError as e:
        print(e)