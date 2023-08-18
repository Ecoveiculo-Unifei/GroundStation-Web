import serial
import serial.tools.list_ports

class EspLora:
    def __init__(self, porta_serial, baud_rate):
        self.porta = porta_serial
        self.baudrate = baud_rate
        self.esp_port = serial.Serial(porta_serial,baudrate = baud_rate)  

    def change_info(self, porta, rate):
        self.porta = porta
        self.baudrate = rate
        self.esp_port = serial.Serial(self.porta,baudrate = self.baudrate)     

    def open(self) -> bool:
        try:
            self.esp_port.open()
            return True
        except:
            pass
        return False
    
    def close(self) -> bool:
        try:
            self.esp_port.close()
            return True
        except:
            pass
        return False
    
    def read(self):
        self.esp_port.flushInput()
        self.esp_port.flushOutput()
        self.esp_port.flush()
        try:
            linha = self.esp_port.readline().decode().strip('\r\n')
            if linha.startswith("<") and linha.endswith(">"):
                pacote = linha[1:-1].split(';')
                pacote = {
                    "Id": int(pacote[0]),
                    "Tempo": int(pacote[1]),
                    "Distancia": float(pacote[2]),
                    "VelInst": float(pacote[3]),
                    "VelMedia": float(pacote[4]),
                    "Voltas": int(pacote[5]),
                    "RPM": int(pacote[6])
                }
                return pacote
            else:
                raise Exception
            
        except:
            return None


def search(comDescricao = False):
    portas = serial.tools.list_ports.comports()
    if comDescricao:
        portas = [(porta.device + "/" +porta.description) for porta in portas]
    else:
        portas = [porta.device for porta in portas]
    return portas 
    
def frequencias():
    return [9600,19200,115200]

        
