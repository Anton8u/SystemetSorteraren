from data import getIndexParameter

productName = []
alcoholPrecentage = []
volume = []
price = []
categoryTypeOne = []
categoryTypeTwo = []
categoryTypeThree = []
accessibility = []
apk = []

for i in range(0,24117):
    productName.append(getIndexParameter("productName", i))
    alcoholPrecentage.append(getIndexParameter("alcoholPrecentage", i))
    volume.append(getIndexParameter("volume", i))
    price.append(getIndexParameter("price", i))
    categoryTypeOne.append(getIndexParameter("categoryTypeOne", i))
    categoryTypeTwo.append(getIndexParameter("categoryTypeTwo", i))
    accessibility.append(getIndexParameter("accessibility", i))
    apk.append(getIndexParameter("apk", i))
    

listOfLists = ["productName", "alcoholPrecentage", "volume", "price","categoryTypeOne", "categoryTypeTwo", "accessibility", "apk"]

def parameterAtIndex(variable, i):
    switcher = {
        "productName": productName[i],
        "alcoholPrecentage": alcoholPrecentage[i],
        "volume": volume[i],
        "price": price[i],
        "categoryTypeOne": categoryTypeOne[i],
        "categoryTypeTwo": categoryTypeTwo[i],
        "accessibility": accessibility[i],
        "apk": apk[i]
    }
    return switcher.get(variable, i)


def productNames(lst):
    names = []
    for i in lst:
        names.append(productName[i])
    return 

def criteriaThresholdFilter(lst, criteria, lowThreshold, highThreshold):
    filtered = []

    def criteriaThresholdFilter(lst, criteria, lowThreshold, highThreshold):
        filtered = []

    if criteria == "apk":
        startValue = 1
        if highThreshold < 72:
            startValue = 5000
        if highThreshold < 56:
            startValue = 10000
        if highThreshold < 41:
            startValue = 15000
        if highThreshold < 25:
            startValue = 20000

        for i in lst:
            if i < startValue:
                continue

            apk = parameterAtIndex(criteria, i)
            if apk <= highThreshold:
                if apk < lowThreshold:
                    break
                filtered.append(i)
        return filtered

    for i in lst:
        x = parameterAtIndex(criteria, i)
        if x >= lowThreshold and x <= highThreshold:
            filtered.append(i)
    return filtered

def thresholdApplyer(indexList, alcoholPrecentageMin, alcoholPrecentageMax, apkMin, apkMax, volumeMin, volumeMax, priceMin, priceMax):
    indexList = criteriaThresholdFilter(indexList, "apk", apkMin, apkMax)
    indexList = criteriaThresholdFilter(indexList, "alcoholPrecentage", alcoholPrecentageMin, alcoholPrecentageMax)
    indexList = criteriaThresholdFilter(indexList, "volume", volumeMin, volumeMax)
    indexList = criteriaThresholdFilter(indexList, "price", priceMin, priceMax)
    return indexList

def allItems():
    all = []
    for i in range(0,24117):
        all.append(i)
    return all

#typeOneCategories = ["Cider & blanddrycker", "Sprit", "Vin", "Öl", "Alkoholfritt"]

def generalCategories(selectedCategories):
    filtered = []
    for i in range(0,24117):
        for category in selectedCategories:
            if parameterAtIndex("categoryTypeOne", i) in selectedCategories:
                filtered.append(i)
                break
    return filtered

#typeTwoCategories = ["Akvavit & Kryddat brännvin", "Ale", "Anissprit", "Annan öl", "Aperitif & Bitter", "Aperitifer", "Armagnac & Brandy", "Avec", "Bitter", "Blanddryck", "Calvados", "Cider","Cider & Blanddryck (Alkoholfri)", "Cognac", "Drinkar & Cocktail (Alkoholfri)", "Drinkar & Cocktails", "Drycker av flera typer", "Frukt & Druvsprit","Gin & Genever", "Glögg & andra juldrycker (Alkoholfri)", "Glögg och Glühwein", "Grappa & Marc", "Likör", "Ljus lager", "Mellanmörk & Mörk lager","Mousserande (Alkoholfri)", "Mousserande vin", "Must (Alkoholfri)", "Porter & Stout", "Punsch", "Rom & Lagrad sockerrörssprit", "Rosé (Alkoholfri)", "Rosévin", "Rött (Alkoholfri)", "Rött vin", "Sake", "Smaksatt sprit", "Smaksatt vin & fruktvin", "Snaps (Alkoholfri)", "Starkvin", "Syrlig öl", "Tequila & Mezcal","Vermouth", "Veteöl", "Vinlåda", "Vitt (Alkoholfri)", "Vitt vin", "Vodka & Okryddat brännvin", "Whisky", "Öl (Alkoholfri)"]
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
            if parameterAtIndex("categoryTypeTwo", i) in selectedCategories:
                filtered.append(i)
                break
    return filtered

