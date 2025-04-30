document.addEventListener('DOMContentLoaded', function() {
    loadTemperature();
});

async function loadTemperature(){
    const response = await fetch('/realtime-weather');
    const data = await response.json();
    data.forEach(City => {
        const id = City.location.name
        const container = document.getElementById(id);
        const img = document.createElement('img');
        img.style.width = '64px';
        img.style.height = '64px';
        img.src = City.current.condition.icon;
        container.appendChild(img);
    });
}