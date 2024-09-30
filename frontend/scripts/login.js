// Validación del formulario en JavaScript
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir que el formulario se envíe de manera predeterminada

    let isValid = true;

    // Limpiar mensajes de error previos
    document.getElementById('emailError').textContent = '';
    document.getElementById('passwordError').textContent = '';

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Validar campo de email
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Ingresa un correo válido.';
        isValid = false;
    }
    // Validar campo de contraseña (mínimo 6 caracteres)
    if (password.length < 6) {
        document.getElementById('passwordError').textContent = 'La contraseña debe tener al menos 6 caracteres.';
        isValid = false;
    }

    if (isValid) {
        // Enviar el formulario al servidor usando fetch: cambiar a conveniencia del puerto
        fetch('http://127.0.0.1:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Inicio de sesión exitoso');
                window.location.href = 'index.html';
            } else {
                alert('Credenciales incorrectas');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al iniciar sesión. Por favor, inténtalo más tarde.');
        });
    }
});