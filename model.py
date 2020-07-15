import random 

def cohort(props):
    sum_lengths=(len(props["nickname"])+ len(props["color"]) + len(props["food"]))*int(props["birthmonth"])
    bankNumber = sum_lengths%5
    banks = ["Goldman Sachs", "Bank of America", "J.P. Morgan Chase & Co.", "Wells Fargo", "Morgan Stanley"]
    return (banks[bankNumber])