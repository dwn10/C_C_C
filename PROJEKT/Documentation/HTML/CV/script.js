// Manejo del tema
const lightModeBtn = document.getElementById('lightMode');
const darkModeBtn = document.getElementById('darkMode');
const body = document.documentElement;

// Cargar tema guardado
const savedTheme = localStorage.getItem('theme') || 'light';
body.setAttribute('data-theme', savedTheme);

lightModeBtn.addEventListener('click', () => {
    body.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
});

darkModeBtn.addEventListener('click', () => {
    body.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
});

// Funcionalidad de descarga del CV
document.getElementById('downloadCV').addEventListener('click', () => {
    // Crear una copia del CV sin los botones de tema y descarga
    const cvContent = document.querySelector('.container').cloneNode(true);
    const themeButtons = cvContent.querySelector('.theme-buttons');
    const downloadBtn = cvContent.querySelector('.download-btn');
    
    if (themeButtons) themeButtons.remove();
    if (downloadBtn) downloadBtn.remove();

    // Crear estilos inline para la impresión
    const styles = Array.from(document.styleSheets)
        .map(sheet => {
            try {
                return Array.from(sheet.cssRules)
                    .map(rule => rule.cssText)
                    .join('\n');
            } catch (e) {
                console.log('Error al acceder a stylesheet:', e);
                return '';
            }
        })
        .join('\n');

    // Crear el contenido HTML completo
    const html = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>CV para Descarga</title>
            <style>${styles}</style>
        </head>
        <body>
            ${cvContent.outerHTML}
        </body>
        </html>
    `;

    // Crear el blob y descargar
    const blob = new Blob([html], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'mi-cv.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
});