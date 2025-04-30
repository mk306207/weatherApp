document.addEventListener('DOMContentLoaded', function() {
    loadTemperature();
});

async function loadTemperature(){
    const response = await fetch('/realtime-weather');
    const data = await response.json();
    data.forEach(City => {
        const id = City.location.name;
        const container = document.getElementById(id);
        const img = document.createElement('img');
        const textContainer = document.createElement('div');
        textContainer.setAttribute('class','textContainer');
        const imgContainer = document.createElement('div');
        imgContainer.setAttribute('class','imageContainer');

        img.style.width = '128px';
        img.style.height = '128px';
        img.src = City.current.condition.icon;
        img.setAttribute('class','weatherImage');
        
        const temp = document.createElement('P');
        temp.setAttribute('class','myText');
        const valueOfTemperature = document.createTextNode(City.current.temp_c + " °C");
        temp.appendChild(valueOfTemperature);

        const wind = document.createElement('P');
        wind.setAttribute('class','myText');
        const valueOfWindSpeed = document.createTextNode(City.current.wind_kph + " km/h");
        wind.appendChild(valueOfWindSpeed);

        textContainer.appendChild(temp);
        textContainer.appendChild(wind);

        container.appendChild(img);
        container.appendChild(textContainer);
    });
}