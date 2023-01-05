def get_yearly_revenue(monthly_revenue):
    return 12*monthly_revenue


def get_yearly_expenses(monthly_expenses):
    return 12*monthly_expenses


def get_tax_amount(profit):
    if profit > 100000:
        tax_amount = profit*0.25
    else:
        tax_amount = profit*0.15
    return tax_amount


def apply_tax_credits(tax_amount, tax_credits):
    amount_to_discount = tax_amount*tax_credits
    return amount_to_discount


monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - \
    get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
