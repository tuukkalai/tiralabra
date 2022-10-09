def pakkaa(teksti: str) -> str:
	sanakirja = {}
	apumuuttuja = ''
	enkoodattavat_sijainnit = []
	seuraavat_merkit = []
	i = 0
	sijainti = 1
	while i < len(teksti):
		apumuuttuja += teksti[i]
		if apumuuttuja not in sanakirja:
			sanakirja[apumuuttuja] = sijainti
			sijainti += 1
			if len(apumuuttuja) > 1 and apumuuttuja[:-1] in sanakirja:
				enkoodattavat_sijainnit.append(sanakirja[apumuuttuja[:-1]])
			else:
				enkoodattavat_sijainnit.append(0)
			seuraavat_merkit.append(apumuuttuja[-1:])
			apumuuttuja = ''
		i += 1
	pakattu_teksti = ''
	for i in range(len(enkoodattavat_sijainnit)):
		pakattu_teksti += str(enkoodattavat_sijainnit[i]) + seuraavat_merkit[i]
	return pakattu_teksti


def pura(pakattu_teksti: str) -> str:
	sijainnit = []
	seuraavat_merkit = []
	for i in range(len(pakattu_teksti)):
		try:
			osoitin = int(pakattu_teksti[i])
		except ValueError:
			seuraavat_merkit.append(pakattu_teksti[i])
		else:
			print('osoitin on ', osoitin, ' ja tyyppiä ', type(osoitin))
			sijainnit.append(osoitin)
	print('sijainnit', sijainnit)
	print('merkit', seuraavat_merkit)


if __name__ == "__main__":
	pakattava_teksti = "AABBBABACABBBACAABABBABABACABCBBCCABABC"
	pakattu = pakkaa(pakattava_teksti)
	pura(pakattu)
