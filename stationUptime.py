#!/usr/bin/env python3

'''
Jorge Sierra
coding-challenge-charger-uptime

Coding chalenge for Electric Era 
Software Engineer (Entry Level) application

Calculate uptime for stations in charging network
Station uptime is the percentage of time that any charger at a station was available,
out of the entire time period that any charger at that station was reporting in.

Station Uptime (%)=( TotalTimeAnyChargerWasAvailable / TotalReportingTimeofAnyCharger ) × 100

'''

from src.util import *

try:
    filePath = getArgs()
    chargerReportsByStation = parseInput(filePath)
    stationsUptime = calculateStationUptime(chargerReportsByStation)

except FileNotFoundError:
    print(f"ERROR - File not found: {filePath}")
    sys.exit(1)
except ValueError as e:
    print(f"ERROR - Invalid input {e} at {filePath}")
    sys.exit(1)
except TooManyArgumentsError:
    print(f"ERROR - Please provide exactly one argument <File path>")
    sys.exit(2)
except Exception as e:
    print(f"ERROR - {e}")
    sys.exit(1)

else:
    output(stationsUptime)
    sys.exit(0)
