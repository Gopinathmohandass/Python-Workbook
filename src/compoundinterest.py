#Function to calculate compound interest

def amount_on_maturity (Prin, ROI, Years):
    CI = Prin * (1 + (ROI / 12)) ** (12 * Years)
    return CI

toInvest = float(input("How much do you want to deposit: "))
Interest = float(input("Expected Annual ROI: "))
Tenure = float(input("Minimum number of years of deposit: "))
x = round(amount_on_maturity(toInvest, float(Interest/100), Tenure),3)
print("A deposit of",toInvest,"with annual ROI of",float(Interest/100),"% will be",x,"in",Tenure,"years")