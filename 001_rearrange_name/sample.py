import re


def rearrange_name(name: str) -> str:
    # Add a period '.' and space inside square bracket to capture period and space after a word
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)", name)
    return name if not result else f"{result[2]} {result[1]}"

# Fictional name list which consists of
# - names in reversed order
# - single-word names
# - names with abbreviated middle names
# - names with one middle name
# - names with more than one middle name


name_list = [
    "Hodson, Lauren K.",
    "Gabrielle",
    "Watkins, Brandee",
    "Pitts, Zachary",
    "Swift, Serina",
    "Blakeslee, Brant I.",
    "Thatcher, Brandy Jermaine",
    "Raleigh",
    "Hurst, Carter",
    "Hopper, Jarvis",
    "Garnet, Evalyn Houston Fiona",
    "Audley, Matthew",
    "Pottinger, Merlin A. K.",
    "Reeves, Ezra",
    "Pearson, Osborn K."
]

for name in name_list:
    print(rearrange_name(name))


# Expected result:

# Lauren K. Hodson
# Gabrielle
# Brandee Watkins
# Zachary Pitts
# Serina Swift
# Brant I. Blakeslee
# Brandy Jermaine Thatcher
# Raleigh
# Carter Hurst
# Jarvis Hopper
# Evalyn Houston Fiona Garnet
# Matthew Audley
# Merlin A. K. Pottinger
# Ezra Reeves
# Osborn K. Pearson
