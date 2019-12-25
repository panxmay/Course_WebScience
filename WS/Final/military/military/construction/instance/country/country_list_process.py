
def extract_chinese(word):
    country = ""
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            country = country + ch
    return country

def load_country(country_list):
    with open('D:\military\military\data\country\\raw_country_list.txt', 'r', encoding='utf-8') as file_obj:
        str = file_obj.readline()
        while str != "":
            country_list.append(extract_chinese(str))
            str = file_obj.readline()
    file_obj.close()
    with open('D:\military\military\data\country\country_list.txt', 'a', encoding='utf-8') as file_obj:
        for country in country_list:
            file_obj.write(country + '\n')
    file_obj.close()
def main():
    country_list = []
    load_country(country_list)

if __name__ == "__main__":
    main()



