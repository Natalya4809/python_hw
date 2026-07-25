from address import Address
from mailing import Mailing

address_from = Address("454015", "Челябинск",
                       "Молдавская", "5", "40")
address_to = Address("123786", "Воронеж",
                     "Лизюкова", "7", "34")
mailing = Mailing(to_address=address_to, from_address=address_from,
                  track="RU54637383839", cost=5465)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment},"
      f"в {mailing.to_address.index}, {mailing.to_address.city},"
      f" {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment},"
      f"стоимость {mailing.cost} рублей")
