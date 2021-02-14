import requests
import json

# the method fetches the weather data and returns the result

def fetch_data(zip=None, city=None):

    # base url for fetching the weather

    baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    # api id for the site

    apiid = "6dbb527c09899fc9e75ee6ef74b101a9"

    # check if the user gave the zip code or the city name

    if zip is not None:

        # us at the end id for usa country , change it as required

        baseUrl += "?zip="+str(zip)+",us"

    else:

        baseUrl += "?q="+str(city)+",us"

    # finally append the api id

    baseUrl += "&appid="+str(apiid)

    # make get requets using requests module

    r = requests.get(baseUrl)

    # return the response

    return r

#this method shows the result in readale format,

def showResult(resp):

    #this means request was successful

    if resp.status_code == 200:

        data= resp.json()

        print(data['name'])

        print(f"""{data['name']} Weather Forecast:

        There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speed']}.

        Visibility will be {data['visibility']}.

        Min. Temp will be {data['main']['temp_min']} and max will be {data['main']['temp_max']}.

        """)

    else:

        print("Request Failed, Try Again Error Code : ",resp.status_code)

#main method , main driver code of the program,

def main():

    #until the user exits keep running the code

    while True:

        #show the user choices

        inp =int(input("Your options :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

        if inp == 1:

            #ask for zip code

            try:

                queryData=int(input("Enter zip code : "))

                #make call to fetch fetch_data

                resp= fetch_data(queryData,None)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp == 2:

            try:

                queryData = input("Enter city name : ")

                #make call to fetch fetch_data

                resp= fetch_data(None,queryData)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp==3:

            break

        else:

            print("Invalid Choice..\n")




if __name__=="__main__":

    #call the main method

    main()
