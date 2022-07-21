WINOWS = 12
wiek_psa = 23


def getDogAge():
    return wiek_psa


print(f"Wiek psa to {getDogAge()}, a okien mam {WINOWS}")


def isDeviceConnected(status):
    status_int = int(status)

    # 1 = polaczony
    # 2 = w takcie laczenia
    # 3 = nie polaczony

    if status_int == 1:
        return "polaczony"
    elif status_int == 2:
        return "w takcie laczenia"
    return "nie polaczony"

    # elif status_polaczenia != 1 or status_polaczenia != 2 or status_polaczenia != 3:
    #     return "error"
    # return "error"


def main():
    # 1 = polaczony
    # 2 = w takcie laczenia
    # 3 = nie polaczony

    user_input = input()
    print("Urządzenie jest " + isDeviceConnected(user_input) + " z internetem")

    user_input2 = input()
    print("Urządzenie 2 jest " +
          isDeviceConnected(user_input2) + " z internetem")


main()
