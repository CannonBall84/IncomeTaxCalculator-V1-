TAXTABLE19 = [range(0,195851),
			range(195851,305851),
			range(305851,423301),
			range(423301,555601),
			range(555601,708311),
			range(708311,1500001),
			range(1500001,1000000000)]

TAXTABLE20 = [range(0,195851),
			range(195851,305851),
			range(305851,423301),
			range(423301,555601),
			range(555601,708311),
			range(708311,1500001),
			range(1500001,1000000000)]

TAXTABLE21 = [range(0,205901),
			range(205901,321601),
			range(321601,445101),
			range(445101,584201),
			range(584201,744801),
			range(744801,1577301),
			range(1577301,1000000000)]

TAXTABLE = [TAXTABLE19,TAXTABLE20,TAXTABLE21]


TAXRATES = {'2019' : {0 : {'base': 0,'rate': 18/100, 'ratebase': 0},
			  		  1 : {'base': 35253,'rate': 26/100, 'ratebase': 195850},
			  		  2 : {'base': 63853,'rate': 31/100, 'ratebase': 305850},
			          3 : {'base': 100263,'rate': 36/100, 'ratebase': 423300},
			          4 : {'base': 147891,'rate': 39/100, 'ratebase': 555600},
			          5 : {'base': 207448,'rate': 41/100, 'ratebase': 708310},
			          6 : {'base': 532041,'rate': 45/100, 'ratebase': 1500000}},

			'2020' : {0 : {'base': 0,'rate': 18/100, 'ratebase': 0},
			          1 : {'base': 35253,'rate': 26/100, 'ratebase': 195850},
			          2 : {'base': 63853,'rate': 31/100, 'ratebase': 305850},
			          3 : {'base': 100263,'rate': 36/100, 'ratebase': 423300},
			          4 : {'base': 147891,'rate': 39/100, 'ratebase': 555600},
			          5 : {'base': 207448,'rate': 41/100, 'ratebase': 708310},
			          6 : {'base': 532041,'rate': 45/100, 'ratebase': 1500000}},

			'2021' : {0 : {'base': 0,'rate': 18/100, 'ratebase': 0},
			          1 : {'base': 37062, 'rate': 26/100, 'ratebase': 205900},
			          2 : {'base': 67144,'rate': 31/100, 'ratebase': 321600},
			          3 : {'base': 105429,'rate': 36/100, 'ratebase': 445100},
			          4 : {'base': 155505,'rate': 39/100, 'ratebase': 584200},
			          5 : {'base': 218139,'rate': 41/100, 'ratebase': 744800},
			          6 : {'base': 559464,'rate': 45/100, 'ratebase': 1577300}}}

REBATES =	{'PRIMARY' : {'2019' : 14067,'2020' : 14220,'2021' : 14958},
			'SECONDARY' : {'2019': 7713,'2020' : 7794,'2021' : 8199},
			'TERTIARY' : {'2019' :2574,'2020' : 2601,'2021' : 2736},}

