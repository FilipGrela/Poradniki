class Motor():
    def __init__(self, port, max_voltage, min_voltage):
        self.port = port
        self.max_voltage = max_voltage

    def setVoltage(self, voltage):
        if voltage >= self.max_voltage:
            voltage = self.max_voltage

        print(voltage)


def main():
    leftMotor = Motor(2, 10)
    leftMotor.setVoltage(710)

    rightMotor = Motor(2, 50)
    rightMotor.setVoltage(30)


if __name__ == '__main__':
    main()
