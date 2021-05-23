<p align="center">
    <img src="https://github.com/AJ-Wi/AJ-Wi.github.io/blob/master/images/AJ-Wi.svg" width="300" title="AJ-Wi">
</p>

# Montar Discos

aplicacion para simular en Windows el efecto de Linux o MAC OSX de que aparezca la unidad conectada por usb en el escritorio

Soy una persona nueva trabajando con linux, aunque en mi vida e toqueteado este SO de vez en cuando, sin embargo una cosa que
más me gustan de lo poco que he usado Linux y que además e visto en videos en SO Mac OSX a lo largo de mi vida es que cuando
montas una unidad, ya sea extraíble o de cd/dvd, nos pone automáticamente un icono para acceder a él en el escritorio.

En Windows es totalmente diferente, de hecho la única forma de acceder a estos es a través de Mi PC o el explorador de archivos.
En algún momento pensé que se podría simplemente creando un acceso directo a dicha unidad, lamentablemente fue inviable porque
cuando se desconecta la unidad sigue el acceso directo de la unidad en el escritorio y es posible que conectemos diferentes
tipos (pendrive, reproductor multimedia, etc) a lo largo del día y muy probablemente se le asigne el mismo icono y acceso
directo que ya tenemos en el escritorio.

Por las razones expuestas anteriormente decidí buscar una alternativa o quizás una opción oculta que tuviera el windows
que yo no supiera, cuando agote mis esfuerzos de búsqueda de esta opción, oculta tome la decisión de crear una aplicación que
lo emulara. Esta aplicación comencé a crearla en 2016, la utilice por un tiempo, con algunas fallas, pero lamentablemente
deje su desarrollo en el olvido

Ejecutada se encuentra en constante revisión de unidades conectadas o desconectadas, en lo que a unidades se refiere,
y si detecta una unidad conectada nos crea un acceso directo a dicha unidad en el escritorio, de lo contrario elimina el
acceso directo, de hecho si eliminamos el acceso directo del escritorio o lo arrastramos a la papelera la aplicación
expulsa la unidad del PC

## Requisitos

- **.net Framework v2.0**
- **Visual Studio 14**

## Licencia

MontarDiscos tiene [licencia MIT](https://github.com/AJ-Wi/MontarDiscos/blob/master/LICENSE)
