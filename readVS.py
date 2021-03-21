import urllib.request, json, re, csv

with urllib.request.urlopen("https://data.vatsim.net/v3/vatsim-data.json") as url:
    rawData = url.read().decode()
    data = json.loads(rawData)

writer = csv.writer(open('statistics.csv', 'a+', newline=''))

time = data["general"]["update_timestamp"]
entryfix = ['BILRA', 'BANUB', 'BINKA', 'PESEL', 'BODLA', 'ALUKA', 'XIGRI', 'SUBIX', 'ARSAP', 'GOVEN', 'POZUM', 'KORUP', 'LASIS', 'NAROX', 'RASAN', 'TOMTI',
            'LAGAR', 'ELVOT', 'ENORU', 'DESEN', 'UTEVO', 'REGLI', 'BAVOK', 'PADKA', 'TUSIN', 'NETIR', 'SKARY', 'BABKO', 'MEBAN', 'SUPAK', 'KELEL', 'REGTO', 
            'LENOV', 'PODAN', 'KEFIR', 'GAWOR', 'LUGOL', 'TEPNA', 'DIBED', 'GOTIX', 'ROLKA', 'USTIL', 'IVNER', 'TOLPA', 'BIGLU', 'TOSPO', 'LETKI', 'ABERO', 
            'RUDKA', 'GORAT', 'ENOBI', 'SOTET', 'VABER', 'BOKSU', 'GOLAD', 'GITOV', 'GOMED', 'IPLIT', 'RANOK', 'KUNER', 'LATMI', 'IVGOR', 'VADRU', 'PENOR'
            'LARMA', 'RUMAR', 'GORPI', 'LUSID', 'AMROR', 'KOLOB', 'GOSOT', 'POKEN']

print(time)
for pilot in data["pilots"]:
    relevant = False
    try:
        fp = pilot["flight_plan"]
        dep = fp["departure"]
        matchDep = re.match(r'^EP..', dep, re.M|re.I)
        if matchDep:
            relevant = True
        arr = fp["arrival"]
        matchArr = re.match(r'^EP..', arr, re.M|re.I)
        if matchArr:
            relevant = True
        altitude = fp["altitude"]
        if altitude.startswith("FL"):
            altitude = altitude[2:] + "00"
        if altitude.startswith("F"):
            altitude = altitude[1:] + "00"
        if len(altitude) < 4:
            altitude = altitude + "00"
        remarks = fp["remarks"]
        matchRmk = re.match(r'EPWW', remarks, re.M|re.I)
        if matchRmk:
            relevant = True
        route = fp["route"]
        if any(fix in route for fix in entryfix):
            relevant = True
        if relevant:
            print(dep, arr, altitude)
            writer.writerow([time, dep, arr, altitude])
    except (RuntimeError, TypeError, NameError):
        pass