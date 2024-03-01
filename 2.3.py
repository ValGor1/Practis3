Seconds = int(input())
Hours = Seconds // 3600
Minutes = (Seconds % 3600) // 60
Sec = Seconds % 60
print(Hours, ':', Minutes, ':', Sec, sep = '')
