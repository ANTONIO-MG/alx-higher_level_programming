def element_at(my_list, idx):

	if idx < 0:
		return None
	elif idx > len(my_list):
		return None
	else:
		print(f"Element at index {idx} is {(my_list[idx] - 1)}")

	
