import tkinter as tk
from tkinter import Listbox, ttk
from alkobeast import specificCategories, generalCategories, allItems, thresholdApplyer, productNames, getIndexParameter
import json
import os
import webbrowser

window = tk.Tk()
window.title("SystemetSorteraren")
window.resizable(0, 0)

# Create a menu bar
menubar = tk.Menu(window)

# Create a menu item
options_menu = tk.Menu(menubar, tearoff=0)

# Add commands to the menu item

options_menu.add_command(label="Reset to default", command=lambda: apply_preset(4)) #preset 4 = default values
options_menu.add_command(label="Open first 5 items in browser", command=lambda: openFilteredLinks(5))
options_menu.add_command(label="Open first 10 items in browser", command=lambda: openFilteredLinks(10))
options_menu.add_command(label="Open first 25 items in browser", command=lambda: openFilteredLinks(25))



# Add the menu item to the menu bar
menubar.add_cascade(label="Options", menu=options_menu)

# Attach the menu bar to the window
window.config(menu=menubar)

# Create a menu item
presets_menu = tk.Menu(menubar, tearoff=0)

# Add commands to the menu item
presets_menu.add_command(label="Apply Preset 1", command=lambda: apply_preset(1))
presets_menu.add_command(label="Save Preset 1", command=lambda: save_preset(1))
presets_menu.add_separator()
presets_menu.add_command(label="Apply Preset 2", command=lambda: apply_preset(2))
presets_menu.add_command(label="Save Preset 2", command=lambda: save_preset(2))
presets_menu.add_separator()
presets_menu.add_command(label="Apply Startup Preset", command=lambda: apply_preset(3))
presets_menu.add_command(label="Save Startup Preset", command=lambda: save_preset(3))

def save_preset(preset_number):
    # Get the current state of the application
    print("save_preset()")
    state = {
        'selected_category': category_var.get(),
        'selected_general_categories': listbox_general.curselection(),
        'selected_specific_categories': listbox_specific.curselection(),
        'threshold_values': [float(entry.get()) for min_entry, max_entry in threshold_entries for entry in (min_entry, max_entry)]
    }

    # Convert the state to a JSON string
    state_json = json.dumps(state)

    # Open the presets file and save the state
    with open('presets.txt', 'r+') as f:
        lines = f.readlines()
        if len(lines) < preset_number:
            lines.append(state_json + '\n')
        else:
            lines[preset_number - 1] = state_json + '\n'
        f.seek(0)
        f.truncate()  # Clear the file content
        f.writelines(lines)


def apply_preset(preset_number):
    print("apply_preset()")
    # Open the presets file and load the state
    with open('presets.txt', 'r') as f:
        lines = f.readlines()
        if len(lines) < preset_number:
            print(f'Preset {preset_number} does not exist')
            return
        state_json = lines[preset_number - 1]

    # Convert the JSON string to a dictionary
    state = json.loads(state_json)

    # Apply the state to the application
    category_var.set(state['selected_category'])
    listbox_general.selection_clear(0, tk.END)
    for index in state['selected_general_categories']:
        listbox_general.selection_set(index)
    listbox_specific.selection_clear(0, tk.END)
    for index in state['selected_specific_categories']:
        listbox_specific.selection_set(index)
    for i, (min_entry, max_entry) in enumerate(threshold_entries):
        min_entry.delete(0, tk.END)
        min_entry.insert(0, state['threshold_values'][i*2])
        max_entry.delete(0, tk.END)
        max_entry.insert(0, state['threshold_values'][i*2+1])

# Add the menu item to the menu bar
menubar.add_cascade(label="Presets", menu=presets_menu)

def reset_to_default():
    # Set the category option to default
    category_var.set(default_category)
    # Reset the thresholds to default values
    for i, (min_entry, max_entry) in enumerate(threshold_entries):
        min_entry.delete(0, tk.END)
        min_entry.insert(0, default_values_min[i])
        max_entry.delete(0, tk.END)
        max_entry.insert(0, default_values_max[i])

# Create the left side frame
left_frame = tk.Frame(window)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW)

# Define the category_var variable
category_var = tk.IntVar()
category_var.set(1)

# All Items Radiobutton
all_items_radiobutton = tk.Radiobutton(left_frame, text="All items", variable=category_var, value=1)
all_items_radiobutton.grid(row=0, column=0, sticky=tk.W)

# General Categories Listbox
general_label = tk.Radiobutton(left_frame, text="General:", variable=category_var, value=2)
general_label.grid(row=1, column=0, sticky=tk.W, pady=(10, 0))

general_categories = ["Cider & blanddrycker", "Sprit", "Vin", "Öl", "Alkoholfritt"]

listbox_general = Listbox(left_frame, selectmode=tk.MULTIPLE, height=5, width=20)
listbox_general.grid(row=2, column=0, sticky=tk.W)

for i, category in enumerate(general_categories):
    listbox_general.insert(tk.END, category)

# Specific Categories Listbox
specific_label = tk.Radiobutton(left_frame, text="Specific:", variable=category_var, value=3)
specific_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 0))

