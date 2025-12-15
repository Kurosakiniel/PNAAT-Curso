# variaveis

za = 10
ze = 20
zi = 30
zo = 40
zu = 50

# expressões
expressao01 = ((za == ze ) > (zi != zo)) or ((zu + zo) < (za - ze) > (zi + zo))
expressao02 = ((za == ze ) > (zi != zo)) and ((zu + zo) < (za != ze) > (zi + zo))
expressao03 = ((za >= ze ) > (zi != zo)) and not((zu <= zo) < (za == ze) > (zi < zo))
expressao04 = ((za >= ze ) > (zi != zo)) and not((zu <= zo) < (zi % 2) > (zi ** 2))
expressao05 = ((za < ze ) or (zi != zo))  or ((zu <= zo) < (zi % 2) > (zi ** 2))

print(expressao01) # False
print(expressao02) # False
print(expressao03) # False
print(expressao04) # False
print(expressao05) # True