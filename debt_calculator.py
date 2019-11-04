def pay_debt(starting_debt, deposit):
    months = 0
    while (starting_debt + ((starting_debt*.01)*months)) - (deposit*months) > 0:
        months += 1
    return months

monthly_deposit = 0
total_months = pay_debt(0, monthly_deposit)
print(f"It will take {total_months} months to pay off debt with a monthly deposit of {monthly_deposit}.")
