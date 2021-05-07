
def isfloat(value):
	'''
	AIM: a boolean helper function to check if the input number is a decimal number

	INPUT: a number

	OUTPUT: True / Flase
	'''
	try:
		float(value)
		return True
	except ValueError:
		return False