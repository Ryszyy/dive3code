import re

# compact re
#pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# VERBOSE re
pattern = """

^					#begining of a string
M{0,3}				#0 to 3 thousands
(CM|CD|D?C{0,3})	#CM - 900, CD - 400, 0-300 C's
(XC|XL|L?X{0,3})	#XC - 90,  XL - 40,  0-30  X's
(IX|IV|V?I{0,3})	#IX - 9,   IV - 4,   0-3   I's
$					#end of a string 
"""

# VERBOSE allow for more readable re
print(re.search(pattern, "MMMDCCCLXXXVIII", re.VERBOSE))
