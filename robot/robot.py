import magicbot
import wpilib
import magicbot
import rev

# TODO: Move to separate file
class DriveTrain:
    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    bakRightMotor: rev.CANSparkMax

    def __init__(self):
        self.leftMotors = 0
        self.rightMotors = 0

    def tankDrive(self, leftSide, rightSide):
        self.leftMotors = leftSide
        self.rightMotors = rightSide

    def arcadeDrive(self, frontBack, turn):
        self.leftMotors = frontBack - turn
        self.rightMotors = frontBack + turn

    def excecute(self):
        self.frontLeftMotor.set(self.leftMotors)
        self.backLeftMotor.set(self.leftMotors)
        self.frontRightMotor.set(self.rightMotors)
        self.bakRightMotor.set(self.rightMotors)
        
        # TODO: Add documentation to these two lines
        self.leftMotors = 0
        self.rightMotors = 0
class MyRobot(magicbot.MagicRobot):
    drivetrain: DriveTrain

    def createObjects(self):
        # TODO: create joystick wrapper class (maybe use the one from last yar)
        self.driverJoystick = wpilib.Joystick(0)

        # Switched to using rev.MotorType here
        self.drivetrain_frontLeftMotor = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.drivetrain_frontRightMotor = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.drivetrain_backLeftMotor = rev.CANSparkMax(4, rev.MotorType.kBrushless)
        self.drivetrain_backRightMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)

    def teleopPeriodic(self):
        speed = 0.1
        self.drivetrain.tankDrive(speed*self.driverJoystick.getY(), speed* self.driverJoystick.getTwist())

if __name__ == '__main__':
    wpilib.run(MyRobot)




     












