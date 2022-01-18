# snm_1_1_rev4.py 
# Automatically generated by Netflux on 28-Oct-2021 
import numpy as np 
def ODEfunc(t,y,tau,ymax,w,n,EC50): 
	AngII = 0 
	AT1R = 1 
	AGT = 2 
	ACE = 3 
	NOX = 4 
	ROS = 5 
	ET1 = 6 
	ETAR = 7 
	DAG = 8 
	PKC = 9 
	TRPC = 10 
	NE = 11 
	BAR = 12 
	AC = 13 
	cAMP = 14 
	PKA = 15 
	CREB = 16 
	CBP = 17 
	TGFB = 18 
	TGFB1R = 19 
	smad3 = 20 
	smad7 = 21 
	latentTGFB = 22 
	BAMBI = 23 
	PDGF = 24 
	PDGFR = 25 
	NP = 26 
	NPRA = 27 
	cGMP = 28 
	PKG = 29 
	tension = 30 
	B1int = 31 
	Rho = 32 
	ROCK = 33 
	Ca = 34 
	calcineurin = 35 
	NFAT = 36 
	IL6 = 37 
	gp130 = 38 
	STAT = 39 
	IL1 = 40 
	IL1RI = 41 
	TNFa = 42 
	TNFaR = 43 
	NFKB = 44 
	PI3K = 45 
	Akt = 46 
	p38 = 47 
	TRAF = 48 
	ASK1 = 49 
	MKK3 = 50 
	PP1 = 51 
	JNK = 52 
	abl = 53 
	Rac1 = 54 
	MEKK1 = 55 
	MKK4 = 56 
	ERK = 57 
	Ras = 58 
	Raf = 59 
	MEK1 = 60 
	FAK = 61 
	epac = 62 
	Factin = 63 
	FA = 64 
	cmyc = 65 
	CTGF = 66 
	proliferation = 67 
	SRF = 68 
	EDAFN = 69 
	aSMA = 70 
	AP1 = 71 
	TIMP1 = 72 
	TIMP2 = 73 
	PAI1 = 74 
	proMMP14 = 75 
	proMMP1 = 76 
	proMMP2 = 77 
	proMMP9 = 78 
	fibronectin = 79 
	periostin = 80 
	proCI = 81 
	proCIII = 82 
	B3int = 83 
	Src = 84 
	Grb2 = 85 
	p130Cas = 86 
	YAP = 87 
	MRTF = 88 
	Gactin = 89 
	TNC = 90 
	mTORC1 = 91 
	mTORC2 = 92 
	p70S6K = 93 
	EBP1 = 94 
	syndecan4 = 95 
	proMMP3 = 96 
	proMMP8 = 97 
	proMMP12 = 98 
	thrombospondin4 = 99 
	osteopontin = 100 
	contractility = 101 
	RhoGEF = 102 
	RhoGDI = 103 
	talin = 104 
	vinculin = 105 
	paxillin = 106 
	MLC = 107 
	AT2R = 108 
	dydt = np.zeros(109) 
	dydt[AngII] = (OR(w[0],AND(w[12],[act(y[AGT],w[12],n[12],EC50[12]),act(y[ACE],w[12],n[12],EC50[12])]))*ymax[AngII] - y[AngII])/tau[AngII] 
	dydt[AT1R] = (OR(act(y[AngII],w[17],n[17],EC50[17]),act(y[tension],w[167],n[167],EC50[167]))*ymax[AT1R] - y[AT1R])/tau[AT1R] 
	dydt[AGT] = (AND(w[26],[inhib(y[AT1R],w[26],n[26],EC50[26]),act(y[p38],w[26],n[26],EC50[26]),inhib(y[JNK],w[26],n[26],EC50[26])])*ymax[AGT] - y[AGT])/tau[AGT] 
	dydt[ACE] = (act(y[TGFB1R],w[49],n[49],EC50[49])*ymax[ACE] - y[ACE])/tau[ACE] 
	dydt[NOX] = (OR(act(y[AT1R],w[18],n[18],EC50[18]),act(y[TGFB1R],w[98],n[98],EC50[98]))*ymax[NOX] - y[NOX])/tau[NOX] 
	dydt[ROS] = (OR(act(y[NOX],w[19],n[19],EC50[19]),act(y[ETAR],w[36],n[36],EC50[36]))*ymax[ROS] - y[ROS])/tau[ROS] 
	dydt[ET1] = (OR(w[8],act(y[AP1],w[16],n[16],EC50[16]))*ymax[ET1] - y[ET1])/tau[ET1] 
	dydt[ETAR] = (act(y[ET1],w[55],n[55],EC50[55])*ymax[ETAR] - y[ETAR])/tau[ETAR] 
	dydt[DAG] = (OR(act(y[ETAR],w[112],n[112],EC50[112]),act(y[AT1R],w[113],n[113],EC50[113]))*ymax[DAG] - y[DAG])/tau[DAG] 
	dydt[PKC] = (OR(act(y[syndecan4],w[132],n[132],EC50[132]),AND(w[148],[act(y[DAG],w[148],n[148],EC50[148]),act(y[mTORC2],w[148],n[148],EC50[148])]))*ymax[PKC] - y[PKC])/tau[PKC] 
	dydt[TRPC] = (OR(act(y[DAG],w[114],n[114],EC50[114]),act(y[tension],w[166],n[166],EC50[166]))*ymax[TRPC] - y[TRPC])/tau[TRPC] 
	dydt[NE] = (w[6]*ymax[NE] - y[NE])/tau[NE] 
	dydt[BAR] = (act(y[NE],w[54],n[54],EC50[54])*ymax[BAR] - y[BAR])/tau[BAR] 
	dydt[AC] = (OR(act(y[BAR],w[63],n[63],EC50[63]),AND(w[64],[act(y[AT1R],w[64],n[64],EC50[64]),act(y[BAR],w[64],n[64],EC50[64])]))*ymax[AC] - y[AC])/tau[AC] 
	dydt[cAMP] = (act(y[AC],w[65],n[65],EC50[65])*ymax[cAMP] - y[cAMP])/tau[cAMP] 
	dydt[PKA] = (act(y[cAMP],w[43],n[43],EC50[43])*ymax[PKA] - y[PKA])/tau[PKA] 
	dydt[CREB] = (act(y[PKA],w[52],n[52],EC50[52])*ymax[CREB] - y[CREB])/tau[CREB] 
	dydt[CBP] = (OR(inhib(y[smad3],w[45],n[45],EC50[45]),inhib(y[CREB],w[46],n[46],EC50[46]))*ymax[CBP] - y[CBP])/tau[CBP] 
	dydt[TGFB] = (OR(w[1],OR(AND(w[10],[act(y[latentTGFB],w[10],n[10],EC50[10]),act(y[proMMP9],w[10],n[10],EC50[10])]),AND(w[11],[act(y[latentTGFB],w[11],n[11],EC50[11]),act(y[proMMP2],w[11],n[11],EC50[11])])))*ymax[TGFB] - y[TGFB])/tau[TGFB] 
	dydt[TGFB1R] = (AND(w[50],[act(y[TGFB],w[50],n[50],EC50[50]),inhib(y[BAMBI],w[50],n[50],EC50[50])])*ymax[TGFB1R] - y[TGFB1R])/tau[TGFB1R] 
	dydt[smad3] = (OR(AND(w[27],[act(y[TGFB1R],w[27],n[27],EC50[27]),inhib(y[smad7],w[27],n[27],EC50[27]),inhib(y[PKG],w[27],n[27],EC50[27])]),act(y[Akt],w[143],n[143],EC50[143]))*ymax[smad3] - y[smad3])/tau[smad3] 
	dydt[smad7] = (OR(act(y[STAT],w[103],n[103],EC50[103]),AND(w[157],[act(y[AP1],w[157],n[157],EC50[157]),inhib(y[YAP],w[157],n[157],EC50[157])]))*ymax[smad7] - y[smad7])/tau[smad7] 
	dydt[latentTGFB] = (act(y[AP1],w[67],n[67],EC50[67])*ymax[latentTGFB] - y[latentTGFB])/tau[latentTGFB] 
	dydt[BAMBI] = (AND(w[102],[act(y[TGFB],w[102],n[102],EC50[102]),act(y[IL1RI],w[102],n[102],EC50[102])])*ymax[BAMBI] - y[BAMBI])/tau[BAMBI] 
	dydt[PDGF] = (w[7]*ymax[PDGF] - y[PDGF])/tau[PDGF] 
	dydt[PDGFR] = (act(y[PDGF],w[62],n[62],EC50[62])*ymax[PDGFR] - y[PDGFR])/tau[PDGFR] 
	dydt[NP] = (w[9]*ymax[NP] - y[NP])/tau[NP] 
	dydt[NPRA] = (act(y[NP],w[71],n[71],EC50[71])*ymax[NPRA] - y[NPRA])/tau[NPRA] 
	dydt[cGMP] = (act(y[NPRA],w[72],n[72],EC50[72])*ymax[cGMP] - y[cGMP])/tau[cGMP] 
	dydt[PKG] = (act(y[cGMP],w[73],n[73],EC50[73])*ymax[PKG] - y[PKG])/tau[PKG] 
	dydt[tension] = (OR(w[2],AND(w[164],[act(y[FA],w[164],n[164],EC50[164]),act(y[contractility],w[164],n[164],EC50[164])]))*ymax[tension] - y[tension])/tau[tension] 
	dydt[B1int] = (OR(AND(w[42],[act(y[PKC],w[42],n[42],EC50[42]),act(y[tension],w[42],n[42],EC50[42])]),act(y[tension],w[47],n[47],EC50[47]))*ymax[B1int] - y[B1int])/tau[B1int] 
	dydt[Rho] = (OR(act(y[TGFB1R],w[117],n[117],EC50[117]),AND(w[130],[inhib(y[PKG],w[130],n[130],EC50[130]),act(y[RhoGEF],w[130],n[130],EC50[130]),inhib(y[RhoGDI],w[130],n[130],EC50[130])]))*ymax[Rho] - y[Rho])/tau[Rho] 
	dydt[ROCK] = (act(y[Rho],w[69],n[69],EC50[69])*ymax[ROCK] - y[ROCK])/tau[ROCK] 
	dydt[Ca] = (act(y[TRPC],w[115],n[115],EC50[115])*ymax[Ca] - y[Ca])/tau[Ca] 
	dydt[calcineurin] = (act(y[Ca],w[116],n[116],EC50[116])*ymax[calcineurin] - y[calcineurin])/tau[calcineurin] 
	dydt[NFAT] = (act(y[calcineurin],w[108],n[108],EC50[108])*ymax[NFAT] - y[NFAT])/tau[NFAT] 
	dydt[IL6] = (OR(w[3],OR(AND(w[13],[act(y[CREB],w[13],n[13],EC50[13]),act(y[CBP],w[13],n[13],EC50[13])]),OR(act(y[NFKB],w[14],n[14],EC50[14]),act(y[AP1],w[15],n[15],EC50[15]))))*ymax[IL6] - y[IL6])/tau[IL6] 
	dydt[gp130] = (act(y[IL6],w[20],n[20],EC50[20])*ymax[gp130] - y[gp130])/tau[gp130] 
	dydt[STAT] = (act(y[gp130],w[24],n[24],EC50[24])*ymax[STAT] - y[STAT])/tau[STAT] 
	dydt[IL1] = (w[4]*ymax[IL1] - y[IL1])/tau[IL1] 
	dydt[IL1RI] = (act(y[IL1],w[57],n[57],EC50[57])*ymax[IL1RI] - y[IL1RI])/tau[IL1RI] 
	dydt[TNFa] = (w[5]*ymax[TNFa] - y[TNFa])/tau[TNFa] 
	dydt[TNFaR] = (act(y[TNFa],w[70],n[70],EC50[70])*ymax[TNFaR] - y[TNFaR])/tau[TNFaR] 
	dydt[NFKB] = (OR(act(y[IL1RI],w[23],n[23],EC50[23]),OR(act(y[ERK],w[33],n[33],EC50[33]),OR(act(y[p38],w[34],n[34],EC50[34]),act(y[Akt],w[99],n[99],EC50[99]))))*ymax[NFKB] - y[NFKB])/tau[NFKB] 
	dydt[PI3K] = (OR(act(y[TNFaR],w[25],n[25],EC50[25]),OR(act(y[TGFB1R],w[95],n[95],EC50[95]),OR(act(y[PDGFR],w[96],n[96],EC50[96]),act(y[FAK],w[97],n[97],EC50[97]))))*ymax[PI3K] - y[PI3K])/tau[PI3K] 
	dydt[Akt] = (AND(w[147],[act(y[PI3K],w[147],n[147],EC50[147]),act(y[mTORC2],w[147],n[147],EC50[147])])*ymax[Akt] - y[Akt])/tau[Akt] 
	dydt[p38] = (OR(act(y[ROS],w[21],n[21],EC50[21]),OR(act(y[MKK3],w[78],n[78],EC50[78]),OR(act(y[Ras],w[94],n[94],EC50[94]),AND(w[105],[act(y[Rho],w[105],n[105],EC50[105]),inhib(y[Rac1],w[105],n[105],EC50[105])]))))*ymax[p38] - y[p38])/tau[p38] 
	dydt[TRAF] = (OR(act(y[TGFB1R],w[79],n[79],EC50[79]),act(y[TNFaR],w[87],n[87],EC50[87]))*ymax[TRAF] - y[TRAF])/tau[TRAF] 
	dydt[ASK1] = (OR(act(y[TRAF],w[88],n[88],EC50[88]),act(y[IL1RI],w[91],n[91],EC50[91]))*ymax[ASK1] - y[ASK1])/tau[ASK1] 
	dydt[MKK3] = (act(y[ASK1],w[89],n[89],EC50[89])*ymax[MKK3] - y[MKK3])/tau[MKK3] 
	dydt[PP1] = (act(y[p38],w[77],n[77],EC50[77])*ymax[PP1] - y[PP1])/tau[PP1] 
	dydt[JNK] = (OR(act(y[ROS],w[22],n[22],EC50[22]),OR(AND(w[82],[inhib(y[NFKB],w[82],n[82],EC50[82]),act(y[MKK4],w[82],n[82],EC50[82])]),AND(w[106],[inhib(y[Rho],w[106],n[106],EC50[106]),act(y[MKK4],w[106],n[106],EC50[106])])))*ymax[JNK] - y[JNK])/tau[JNK] 
	dydt[abl] = (act(y[PDGFR],w[83],n[83],EC50[83])*ymax[abl] - y[abl])/tau[abl] 
	dydt[Rac1] = (OR(act(y[abl],w[84],n[84],EC50[84]),AND(w[127],[act(y[abl],w[127],n[127],EC50[127]),act(y[p130Cas],w[127],n[127],EC50[127])]))*ymax[Rac1] - y[Rac1])/tau[Rac1] 
	dydt[MEKK1] = (OR(act(y[FAK],w[66],n[66],EC50[66]),act(y[Rac1],w[80],n[80],EC50[80]))*ymax[MEKK1] - y[MEKK1])/tau[MEKK1] 
	dydt[MKK4] = (OR(act(y[MEKK1],w[81],n[81],EC50[81]),act(y[ASK1],w[90],n[90],EC50[90]))*ymax[MKK4] - y[MKK4])/tau[MKK4] 
	dydt[ERK] = (OR(AND(w[76],[inhib(y[PP1],w[76],n[76],EC50[76]),act(y[MEK1],w[76],n[76],EC50[76])]),AND(w[171],[act(y[ROS],w[171],n[171],EC50[171]),inhib(y[AT2R],w[171],n[171],EC50[171])]))*ymax[ERK] - y[ERK])/tau[ERK] 
	dydt[Ras] = (OR(act(y[AT1R],w[109],n[109],EC50[109]),act(y[Grb2],w[121],n[121],EC50[121]))*ymax[Ras] - y[Ras])/tau[Ras] 
	dydt[Raf] = (act(y[Ras],w[74],n[74],EC50[74])*ymax[Raf] - y[Raf])/tau[Raf] 
	dydt[MEK1] = (AND(w[75],[inhib(y[ERK],w[75],n[75],EC50[75]),act(y[Raf],w[75],n[75],EC50[75])])*ymax[MEK1] - y[MEK1])/tau[MEK1] 
	dydt[FAK] = (act(y[B1int],w[119],n[119],EC50[119])*ymax[FAK] - y[FAK])/tau[FAK] 
	dydt[epac] = (act(y[cAMP],w[68],n[68],EC50[68])*ymax[epac] - y[epac])/tau[epac] 
	dydt[Factin] = (AND(w[135],[act(y[ROCK],w[135],n[135],EC50[135]),act(y[Gactin],w[135],n[135],EC50[135])])*ymax[Factin] - y[Factin])/tau[Factin] 
	dydt[FA] = (AND(w[159],[act(y[vinculin],w[159],n[159],EC50[159]),inhib(y[paxillin],w[159],n[159],EC50[159])])*ymax[FA] - y[FA])/tau[FA] 
	dydt[cmyc] = (act(y[JNK],w[85],n[85],EC50[85])*ymax[cmyc] - y[cmyc])/tau[cmyc] 
	dydt[CTGF] = (OR(AND(w[28],[act(y[CBP],w[28],n[28],EC50[28]),act(y[smad3],w[28],n[28],EC50[28]),act(y[ERK],w[28],n[28],EC50[28])]),act(y[YAP],w[131],n[131],EC50[131]))*ymax[CTGF] - y[CTGF])/tau[CTGF] 
	dydt[proliferation] = (OR(act(y[AP1],w[51],n[51],EC50[51]),OR(act(y[CREB],w[53],n[53],EC50[53]),OR(act(y[CTGF],w[56],n[56],EC50[56]),OR(act(y[PKC],w[58],n[58],EC50[58]),OR(act(y[cmyc],w[86],n[86],EC50[86]),AND(w[142],[act(y[p70S6K],w[142],n[142],EC50[142]),inhib(y[EBP1],w[142],n[142],EC50[142])]))))))*ymax[proliferation] - y[proliferation])/tau[proliferation] 
	dydt[SRF] = (act(y[MRTF],w[137],n[137],EC50[137])*ymax[SRF] - y[SRF])/tau[SRF] 
	dydt[EDAFN] = (act(y[NFAT],w[48],n[48],EC50[48])*ymax[EDAFN] - y[EDAFN])/tau[EDAFN] 
	dydt[aSMA] = (OR(AND(w[110],[act(y[CBP],w[110],n[110],EC50[110]),act(y[smad3],w[110],n[110],EC50[110])]),OR(act(y[SRF],w[111],n[111],EC50[111]),act(y[YAP],w[169],n[169],EC50[169])))*ymax[aSMA] - y[aSMA])/tau[aSMA] 
	dydt[AP1] = (OR(act(y[ERK],w[37],n[37],EC50[37]),act(y[JNK],w[101],n[101],EC50[101]))*ymax[AP1] - y[AP1])/tau[AP1] 
	dydt[TIMP1] = (act(y[AP1],w[40],n[40],EC50[40])*ymax[TIMP1] - y[TIMP1])/tau[TIMP1] 
	dydt[TIMP2] = (act(y[AP1],w[41],n[41],EC50[41])*ymax[TIMP2] - y[TIMP2])/tau[TIMP2] 
	dydt[PAI1] = (OR(act(y[smad3],w[92],n[92],EC50[92]),act(y[YAP],w[149],n[149],EC50[149]))*ymax[PAI1] - y[PAI1])/tau[PAI1] 
	dydt[proMMP14] = (OR(act(y[AP1],w[61],n[61],EC50[61]),act(y[NFKB],w[93],n[93],EC50[93]))*ymax[proMMP14] - y[proMMP14])/tau[proMMP14] 
	dydt[proMMP1] = (AND(w[35],[inhib(y[smad3],w[35],n[35],EC50[35]),act(y[NFKB],w[35],n[35],EC50[35]),act(y[AP1],w[35],n[35],EC50[35])])*ymax[proMMP1] - y[proMMP1])/tau[proMMP1] 
	dydt[proMMP2] = (OR(act(y[STAT],w[29],n[29],EC50[29]),act(y[AP1],w[38],n[38],EC50[38]))*ymax[proMMP2] - y[proMMP2])/tau[proMMP2] 
	dydt[proMMP9] = (OR(act(y[STAT],w[30],n[30],EC50[30]),AND(w[39],[act(y[NFKB],w[39],n[39],EC50[39]),act(y[AP1],w[39],n[39],EC50[39])]))*ymax[proMMP9] - y[proMMP9])/tau[proMMP9] 
	dydt[fibronectin] = (OR(AND(w[44],[act(y[CBP],w[44],n[44],EC50[44]),act(y[smad3],w[44],n[44],EC50[44])]),act(y[NFKB],w[100],n[100],EC50[100]))*ymax[fibronectin] - y[fibronectin])/tau[fibronectin] 
	dydt[periostin] = (OR(AND(w[31],[act(y[CBP],w[31],n[31],EC50[31]),act(y[smad3],w[31],n[31],EC50[31])]),AND(w[32],[act(y[CREB],w[32],n[32],EC50[32]),act(y[CBP],w[32],n[32],EC50[32])]))*ymax[periostin] - y[periostin])/tau[periostin] 
	dydt[proCI] = (OR(AND(w[59],[act(y[CBP],w[59],n[59],EC50[59]),act(y[smad3],w[59],n[59],EC50[59]),inhib(y[epac],w[59],n[59],EC50[59])]),act(y[SRF],w[104],n[104],EC50[104]))*ymax[proCI] - y[proCI])/tau[proCI] 
	dydt[proCIII] = (OR(AND(w[60],[act(y[CBP],w[60],n[60],EC50[60]),act(y[smad3],w[60],n[60],EC50[60]),inhib(y[epac],w[60],n[60],EC50[60])]),act(y[SRF],w[107],n[107],EC50[107]))*ymax[proCIII] - y[proCIII])/tau[proCIII] 
	dydt[B3int] = (OR(AND(w[151],[act(y[tension],w[151],n[151],EC50[151]),inhib(y[thrombospondin4],w[151],n[151],EC50[151])]),act(y[osteopontin],w[155],n[155],EC50[155]))*ymax[B3int] - y[B3int])/tau[B3int] 
	dydt[Src] = (OR(act(y[B3int],w[118],n[118],EC50[118]),act(y[PDGFR],w[125],n[125],EC50[125]))*ymax[Src] - y[Src])/tau[Src] 
	dydt[Grb2] = (AND(w[120],[act(y[FAK],w[120],n[120],EC50[120]),act(y[Src],w[120],n[120],EC50[120])])*ymax[Grb2] - y[Grb2])/tau[Grb2] 
	dydt[p130Cas] = (OR(AND(w[124],[act(y[FAK],w[124],n[124],EC50[124]),act(y[Src],w[124],n[124],EC50[124])]),AND(w[126],[act(y[tension],w[126],n[126],EC50[126]),act(y[Src],w[126],n[126],EC50[126])]))*ymax[p130Cas] - y[p130Cas])/tau[p130Cas] 
	dydt[YAP] = (OR(act(y[Factin],w[128],n[128],EC50[128]),act(y[AT1R],w[168],n[168],EC50[168]))*ymax[YAP] - y[YAP])/tau[YAP] 
	dydt[MRTF] = (AND(w[134],[act(y[NFAT],w[134],n[134],EC50[134]),inhib(y[Gactin],w[134],n[134],EC50[134])])*ymax[MRTF] - y[MRTF])/tau[MRTF] 
	dydt[Gactin] = (inhib(y[Factin],w[136],n[136],EC50[136])*ymax[Gactin] - y[Gactin])/tau[Gactin] 
	dydt[TNC] = (OR(act(y[NFKB],w[144],n[144],EC50[144]),act(y[MRTF],w[145],n[145],EC50[145]))*ymax[TNC] - y[TNC])/tau[TNC] 
	dydt[mTORC1] = (act(y[Akt],w[139],n[139],EC50[139])*ymax[mTORC1] - y[mTORC1])/tau[mTORC1] 
	dydt[mTORC2] = (inhib(y[p70S6K],w[146],n[146],EC50[146])*ymax[mTORC2] - y[mTORC2])/tau[mTORC2] 
	dydt[p70S6K] = (act(y[mTORC1],w[140],n[140],EC50[140])*ymax[p70S6K] - y[p70S6K])/tau[p70S6K] 
	dydt[EBP1] = (inhib(y[mTORC1],w[141],n[141],EC50[141])*ymax[EBP1] - y[EBP1])/tau[EBP1] 
	dydt[syndecan4] = (AND(w[138],[act(y[tension],w[138],n[138],EC50[138]),inhib(y[TNC],w[138],n[138],EC50[138])])*ymax[syndecan4] - y[syndecan4])/tau[syndecan4] 
	dydt[proMMP3] = (AND(w[153],[inhib(y[smad3],w[153],n[153],EC50[153]),act(y[NFKB],w[153],n[153],EC50[153]),act(y[AP1],w[153],n[153],EC50[153])])*ymax[proMMP3] - y[proMMP3])/tau[proMMP3] 
	dydt[proMMP8] = (AND(w[152],[inhib(y[smad3],w[152],n[152],EC50[152]),act(y[NFKB],w[152],n[152],EC50[152]),act(y[AP1],w[152],n[152],EC50[152])])*ymax[proMMP8] - y[proMMP8])/tau[proMMP8] 
	dydt[proMMP12] = (act(y[CREB],w[156],n[156],EC50[156])*ymax[proMMP12] - y[proMMP12])/tau[proMMP12] 
	dydt[thrombospondin4] = (act(y[smad3],w[150],n[150],EC50[150])*ymax[thrombospondin4] - y[thrombospondin4])/tau[thrombospondin4] 
	dydt[osteopontin] = (act(y[AP1],w[154],n[154],EC50[154])*ymax[osteopontin] - y[osteopontin])/tau[osteopontin] 
	dydt[contractility] = (AND(w[163],[act(y[Factin],w[163],n[163],EC50[163]),act(y[vinculin],w[163],n[163],EC50[163]),act(y[MLC],w[163],n[163],EC50[163])])*ymax[contractility] - y[contractility])/tau[contractility] 
	dydt[RhoGEF] = (AND(w[122],[act(y[FAK],w[122],n[122],EC50[122]),act(y[Src],w[122],n[122],EC50[122])])*ymax[RhoGEF] - y[RhoGEF])/tau[RhoGEF] 
	dydt[RhoGDI] = (OR(inhib(y[Src],w[123],n[123],EC50[123]),OR(act(y[PKA],w[129],n[129],EC50[129]),inhib(y[PKC],w[133],n[133],EC50[133])))*ymax[RhoGDI] - y[RhoGDI])/tau[RhoGDI] 
	dydt[talin] = (OR(act(y[B1int],w[160],n[160],EC50[160]),act(y[B3int],w[161],n[161],EC50[161]))*ymax[talin] - y[talin])/tau[talin] 
	dydt[vinculin] = (AND(w[162],[act(y[tension],w[162],n[162],EC50[162]),act(y[talin],w[162],n[162],EC50[162])])*ymax[vinculin] - y[vinculin])/tau[vinculin] 
	dydt[paxillin] = (AND(w[158],[act(y[FAK],w[158],n[158],EC50[158]),act(y[Src],w[158],n[158],EC50[158]),act(y[MLC],w[158],n[158],EC50[158])])*ymax[paxillin] - y[paxillin])/tau[paxillin] 
	dydt[MLC] = (act(y[ROCK],w[165],n[165],EC50[165])*ymax[MLC] - y[MLC])/tau[MLC] 
	dydt[AT2R] = (act(y[AngII],w[170],n[170],EC50[170])*ymax[AT2R] - y[AT2R])/tau[AT2R] 
	return dydt 

# utility functions
 
def act(x, w, n, EC50): 
	# hill activation function with parameters w (weight), n (Hill coeff), EC50 
	beta = ((EC50**n)-1)/(2*EC50**n-1) 
	K = (beta-1)**(1/n) 
	fact = w*(beta*x**n)/(K**n+x**n) 
	if fact > w: 
		fact = w 
	return fact
 
def inhib(x, w, n, EC50): 
	# inverse hill function with parameters w (weight), n (Hill coeff), EC50 
	finhib = w - act(x, w, n, EC50) 
	return finhib
 
def OR(x, y): 
	# OR logic gate 
	z = x + y - x*y 
	return z
 
def AND(w, reactList): 
	# AND logic gate, multiplying all of the reactants together 
	if w == 0: 
		z = 0 
	else: 
		p = np.array(reactList).prod() 
		z = p/w**(len(reactList)-2) 
	return z
 
