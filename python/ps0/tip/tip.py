def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float((dollars * percent)/100)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars=d.strip('$')
    return float(dollars)


def percent_to_float(p):
    rate=p.strip('%')
    return float(rate)

main()
