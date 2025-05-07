document.addEventListener('DOMContentLoaded', function() {
    loadTemperature();
});

async function loadTemperature(){
    const response = await fetch('/realtime-weather');
    const forecastResponse = await fetch('/forecast-weather');
    const forecastData = await forecastResponse.json();
    const data = await response.json();
    data.forEach(City => {
        const id = City.location.name;
        const container = document.getElementById(id);
        const temperatureContainer = document.createElement('div');
        const windContainer = document.createElement('div');
        const img = document.createElement('img');
        temperatureContainer.setAttribute('class','temperatureContainer');
        windContainer.setAttribute('class','windContainer');

        img.style.width = '128px';
        img.style.height = '128px';
        img.src = City.current.condition.icon;
        img.setAttribute('class','weatherImage');

        const valueOfTemperature = document.createTextNode(City.current.temp_c + " °C");
        temperatureContainer.appendChild(valueOfTemperature);
        temperatureContainer.appendChild(img);

        const imgW = document.createElement('img');
        imgW.style.width = '100px';
        imgW.style.height = '100px';
        imgW.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXdpbmQtaWNvbiBsdWNpZGUtd2luZCI+PHBhdGggZD0iTTEyLjggMTkuNkEyIDIgMCAxIDAgMTQgMTZIMiIvPjxwYXRoIGQ9Ik0xNy41IDhhMi41IDIuNSAwIDEgMSAyIDRIMiIvPjxwYXRoIGQ9Ik05LjggNC40QTIgMiAwIDEgMSAxMSA4SDIiLz48L3N2Zz4=';
        imgW.setAttribute('class','weatherImage');

        const valueOfWindSpeed = document.createTextNode(City.current.wind_kph + " kph");
        windContainer.appendChild(valueOfWindSpeed);
        windContainer.appendChild(imgW);

        const testContainer = document.createElement('div');
        testContainer.setAttribute('class','forecastContainer');

        const forecastContainer = document.createElement('div');
        forecastContainer.setAttribute('class','forecastContainer');


        forecastData.forEach(a=>{
            if(a.location == id){

                
                a.forecast.forEach(day=>{
                    const col = document.createElement('div');
                    col.setAttribute('class','col');

                    const dateDiv = document.createElement('div');
                    dateDiv.setAttribute('class','dateDiv');
                    const date = document.createTextNode(day.date);
                    dateDiv.appendChild(date);

                    const tempDiv = document.createElement('div');
                    const tempForecast_c = document.createTextNode(day.temp + "°C");
                    tempDiv.appendChild(tempForecast_c);

                    const windDiv = document.createElement('div');
                    const windForecast = document.createTextNode(day.windMAX + "kph");
                    windDiv.appendChild(windForecast);

                    const imgDiv = document.createElement('div');
                    const imgForecast = document.createElement('img');
                    imgForecast.style.width = '50px';
                    imgForecast.style.height = '50px';
                    imgForecast.src = day.weatherIcon;
                    imgDiv.appendChild(imgForecast);

                    col.appendChild(dateDiv);
                    col.appendChild(tempDiv);
                    col.appendChild(windDiv);
                    col.appendChild(imgDiv);
                    forecastContainer.appendChild(col);
                })
                }
            }
        );
        container.appendChild(temperatureContainer);
        container.appendChild(windContainer);
        container.appendChild(forecastContainer);

        // let col1 = document.createElement('div');
        // col1.setAttribute('class','col');
        // let text1 = document.createTextNode("MON");
        // col1.appendChild(text1);
        // testContainer.appendChild(col1);

        // let col2 = document.createElement('div');
        // col2.setAttribute('class','col');
        // let text2 = document.createTextNode("MON");
        // col2.appendChild(text2);
        // testContainer.appendChild(col2);

        // let col3 = document.createElement('div');
        // col3.setAttribute('class','col');
        // let text3 = document.createTextNode("MON");
        // col3.appendChild(text3);
        // testContainer.appendChild(col3);

        // let col4 = document.createElement('div');
        // col4.setAttribute('class','col');
        // let text4 = document.createTextNode("MON");
        // col4.appendChild(text4);
        // testContainer.appendChild(col4);

        // let col5 = document.createElement('div');
        // col5.setAttribute('class','col');
        // let text5 = document.createTextNode("MON");
        // col5.appendChild(text5);
        // testContainer.appendChild(col5);

        // let col6 = document.createElement('div');
        // col6.setAttribute('class','col');
        // let text6 = document.createTextNode("MON");
        // col6.appendChild(text6);
        // testContainer.appendChild(col6);

        // let col7 = document.createElement('div');
        // col7.setAttribute('class','col');
        // let text7 = document.createTextNode("MON");
        // col7.appendChild(text7);
        // testContainer.appendChild(col7);
        
    });
}