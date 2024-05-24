end='s'
while end=='s':	
	saldo=float(input('DIGA O VALOR TOTAL DO FINANCIAMENTO: '))
	nP=int(input('DIGA O NUMERO TOTAL DE PARCELAS: '))
	amtz=saldo/nP
	jSaldo=float(input('DIGA O JUROS QUE HAVERÁ SOBRE O SALDO DEVEDOR: '))
	
	caracMes=len(str(round(nP,2)))
	if caracMes<3:
		caracMes=3
	caracAmtz=len(str(round(amtz,2)))
	if caracAmtz<11:
		caracAmtz=11
	caracJuros=len(str(round(jSaldo/100*saldo,2)))
	if caracJuros<5:
		caracJuros=5
	caracPrest=len(str(round(amtz+(jSaldo/100*saldo),2)))
	if caracPrest<9:
		caracPrest=9
	caracSaldo=len(str(round(saldo,2)))
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
	
	for i in range(0,nP+1):	
		if i==0:
			print('|'+str.center(str(0),caracMes)+'|'+str.center(str(0),caracAmtz)+'|'+str.center(str(0),caracJuros)+'|'+str.center(str(0),caracPrest)+'|'+str.center(str(saldo),caracSaldo)+'|')
		else:
			jur=jSaldo/100*saldo
			prest=amtz+(jSaldo/100*saldo)
			saldo-=amtz
			jTotal+=jur
			total+=prest
			print('|'+str.center(str(i),caracMes)+'|'+str.center(str(round(amtz,2)),caracAmtz)+'|'+str.center(str(round(jur,2)),caracJuros)+'|'+str.center(str(round(prest,2)),caracPrest)+'|'+str.center(str(round(saldo,2)),caracSaldo)+'|')
	
	print('+'+'-'*compTabela+'+')
	
	print('\nTOTAL PAGO:',round(total,2))
	print('TOTAL DE JUROS:',round(jTotal,2))
	end=input('\nCONTINUAR? [s/n] ')
