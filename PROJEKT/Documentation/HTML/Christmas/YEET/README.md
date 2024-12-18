https://yeet-dokumentation.vectorsoft.de/

----------------------------------------
SCAN TEST 1
----------------------------------------
# Pasos para hacer funcionar el escáner en yeet con una tabla producto de un inventario versión simulación

1. **Asegúrate de tener una entidad de inventario definida**: Esta entidad debe contener las propiedades relevantes para tu `inventario`, como `nombre del producto`, `cantidad`, etc.
2. **Crea una página o ventana emergente (popup)**: En el UI Designer, diseña la interfaz donde se mostrarán los resultados del escaneo.
3. **Añade una tabla (yTable)**: Configura la tabla para que se conecte a tu entidad de inventario. Esto permitirá que la tabla muestre los datos del inventario.
4. **Implementa la lógica del escáner**: Utiliza JavaScript en la UI Logic para interactuar con el escáner. Esto implicará:
    * Acceder a la cámara del dispositivo.
    * Capturar la información del código de barras o QR.
    * Decodificar la información capturada.
5. **Conecta el escáner a la tabla**: Una vez que la información del escáner esté decodificada, utiliza JavaScript para:
    * Buscar el producto correspondiente en tu entidad de inventario.
    * Actualizar la tabla con la información del producto escaneado. Esto podría implicar añadir una nueva fila si el producto no existe, o actualizar la cantidad si ya está en la tabla.
6. **Prueba y ajusta**: Escanea algunos productos para verificar que la información se muestra correctamente en la tabla. Ajusta la lógica del escáner o la configuración de la tabla según sea necesario.

## Ejemplo de código JavaScript (UI Logic)
```js
// Función para manejar el evento de escaneo
function onScannerData(data) {
  // Decodificar la información del código de barras/QR
  const productInfo = decodeScannerData(data);

  // Buscar el producto en la entidad de inventario (usando apiObject.odata)
  const product = apiObject.odata.odataEntityRead('Inventario', undefined, { _id: productInfo.id });

  // Actualizar la tabla (yTable)
  if (product) {
    // Actualizar cantidad
    apiObject.ui.getObject(1, 'y-table').updateRow(product.index, { cantidad: product.cantidad + 1 });
  } else {
    // Añadir nueva fila
    apiObject.ui.getObject(1, 'y-table').addRow(productInfo);
  }
}
```

- Recuerda: Este es un ejemplo básico y puede requerir modificaciones dependiendo de tu configuración específica y la complejidad de tu lógica de inventario.

**Consideraciones adicionales:**

*   **Manejo de errores**: Implementa un manejo de errores adecuado para situaciones como productos no encontrados o errores de lectura del escáner.
*   **Optimización del rendimiento**: Si tu inventario es muy grande, considera la posibilidad de optimizar la búsqueda de productos para evitar retrasos en la actualización de la tabla.
*   **Seguridad**: Si tu aplicación maneja información sensible, asegúrate de implementar medidas de seguridad adecuadas para proteger los datos del inventario y el acceso al escáner.

----------------------------------------
SCAN TEST 2
----------------------------------------

## Pasos para hacer funcionar el escáner en yeet con una tabla producto de un inventario versión simulación

Asegúrate de tener una entidad de inventario definida: Esta entidad debe contener las propiedades relevantes para tu inventario, como nombre del producto, cantidad, etc.

1. **Crea una página o ventana emergente (popup)**: En el UI Designer, diseña la interfaz donde se mostrarán los resultados del escaneo.

2. **Añade una tabla (yTable)**: Configura la tabla para que se conecte a tu entidad de inventario. Esto permitirá que la tabla muestre los datos del inventario.

3. **Implementa la lógica del escáner**: Utiliza JavaScript en la UI Logic para interactuar con el escáner. Esto implicará:

    * Acceder a la cámara del dispositivo.
    * Capturar la información del código de barras o QR.
    * Decodificar la información capturada.

4. **Conecta el escáner a la tabla**: Una vez que la información del escáner esté decodificada, utiliza JavaScript para:

    * Buscar el producto correspondiente en tu entidad de inventario.
    * Actualizar la tabla con la información del producto escaneado. Esto podría implicar añadir una nueva fila si el producto no existe, o actualizar la cantidad si ya está en la tabla.

5. **Prueba y ajusta**: Escanea algunos productos para verificar que la información se muestra correctamente en la tabla. Ajusta la lógica del escáner o la configuración de la tabla según sea necesario.

**Ejemplo de código JavaScript (UI Logic)**

```js
// Función para manejar el evento de escaneo
function onScannerData(data) {
  // Decodificar la información del código de barras/QR
  const productInfo = decodeScannerData(data);
  // Buscar el producto en la entidad de inventario (usando apiObject.odata)
  const product = apiObject.odata.odataEntityRead('Inventario', undefined, { _id: productInfo.id });
  // Actualizar la tabla (yTable)
  if (product) {
    // Actualizar cantidad
    apiObject.ui.getObject(1, 'y-table').updateRow(product.index, { cantidad: product.cantidad + 1 });
  } else {
    // Añadir nueva fila
    apiObject.ui.getObject(1, 'y-table').addRow(productInfo);
  }
}
```

- Recuerda: Este es un ejemplo básico y puede requerir modificaciones dependiendo de tu configuración específica y la complejidad de tu lógica de inventario.

**Consideraciones adicionales:**

*   **Manejo de errores**: Implementa un manejo de errores adecuado para situaciones como productos no encontrados o errores de lectura del escáner.
*   **Optimización del rendimiento**: Si tu inventario es muy grande, considera la posibilidad de optimizar la búsqueda de productos para evitar retrasos en la actualización de la tabla.
*   **Seguridad**: Si tu aplicación maneja información sensible, asegúrate de implementar medidas de seguridad adecuadas para proteger los datos del inventario y el acceso al escáner.
