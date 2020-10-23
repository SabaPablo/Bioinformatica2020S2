test = 'ABPPDKKFTATAGANETATALLASFDKLDFEERLOWENNTRETERT'


def searchPromoter(adnSecuence):
	sec = adnSecuence[(adnSecuence.find('TATA',5) + 4):]
	sec = sec[:(sec.find('TATA'))]
	return sec

