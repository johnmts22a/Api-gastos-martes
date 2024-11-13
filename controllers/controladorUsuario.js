import { BuscarUsuario,RegistrarUsuario } from "../services/serviciosUsuario.js"

//Recoger los datos de un formularios utilizando JS

//1. A cada input, select, area del form le creo una variable. Crear una variable asociada al id del HTML

let nombreUsuario = document.getElementById("nombre") 
let fechaNacimientoUsuario = document.getElementById("fechaNacimiento")
let ubicacionUsuario = document.getElementById("ubicacion")
let metaAhorroUsuario = document.getElementById("metaAhorro")

//2. Se crea una variable para asociarla con el botón del formulario.

let botonRegistro = document.getElementById("registro")

//3. Se detecta el click del botón del formulario.

botonRegistro.addEventListener("click", function(evento){
    evento.preventDefault()

    //4. Se construye un objeto con los datos del formulario.

    let objetoEnvioDatosUsuario = {
        nombres: nombreUsuario.value,
        fechaNacimiento: fechaNacimientoUsuario.value,
        ubicacion: ubicacionUsuario.value,
        metaAhorro: metaAhorroUsuario.value
    }

    RegistrarUsuario(objetoEnvioDatosUsuario)

    Swal.fire({
        title: "En hora buena",
        text: "Has registrado un usuario",
        icon: "success"
      });

    limpiarDatos()
})

//Objetivo: renderizar datos que vienen del backend.

//1. Se queman los datos.

//Llamando a la función que va al api a buscar usuarios

BuscarUsuario().then(function(respuesta){

    //2. Recorrer el arreglo e datos del backend.

    let fila = document.getElementById("fila")
    respuesta.forEach(function(usuario){
    
        //2.1 Traversing
        let columna = document.createElement("div")
        columna.classList.add("col")

        let tarjeta = document.createElement("div")
        tarjeta.classList.add("card","h-100","p-5","shadow")

        let nombreCard = document.createElement("h3")
        nombreCard.textContent = usuario.nombres

        //2.2 Se asocian las creaciones
        tarjeta.appendChild(nombreCard)
        columna.appendChild(tarjeta)
        fila.appendChild(columna)

    })
})

function limpiarDatos(){
    nombreUsuario.value = ""
    fechaNacimientoUsuario.value = ""
    ubicacionUsuario.value = ""
    metaAhorroUsuario.value = ""
    nombreUsuario.focus
}

