import pymodbus
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method = 'rtu',port='/dev//ttyUSB0',baudrate=19200,timeout=10)
print(client.port)
result = client.read_holding_registers(address=1018,count=2,unit=1)
print("WattNode VoltA Registers 1019-1020:",result.registers)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers,Endian.Big,Endian.Little)
print("VoltA=",decoder.decode_32bit_float())

