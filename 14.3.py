N = float(input())
Hours = N / 30
Hours = int(Hours)
Minutes = (N - Hours*30) * 2
Minutes = int(Minutes)
print("полных часов ", Hours, "полных минут", Minutes)