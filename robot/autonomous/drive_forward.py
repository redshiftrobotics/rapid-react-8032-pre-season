from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

from components.drivetrain import DriveTrain


class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = True
    # Injected from the definition in robot.py
    drivetrain: DriveTrain

    @state(first=True)
    def drive_forward(self):
        target = (5.0/3.5) * 3
        current = self.drivetrain.getLeftWheelDistance()
        error = target - current
        if error > 0.05:
            error = 0.05
           
        if error < -0.05:
            error = -0.05
        
        self.drivetrain.tankDrive(error, error)