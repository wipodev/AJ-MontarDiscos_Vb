<p align="center">
    <img src="https://github.com/wipodev/wipodev/blob/main/assets/logo-main.svg" width="300" title="AJ-Wi">
</p>

# USB Drive Monitor

aplicación para simular en Windows el efecto de Linux o MAC OSX de que aparezca la unidad conectada por usb en el escritorio

Ejecutada se encuentra en constante revisión de unidades conectadas o desconectadas, en lo que a unidades se refiere,
y si detecta una unidad conectada nos crea un acceso directo a dicha unidad en el escritorio, de lo contrario elimina el
acceso directo, de hecho si eliminamos el acceso directo del escritorio o lo arrastramos a la papelera la aplicación
expulsa la unidad del PC

## Uso

Para usar `USB Drive Monitor`, sigue estos pasos:

1. Clona o descarga el repositorio a tu sistema.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta `USB Drive Monitor` en tu sistema.
4. El módulo monitoreará continuamente la conexión y desconexión de unidades USB y realizará las siguientes acciones:

   - **Al conectarse una unidad USB:** Creará un acceso directo en el escritorio para la unidad recién conectada.
   - **Al Desconectarse una unidad USB:** Eliminará el acceso directo correspondiente del escritorio.
   - **Al arrastrar acceso directo a la papelera:** Desconecta de forma segura la unidad USB.
   - **Al eliminar acceso directo:** Desconecta de forma segura la unidad USB.

## Características

- Detección automática de unidades USB conectadas.
- Creación automática de accesos directos en el escritorio para unidades USB.
- Gestión de accesos directos en el escritorio.
- Facilita la expulsión segura de dispositivos USB al eliminar su acceso directo.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](https://github.com/wipodev/USB_Drive_Monitor/blob/master/LICENSE).

## Repositorio

Puedes encontrar el código fuente y más detalles en el repositorio de GitHub: [wipodev/USB_Drive_Monitor](https://github.com/wipodev/USB_Drive_Monitor).
