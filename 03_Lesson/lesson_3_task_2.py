from smartphone import Smartphone

katalog = [
     Smartphone(brand = "realmi",model = "14 Pro 5G", number = "+79054851231"),
     Smartphone(brand = "realmi",model = "11 Pro ", number = "+79089992424"),
     Smartphone(brand = "Apple",model = "iPhone 17 Pro Max", number = "+79221004563"),
     Smartphone(brand = "Samsung",model = "Galaxy S26 Ultra", number = "+79516782222"),
     Smartphone(brand = "Huawei",model = "Pura 80 Ultra", number = "+79023376545"),
     Smartphone(brand = "Honor",model = "Magic 8 Pro", number = "+79824563767"),
    ]
for phone in katalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")



