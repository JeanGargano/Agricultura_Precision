// document.getElementById('fetchData').addEventListener('click', function() {
//     const resultDiv = document.getElementById('result');
//     resultDiv.style.display = 'flex'; // Mostrar div de resultados
// });

// document.getElementById('fetchData2').addEventListener('click', function() {
//     const resultDiv2 = document.getElementById('result2');
//     resultDiv2.style.display = 'flex'; // Mostrar div de recomendaciones
// });

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetchData').addEventListener('click', function() {
        // Simular un JSON de respuesta
        let res ='';
        const jsonResponse = {
            mensaje: "Hola mundo, esta es una cadena de prueba más larga que simula una respuesta JSON desde un servidor. El propósito de este ejemplo es ilustrar cómo manejar datos más extensos y complejos, incluyendo múltiples campos como nombre, edad, y detalles adicionales sobre el usuario.",
            estado: "éxito",
            usuario: {
                nombre: "Juan Pérez",
                edad: 30,
                email: "juan.perez@example.com",
                intereses: ["programación", "música", "viajes"],
                detalles: {
                    direccion: {
                        calle: "123 Calle Falsa",
                        ciudad: "Ciudad Ejemplo",
                        pais: "Colombia"
                    },
                    telefono: "123-456-7890"
                }
            },
            fecha: "2024-09-29",
            version: "1.0.0"
        };
        
        // Convertir el objeto JSON a una cadena para mostrarlo
        // const jsonString = JSON.stringify(jsonResponse, null, 2);

        res += "Mensaje: " + jsonResponse.mensaje + "\n\n"+ "Estado: " + jsonResponse.estado + "\n" + "Usuario: " + jsonResponse.usuario.nombre + "\n" + "Edad: " + jsonResponse.usuario.edad + "\n" + "Email: " + jsonResponse.usuario.email + "\n" + "Intereses: " + jsonResponse.usuario.intereses + "\n" + "Detalles: " + jsonResponse.usuario.detalles.direccion.calle + "\n" + "Ciudad: " + jsonResponse.usuario.detalles.direccion.ciudad + "\n" + "País: " + jsonResponse.usuario.detalles.direccion.pais + "\n" + "Teléfono: " + jsonResponse.usuario.detalles.telefono + "\n" + "Fecha: " + jsonResponse.fecha + "\n" + "Versión: " + jsonResponse.version;
        
        const cadenaConSaltosHTML = res.replace(/\n/g, "<br>");
        // Mostrar el JSON en el elemento con id 'result'
        document.getElementById('result').innerHTML = cadenaConSaltosHTML;
    });
});
// document.getElementById('fetchData').addEventListener('click', () => {
//     fetch('http://127.0.0.1:5000/api/data') // Cambiar el puerto a conveniencia
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('result').textContent = JSON.stringify(data);
//         })
//         .catch(error => console.error('Error:', error));
// });

// document.getElementById('fetchData2').addEventListener('click', () => {
//     fetch('http://127.0.0.1:5000/api/data2') // Cambiar el puerto a conveniencia
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('result2').textContent = JSON.stringify(data);
//         })
//         .catch(error => console.error('Error:', error));
// });

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetchData2').addEventListener('click', function() {
        // Simular un JSON de respuesta
        const jsonResponse = {
            mensaje: "hola mundo",
            estado: "éxito"
        };
        
        // Convertir el objeto JSON a una cadena para mostrarlo
        const jsonString = JSON.stringify(jsonResponse, null, 2);
        
        // Mostrar el JSON en el elemento con id 'result'
        document.getElementById('result2').textContent = jsonString;
    });
});

