import magicbot
import wpilib
import rev

class DriveTrain:
    '''Uses objects created in robot.py to create functions for drivetrain.'''
    frontLeftMotor: rev.CANSparkMax
    frontRightMotor: rev.CANSparkMax
    backLeftMotor: rev.CANSparkMax
    backRightMotor: rev.CANSparkMax
    leftEncoder: rev.CANEncoder
    rightEncoder: rev.CANEncoder

    def __init__(self):
        '''sets motor values to zero when initiating. '''
        self.leftMotors = 0
        self.rightMotors = 0

    def tankDrive(self, leftSide, rightSide):
        '''sets right and left motors to directly corespond to right and left joystick (tank drive)'''
        self.leftMotors = leftSide
        self.rightMotors = rightSide

    def arcadeDrive(self, frontBack, turn):
        '''one joystick controls the robot's left and right motors'''
        self.leftMotors = frontBack - turn
        self.rightMotors = frontBack + turn

    def execute(self):
        '''this groups the motors to their sides and stors and pushes the encoder's data to the dashboard'''
        self.frontLeftMotor.set(self.leftMotors)
        self.backLeftMotor.set(self.leftMotors)
        self.frontRightMotor.set(self.rightMotors)
        self.backRightMotor.set(self.rightMotors)
        wpilib.SmartDashboard.putNumber('leftWheel', self.getLeftWheelDistance())
        wpilib.SmartDashboard.putNumber('RightWheel', self.getRightWheelDistance())

        '''this sets the defalt speed to 0 so the robot does not just turn on and run off'''
        self.leftMotors = 0
        self.rightMotors = 0

    def getLeftWheelDistance(self):
        '''get encoder value of the left side of robot.'''
        return self.leftEncoder.getPosition()

    def getRightWheelDistance(self):
        '''gets encoder value of the right side of robot.'''
        return self.rightEncoder.getPosition()

    def resetEncoders(self):
        '''Resets encoders to zero.'''
        self.leftEncoder.setPosition(0.0)
        self.rightEncoder.setPosition(0.0)

    