specific_categories = ["Akvavit & Kryddat brännvin", "Ale", "Anissprit", "Annan öl", "Aperitif & Bitter", "Aperitifer", "Armagnac & Brandy", "Avec", "Bitter", "Blanddryck", "Calvados", "Cider","Cider & Blanddryck (Alkoholfri)", "Cognac", "Drinkar & Cocktail (Alkoholfri)", "Drinkar & Cocktails", "Drycker av flera typer", "Frukt & Druvsprit","Gin & Genever", "Glögg & andra juldrycker (Alkoholfri)", "Glögg och Glühwein", "Grappa & Marc", "Likör", "Ljus lager", "Mellanmörk & Mörk lager","Mousserande (Alkoholfri)", "Mousserande vin", "Must (Alkoholfri)", "Porter & Stout", "Punsch", "Rom & Lagrad sockerrörssprit", "Rosé (Alkoholfri)", "Rosévin", "Rött (Alkoholfri)", "Rött vin", "Sake", "Smaksatt sprit", "Smaksatt vin & fruktvin", "Snaps (Alkoholfri)", "Starkvin", "Syrlig öl", "Tequila & Mezcal","Vermouth", "Veteöl", "Vinlåda", "Vitt (Alkoholfri)", "Vitt vin", "Vodka & Okryddat brännvin", "Whisky", "Öl (Alkoholfri)"]
listbox_specific = Listbox(left_frame, selectmode=tk.MULTIPLE, height=10, width=20)
listbox_specific.grid(row=4, column=0, sticky=tk.W)

for i, category in enumerate(specific_categories):
    listbox_specific.insert(tk.END, category)

def select_general_category(event):
    selected_indices = listbox_general.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        category_var.set(general_categories[selected_index])
        general_label.select()

def select_specific_category(event):
    selected_indices = listbox_specific.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        category_var.set(specific_categories[selected_index])
        specific_label.select()

# Bind the <<ListboxSelect>> event to the listboxes
listbox_general.bind("<<ListboxSelect>>", select_general_category)
listbox_specific.bind("<<ListboxSelect>>", select_specific_category)

# Create a separator
separator = ttk.Separator(window, orient='vertical')
separator.grid(row=0, column=1, sticky='ns')

# Create the right side frame
right_frame = tk.Frame(window)
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky=tk.NW)

# Threshold Entry
threshold_frame = tk.Frame(right_frame)
threshold_frame.grid(row=0, column=0, sticky=tk.NW)

threshold_entries = []
labels = ["Alcohol %", "APK", "Volume", "Price"]
default_values_max = [100, 300, 10000, 10000]
default_values_min = [0, 0, 0, 0]

for i in range(4):
    label = tk.Label(threshold_frame, text=labels[i])
    label.grid(row=i, column=0, sticky=tk.W, padx=10)
    
    min_entry = tk.Entry(threshold_frame, width=7)
    min_entry.insert(tk.END, str(default_values_min[i]))  # Set default value
    min_entry.grid(row=i, column=1, sticky=tk.W, padx=(0, 5))
    
    tk.Label(threshold_frame, text="-").grid(row=i, column=2, sticky=tk.W, padx=5)
    
    max_entry = tk.Entry(threshold_frame, width=7)
    max_entry.insert(tk.END, str(default_values_max[i]))  # Set default value
    max_entry.grid(row=i, column=3, sticky=tk.W)
    
    threshold_entries.append((min_entry, max_entry))



outputType = 0 #0 = productName, #1 = link
apply_preset(3)
indexItems = []
items = []

# Button to trigger filtering
def filter_items():
    global items
    global indexItems

    # Get the values from the listboxes
    
    selected_category = category_var.get()
    if selected_category == 1:  # All items
        indexItems = allItems()

    elif selected_category == 2:  # General categories
        selected_general_categories = listbox_general.curselection()
        selected_general_categories = [listbox_general.get(index) for index in selected_general_categories]
        indexItems = generalCategories(selected_general_categories)

    elif selected_category == 3:  # Specific categories
        selected_specific_categories = listbox_specific.curselection()
        selected_specific_categories = [listbox_specific.get(index) for index in selected_specific_categories]
        indexItems = specificCategories(selected_specific_categories)
    
    # Create a list to store the retrieved values
    threshold_values = []

    # Loop through the threshold_entries list
    for min_entry, max_entry in threshold_entries:
        try: 
            threshold_values.append(float(min_entry.get()))
            threshold_values.append(float(max_entry.get()))
        except:
            return

        #(alcoholPrecentageMin, alcoholPrecentageMax, apkMin, apkMax, volumeMin, volumeMax, priceMin, priceMax)
        #(threshold_values[0], threshold_values[1], threshold_values[2], threshold_values[3], threshold_values[4], threshold_values[5], threshold_values[6], threshold_values[7])
    indexItems = thresholdApplyer(indexItems, threshold_values[0], threshold_values[1], threshold_values[2], threshold_values[3], threshold_values[4], threshold_values[5], threshold_values[6], threshold_values[7])

    result = ["Matching items...","---------------------------------"]
    for i in indexItems:
        result.append(getIndexParameter("productName", i))
    items = result

    # Display the filtered items in the listbox
    
    listbox_filtered.delete(0, tk.END)
    for item in items:
        listbox_filtered.insert(tk.END, item)

def openFilteredLinks(amountOfUrls):
    global indexItems
    counter = 0
    try:
        for i in indexItems:
            url = "https://www.systembolaget.se/"+getIndexParameter("productNumber", i)+"/"
            webbrowser.open_new(url)
            counter += 1
            if counter == amountOfUrls:
                return
                
    finally: pass

filter_button = tk.Button(right_frame, text="Filter", command=filter_items, width=14)
filter_button.grid(row=1, column=0, pady=10)

# Listbox to display filtered items
listbox_filtered = Listbox(right_frame, height=13, width=35)
listbox_filtered.grid(row=2, column=0, sticky=tk.W)

window.mainloop()
