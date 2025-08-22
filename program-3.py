def series_generation(a):
    if a%2 == 0:
        a -= 1
     
    series = []
    for i in range(a):
        series.append(2*i+1)
    return series


a = int(input("Enter a number"))
result = series_generation(a)

print(", ".join(map(str, result)))

