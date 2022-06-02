import re

s = 'stop app pid:'
match = re.match(r'.*stop app pid: (\d+).*', s)

print(match.group(1))