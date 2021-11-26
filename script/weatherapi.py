import pandas as pd
import requests, json, time
from datetime import date, timedelta

def api_request(city, day):

    url = "https://weatherapi-com.p.rapidapi.com/history.json"

    querystring = {"q":"{0}".format(city),"dt":"{0}".format(day),"lang":"pt"}

    print(querystring)

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "addyourkey"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = pd.DataFrame.from_records(json.loads(response.content)['forecast']['forecastday'][0]['hour'])
    
    data['city'] = [city]*len(data)

    print(data.head())

    return data

def data_request(file_path):

    data = pd.DataFrame()

    month  = {

    'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4, 'Mai': 5, 'Jun': 6, 'Jul': 7, 'Ago': 8, 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12

    }

    with open(file_path, encoding='utf-8') as f:
        json_input = json.load(f)

    for parameters in json_input:

        print(parameters)
        
        date_range = pd.date_range(
                    date(int(parameters['Data início'].split('/')[2]),
                        int(month['{0}'.format(parameters['Data início'].split('/')[1])]),
                        int(parameters['Data início'].split('/')[0])),
                    date(int(parameters['Data fim'].split('/')[2]),
                        int(month['{0}'.format(parameters['Data fim'].split('/')[1])]),
                        int(parameters['Data fim'].split('/')[0]))-timedelta(days=1), freq='d'
                )
        
        dates = [str(x) for x in date_range.date]
        
        dates.append(parameters['Data fim'].split('/')[2]+'-'+str(month['{0}'.format(parameters['Data fim'].split('/')[1])])+'-'+parameters['Data fim'].split('/')[0])
        
        for city in parameters['Cidade'].split(','):
            
            for day in dates:
                
                try:

                    data = data.append(api_request(city, day))
                                    
                except Exception as e:
                    
                    print (e.__class__, "occured.")
                
                time.sleep(2.0)

    data.to_csv('output.csv', index=False)

    return None

if __name__ == "__main__":
    data_request("C:\\your\\file\\path\\dadosClimaticos.json")