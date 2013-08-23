import string

vowels = 'AEIOU'
alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
month = {'01': 'A', '02': 'B', '03': 'C', '04': 'D',
         '05': 'E', '06': 'H', '07': 'L', '08': 'M',
         '09': 'P', '10': 'R', '11': 'S', '12': 'T'}
dseq = [1,0,5,7,9,13,15,17,19,21,2,4,18,20,11,3,6,8,12,14,16,10,22,25,24,23]
pari_cod = dict(zip(alfa,xrange(0,26)))
pari_cod.update(zip('0123456789',xrange(0,10)))
dispari_cod = dict(zip(alfa,dseq))
dispari_cod.update(zip('0123456789',dseq))

def compute_lname(lname):
	vow = [x for x in lname if x in vowels]
	con = [x for x in lname if x not in vowels]
	return ''.join((con+vow+['X']*2)[:3])

def compute_fname(fname):
	vow = [x for x in fname if x in vowels]
	con = [x for x in fname if x not in vowels]
	if len(con)>3:
		con[1:2]=[]
	return ''.join((con+vow+['X']*2)[:3])

def compute_birth(birth,gender):
	date = birth.split('/')
	ret = date[2]
	ret = ret+month[date[1]]
	if gender in ('f','F'):
		date[0] = str(int(date[0])+40)
	ret = ret+date[0]
	return ret

def compute_city_code(city):
	file_cod = open('COD.txt','r')
	for line in file_cod:
		com,cod = line.split(';')
		if com.capitalize() == city:
			file_cod.close()
			return cod[:4]
	file_cod.close()
	return 'null'

def compute_control_code(cf):
	count = 1
	p=0
	d=0
	for c in cf:
		if count%2==0:
			p = p+pari_cod[c]
		else:
			d = d+dispari_cod[c]
		count = count+1
	return alfa[(p+d)%26]

if __name__ == '__main__':
	print '---   Generatore Codice Fiscale   ---'
	fname = raw_input('Nome: ').upper()
	lname = raw_input('Cognome: ').upper()
	city = raw_input('Comune di nascita: ').capitalize()
	birth = raw_input('Data di nascita(gg/mm/aa): ')
	gender = raw_input('Sesso(m/f): ')

	cf = compute_lname(lname)+compute_fname(fname)+compute_birth(birth,gender)+compute_city_code(city)
	cf = cf+compute_control_code(cf)

	print 'Codice Fiscale:',cf

