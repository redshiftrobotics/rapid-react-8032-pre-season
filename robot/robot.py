import magicbot
import wpilib
import rev
from components.drivetrain import DriveTrain


class MyRobot(magicbot.MagicRobot):
    drivetrain: DriveTrain

    def createObjects(self):
        # TODO: create joystick wrapper class (maybe use the one from last yar)
        self.driverJoystick = wpilib.Joystick(0)
        self.driverJoystick.setZChannel(5)

        self.drivetrain_frontLeftMotor = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.drivetrain_frontRightMotor = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.drivetrain_backLeftMotor = rev.CANSparkMax(4, rev.MotorType.kBrushless)
        self.drivetrain_backRightMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)

        self.drivetrain_frontLeftMotor.setInverted(False)
        self.drivetrain_backLeftMotor.setInverted(False)
        self.drivetrain_backRightMotor.setInverted(True)
        self.drivetrain_frontRightMotor.setInverted(True)

        self.drivetrain_leftEncoder = self.drivetrain_backLeftMotor.getEncoder()
        self.drivetrain_rightEncoder = self.drivetrain_backRightMotor.getEncoder()
        self.exSole = wpilib.DoubleSolenoid(0,0,1)
        self.c = wpilib.Compressor(0)


    def teleopInit(self):
        self.drivetrain.resetEncoders()

        self.c.setClosedLoopControl(True)
        self.c.start()
        


    def teleopPeriodic(self):

        '''This sets the max speed that the robot can go and also controls the how fast it '''
        #speed = 0.2
        #self.drivetrain.tankDrive(-1* speed*self.driverJoystick.getY(), -1* speed* self.driverJoystick.getZ())
        #print(self.driverJoystick.getRawAxis(1))
        #self.logger.info(self.drivetrain.getLeftWheelDistance())
        #wpilib.SmartDashboard.putNumber('leftJoystick', speed*self.driverJoystick.getY())

        if self.driverJoystick.getTopPressed() == True:
            self.exSole.set(wpilib.DoubleSolenoid.Value.kForward)

    def autonomousInit(self):
        self.drivetrain.resetEncoders()

if __name__ == '__main__':
    wpilib.run(MyRobot)




     












