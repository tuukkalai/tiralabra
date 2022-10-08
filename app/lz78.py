def pakkaa(teksti: str) -> str:
	sanakirja = {}
	apumuuttuja = ''
	i = 0
	sijainti = 1
	while i < len(teksti):
		apumuuttuja += teksti[i]
		print(apumuuttuja)
		if len(apumuuttuja) > 0:
			print("--", apumuuttuja[:-1])
		if apumuuttuja not in sanakirja:
			if len(apumuuttuja) > 1:
				sanakirja[apumuuttuja] = sanakirja[apumuuttuja[:-1]]
			else:
				sanakirja[apumuuttuja] = 0
			apumuuttuja = ''
		i += 1
	print(sanakirja)


if __name__ == "__main__":
	pakattava_teksti = "AABABABBBCBCBBABABBBAB"
	pakkaa(pakattava_teksti)
