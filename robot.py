import wpilib
from phoenix5 import WPI_TalonSRX, NeutralMode
import wpilib.drive

breakMode = NeutralMode(2)

class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.motorRightMaster = WPI_TalonSRX(1)
        self.motorRightSlave = WPI_TalonSRX(2)

        self.motorRightMaster.setNeutralMode(breakMode)
        self.motorRightSlave.setNeutralMode(breakMode)

        self.motorRightMaster.setSafetyEnabled(True)
        self.motorRightSlave.setSafetyEnabled(True)

        self.right = wpilib.MotorControllerGroup(self.motorRightMaster, self.motorRightSlave)
        self.right.setInverted(True)

        self.motorLeftMaster = WPI_TalonSRX(3)
        self.motorLeftSlave = WPI_TalonSRX(4)

        self.motorLeftMaster.setNeutralMode(breakMode)
        self.motorLeftSlave.setNeutralMode(breakMode)

        self.motorLeftMaster.setSafetyEnabled(True)
        self.motorLeftSlave.setSafetyEnabled(True)

        self.left = wpilib.MotorControllerGroup(self.motorLeftMaster, self.motorLeftSlave)
        self.left.setInverted(False)

        self.robotDrive = wpilib.drive.DifferentialDrive(self.left, self.right)
        

        self.controller = wpilib.XboxController(0)

    def autonomousInit(self) -> None:
        """The function is called when autonomous starts"""
        return None
    
    def autonomousPeriodic(self) -> None:
        """The function is called periodically during autonomous mode"""
        return None
    
    def teleopInit(self) -> None:
        """The function is called when teleoperated starts"""
        return None
    
    def teleopPeriodic(self) -> None:
        """The function is called periodically during teleoperated mode"""
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getRightX(), True
        )
    
if __name__ == "__main__":
    wpilib.run(MyRobot)
