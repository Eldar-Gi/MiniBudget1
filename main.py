from Mylib.funkcijos import ivesti_pajamas, ivesti_islaidas, spausdinti_eiles, spausdinti_statistika, trinti_eilute, \
    issaugoti_duomenis


def main():
    pajamos = []
    islaidos = []

    while True:
        print("\nMeniu:")
        print("1. Ivesti pajamas")
        print("2. Ivesti išlaidas")
        print("3. Rodyti pajamu eilutes")
        print("4. Rodyti išlaidu eilutes")
        print("5. Rodyti statistika")
        print("6. Istrinti pajamu eile")
        print("7. Istrinti islaidu eile")
        print("8. Issaugoti duomenis pickle")
        print("q. Iseiti")

        pasirinkimas = input("Vartotojo pasirinkimas: ").strip().lower()

        if pasirinkimas == '1':
            ivesti_pajamas(pajamos)
        elif pasirinkimas == '2':
            ivesti_islaidas(islaidos)
        elif pasirinkimas == '3':
            spausdinti_eiles(pajamos, "Pajamos")
        elif pasirinkimas == '4':
            spausdinti_eiles(islaidos, "Islaidos")
        elif pasirinkimas == '5':
            spausdinti_statistika(pajamos, islaidos)
        elif pasirinkimas == '6':
            trinti_eilute(pajamos, "Pajamos")
        elif pasirinkimas == '7':
            trinti_eilute(islaidos, "Islaidos")
        elif pasirinkimas == '8':
            issaugoti_duomenis(islaidos + pajamos, "Isaugoti duoemnys")
        elif pasirinkimas == 'q':
            print("Programa baigta.")
            break
        else:
            print("Netinkamas pasirinkimas")


if __name__ == "__main__":
    main()
