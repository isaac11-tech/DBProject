class Agent:
    def __init__(self, code_name: str, real_name: str, location: str, status: str, missions_completed: int):
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status  # "Active", "Injured", "Missing", "Retired"
        self.missions_completed = missions_completed

    def __str__(self):
        return f"Agent {self.code_name} ({self.real_name}) - Status: {self.status}, Location: {self.location}, Missions: {self.missions_completed}"

