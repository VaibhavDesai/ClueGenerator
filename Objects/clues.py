class clue:
    def __init__(self, curID, rawClu, procClu, sour, dateExtract, targ, typ, targInfl, leng, avgCO, curMaxPMI, blan,
                 origClueQual, newClueQuality):
        self.id = curID
        self.rawClue = rawClu
        self.procClue = procClu
        self.source = sour
        self.dateExtracted = dateExtract
        self.target = targ
        self.type = typ
        self.targInflections = targInfl
        self.length = leng
        self.avgCOPMI = avgCO
        self.maxPMI = curMaxPMI
        self.blank = blan
        self.oldClueQuality = origClueQual
        self.finClueQuality = newClueQuality
