import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")

print(result.groups())
print(result[0])
print(result[1])
print(result[2])


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"


print(rearrange_name("Kidane, Robel"))
