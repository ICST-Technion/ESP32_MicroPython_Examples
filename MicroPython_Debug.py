try:
    # Allocate an array of size 5
    my_array = [0, 1, 2, 3, 4]
    print("Array created:", my_array)

    # Attempt to access the 6th cell (index 5)
    print("Trying to access the 6th element...")
    value = my_array[5]  # This will raise an IndexError

    # This line won't execute due to the exception
    print("6th element value:", value)

except IndexError as e:
    # Handle the IndexError exception
    print("Error: Tried to access an index out of range!")
    print(f"Exception message: {e}")
