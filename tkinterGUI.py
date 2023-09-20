import tkinter as tk
from tkinter import Listbox, ttk
from alkobeast import allList, typeGetter, thresholdApplyer, productNames

window = tk.Tk()
window.title("Store Item Filter")
window.resizable(0, 0)

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

general_categories = ['General 1', 'General 2', 'General 3',
                      'General 4', 'General 5', 'General 6']

listbox_general = Listbox(left_frame, selectmode=tk.MULTIPLE, height=5, width=20)
listbox_general.grid(row=2, column=0, sticky=tk.W)

for i, category in enumerate(general_categories):
    listbox_general.insert(tk.END, category)

# Specific Categories Listbox
specific_label = tk.Radiobutton(left_frame, text="Specific:", variable=category_var, value=3)
specific_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 0))

specific_categories = ['Specific 1', 'Specific 2', 'Specific 3', 'Specific 4', 'Specific 5',
                       'Specific 6', 'Specific 7', 'Specific 8', 'Specific 9', 'Specific 10','test']

listbox_specific = Listbox(left_frame, selectmode=tk.MULTIPLE, height=10, width=20)
listbox_specific.grid(row=4, column=0, sticky=tk.W)

for i, category in enumerate(specific_categories):
    listbox_specific.insert(tk.END, category)

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

# Button to trigger filtering
def filter_items():
    # Get the values from the listboxes
    selected_specific_categories = listbox_specific.curselection()
    selected_specific_categories = [listbox_specific.get(index) for index in selected_specific_categories]

    selected_general_categories = listbox_general.curselection()
    selected_general_categories = [listbox_general.get(index) for index in selected_general_categories]
    
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

    # Append the retrieved values to the threshold_values list
    print(threshold_values)
    # Perform the filtering logic here
    # Use the retrieved values to filter the items from your store
    print("-------------------------------------------")
    filtered_items = productNames(thresholdApplyer(allList(), threshold_values[0], threshold_values[1], threshold_values[2], threshold_values[3], threshold_values[4], threshold_values[5], threshold_values[6], threshold_values[7]))
    resultString = str(len(filtered_items)) + " Matching items..."
    
    filtered_items = [resultString, "---------------------------------"] + filtered_items

    # Display the filtered items in the listbox
    
    listbox_filtered.delete(0, tk.END)
    for item in filtered_items:
        listbox_filtered.insert(tk.END, item)

filter_button = tk.Button(right_frame, text="Filter", command=filter_items, width=14)
filter_button.grid(row=1, column=0, pady=10)

# Listbox to display filtered items
listbox_filtered = Listbox(right_frame, height=13, width=35)
listbox_filtered.grid(row=2, column=0, sticky=tk.W)

window.mainloop()
