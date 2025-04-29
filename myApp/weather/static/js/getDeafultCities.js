document.addEventListener('DOMContentLoaded', function() {
    loadTemperature();
});

async function loadTemperature(){
    const response = await fetch('/realtime-weather');
    const data = await response.json();
    data.forEach(City => {
        console.log(City.location.name)
    });
}