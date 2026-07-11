server_location = (30.2672, -97.7431)
print("Server Coordinates:", server_location)

submitted_ids = ["user10", "user25", "user10", "user42", "user25", "user99"]

unique_ids_set = set(submitted_ids)

clean_id_list = list(unique_ids_set)

print("Original List with duplicates:", submitted_ids)
print("Clean list via Set conversion:", clean_id_list)
