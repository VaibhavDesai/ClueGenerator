#read dictionary at path first system arguement
import sys
import cPickle

class clue:
        def __init__(self,curID,rawClu,procClu,sour,dateExtract,targ,typ,targInfl,leng,avgCO,curMaxPMI,blan,oldClueQual,finClueQual):
                self.id=curID
                self.rawClue=rawClu
                self.procClue=procClu
                self.source=sour
                self.dateExtracted=dateExtract
                self.target=targ
                self.type=typ
                self.targInflections=targInfl
                self.length=leng
                self.avgCOPMI=avgCO
                self.maxPMI=curMaxPMI
                self.blank=blan
                self.oldQual=oldClueQual
                self.finQual=finClueQual

dic={}
file_path = "Data/combinedFinDic.dms"
with open(file_path,"rb") as f:
        dic=cPickle.load(f)

for key, value in dic.iteritems():
	print key, value.target
