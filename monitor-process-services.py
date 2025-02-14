import psutil
import time
import os

def monitor_services(services):
    """
    Função para monitorar e garantir que os serviços essenciais estão rodando.
    :param services: Lista de nomes dos serviços para monitorar
    :return: None
    """
    while True:
        for service in services:
            found = False
            for proc in psutil.process_iter(['pid', 'name']):
                if service.lower() in proc.info['name'].lower():
                    found = True
                    break
            
            if not found:
                print(f"Serviço {service} não encontrado. Reiniciando...")
                os.system(f"systemctl start {service}")  # Comando para reiniciar o serviço em sistemas Linux
            else:
                print(f"Serviço {service} está em execução.")
        
        time.sleep(60)  # Verifica a cada 60 segundos

# Lista de serviços essenciais para monitorar
services = ["apache2", "nginx", "mysql"]
monitor_services(services)
