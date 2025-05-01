from src.factory.Creador import CreadorTransporte
from src.models.SistemaTransporteCli import SistemaTransporteCli

def main():
    try:
        sistema_transporte = SistemaTransporteCli()
        sistema_transporte.conseguir_input_vehiculo()
        sistema_transporte.conseguir_input_origen_destino()
        
        creador = CreadorTransporte.get_creador(sistema_transporte.vehiculo)
        transporte = creador.get_transporte()
        
        print(transporte.transportar(sistema_transporte.origen, sistema_transporte.destino))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    