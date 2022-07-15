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

//Validar contacto

const formulario = document.getElementById('form')
const inputs = document.querySelectorAll('#form input')
const tarea = document.querySelectorAll('#form textarea')
const select = document.querySelectorAll('#form select')


//Expresiones modelo
const expresiones = {
  rut : /^[0-9]+\-[0-9kK]$/,
  nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
  telefono: /^\d{8,9}$/, // 8 o 9 numeros.
  comentario: /^[a-zA-ZÀ-ÿ\s]{0,120}$/
}
//Estado de los campos (valido o invalido)
const valides = {
    rut: false,
    nombre: false,
    correo: false,
    numero: false,
    //password: false,
    comentario : false,
    check: false,
  }
//validacion de formulario
  const validarForm = (event) => {
    switch(event.target.name) {
      case "rut":
          validarInput(expresiones.rut, event.target, event.target.name);
      break;
      case "nombre":
          validarInput(expresiones.nombre, event.target, event.target.name);
      break;
      case "correo":
        validarInput(expresiones.correo, event.target, event.target.name);
      break;
      case "numero":
          validarInput(expresiones.telefono, event.target, event.target.name);
      break;
      case "comentario":
        validarInput(expresiones.comentario, event.target, event.target.name);
      break;
      case "check":
        validarCheck();
      break;
  }
}
//Validacion de campos
const validarInput = (expresiones, input , cuadro) => {
    if(expresiones.test(input.value)){
      document.getElementById(cuadro).classList.add('is-valid');
      document.getElementById(cuadro).classList.remove('is-invalid');
      valides[cuadro] = true;
    }else {
      document.getElementById(cuadro).classList.add('is-invalid');
      document.getElementById(cuadro).classList.remove('is-valid');
      valides[cuadro] = false;
    }
  }
//Validacion de checkbox
  const validarCheck = () =>{
    const check = form.check.checked
    if(check ){
      document.getElementById('invalidCheck').classList.add('is-valid');
      document.getElementById('invalidCheck').classList.remove('is-invalid');
      valides['check'] = true;
    }else{
      document.getElementById('invalidCheck').classList.add('is-invalid');
      document.getElementById('invalidCheck').classList.remove('is-valid');
      valides['check'] = false;
    }
  }
//Guardar datos y alerta
  const alertaInfo = () =>{
    const rt = document.getElementById('rut').value
    const nom = document.getElementById('nombre').value
    const cor = document.getElementById('correo').value
    const num = document.getElementById('numero').value
    const comen = document.getElementById('comentario').value
    const sel = form.select.value
  
    alert('Informacion registrada\nRut:' +rt+ '\nNombre:'+nom+
        '\nCorreo: '+cor+'\nNumero: '+num+ '\nComentario: '+comen+
        '\nOpcion Seleccionada: '+sel
    ); 
  }

//Evita el enviar datos incompletos

(function () {
    formulario.addEventListener('submit', (event) => {
    
      if(valides.select && valides.nombre && valides.apellido && valides.numero 
        && valides.rut && valides.direccion && valides.correo && valides.comentario && valides.check ){
        }
        else{
          event.preventDefault();
        }
      } 
    );
  })();