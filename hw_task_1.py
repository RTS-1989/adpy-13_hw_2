import json

class Country_iterator:

    def __init__(self, start, end, from_file_path):

        self.start = start
        self.end = end
        self.current = start - 1
        self.from_file_path = from_file_path
        
    def __iter__(self):

        return self
    
    def __next__(self):

        self.current += 1
        
        if self.current == self.end:
            raise StopIteration
        info_list = Country_iterator.get_countries(self.from_file_path)[self.current]
        result = {'country_name': info_list, 'link': f'https://en.wikipedia.org/wiki/{info_list}'}
       
        return result
        
    @classmethod
    def get_countries(cls, file_path):

        with open(file_path, encoding='utf8') as fi:

            countries_list = []
            countries_info = json.load(fi)

            for country in countries_info:
                countries_list.append(country['name']['common'])
                
            return countries_list

    @classmethod
    def write_to_file(cls, file_path, result_list):

        with open(file_path, 'a', encoding='utf8') as fo:
            json.dump(result_list, fo, ensure_ascii=False, indent=4)

if __name__ == '__main__':

    result_list = []
    for item in Country_iterator(0, len(Country_iterator.get_countries('countries.json')), 'countries.json'):
        result_list.append(item)
    Country_iterator.write_to_file('country_info.json', result_list)
     
