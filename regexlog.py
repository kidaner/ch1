import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"
resultfinal = re.search(regex, log)
print(resultfinal[1])
