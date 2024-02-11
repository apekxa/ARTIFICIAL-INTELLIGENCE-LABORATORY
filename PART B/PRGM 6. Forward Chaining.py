# Forward chaining example code 
# Define the initial state
initial_state = ["dirty", "smelly"]
# Define the rules
rules = [
    {"if": ["dirty"], "then": ["clean"]},
    {"if": ["clean", "smelly"], "then": ["fresh"]},
]
# Define the goal
goal = ["fresh"]
# Initialize the current state
current_state = initial_state
# Apply the rules until the goal is reached
while not all(x in current_state for x in goal):
    for rule in rules:
        if all(x in current_state for x in rule["if"]):
            current_state += rule["then"]
# Print the final state
print("The final state is:", current_state)
