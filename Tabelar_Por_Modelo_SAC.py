end='s'
while end=='s':	
	saldo=float(input('DIGA O VALOR TOTAL DO FINANCIAMENTO: '))
	nP=int(input('DIGA O NUMERO TOTAL DE PARCELAS: '))
	amtz=saldo/nP
	jSaldo=float(input('DIGA O JUROS QUE HAVERÁ SOBRE O SALDO DEVEDOR: '))
	
	caracMes=len(f'{nP:.2f}')
	if caracMes<3:
		caracMes=3
	caracAmtz=len(f'{amtz:.2f}')
	if caracAmtz<11:
		caracAmtz=11
	caracJuros=len(f'{jSaldo/100*saldo:.2f}')
	if caracJuros<5:
		caracJuros=5
	caracPrest=len(f'{amtz+(jSaldo/100*saldo):.2f}')
	if caracPrest<9:
		caracPrest=9
	caracSaldo=len(f'{saldo:.2f}')
	if caracSaldo<13:
		caracSaldo=13
	
	compTabela=caracMes+caracAmtz+caracJuros+caracPrest+caracSaldo+4
	
	if compTabela<45:
		compTabela=45
	
	print('\n'+'+'+'-'*compTabela+'+')
	print('|'+str.center('Mes',caracMes)+'|'+str.center('Amortizacao',caracAmtz)+'|'+str.center('Juros',caracJuros)+'|'+str.center('Prestacao',caracPrest)+'|'+str.center('Saldo Devedor',caracSaldo)+'|')
	print('+'+'-'*compTabela+'+')
	
	total=0
	jTotal=0

	print('|'+str.center(str(0),caracMes)+'|'+str.center(f'{0:.2f}',caracAmtz)+'|'+str.center(f'{0:.2f}',caracJuros)+'|'+str.center(f'{0:.2f}',caracPrest)+'|'+str.center(f'{saldo:.2f}',caracSaldo)+'|')
	for i in range(1,nP+1):	
		jur=jSaldo/100*saldo
		prest=amtz+(jSaldo/100*saldo)
		saldo-=amtz
		jTotal+=jur
		total+=prest
		print('|'+str.center(str(i),caracMes)+'|'+str.center(f'{amtz:.2f}',caracAmtz)+'|'+str.center(f'{jur:.2f}',caracJuros)+'|'+str.center(f'{prest:.2f}',caracPrest)+'|'+str.center(f'{saldo:.2f}',caracSaldo)+'|')
	
	print('+'+'-'*compTabela+'+')
	
	print('\nTOTAL PAGO:',round(total,2))
	print('TOTAL DE JUROS:',round(jTotal,2))
	end=input('\nCONTINUAR? [s/n] ')