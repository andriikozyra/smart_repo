from __future__ import division

TAXES = {'Chico': 0.5, 'Groucho': 0.7, 'Harpo': 0.5, 'Zeppo': 0.4}

def  calculate_tax(amount, province, hour):
    percent = hour/24
    if percent > 1:
        percent = 1
    try:
        return "{:.2f}".format(amount + amount*TAXES[province]*percent)
    except:
        return None