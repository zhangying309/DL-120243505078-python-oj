m = float(input())
if m <= 1000:
    tax = 0
elif 1000<m <= 3000:
    tax = m * 0.03
elif 3000<m <= 5000:
    tax = m * 0.04
else:
    tax = m * 0.06
if tax == int(tax):
    print(int(tax))  
else:
    print("{0:.2f}".format(tax).rstrip('0').rstrip('.') if "{0:.2f}".format(tax).endswith('0') else "{0:.2f}".format(tax))
