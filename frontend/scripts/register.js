// Validación del formulario en JavaScript
document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let isValid = true;

    // Limpiar mensajes de error previos
    document.getElementById('nameError').textContent = '';
    document.getElementById('emailError').textContent = '';
    document.getElementById('passwordError').textContent = '';

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Validar campo de nombre
    if (name.trim() === '') {
        document.getElementById('nameError').textContent = 'El nombre es obligatorio.';
        isValid = false;
    }

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
        // Aquí puedes enviar el formulario al servidor usando fetch o AJAX
        fetch('http://127.0.0.1:5000/api/resgister', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, email: email, password: password })
        })
        .then (responson => response.json())
        .then(data => {
            if (data.success) {
                alert('Registro exitoso');
                window.location.href = 'login.html';
            } else {
                alert('Error al registrar usuario');
            }
        })
        alert('Registro exitoso');
    }
});