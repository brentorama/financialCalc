import locale
locale.setlocale( locale.LC_ALL, '' )

def compoundInterestCalc(princ = 1000, rate = 3.6, taxRate = 23.0, years = 10):
    print '%s principle at a %s%% interest rate taxed at %s%% over %s years' % (locale.currency(princ, grouping=True), rate, taxRate, years)
    canTax = 10.0
    print 'Canadian witholding tax = 10.0%\n'
    origSum = princ
    total = 0.0
    for i in range(years):
        interest = (princ * (rate * 0.01))
        tax = interest * (taxRate * 0.01)
        canWithtax = interest * (canTax * 0.01)
        subtotal = princ + interest
        total = princ + interest - tax - canWithtax
        princ = total
        
        print 'year %s:' % str(i+1)
        print '{:<15}{:5}{:>12}'.format('Capital gains ', ':', locale.currency(interest, grouping=True))
        print '{:<15}{:5}{:>12}'.format('subtotal ', ':', locale.currency(subtotal, grouping=True))
        print '{:<15}{:5}{:>12}'.format('Japan tax ', ':', locale.currency(tax, grouping=True))
        print '{:<15}{:5}{:>12}'.format('Canada tax ', ':', locale.currency(canWithtax, grouping=True))
        print '{:<15}{:5}{:>12}'.format('Total ', ':', locale.currency(princ, grouping=True)) + '\n'
        
    profit = total - origSum
    percentageGain = profit / origSum * 100
    print 'Profit: '+ locale.currency(profit, grouping=True)
    print '%.2f%% percentage gain' % percentageGain
    
    
compoundInterestCalc(princ = (10000), years = 5)

