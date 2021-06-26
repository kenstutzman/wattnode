import pymodbus

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client = ModbusClient(method = 'rtu',port='/dev//ttyUSB0',baudrate=19200,timeout=10)
print(client.port)
result = client.read_holding_registers(address=1212,count=9,unit=1)
print("WattNode Int Registers 1213-1221:",result.registers)
print("VoltAvgLN",result.registers[0])
print("VoltA",result.registers[1])
print("VoltB",result.registers[2])
print("VoltC",result.registers[3])
print("VoltAvgLL",result.registers[4])
print("VoltAvgAB",result.registers[5])
print("VoltAvgBC",result.registers[6])
print("VoltAvgAC",result.registers[7])
print("Freq",result.registers[8])
