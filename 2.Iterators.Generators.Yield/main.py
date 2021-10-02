import json

read_file = 'countries.json'


class WikiLinkFromFile:

    def __init__(self, json_file_r, file_w):
        self.json_read = json.load(open(json_file_r, encoding='utf-8'))
        self.file_write = open(file_w, 'w', encoding='utf-8')

    def __iter__(self):
        wiki_url = 'https://en.wikipedia.org/wiki/'
        for item in self.json_read:
            country = item['name']['common']
            country_for_link = country.replace(' ', '_')
            result = f'{country} - {wiki_url + country_for_link}\n'
            self.file_write.writelines(result)
            yield result


if __name__ == '__main__':

    country = WikiLinkFromFile(read_file, 'country_wikilink.txt')
    for item in country:
        print(item)
