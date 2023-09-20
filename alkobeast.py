from data import fromListGetElem

listOfLists = ["productName", "alcoholPrecentage", "volume", "price","categoryTypeOne", "categoryTypeTwo", "categoryTypeThree", "accessibility", "apk"]

def criteriaThresholdFilter(unfiltered, criteria, lowTreshhold, highThreshhold):
    filtered = []
    for i in unfiltered:
        x = fromListGetElem(criteria, i)
        if x >= lowTreshhold and x <= highThreshhold:
            filtered.append(i)
    return filtered

def thresholdApplyer(indexList, alcoholPrecentageMin, alcoholPrecentageMax, apkMin, apkMax, volumeMin, volumeMax, priceMin, priceMax):
    indexList = criteriaThresholdFilter(indexList, "alcoholPrecentage", alcoholPrecentageMin, alcoholPrecentageMax)
    indexList = criteriaThresholdFilter(indexList, "apk", apkMin, apkMax)
    indexList = criteriaThresholdFilter(indexList, "volume", volumeMin, volumeMax)
    indexList = criteriaThresholdFilter(indexList, "price", priceMin, priceMax)
    return indexList

def productNames(indexList):
    names = []
    for i in indexList:
        names.append(fromListGetElem("productName", i))
        #print(i,x)
    return names

def allItems():
    all = []
    for i in range(0,24117):
        all.append(i)
        #print(i,x)
    return all

def typeGetter(typeLvl, typeStr):
    filtered = []
    for i in range(0,24117):
        x = fromListGetElem(typeLvl, i)
        if x == typeStr:
            filtered.append(i)
    return filtered

#type1
#Cider & blanddrycker, Sprit, Vin, Öl, Alkoholfritt
def generalCategories(selectedCategories):
    for i in range(0,24117):
        for category in selectedCategories:
            if fromListGetElem("categoryTypeOne", i) in selectedCategories:
                print(fromListGetElem("productName", i), fromListGetElem("categoryTypeOne", i))
        
#alkoholfria - "Cider & Blanddryck", "Drinkar & Cocktail", "Glögg & andra juldrycker", "Mousserande", "Must", "Rosé", "Rött"
#"Snaps", "Vitt", "Öl"

#speciella - Drycker av flera typer (vin)

#"Akvavit & Kryddat brännvin", "Ale", "Anissprit", "Annan öl", "Aperitif & Bitter", "Aperitifer", "Armagnac & Brandy", "Avec", "Bitter", "Blanddryck", "Calvados", "Cider",
#"Cider & Blanddryck", "Cognac", "Drinkar & Cocktail", "Drinkar & Cocktails", "Drycker av flera typer", "Frukt & Druvsprit",
#"Gin & Genever", "Glögg & andra juldrycker", "Glögg och Glühwein", "Grappa & Marc", "Likör", "Ljus lager", "Mellanmörk & Mörk lager",
#"Mousserande", "Mousserande vin", "Must", "Porter & Stout", "Punsch", "Rom & Lagrad sockerrörssprit", "Rosé", "Rosévin",
#"Rött", "Rött vin" "Sake", "Smaksatt sprit", "Smaksatt vin & fruktvin", "Snaps", "Starkvin", "Syrlig öl", "Tequila & Mezcal",
#"Vermouth", "Veteöl", "Vinlåda", "Vitt", "Vitt vin", "Vodka & Okryddat brännvin", "Whisky", "Öl"
def specificCategories(selectedCategories):
    for i in range(0,24117):
        for category in selectedCategories:
            if fromListGetElem("categoryTypeOne", i) in selectedCategories:
                print(fromListGetElem("productName", i), fromListGetElem("categoryTypeOne", i))