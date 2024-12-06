const rows = document.querySelectorAll('.row');

rows.forEach(row => {
  const numStars = row.offsetWidth / 20; // Calcula el número de estrellas por fila
  for (let i = 0; i < numStars; i++) {
    const star = document.createElement('div');
    star.style.backgroundColor = getRandomColor(); // Asigna un color aleatorio inicial
    row.appendChild(star);

    // Cambia el color de la estrella automáticamente
    setInterval(() => {
      let currentColor = star.style.backgroundColor;
      let newColor = getNextColor(currentColor);
      star.style.backgroundColor = newColor;
    }, 400); // Cambia el color cada 400 milisegundos (0.4 segundos)

    // Agrega un efecto de brillo gradual
    setInterval(() => {
      star.style.opacity = Math.random(); // Cambia la opacidad aleatoriamente
    }, 300); // Cambia la opacidad cada 100 milisegundos

    // Agrega un efecto de cambio de tamaño
    setInterval(() => {
      let scale = 0.8 + Math.random() * 0.5; // Escala entre 0.8 y 1.2
      star.style.transform = `scale(${scale})`;
    }, 500); // Cambia el tamaño cada 500 milisegundos
  }
});

function getRandomColor() {
  const colors = ['#ff0', '#0f0', '#f00']; // Amarillo, verde, rojo
  return colors[Math.floor(Math.random() * colors.length)];
}

function getNextColor(currentColor) {
  switch (currentColor) {
    case '#ff0': // Amarillo
      return '#0f0'; // Verde
    case '#0f0': // Verde
      return '#f00'; // Rojo
    case '#f00': // Rojo
      return '#ff0'; // Amarillo
    default:
      return getRandomColor(); // Si el color no es ninguno de los anteriores, elige uno al azar
  }
}