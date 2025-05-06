document.addEventListener('DOMContentLoaded', function() {
    loadTemperature();
});

async function loadTemperature(){
    const response = await fetch('/realtime-weather');
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

        const valueOfWindSpeed = document.createTextNode(City.current.wind_kph + " km/h");
        windContainer.appendChild(valueOfWindSpeed);
        windContainer.appendChild(imgW);

        container.appendChild(temperatureContainer);
        container.appendChild(windContainer);
    });
}