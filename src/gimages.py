from bs4 import BeautifulSoup
import requests

def get_google_img(query):
    url = "https://www.google.ca/search?q=" + query  + "&tbm=isch&hl=en&chips=q:python,g_1:logo:Ex8DYjnWxFQ%3D,g_1:transparent:cULjZ5VPkXE%3D&authuser=0&sa=X&ved=2ahUKEwjksN7r6q3uAhUHHjQIHdkcBPgQ4lYoAHoECAEQGw&biw=1886&bih=953#imgrc=ZlaIuw2nTjGseM"
    print(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup.findAll("img", class_="t0fcAb")[0]["src"]

if __name__ == '__main__':
    print(get_google_img("python lang icon png"))
