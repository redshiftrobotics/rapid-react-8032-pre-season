import wpilib

class PCM:
    pcm_id: int

    def __init__(self):
        self.compressor = wpilib.Compressor(self.pcm_id)
        self.compressor.setClosedLoopControl(True)

        self.solenoids = {}

        self.type_single = "SINGLE"
        self.type_double = "DOUBLE"
    
    def setupSingleSolenoid(self, name, solenoid_id):
        self.solenoids[name] = {
            'solenoid': wpilib.Solenoid(self.pcm_id, solenoid_id),
            'type': self.type_single
        }
    
    def setupDoubleSolenoid(self, name, forward_id, reverse_id, start_state):
        self.solenoids[name] = {
            'solenoid': wpilib.DoubleSolenoid(self.pcm_id, forward_id, reverse_id),
            'type': self.type_double
        }

        self.solenoids[name]['solenoid'].set(start_state)

    def setSingleSolenoid(self, name, state):
        if self.solenoids[name]['type'] == self.type_single:
            self.solenoids[name]['solenoid'].set(state)
        else:
            raise Exception(f"Solenoid {name} is not a single solenoid")
    
    def toggleSingleSolenoid(self, name):
        if self.solenoids[name]['type'] == self.type_single:
            self.solenoids[name]['solenoid'].toggle()
        else:
            raise Exception(f"Solenoid {name} is not a double solenoid")

    def setDoubleSolenoid(self, name, state):
        if self.solenoids[name]['type'] == self.type_double:
            self.solenoids[name]['solenoid'].set(state)
        else:
            raise Exception(f"Solenoid {name} is not a single solenoid")
    
    def toggleDoubleSolenoid(self, name):
        if self.solenoids[name]['type'] == self.type_double:
            self.solenoids[name]['solenoid'].toggle()
        else:
            raise Exception(f"Solenoid {name} is not a double solenoid")

    def execute(self):
        self.leftMotors = 0
        self.rightMotors = 0