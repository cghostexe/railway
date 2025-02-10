document.getElementById('mental-health-form').addEventListener('submit', function(event) {
    event.preventDefault();  

    // Obtén los valores del formulario
    const sentimientos = document.getElementById('sentimientos').value.trim();
    const estres = document.querySelector('input[name="estres"]:checked')?.value || '';
    const miedos = document.getElementById('miedos').value;
    const apoyo = document.querySelector('input[name="apoyo"]:checked')?.value || '';
    const comentarios = document.getElementById('comentarios').value.trim();

    // Valida que los campos obligatorios estén completos
    if (!sentimientos || !estres || !apoyo) {
        document.getElementById('modal-text').innerText = 'Por favor, completa todos los campos obligatorios.';
        document.getElementById('modal').style.display = 'flex';
        return;
    }

    // Envía los datos al servidor
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `sentimientos=${encodeURIComponent(sentimientos)}&estres=${encodeURIComponent(estres)}&miedos=${encodeURIComponent(miedos)}&apoyo=${encodeURIComponent(apoyo)}&comentarios=${encodeURIComponent(comentarios)}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor.');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('modal-text').innerText = data.response || 'Sin respuesta disponible.';
        document.getElementById('modal').style.display = 'flex';
    })
    .catch(error => {
        console.error('Error al enviar los datos:', error);
        document.getElementById('modal-text').innerText = 'Hubo un error al procesar la solicitud.';
        document.getElementById('modal').style.display = 'flex';
    });
});

// Lógica para cerrar el modal
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
});
