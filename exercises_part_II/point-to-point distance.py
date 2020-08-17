"""TEST - DISTANCE BETWEEN DECIMAL DEGREES

1.OPEN FILE
2.READ LINE BY LINE OF FILE
3.SPLIT BY ","
4.WRITE HEADER IN FILE
5.TAKE 3RD, 4TH, 5TH AND 6TH POSITIONS FOR EACH LINE
6.MAKE CALCULATION OF POIN TO POINT DISTANCE FOR EACH LINE
7.WRITE LINE BY LINE INCLUDING THE NEW FIELD DISTANCE IN FILE """

import math
import csv

list_row = []
line_ok = []
line_nok = []
duplicated_list = []

with open("FlightDistanceTest.csv") as csv_file:
    file_flight_distance = csv_reader = csv.reader(csv_file, delimiter=",")
    csv_reader.__next__()

    with open("exitFlightDistanceTest.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Normalised City Pair", "Departure Code", "Arrival Code", "Departure_lat", "Departure_lon", "Arrival_lat", "Arrival_lon", "Distance"])
        for row in file_flight_distance:
            duplicado_lista = row
            controle = False

            for duplicated in duplicated_list:
                if (duplicated[1] == row[1] and duplicated[2] == row[2] and
                    duplicated[3] == row[3] and duplicated[4] == row[4] and  
                    duplicated[5] == row[5] and duplicated[6] == row[6]):
                    controle = True
               
            if controle == False:
                depart_lat = row[3]
                depart_lon = row[4]
                arrival_lat = row[5]
                arrival_lon = row[6]
                #=Raio*ACOS(COS(RADIANOS(90-Latitude_1))*COS(RADIANOS(90-Latitude_2))+SEN(RADIANOS(90-Latitude_1))*SEN(RADIANOS(90-Latitude_2))*COS(RADIANOS(Longitude_1-Longitude_2))*Fator_Ajuste
                radius = 6372.795477598
                adjust_factor = 1
                distance = radius * (math.acos(math.cos(math.radians(90 - float(depart_lat))) * math.cos(math.radians(90 - float(arrival_lat))) + math.sin(math.radians(90 - float(depart_lat))) * math.sin(math.radians(90 - float(arrival_lat))) * math.cos(math.radians(float(depart_lon) - float(arrival_lon))) * adjust_factor))
                distance = "{0:.2f}".format(distance)
                row.append(distance)
                list_row.append(row)
                duplicated_list.append(duplicado_lista)
                writer.writerow(row)
            
        for item in list_row:
            control = 0
            for i in list_row:
                a = float(i[7])*0.97
                b = float(i[7])*1.03
                c = float(item[7])
                if item[1] == i[2] and item[2] == i[1]:
                    control = control + 1
                    if c >= a and c <= b:
                        line_ok.append(item[1] + "-" + item[2] + ":" + item[7])
                    else:
                        line_nok.append(item[1] + "-" + item[2] + ":" + item[7])
            if control == 0:
                line_ok.append(item[1] + "-" + item[2] + ":" + item[7])         

        with open("file_ok.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for line in line_ok:
                writer.writerow([line])
        with open("file_nok.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for line in line_nok:
                writer.writerow([line])