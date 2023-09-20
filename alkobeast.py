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

typeOneCatories = [Cider & blanddrycker, Sprit, Vin, Öl, Alkoholfritt]

def generalCategories(selectedCategories):
    for i in range(0,24117):
        for category in selectedCategories:
            if fromListGetElem("categoryTypeOne", i) in selectedCategories:
                print(fromListGetElem("productName", i), fromListGetElem("categoryTypeOne", i))
        
typeTwoCategories = ["Akvavit & Kryddat brännvin", "Ale", "Anissprit", "Annan öl", "Aperitif & Bitter", "Aperitifer", "Armagnac & Brandy", "Avec", "Bitter", "Blanddryck", "Calvados", "Cider","Cider & Blanddryck", "Cognac", "Drinkar & Cocktail", "Drinkar & Cocktails", "Drycker av flera typer", "Frukt & Druvsprit","Gin & Genever", "Glögg & andra juldrycker", "Glögg och Glühwein", "Grappa & Marc", "Likör", "Ljus lager", "Mellanmörk & Mörk lager","Mousserande", "Mousserande vin", "Must", "Porter & Stout", "Punsch", "Rom & Lagrad sockerrörssprit", "Rosé", "Rosévin","Rött", "Rött vin", "Sake", "Smaksatt sprit", "Smaksatt vin & fruktvin", "Snaps", "Starkvin", "Syrlig öl", "Tequila & Mezcal","Vermouth", "Veteöl", "Vinlåda", "Vitt", "Vitt vin", "Vodka & Okryddat brännvin", "Whisky", "Öl"]
alcoholFree = ["Cider & Blanddryck (Alkoholfri)", "Drinkar & Cocktail (Alkoholfri)", "Glögg & andra juldrycker (Alkoholfri)", "Mousserande (Alkoholfri)", "Must (Alkoholfri)", "Rosé (Alkoholfri)", "Rött (Alkoholfri)", "Snaps (Alkoholfri)", "Vitt (Alkoholfri)", "Öl (Alkoholfri)"]
#speciella - Drycker av flera typer (vin) //ta inte med denna

def specificCategories(selectedCategories):
    #ta bort speciella taggar på alkoholfri tagg på kategorier)
    for i in range(0,len(selectedCategories)):
        if selectedCategories[i] in alcoholFree:
            selectedCategories[i] = selectedCategories[i].replace(" (Alkoholfri)", "")
    
    filtered = []
    for i in range(0,24117):
        for category in selectedCategories:
            if fromListGetElem("categoryTypeTwo", i) in selectedCategories:
                filtered.append(i)
                break
    return filtered

