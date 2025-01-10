# Overview

This is a simple coding challenge to test abilities. To join the software program at Electric Era Technologies.

**Candidate**

Jorge Sierra

(253)-670-9994

jorg.sierrar@gmail.com

https://www.linkedin.com/in/jorgsierra/

# Station Uptime 
*Is defined as the percentage of time that any charger at a station was available, out of the entire time period that any charger *at that station* was reporting in.*

**Time that any charger at a station was available** - If more than one charger was available (UP) during overlaping time intervals, their availability periods are merged to calculate the total duaration that at least one charger was UP at the station.

**Time period that any charger at that station was reporting** - The total time elapsed from the earliest "start time" from any charger belonging to the station to "end time" of last report received from any charger at the station. *A gap in time in a given Charger ID's availability report should count as downtime.*

The Station Uptime value is rounded down to the nearest percent.

If a station has no designed chargers, it is considered an input error.

If a station lacks reports, the station is ignored.

## Program Parameters and Runtime Conditions
**Verify the installation of Python 3**
```shell
python --version
```
**Give execution permissions to the script**

**Avoid** placing script files in system directories or directories where you do not have ownership or proper permissions.

```shell
chmod +x stationUptime.py
```

The program accepts a single argument: the path to the input file. The input file **does not** need to be co-located in the same directory as the program.

Example CLI execution:
```shell
./stationUptime.py relative/path/to/input/file
```

## Output Format

The output is written to `stdout` and is sorted by **Station IDs** in ascending order, as follows:

```
<Station ID 1> <Station ID 1 uptime>
<Station ID 2> <Station ID 2 uptime>
...
<Station ID n> <Station ID n uptime>
```