using JSON

# Specify the path to your JSON file
json_file_path = "products.json"

# Read and parse the JSON data
data = JSON.parsefile(json_file_path)

function getIndexParameter(parameter, index)
    return data[index][parameter]  
end

function allItems()
    all = []
    for i in 1:24118
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

function criteriaThresholdFilter(unfiltered, criteria, lowTreshhold, highThreshhold)
    filtered = []
    for i in unfiltered
        x = getIndexParameter(criteria, i)
        if x >= lowTreshhold && x <= highThreshhold
            push!(filtered, i)
        end
    end
    return filtered
end

function thresholdApplyer(indexList, alcoholPrecentageMin, alcoholPrecentageMax, apkMin, apkMax, volumeMin, volumeMax, priceMin, priceMax)
    indexList = criteriaThresholdFilter(indexList, "alcoholPrecentage", alcoholPrecentageMin, alcoholPrecentageMax)
    indexList = criteriaThresholdFilter(indexList, "apk", apkMin, apkMax)
    indexList = criteriaThresholdFilter(indexList, "volume", volumeMin, volumeMax)
    indexList = criteriaThresholdFilter(indexList, "price", priceMin, priceMax)
    return indexList
end

function productNames(indexList)
    names = String[]
    for i in indexList
        productNameThin = getIndexParameter("productNameThin", i)
        if !isnothing(productNameThin)
            push!(names, (getIndexParameter("productNameBold", i) * " " * productNameThin))
        else
            push!(names, (getIndexParameter("productNameBold", i)))
        end
    end
    return names
end


print(productNames(generalCategories(["Alkoholfritt"])))
