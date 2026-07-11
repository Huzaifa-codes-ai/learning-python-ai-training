user_profile = {
    "name": "Sarah",
    "role": "AI Trainer",
    "tasks_completed": 42,
    "is_active": True
}

print("--- Accessing Dictionary Data ---")

print("User Name: " + user_profile["name"])
print("Total Tasks: " + str(user_profile["tasks_completed"]))

user_profile["location"] = "Texas"

user_profile["tasks_completed"] = 43

print("\nUpdated Profile Dictionary:")
print(user_profile)
