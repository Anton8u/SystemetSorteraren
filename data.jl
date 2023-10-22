using JSON

# Specify the path to your JSON file
json_file_path = "products_reformated.json"

# Read and parse the JSON data
data = JSON.parsefile(json_file_path)

function getIndexParameter(parameter, index)
    return data[index][parameter]  
end

function allItems()
    all = []
    for i in 1:24117
        push!(all, i)
    end
    return all
end

#typeOneCategories = ["Cider & blanddrycker", "Sprit", "Vin", "Öl", "Alkoholfritt"]

function generalCategories(selectedCategories)
    filtered = Int[]
    for i in 1:24117
        if getIndexParameter("categoryLevel1", i) in selectedCategories
            push!(filtered, i)
        end
    end
    return filtered
end

function specificCategories(selectedCategories)
    #ta bort speciella taggar på alkoholfri tagg på kategorier)
    alcoholFree = ["Cider & Blanddryck (Alkoholfri)", "Drinkar & Cocktail (Alkoholfri)", "Glögg & andra juldrycker (Alkoholfri)", "Mousserande (Alkoholfri)", "Must (Alkoholfri)", "Rosé (Alkoholfri)", "Rött (Alkoholfri)", "Snaps (Alkoholfri)", "Vitt (Alkoholfri)", "Öl (Alkoholfri)"]
    for i in 1:length(selectedCategories)
        if selectedCategories[i] in alcoholFree
            selectedCategories[i] = replace(selectedCategories[i], " (Alkoholfri)" => "")
        end
    end
    
    filtered = Int[]
    for i in 1:24117
        if getIndexParameter("categoryLevel2", i) in selectedCategories
            push!(filtered, i)
        end
    end
    return filtered
end

function criteriaThresholdFilter(list, criteria, lowThreshold, highThreshold)
    filtered = Int[]

    if criteria == "apk"
        startValue = 1
        if highThreshold < 72
            startValue = 5000
        end
        if highThreshold < 56
            startValue = 10000
        end
        if highThreshold < 41
            startValue = 15000
        end
        if highThreshold < 25
            startValue = 20000
        end

        for i in list
            if i < startValue
                continue
            end

            apk = getIndexParameter(criteria, i)
            if apk <= highThreshold
                if apk < lowThreshold
                    break
                end
                push!(filtered, i)
            end
        end
        return filtered
    end
    
    
    for i in list
        x = getIndexParameter(criteria, i)
        if x >= lowThreshold && x <= highThreshold
            push!(filtered, i)
        end
    end
    return filtered
end

function thresholdApplyer(indexList, alcoholPrecentageMin, alcoholPrecentageMax, apkMin, apkMax, volumeMin, volumeMax, priceMin, priceMax)
    indexList = criteriaThresholdFilter(indexList, "apk", apkMin, apkMax)
    indexList = criteriaThresholdFilter(indexList, "alcoholPrecentage", alcoholPrecentageMin, alcoholPrecentageMax)
    indexList = criteriaThresholdFilter(indexList, "volume", volumeMin, volumeMax)
    indexList = criteriaThresholdFilter(indexList, "price", priceMin, priceMax)
    return indexList
end


