#Luzon Regions
def Region_Check(city):
	CAR = ["Tabuk","Baguio"]
	NCR = ["Caloocan","Las Pinas","Makati","Malabon","Mandaluyong","Manila","Marikina", 		"Muntinlupa","Navotas","Paranaque","Pasay","Pasig","Quezon","San Juan", "Taguig","Valenzuela"]
	I = ["Alaminos","Batac","Candon","Dagupan","Laoag","San Carlos Pangasinan","San Fernando La Union",
		"Urdaneta","Vigan"]
	II = ["Cauayan","Ilagan","Santiago","Tuguegarao"]
	III = ["Angeles","Balanga","Cabanatuan","Gapan","Mabalacat","Malolos","Meycauayan",
	       "Munoz","Olongapo","Palayan","San Fernando Pampanga","San Jose","San Jose del Monte","Tarlac"]
	IV_A = ["Antipolo","Bacoor","Batangas","Binan","Cabuyao","Calamba","Cavite",
	        "Dasmarinas","General Trias","Imus","Lipa","Lucena","San Pablo","San Pedro",
	        "Santo Tomas","Santa Rosa","Tagaytay","Tanauan","Tayabas","Trece Martires"]
	IV_B = ["Calapan","Puerto Princesa"]
	V = ["Iriga","Legazpi","Ligao","Masbate","Naga","Sorsogon","Tabaco"]

	if city in CAR:
		region = 'CAR'
	elif city in NCR:
		region = 'NCR'
	elif city in I:
		region = 'I'
	elif city in II:
		region = 'II'
	elif city in III:
		region = 'III'
	elif city in IV_A:
		region = 'IV_A'
	elif city in IV_B:
		region = 'IV_B'
	elif city in V:
		region = 'V'
	return (region)
    
#algorithm for island_group and region checking still undeveloped due to lack datasets from visayas and mindanao
