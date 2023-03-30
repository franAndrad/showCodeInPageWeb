# Codigo en Pagina Web (HTML, CSS y JavaScript)

## Comenzando 🚀
Este codigo te va a permitir mostrar y copiar un codigo escrito en un lenguaje de programacion en una pagina web.

### Descargar 📋
```
git clone ......
```

## Construido con 🛠️
Para este ejemplo usamos el plugin:

* [Prism](https://prismjs.com/download.html#themes=prism-okaidia&languages=markup+css+clike+javascript+css-extras+js-extras+json+json5+jsonp+mongodb&)

## Herramienta 🛠️

En el directorio `/herramientas` encontraremos un archivo texto `html.txt` y un programa en python el que nos permitira modificar un html para que pueda ser legible a la hora de cargarlo en la etiqueta <code></code>

### Pasos para su uso
1. Ingresar al `html.txt` y pegar el codigo en html
2. Ejecutar en shell     `$python /herramienta/program.py`
3. Abrir el `legiblePrismHtml.txt` y encontraremos el codigo legible

### Ejemplo
Codigo a ingresar en `html.txt`
```
<code class="language-html">
        <h1>Hola Mundo</h1>
</code>
```
Salida `legiblePrismHtml.txt`
```
&lt;pre class="code"&gt;
        &lt;code class="language-html"&gt;
          &lt;h1&gt;Hola Mundo&lt;/h1&gt;
        &lt;/code&gt;
&lt;/pre&gt;
```

## Lenguajes 📌

Si queremos agegar otros lenguajes, debemos entrar a la pagina y seleccionar la configuracion que deseemos y descargarla en la carpeta [Prism](https://prismjs.com/download.html#themes=prism-okaidia&languages=markup+css+clike+javascript+css-extras+js-extras+json+json5+jsonp+mongodb&)

### Lenguaje en el codigo html
Para poder especificar el lenguaje se lo hace cambiando la clase en <code class='language-xxxx'></code>, estas las encontramos en [Prism-languajes](https://prismjs.com/index.html#supported-languages)

## Autores ✒️
* **Andrade Francisco** - [Git](https://github.com/franAndrad)


## Expresiones de Gratitud 🎁
* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕. 
* Da las gracias públicamente 🤓.

