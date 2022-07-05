function darkMode() {
    var element = document.body;
    var content = document.getElementById("DarkModetext");
    element.className = "dark-mode";
    content.innerText = "Dark Mode is ON";
  }
  function lightMode() {
    var element = document.body;
    var content = document.getElementById("DarkModetext");
    element.className = "light-mode";
    content.innerText = "Dark Mode is OFF";
  }

$(document).ready(function() {
    var url = `https://chilealerta.com/api/query/?user=tomas&select=ultimos_sismos_chilehttps://chilealerta.com/api/query/?user=tomas&select=ultimos_sismos&limit=1&country=Chile`;
    $.getJSON(url,function(data) {
        if(data.ultimos_sismos_Chile[0] != null) {
            $('#fecha').text(data.ultimos_sismos_Chile[0].local_time);
            $('#referencia').text(data.ultimos_sismos_Chile[0].reference);
            $('#magnitud').text(data.ultimos_sismos_Chile[0].magnitude);
        }
        else{
            Swal.fire({
                title: 'Error',
                text: 'en estos momentos estamos caidos, vuelva en otro momento',
                icon: 'error',
                confirmButtonText: 'Continuar'
            })
        }
    },'json').fail(function() {
        Swal.fire({
            title: 'Error',
            text: 'la API no funciona en estos momentos',
            icon: 'error',
            confirmButtonText: 'Continuar'
        })
    });
});

$(document).ready(function(){
    var ubicacion = navigator.geolocation.getCurrentPosition(function(info){
        var latitud = info.coords.latitude;
        var longitud = info.coords.longitude;

        $.getJSON(`https://api.openweathermap.org/data/2.5/weather?lat=${latitud}&lon=${longitud}&lang=es&units=metric&appid=68a417ccd8493e33698b951ac65f49c4`, function(data){
            console.log(data)
            var html = `<h7 id="ciudad" class="text-capitalize">${data.name}, Siglas del pais: (${data.sys.country}) Clima: ${data.weather[0].description}, <h7>
                        <h7 id="temperatura" class="text-capitalize"> Temperatura: ${data.main.temp} C°, humedad: ${data.main.humidity}% <h7>`;
            $('#info-clima').html(html);
        },'json').fail(function(){
            Swal.fire({
                title: 'Error',
                title: 'En estos momentos la api no funciona',
                icon: 'error',
                confirmButtonText: 'Continuar'
              });
        })
    })
})

function findMe(){
    var output = document.getElementById('map');
    // Verificar si soporta geolocalizacion
    if (navigator.geolocation) {
        output.innerHTML = "<p>Tu navegador soporta Geolocalizacion</p>";
    }else{
        output.innerHTML = "<p>Tu navegador no soporta Geolocalizacion</p>";
    }
    //Obtenemos latitud y longitud
    function localizacion(posicion){
        var latitude = posicion.coords.latitude;
        var longitude = posicion.coords.longitude;
        var imgURL = "https://maps.googleapis.com/maps/api/staticmap?center="+latitude+","+longitude+"&size=150x150&markers=color:red%7C"+latitude+","+longitude+"&key=AIzaSyD1IH_7XELVMY_fFNucrU5MUKAuw-xEpbI";
        output.innerHTML ="<img src='"+imgURL+"'>";
    }
    function error(){
        output.innerHTML = "<p>No se pudo obtener tu ubicacion</p>";
    }
    navigator.geolocation.getCurrentPosition(localizacion,error);
}

let mostrarFecha = document.getElementById('fecha1');
let mostrarReloj = document.getElementById('reloj');

let fecha = new Date();

let diaSemana = ['Domingo','Lunes', 'Martes','Miércoles','Jueves','Viernes','Sábado'];

let mesAnyo = ['Enero','Febrero', 'Marzo','abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];

mostrarFecha.innerHTML = `${diaSemana[fecha.getDay()]}, ${fecha.getDate()} de ${mesAnyo[fecha.getMonth()]} de ${fecha.getFullYear()}`;

setInterval(()=>{
  let hora = new Date();
  mostrarReloj.innerHTML = hora.toLocaleTimeString();
},1000);