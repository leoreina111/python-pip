import mod
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  country_input = input('Digite el pais: ')
  result = mod.get_population_by_country(data,country_input)

  if len(result) > 0:
    country = result[0]
    labels,values = mod.get_population(country)
    charts.generate_bar_char(labels,values)

def run02():
  country = input('Type Country => ')

  #data = read_csv.read_csv('data.csv')
  #labels,values = mod.world_poulation_percentage(data)
  #charts.generate_pie_char(labels,values,country)

  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_char(countries, percentages, country)
  
  result = mod.get_population_by_country(data, country)

  if len(result) > 0:
    country_dict = result[0]
    labels, values = mod.get_population(country_dict)
    charts.generate_bar_char(labels, values, country)

if __name__ == '__main__':
  run02()