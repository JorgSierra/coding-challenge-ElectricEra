import sys
from collections import defaultdict
from .exeptions import *

SECTION_STATIONS = '[Stations]'
CHARGER_REPORTS = '[Charger Availability Reports]'

def xnor (a, b):
    return a == b

def getArgs():
    # Fetch and validate command-line arguments.
    if len(sys.argv) != 2:
        raise TooManyArgumentsError(f'{sys.argv[0]} accepts exactly one argument: the input file path')
    return sys.argv[1]

def parseStation(stations, line):
    # Parce dictionary of chargers in a station.
    ids = list(map(int, line.split()))
    if any(identificator < 0 for identificator in ids):
        raise InvalidFormat(f'Invalid input negative number')
    stationId, chargerIds = ids[0], ids[1:]

    if stationId in stations.keys():
        raise DuplicatedStationID(f'Station ID: {stationId} is duplicated')
    
    if len(chargerIds) < 1:
        raise EmptyStation(f'Station ID: {stationId} has no chargers associated')
    
    for currentChargers in stations.values():
        duplicatedChargerIds = set(chargerIds) & set(currentChargers)
        if (duplicatedChargerIds):
            raise DuplicatedChargerID(f'Charger ID(s): {duplicatedChargerIds} duplicated across stations')
        
    stations[stationId] = chargerIds

def parseReports(stations, chargerReportsByStation, line):
    # Parse charger availability reports.
    chargerData = line.split()

    if len(chargerData) != 4:
        raise InvalidFormat()

    if chargerData[3].lower() == 'true':
        isUp = True
    elif chargerData[3].lower() == 'false':
        isUp = False
    else:
        raise InvalidFormat(f'Invalid input format for true/false')
    
    chargerId = int(chargerData[0])
    startTime = float(chargerData[1])
    endTime = float(chargerData[2])
    if chargerId < 0 or startTime < 0 or endTime < 0:
        raise InvalidFormat(f'Invalid input negative number')    
    
    if startTime > endTime:
        raise InvalidFormat(f'End time less than start time in ID: {chargerId} Start time: {startTime} End time: {endTime}')
    
    stationId_ChargerId = next((stationId for stationId, chargers in stations.items() if chargerId in chargers), None)
    if stationId_ChargerId is None:
        raise ChargerWitoutStation(f'Charger {chargerId} does not belong to any station')

    chargerReportsByStation[stationId_ChargerId].append((
        chargerId,
        startTime,
        endTime,
        isUp
    ))

def parseInput(filePath):
    # Open file and parse document lines.
    stations = {}
    chargerReportsByStation = defaultdict(list)
    currentSection = None

    with open(filePath, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()

        if not line:
            continue
        if line.startswith('['):
            if xnor(line != SECTION_STATIONS, line != CHARGER_REPORTS):
                raise  MissnamedSection(f'{line} Is not an expected section')
            currentSection = line
            continue

        if currentSection == SECTION_STATIONS:
            parseStation(stations, line)
            
        elif currentSection == CHARGER_REPORTS:
            parseReports(stations, chargerReportsByStation, line)
             
    if not stations or not chargerReportsByStation:
        raise MissingSection(f'No data parsed for: {'' if stations else '[Stations]'}{'' if chargerReportsByStation else '[Charger Availability Reports]'}')

    return chargerReportsByStation

def computeUptime(chargerReports):
    # Calculate a station uptime.
    if not chargerReports:
        return 0, 0

    totalTime = 0
    upTime = 0
    sortedReports = sorted(chargerReports, key = lambda x : (x[1], x[2]))

    upTime = 0
    lastEndTime = None
    minStartTime = None
    maxEndTime = None
    for chargerId, startTime, endTime, isUp in sortedReports:
        if lastEndTime is None and minStartTime is None and maxEndTime is None:
            lastEndTime = startTime
            minStartTime = startTime
            maxEndTime = endTime

        minStartTime = min(minStartTime, startTime)
        maxEndTime = max(maxEndTime, endTime)

        if isUp:
            if (lastEndTime >= startTime) and (lastEndTime <= endTime):
                upTime += endTime - lastEndTime
            elif lastEndTime < startTime:
                upTime += endTime - startTime
            lastEndTime = max(lastEndTime, endTime)
    
    totalTime = maxEndTime - minStartTime     
    return upTime, totalTime

def calculateStationUptime(chargerReportsByStation):
    # Iterates over stations an its carger reports to calculate the station uptime.   
    stationUptimes = []

    for stationId, chargerReports in chargerReportsByStation.items():
        upTime, totalTime = computeUptime(chargerReports)
        if totalTime > 0:
            stationUptimes.append((stationId, int((upTime / totalTime) * 100)))
        else:
            raise InvalidFormat('Inconsistent report data')
        
    return stationUptimes

def output(stationsUptime):
    # Pint the stations uptime in ascending order.
    sortedStationUptime = sorted(stationsUptime, key = lambda x : (x[0]))
    for stationId, upTime in sortedStationUptime:
        print(f'{stationId} {upTime}')