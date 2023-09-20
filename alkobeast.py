from data import fromListGetElem

listOfLists = ["productName", "alcoholPrecentage", "volume", "price","categoryTypeOne", "categoryTypeTwo", "categoryTypeThree", "accessibility", "apk"]



def typeGetter(typeLvl, typeStr):
    filtered = []
    for i in range(0,24117):
        x = fromListGetElem(typeLvl, i)
        if x == typeStr:
            filtered.append(i)
    return filtered

def filterPrio(first = "apk", second = "price"):
    pass


def criteriaThresholdFilter(unfiltered, criteria, lowTreshhold, highThreshhold):
    filtered = []
    for i in unfiltered:
        x = fromListGetElem(criteria, i)
        if x >= lowTreshhold and x <= highThreshhold:
            filtered.append(i)
    return filtered

def allList():
    all = []
    for i in range(0,24117):
        all.append(i)
        #print(i,x)
    return all
#allList()
#print(allList())

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