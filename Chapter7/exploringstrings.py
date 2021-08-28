'species'.startswith('a')

'species'.startswith('spe')

compund = '	     \n Methyl  \n butanol   \n'

compund.lstrip()
'Methyl  \n butanol   \n'
compund.rstrip()
'\t     \n Methyl  \n butanol'
compund.strip()
'Methyl  \n butanol'
'"{0}" is derived from "{1}"'.format('none', 'none')
'"none" is derived from "none"'
'"{0}" is derived from the {1} "{2}"'.format('Etymology', 'Greek', 'ethos')
'"Etymology" is derived from the Greek "ethos"'

my_pi = 3.14159
print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi))
print('Pi rounded to {0} decimal places is {1:.3f}'.format(3, my_pi))