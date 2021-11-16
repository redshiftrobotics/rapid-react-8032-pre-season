import magicbot
import wpilib
import rev

class DriveTrain:
    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    leftEncoder: rev.CANEncoder
    rightEncoder: rev.CANEncoder

    def __init__(self):
        self.leftMotors = 0
        self.rightMotors = 0

    def tankDrive(self, leftSide, rightSide):
        self.leftMotors = leftSide
        self.rightMotors = rightSide

    def arcadeDrive(self, frontBack, turn):
        self.leftMotors = frontBack - turn
        self.rightMotors = frontBack + turn

    def execute(self):
        self.frontLeftMotor.set(self.leftMotors)
        self.backLeftMotor.set(self.leftMotors)
        self.frontRightMotor.set(self.rightMotors)
        self.backRightMotor.set(self.rightMotors)
        wpilib.SmartDashboard.putNumber('leftWheel', self.getLeftWheelDistance())
        wpilib.SmartDashboard.putNumber('RightWheel', self.getRightWheelDistance())

        # TODO: Add documentation to these two lines
        self.leftMotors = 0
        self.rightMotors = 0

    def getLeftWheelDistance(self):
        return self.leftEncoder.getPosition()
        # return  self.leftEncoder.getPosition() / self.leftEncoder.getPositionConversionFactor()
        # return self.leftEncoder.getPositionConversionFactor()

    def getRightWheelDistance(self):
        return self.rightEncoder.getPosition()

    def resetEncoders(self):
        self.leftEncoder.setPosition(0.0)
        self.rightEncoder.setPosition(0.0)
    
