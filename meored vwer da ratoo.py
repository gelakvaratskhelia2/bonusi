# class Patient:
#     def __init__(self, personal_number, name, birth_certificate, doctor):
#         self.personal_number = personal_number
#         self.name = name
#         self.birth_certificate = birth_certificate
#         self.doctor = doctor
#
#     def __str__(self):
#         return f"პირადი ნომერი: {self.personal_number}, სახელი: {self.name}, დაავადების დასახელება: {self.birth_certificate}, მკურნალი ექიმი: {self.doctor}"
#
#     def diagnose(self, birth_certificate, doctor=None):
#         if doctor is None:
#             print("ექიმის მიმაგრება ვერ მოხდება")
#             return
#
#         if doctor.get_patient_count() < 20:
#             doctor.add_patient(self)
#             print(f"ექიმმა {self.name}-ს დაამაგრა დიაგნოზი")
#         else:
#             print("ექიმის მიმაგრება ვერ მოხდება")
#
#
# class Doctor:
#     def __init__(self, name, specialization):
#         self.name = name
#         self.specialization = specialization
#         self.patients = []
#
#     def add_patient(self, patient):
#         self.patients.append(patient)
#
#     def get_patient_count(self):
#         return len(self.patients)
#
#
# # კლასის ტესტირება
# doctor = Doctor("დოქტორი განაკურდია", "პედიატრია")
# patient = Patient("123456789", "პატიენტი", "დაავადება", doctor)
# print(patient)
# patient.diagnose("დაავადება", doctor)
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/crypto/"
# Send a GET request to the specified URL
response = requests.get(url)
print(response.status_code)
content = response.text
print(response.text)
soup = BeautifulSoup(content, 'html.parser')

# btc_row = soup.find('tr', {'data-reactid': '52'}).find_parent('table').find_all('tr')[1]

body = soup.find("body")
wrapper = body.find("div", id='app')
div = wrapper.find("div")
render = div.find("div", {"id": "render-target-default"})
bgc = render.find("div")
lead = bgc.find("div", {"id": "YDC-Lead"})
stack = lead.find("div", {"id": "YDC-Lead-Stack"})
composite = stack.find("div", {"id": "YDC-Lead-Stack-Composite"})
div_2 = composite.find_all("div")[5]
res = div_2.find("div", {"id": "mrt-node-Lead-5-ScreenerResults"})
res_2 = res.find("section", {"id": "screener-results"})
table = res_2.find("div")
pos = table.find("div", {"class": "Pos(r)"})
div_3 = pos.find("div")
table_2 = div_3.find("table", _class="W(100%)")
tbody = table_2.find("tbody")
bt_row = tbody.find("tr", {"class": "simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor) "})
bt_name = bt_row.find('td', {'aria-label': 'Name'}).text
bt_price = bt_row.find('td', {'aria-label': 'Price (Intraday)'}).find('span').text
bt_change = bt_row.find('td', {'aria-label': 'Change'}).text
bt_percent = bt_row.find('td', {'aria-label': '% Change'}).text
bt_market = bt_row.find('td', {'aria-label': 'Market Cap'}).text

print("Bitcoinis saxeli:", bt_name)
print("Bitcoinis fasi:", bt_price)
print("Bitcoinis gadacvla:", bt_change)
print("Bitcoinis % gadacvla:", bt_percent)
print("Bitcoin Market Cap:", bt_market)