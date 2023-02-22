from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def country_details():
    if request.method == 'POST':
        countryy = request.form.get('country')
        comp_api_link = f"https://restcountries.com/v3.1/name/{countryy}?fullText=true"
        api_link = requests.get(comp_api_link)
        data = api_link.json()

        official = (data[0]['name']['official'])
        reg = (data[0]['region'])
        subr = (data[0]['subregion'])
        cap = (data[0]['capital'][0])
        popu = (data[0]['population'])
        countryarea = (data[0]['area'])
        tmzone = (data[0]['timezones'][0])
        lat = (data[0]['latlng'][0])
        long = (data[0]['latlng'][1])
        flags = (data[0]['flags'])
        f = flags.get('png')
        lang = (data[0]['languages'])
        val = lang.values()
        cur = (data[0]['currencies'])

        for key, values in cur.items():
            final = (cur.get(key))
            # print(type(final))
            a = final['name']
            b = final['symbol']

            return render_template('mainhome.html',official_ = official, reg_ = reg, subr_ = subr,cap_ = cap,popu_ = popu, countryarea_ = countryarea, tmzone_ = tmzone, lat_ = lat,long_ = long,f_ = f,val_=val,cur_ = cur,a_=a,b_=b)
    return render_template('mainhome.html')

if __name__ == '__main__':
    app.run(debug=True)