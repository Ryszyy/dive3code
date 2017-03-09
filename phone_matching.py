import re
#\D - not numeric value
#\D+ - one or more
#\D* - zero or more
#\d -decimals/digits
#{3} how much of them
phonePattern = re.compile(r"""
	(\d{3})		#3 digits
	\D*			#0 or more not digits
	(\d{3})		#3 digits
	\D*			#optional separator
	(\d{4})		#4 digs
	\D*			#opt sep
	(\d*)		#optional digits
	$

""",re.VERBOSE)
# groups() returns tuple of matched pattern
print(phonePattern.search('123 danger 455 of unexpected 7890 behaviors in text with numbers 42342').groups())
print(phonePattern.search('123.456.7890.42342').groups())
print(phonePattern.search('123-456-7890-42342').groups())

#the more re is loose - more errors can appear, but can also take more patterns of the same thing (phone number)