area = float(input())

if(area < 11.2):
    print("Para area = {:.1f} : Recomendamos 9800 BTU/h".format(area))
elif(11.2 <= area < 16.2):
    print("Para area = {:.1f} : Recomendamos 12800 BTU/h".format(area))
elif(16.2 <= area < 21.2):
    print("Para area = {:.1f} : Recomendamos 15800 BTU/h".format(area))
elif(21.2 <= area < 26.2):
    print("Para area = {:.1f} : Recomendamos 18800 BTU/h".format(area))
elif(26.2 <= area <= 31.2):
    print("Para area = {:.1f} : Recomendamos 21800 BTU/h".format(area))
else:
    print("Para area = {:.1f} : Sem recomendacao".format(area))
