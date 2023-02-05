import yfinance as yf
import os

symbols = ['AAF.L', 'AAF.L', 'AAL.L', 'ABDN.L', 'ABF.L', 'ADM.L', 'AHT.L', 'ANTO.L', 'AUTO.L', 
            'AV.L', 'AZN.L', 'BA.L', 'BARC.L', 'BATS.L', 'BDEV.L', 'BEZ.L', 'BKG.L', 'BLND.L', 
            'BME.L', 'BNZL.L', 'BP.L', 'BRBY.L', 'BT-A.L', 'CCH.L', 'CNA.L', 'CPG.L', 'CRDA.L', 
            'CRH.L', 'CTEC.L', 'DCC.L', 'DGE.L', 'EDV.L', 'ENT.L', 'EXPN.L', 'FCIT.L', 'FLTR.L', 
            'FRAS.L', 'FRES.L', 'GLEN.L', 'GSK.L', 'HL.L', 'HLMA.L', 'HLN.L', 'HSBA.L', 'HSX.L', 
            'IAG.L', 'IHG.L', 'III.L', 'IMB.L', 'INF.L', 'ITRK.L', 'JD.L', 'JMAT.L', 'KGF.L', 
            'LAND.L', 'LGEN.L', 'LLOY.L', 'LSEG.L', 'MNDI.L', 'MNG.L', 'MRO.L', 'NG.L', 'NWG.L', 
            'NXT.L', 'OCDO.L', 'PHNX.L', 'PRU.L', 'PSH.L', 'PSN.L', 'PSON.L', 'REL.L', 'RIO.L', 
            'RKT.L', 'RMV.L', 'RR.L', 'RS1.L', 'RTO.L', 'SBRY.L', 'SDR.L', 'SGE.L', 'SGRO.L', 
            'SHEL.L', 'SKG.L', 'SMDS.L', 'SMIN.L', 'SMT.L', 'SN.L', 'SPX.L', 'SSE.L', 'STAN.L', 
            'STJ.L', 'SVT.L', 'TSCO.L', 'TW.L', 'ULVR.L', 'UTG.L', 'UU.L', 'VOD.L', 'WEIR.L', 'WPP.L']

if not os.path.exists('data'):
    os.mkdir('data')

for symbol in symbols:
    if not os.path.exists(f"data/{symbol}.csv"):
        data = yf.download(symbol, start="2021-01-01", end="2023-1-31")
        if data.size > 0:
            data.to_csv(f"data/{symbol}.csv")
        else:
            print("File not created")

for symbol in symbols:
    s = open(f"data/{symbol}.csv").readlines()
    if len(s) < 10:
        os.system(f"rm data/{symbol}.csv")
