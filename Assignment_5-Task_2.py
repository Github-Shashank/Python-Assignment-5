# Demonstrate List Slicing

num_list = [i for i in range(1,11)]
print("Original list: {}".format(num_list))

ext_list = num_list[:5]
print("Extracted first five elements: {}".format(ext_list))

ext_list.reverse()
print("Reversed extracted elements: {}".format(ext_list))
