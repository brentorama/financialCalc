import locale
locale.setlocale( locale.LC_ALL, '' )


def compoundInterestCalc(princ = 100000, rate = 3.0, taxRate = 0.0, years = 10):
    print '%s principle at a %s%% interest rate taxed at %s%% over %s years' % (locale.currency(princ, grouping=True), rate, taxRate, years)
    for i in range(years):
        interest = (princ * (rate * 0.01))
        tax = interest * (taxRate * 0.01)
        subtotal = princ + interest
        total = princ + interest - tax
        princ = total
        print 'year %s:' % str(i+1)
        print 'subtotal: ' + locale.currency(subtotal, grouping=True)
        print 'total:    ' + locale.currency(princ, grouping=True) + '\n'
        
compoundInterestCalc()