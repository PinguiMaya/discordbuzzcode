<script>
function copy(texto) {
  navigator.clipboard.writeText(texto)
    .then(function() {
      console.log('Texto copiado al portapapeles');
      window.location.href = "https://www.ejemplo.com/"; // Aquí debes especificar la URL a la que deseas redirigir al usuario después de copiar el texto
    })
    .catch(function() {
      console.log('Error al copiar el texto');
    })
}
</script>