## comandos cmd
### eliminar archivos basura en windows
- paso 1: abrir cmd como administrador
- paso 2: dism /online /cleanup-image /analyzecomponentstore
- paso 3: dism /online /cleanup-image /startcomponentcleanup

### aumentar memoria ram en windows
- paso 1: abrir cmd como administrador
- paso 2: msconfig
    - pestaña inicio normal
    - sin selecccionar diagnostico
    - seleccionar servicios ocultar todos los de microsoft
    - deseleccionar todos
    - pestaña inicio
    - administrador de tareas
    - deshabilitar todos los programas
    - cerrar administrador de tareas
    - aceptar
    - reiniciar windows

### mejorar el rendimiento de la pc
- paso 1: abrir powershell como administrador
- paso 2: ejecutar los siguientes comandos:
irm christitus.com/win | iex
-  Luego ir a pestaña tweaks / standard
- elegir los tweaks para posteriormente desinstalar los programas que no se necesitan
- Hacer clic en Btn Run Tweaks para ejecutar

### mirar quien esta en tu red
- paso 1: abrir powershell como administrador
- paso 2: ejecutar los siguientes comandos:
- netstat -ano 
  - despues q muestre el listado de procesos buscar el numero de puerto q aparece en la ultima columna

### Identificar con exactitud qué programa usa cada puerto
- paso 1: abrir powershell como administrador
- paso 2: ejecutar los siguientes comandos:

  ```powershell
  Get-NetTCPConnection | Where-Object State -eq 'Listen' | 
    Select-Object LocalAddress, LocalPort, OwningProcess, @{Name="ProcessName"; Expression={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} | 
    Sort-Object LocalPort | Format-Table -AutoSize
  ```