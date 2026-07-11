stores = [
    ("Tech Hub", (27.2123, 85.3249)),
    ("Book World", (27.2353, 85.7649)),
    ("Coffee Spot", (27.2323, 85.3789)),
]

def show_stores(store_list):
    for name, (lat, lon) in store_list:
        print(f"{name} is located at latitude: {lat}, Longitude: {lon}")

def find_store(store_list, search_name):
    for name, coords in store_list:
        if name.lower() == search_name.lower():
            return coords
    return None

# Show all stores
show_stores(stores)

# Find a specific store
location = find_store(stores, "Book World")
if location:
    print(f"\nFound 'Book World' at {location}")
else:
    print("\nStore not found.")
