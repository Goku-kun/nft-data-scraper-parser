import bs4
import csv
from bs4 import BeautifulSoup


def formatter(string):
    string = string.replace(
        "\\n", "").replace("', '", "").replace("""'="" '""", "").replace(',=""', "").replace("""="" '""", "").replace("',", "").replace('=""', "")
    return string


def get_td(string):
    return BeautifulSoup(string, 'html.parser').find_all("td")


def parse_first_td(td):
    soup = BeautifulSoup(td, "html.parser")
    value0 = soup.get_text()
    value1 = soup.a["href"]
    return value0, value1


def parse_second_td(td):
    soup = BeautifulSoup(td, "html.parser")
    value2 = soup.get_text()
    value3 = soup.a["href"]
    return value2, value3


def parse_third_td(td):
    soup = BeautifulSoup(td, 'html.parser')
    return soup.get_text()


def parse_fourth_td(td):
    soup = BeautifulSoup(td, 'html.parser')
    return soup.get_text()


def parse_fifth_td(td):
    soup = BeautifulSoup(td, 'html.parser')
    return soup.get_text()


def parse_sixth_td(td):
    soup = BeautifulSoup(td, 'html.parser')
    a = soup.a
    return a.get('data-original-title'), a.get('href')


def parse_seventh_td(td):
    soup = BeautifulSoup(td, 'html.parser')
    a = soup.a
    return a.get('data-original-title'), a.get('href')


if __name__ == "__main__":

    with open("./nft.html", "r+", encoding="utf-8") as f:
        soup = BeautifulSoup(str(f.readlines()), 'html.parser')
        data = soup.find_all("tr", attrs={"role": "row"})
        data = data[2:]

    rows = []
    for value in data:
        rows.append(get_td(formatter(str(value))))

    filename = "data.csv"
    fields = ["sold time", "time since transaction link", "nft", "nft link",
              "price", "usd", "attributes", "seller", "seller link", "buyer", "buyer link"]

    with open(filename, 'w', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for row in rows:
            if (len(row) == 0):
                continue
            sold_time, time_since_last_transaction_link = parse_first_td(
                str(row[1]))
            nft, nft_link = parse_second_td(str(row[2]))
            price = parse_third_td(str(row[3]))
            usd = parse_fourth_td(str(row[4]))
            attributes = parse_fifth_td(str(row[5]))
            seller, seller_link = parse_sixth_td(str(row[6]))
            buyer, buyer_link = parse_seventh_td(str(row[7]))
            csvwriter.writerow([sold_time, time_since_last_transaction_link, nft,
                               nft_link, price, usd, attributes, seller, seller_link, buyer, buyer_link])

        csvfile.close()
