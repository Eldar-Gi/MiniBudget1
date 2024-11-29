import logging
import pickle


def ivesti_pajamas(pajamos):
    data = input("Iveskite data (YYYY-MM-DD): ")
    pavadinimas = input("Iveskite pavadinima: ")
    suma = float(input("Ivesti pajamu suma: "))
    pajamos.append([data, pavadinimas, suma])
    print("Pajamos  ivestos.")


def ivesti_islaidas(islaidos):
    data = input("Iveskite data (YYYY-MM-DD): ")
    pavadinimas = input("Iveskite pavadinima: ")
    suma = float(input("Ivesti pajamu suma: "))
    islaidos.append([data, pavadinimas, suma])
    print("Pajamos  ivestos.")


def spausdinti_eiles(sarasas, tipas):
    print(f"\n{tipas}:")
    for i, line in enumerate(sarasas, start=1):
        print(f"{i}. {line[0]} - {line[1]}: {line[2]:.2f} EUR")


def spausdinti_statistika(pajamos, islaidos):
    suma_pajamu = sum(item[2] for item in pajamos)
    suma_islaidu = sum(item[2] for item in islaidos)
    balansas = suma_pajamu - suma_islaidu
    print("\nStatistika:")
    print(f"Pajamos: {suma_pajamu:.2f} EUR")
    print(f"Islaidos: {suma_islaidu:.2f} EUR")
    print(f"Balansas: {balansas:.2f} EUR")


logging.basicConfig(
    filename="../errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def trinti_eilute(sarasas, tipas):
    print(f"\n{tipas} Ivestis:")
    for info, ivadas in enumerate(sarasas, start=1):
        print(f"{info}. {ivadas[0]} - {ivadas[1]}: {ivadas[2]:.2f} EUR")
    try:
        indeksas = int(input(f"Iveskite  {tipas} ka istrinti: ")) - 1
        if 0 <= indeksas < len(sarasas):
            sarasas.pop(indeksas)
            print(f"{tipas} istrinta.")
        else:
            raise IndexError("Invalid index.")
    except ValueError:
        logging.error("Ivedet ne skaicius.")
        print("Error: Iveskite tinkama skaiciu.")
    except IndexError as elem:
        logging.error(f"Nepasiekama: {elem}")
        print("Error: Netinkamas pasirinkimas.")


def issaugoti_duomenis(pajamos, islaidos, filename="duomenys.pkl"):
    try:
        with open(filename, 'wb') as file:
            # noinspection PyTypeChecker
            pickle.dump({'pajamos': pajamos, "islaidos": islaidos}, file)
            print('Duomenys issaugoti')
    except NameError:
        logging.error(f"Duomenu issaugojimo klaida")
    print("Error: Nepavyko issaugoti duomenuu.")
