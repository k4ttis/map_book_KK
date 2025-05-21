from geocoder import location


class User:
    def __init__(self,name,surname,location,post):
        self.name=name
        self.surname=surname
        self.location=location
        self.post=post
        self.get_coordinates=self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]








user_01=User(name="Jhon",surname="Konrad",location="Kraków",post="Konrad")
user_02=User(name="JON",surname="KON",location="Warszawa",post="Konrad")


print(user_01.name,user_01.surname,user_01.location,user_01.post)
print(user_02.name,user_02.surname,user_02.location,user_02.post)











