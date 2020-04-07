#Rebate Constant List [ 0 = 2019, 1 = 2020, 2 = 2021]

from taxTables import REBATES, TAXTABLE, TAXRATES

#Obtain User Basic Personal Details
def personalDetails():
    age = int(input("Please tell me your age?"))
    financialYear = input('''Applicable financial year(yyyy): \n2019(01/03/2018 - 28/02/2019),\n2020(01/03/2019 - 29/02/2020), \n2021(01/03/2019 - 28/02/2021)? ''')
    monthlySal = int(input("What is your gross monthly Salary?"))
    return age, financialYear, monthlySal

#Determines User Tax Rates to be used - Returns an index
def taxRates(income, year):
    # Determines year to be searched for in taxtable.
    if year == "2019":
        taxRange = 0
    elif year =="2020":
        taxRange = 1
    else:
        taxRange = 2

    # Determines index to be used to calculate Tax Rates
    for i in TAXTABLE[taxRange]:
        if income in i:
            return TAXRATES[year][TAXTABLE[taxRange].index(i)]
            break
    else:
        if income not in i:
            print("Not in range!")
        else:
            pass

#Based on Age and Year, calculates allowable Annual Rebates
def rebateCalc(age,year):
    if age < 65:
        rebate = REBATES["PRIMARY"][year]
    elif age >=65 and age<75:
        rebate = REBATES["PRIMARY"][year] + REBATES["SECONDARY"][year]
    else:
        rebate = REBATES["PRIMARY"][year] + REBATES["SECONDARY"][year] + REBATES["TERTIARY"][year]

    return rebate

#Calculates Income Tax
def personalTaxCalc():
    """Calculates Income Tax for the individual"""
    reqDetails = personalDetails()
    taxRebate = rebateCalc(reqDetails[0],reqDetails[1])
    threshold = taxRebate/.18
    annual = reqDetails[2] * 12
    rateOfTax = taxRates(annual,reqDetails[1])

    if annual <= threshold:
        print("You have no taxes payable.")
    else:
        taxes = rateOfTax['base'] + ((annual - rateOfTax['ratebase'])*rateOfTax['rate'])
        netAnnualTax = taxes - taxRebate
        monthlyTax = int(taxes/12)
        netMonthlySal = int(reqDetails[2]) - monthlyTax
        print(rateOfTax)
        print("Gross Annual Salary: R" + str(annual))
        print("Annual tax rebate available: R" + str(taxRebate))
        print("Annual tax payable: R" + str(netAnnualTax))
        print("Monthly tax payable: R" + str(monthlyTax))
        print("Net monthly salary: R" + str(netMonthlySal))

personalTaxCalc()










