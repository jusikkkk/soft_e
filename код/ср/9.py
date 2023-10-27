from datetime import datetime as dati
from datetime import timedelta as dt

def main():
    print(
        f"Сегодня {dati.today().date()}."
        f"День недели - {dati.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    today = dati.today()
    result = today + dt(days=n)
    print(
        f"Через {n} дней будет {result.date()}."
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
