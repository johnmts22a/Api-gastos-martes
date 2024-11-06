export async function BuscarUsuario(){

    //1. Para donde voy?, URL del servicio.

    const url = "http://localhost:8000/usuario"

    //2. Qué va a hacer?, configuración de la petición.

    let peticion = {
        method:"GET"
    }

    //3. Vaya pues. Consuma el API.

    let respuestaInicial = await fetch(url,peticion)
    let respuestaFinal = await respuestaInicial.json()

    return(respuestaFinal)
}

export async function RegistrarUsuario(datosUsuario){

    const url = "http://localhost:8000/usuario"

    let peticion = {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(datosUsuario)
    }

    let respuestaInicial = await fetch(url,peticion)
    let respuestaFinal = await respuestaInicial.json()

    console.log(respuestaFinal)
}