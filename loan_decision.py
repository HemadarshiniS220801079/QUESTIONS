def loan_decision(income, credit_score, existing_debt):
    debt_ratio = existing_debt / income if income > 0 else 1
    if income >= 50000 and credit_score >= 700 and debt_ratio <= 0.4:
        return "Eligible"
    elif income >= 30000 and credit_score >= 600 and debt_ratio <= 0.6:
        return "Review"
    else:
        return "Reject"


if __name__ == "__main__":
    income = float(input().strip())
    credit_score = int(input().strip())
    existing_debt = float(input().strip())
    
    result = loan_decision(income, credit_score, existing_debt)
    print(result)
