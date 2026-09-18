from decimal import Decimal, ROUND_HALF_UP


def get_positive_float(prompt):
    while True:
        value = input(prompt).replace(",", ".")
        try:
            value = float(value)
        except ValueError:
            print("Введіть число")
            continue
        if value <= 0:
            print("Значення повинно бути більше нуля")
            continue
        return value


def get_years(prompt, default=2):
    while True:
        value = input(prompt)
        if value.strip() == "":
            return default
        try:
            value = int(value)
        except ValueError:
            print("Введіть ціле число")
            continue
        if value <= 0:
            print("Термін повинен бути більше нуля")
            continue
        return value


def calculate_deposit(amount, rate, years):
    amount = Decimal(str(amount))
    monthly_rate = Decimal(str(rate)) / Decimal("100") / Decimal("12")
    months = years * 12

    balance = amount
    schedule = []

    for month in range(1, months + 1):
        interest = (balance * monthly_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        balance = (balance + interest).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        schedule.append((month, interest, balance))

    return schedule


if __name__ == "__main__":
    print("Депозитний калькулятор")

    amount = get_positive_float("Введіть початкову суму депозиту: ")
    rate = get_positive_float("Введіть річну відсоткову ставку (%): ")
    years = get_years("Введіть термін депозиту в роках (за замовчуванням 2): ")

    schedule = calculate_deposit(amount, rate, years)

    print("\nМісяць | Нараховані відсотки | Баланс")
    for month, interest, balance in schedule:
        print(f"{month:>6} | {interest:>20} | {balance}")

    print(f"\nПідсумкова сума на рахунку через {years} р.: {schedule[-1][2]}")
