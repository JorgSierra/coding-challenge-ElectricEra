class TooManyArgumentsError(Exception):
    """Raised when too many arguments are passed."""
    def __init__(self, message="Too many arguments were provided."):
        super().__init__(message)

class MissnamedSection(Exception):
    """Raised when a section of the input is other than specifications."""
    def __init__(self, message="Found a non desired section."):
        super().__init__(message)

class MissingSection(Exception):
    """Raised when a expected section is not in the input file."""
    def __init__(self, message="Missing input section."):
        super().__init__(message)

class ChargerWitoutStation(Exception):
    """Raised when a chargerId does not belong to a stationId."""
    def __init__(self, message="The charger lacks an association with any station."):
        super().__init__(message)

class DuplicatedStationID(Exception):
    """Raised when a station ID is not unique."""
    def __init__(self, message="Station ID duplicated."):
        super().__init__(message)

class DuplicatedChargerID(Exception):
    """Raised when a charger ID is not unique across stations."""
    def __init__(self, message="Charger ID duplicated."):
        super().__init__(message)

class EmptyStation(Exception):
    """Raised when a station has no chargers."""
    def __init__(self, message="Empty station."):
        super().__init__(message)

class InvalidFormat(Exception):
    """Raised when the input the input doesn't follow the expected format."""
    def __init__(self, message="Invalid input format."):
        super().__init__(message)