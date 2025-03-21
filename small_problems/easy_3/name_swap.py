# def swap_name(name):
#     return ', '.join(name.split()[::-1])

def swap_name(name):
    # refactored to accept middle names
    names_lst = name.split()
    last_name = names_lst.pop()
    return f"{last_name}, {' '.join(names_lst)}"


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True

