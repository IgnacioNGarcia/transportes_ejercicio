from src.factory.Creador import CreadorTransporte

def realizar_viaje_en_auto():
    print("\n=== Viaje en Auto ===")
    creador_auto = CreadorTransporte.get_creador("Auto")
    auto = creador_auto.get_transporte()
    print(auto.transportar("Santiago", "Valparaíso"))
    print("=== Fin del viaje en auto ===\n")

def realizar_viaje_en_dron():
    print("\n=== Viaje en Dron ===")
    creador_dron = CreadorTransporte.get_creador("Dron")
    dron = creador_dron.get_transporte()
    print(dron.transportar("Santiago", "Valparaíso"))
    print("=== Fin del viaje en dron ===\n")

def main():

    realizar_viaje_en_auto()
    realizar_viaje_en_dron()

if __name__ == "__main__":
    main() 