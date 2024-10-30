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

    console.log(objetoEnvioDatosUsuario)

    /*Swal.fire({
        title: "Good job!",
        text: "You clicked the button!",
        icon: "success"
      });*/
})

//Objetivo: renderizar datos que vienen del backend.

//1. Se queman los datos. 

let usuarios = [
    {
        id:20,
        nombres:"John Martinez",
        metaAhorro:20000000
    },//(mock)
    {
        id:30,
        nombres:"César Cardona",
        metaAhorro:15000000
    },
    {
        id:45,
        nombres:"Luisa Sepúlveda",
        metaAhorro:25000000
    }
]

//2. Recorrer el arreglo e datos del backend.

let fila = document.getElementById("fila")
usuarios.forEach(function(usuario){
    console.log(usuario)

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