import streamlit as st
import random

# Título del test
st.title("Test de prueba de Razonamiento Aproximado (batería 2024)")

# Lista de preguntas con sus opciones y respuestas correctas
preguntas = [
    {
        "pregunta": "Se basa en el uso de números aleatorios y probabilidad estadística. Estamos hablando de:",
        "opciones": ["Método de Monte Carlo", "Redes Bayesianas", "Distribución Gaussiana", "Ley de Murphy"],
        "correcta": "Método de Monte Carlo"
    },
    {
        "pregunta": "¿Cuáles son los componentes de los sistemas basados en reglas?",
        "opciones": ["Conocimiento, almacenaje y diferencias", "Base de conocimiento, Base de datos y mecanismos de inferencia", "Bases, reglas y normas", "Ninguna es correcta"],
        "correcta": "Base de conocimiento, Base de datos y mecanismos de inferencia"
    },
    {
        "pregunta": "Selecciona la respuesta correcta con respecto a los mecanismos basados en reglas:",
        "opciones": ["En el “modus ponens” tenemos las premisas y las normas", "Son poco eficaces aunque las reglas cubran las entradas almacenadas en la BD", "Son mecanismos poco costosos de ejecutar dada su simplicidad", "Se pueden considerar como la forma más compleja de representar sistemas de IA"],
        "correcta": "Son mecanismos poco costosos de ejecutar dada su simplicidad"
    },
    {
        "pregunta": "¿Cuáles son las fuentes de incertidumbre en el razonamiento aproximado?",
        "opciones": ["Deficiencias de la información, agentes del mundo real y deficiencias de las realidades sociales", "Deficiencias de la información, agentes del mundo real y deficiencia de los modelos que intentan explicar el problema", "Agentes del mundo real, deficiencias de la información y realidades sociopolíticas de la posmodernidad", "Deficiencias en el sistema ideológico neoliberal, agentes del mundo distópico y deficiencias del idealismo político"],
        "correcta": "Deficiencias de la información, agentes del mundo real y deficiencia de los modelos que intentan explicar el problema"
    },
    {
        "pregunta": "¿Cuál de las siguientes opciones describe mejor el Método Monte Carlo?",
        "opciones": ["Un método de resolución numérica de ecuaciones diferenciales", "Un método de estimación estadística basado en la generación de números aleatorios", "Un método de clasificación de datos basado en árboles de decisión", "Un método de interpolación de datos a partir de puntos discretos"],
        "correcta": "Un método de estimación estadística basado en la generación de números aleatorios"
    },
    {
        "pregunta": "¿En teoría de grafos e informática qué es un DAG?",
        "opciones": ["Digital Agreement Graphics", "Un grafo dirigido en el que no hay ciclos", "Diseño Adquirido de Grafos", "Ninguna de las anteriores"],
        "correcta": "Un grafo dirigido en el que no hay ciclos"
    },
    {
        "pregunta": "La lógica difusa sirve para:",
        "opciones": ["Poder cuantificar la incertidumbre del mundo que nos rodea", "Poder calcular la probabilidad que ocurra un suceso no aleatorio", "Establecer reglas de funcionamiento del mundo abstracto", "Establece los principios de funcionamiento de la naturaleza humana"],
        "correcta": "Poder cuantificar la incertidumbre del mundo que nos rodea"
    },
    {
        "pregunta": "¿Qué son las redes bayesianas?",
        "opciones": ["Son representaciones de mecanismos poco costosos de ejecutar dada su simplicidad", "Son estructuras matemáticas representadas por nodos dependientes", "Son representaciones a través de grafos acíclicos dirigidos, donde los nodos representan variables aleatorias y los arcos sus dependencias", "Son las representaciones lógicas basadas en la Ley de Bayes"],
        "correcta": "Son representaciones a través de grafos acíclicos dirigidos, donde los nodos representan variables aleatorias y los arcos sus dependencias"
    },
    {
        "pregunta": "Es la probabilidad de una variable aleatoria basada en datos del experimento, es decir, después de considerar la evidencia, estamos hablando de:",
        "opciones": ["Probabilidad condicionada", "Probabilidad conjunta", "Probabilidad posterior", "Todas son correctas"],
        "correcta": "Probabilidad posterior"
    },
    {
        "pregunta": "Redes bayesianas (Grafos acíclicos). Indica la falsa:",
        "opciones": ["Un grafo se compone de vértices y aristas, con cada arista apuntando al vértice siguiente", "Se considera que un grafo es dirigido cuando todas las direcciones son consistentes y los vértices tienen un orden lineal", "Un DAG es un grafo dirigido con múltiples ciclos", "Se considera que un grafo es acíclico cuando sigue las direcciones nunca conduce a un bucle cerrado"],
        "correcta": "Un DAG es un grafo dirigido con múltiples ciclos"
    },
    {
        "pregunta": "Sobre la Teoría de Dempster-Shafer:",
        "opciones": ["Un modelo de clasificación no supervisada para la segmentación de imágenes", "Es una generalización del método bayesiano donde se combinan entre sí todas las posibilidades a las que nos podemos enfrentar en un problema dado", "Una técnica de reducción de dimensionalidad para datos de alta dimensionalidad", "Todas las anteriores son correctas"],
        "correcta": "Es una generalización del método bayesiano donde se combinan entre sí todas las posibilidades a las que nos podemos enfrentar en un problema dado"
    },
    {
        "pregunta": "Sobre el método de Aceptación-Rechazo:",
        "opciones": ["Se puede enfocar aplicando el método de Monte Carlo", "Consiste en la generación sistemática de puntos aleatorios en un determinado rango", "Permite la aproximación del área de una determinada región", "Todas las anteriores son correctas"],
        "correcta": "Todas las anteriores son correctas"
    },
    {
        "pregunta": "¿Cuál de las siguientes opciones es una característica de las redes bayesianas?",
        "opciones": ["Son modelos gráficos probabilísticos", "Son modelos de regresión lineal", "Son modelos de clasificación no supervisada", "Son modelos de aprendizaje por refuerzo"],
        "correcta": "Son modelos gráficos probabilísticos"
    },
    {
        "pregunta": "¿Cuál de las siguientes opciones es una característica de la lógica difusa?",
        "opciones": ["Permite tomar decisiones más o menos intensas en función de grados intermedios de cumplimiento de una premisa", "Es una lógica paraconsistente multivaluada en la cual los valores de verdad de las variables pueden ser cualquier número real comprendido entre 0 y 1", "Es una lógica que se utiliza para representar relaciones de dependencia entre variables aleatorias y para realizar inferencias sobre ellas", "Es una lógica que se utiliza para modelar sistemas complejos y no lineales"],
        "correcta": "Es una lógica paraconsistente multivaluada en la cual los valores de verdad de las variables pueden ser cualquier número real comprendido entre 0 y 1"
    },
    {
        "pregunta": "¿Cuál es la principal ventaja del método de inferencia de Takagi-Sugeno sobre el método de inferencia de Mamdani?",
        "opciones": ["El método de Takagi-Sugeno es más simple y fácil de implementar, siendo el más utilizado en lógica difusa", "El método de Takagi-Sugeno proporciona resultados más precisos", "El método de Takagi-Sugeno es más rápido en el procesamiento de datos", "La salida del sistema de Mamdani se representa como una expresión matemática"],
        "correcta": "El método de Takagi-Sugeno es más rápido en el procesamiento de datos"
    },
    {
        "pregunta": "Indica las partes de un controlador difuso",
        "opciones": ["Codificación o fuzzificación, base de conocimiento, motor de inferencia y decodificador o defuzzificador", "Codificación o fuzzificación, base de conocimiento y motor de inferencia", "Decodificador, base de conocimiento y motor diferencial", "Decodificador, base de conocimiento y motor de lógica difusa"],
        "correcta": "Codificación o fuzzificación, base de conocimiento, motor de inferencia y decodificador o defuzzificador"
    },
    {
        "pregunta": "Sobre el método de Monte Carlo, indica la opción correcta:",
        "opciones": ["Aplicarlo para casos sencillos, unidimensionales, no compensa", "Al calcular una aproximación, no permite resolver problemas complejos", "Es buena elección para problemas unidimensionales", "Ninguna es correcta"],
        "correcta": "Aplicarlo para casos sencillos, unidimensionales, no compensa"
    },
    {
        "pregunta": "Variational Bayes vs Monte Carlo",
        "opciones": ["El método de Montecarlo es computacional más costoso", "Variational Bayes es adecuado para explorar muchos modelos en conjuntos grandes de datos", "El método de Monte Carlo proporciona una aproximación numérica al posterior exacto", "Todas las anteriores"],
        "correcta": "Todas las anteriores"
    },
    {
        "pregunta": "Indica la correcta sobre el método de inferencia Mamdani:",
        "opciones": ["Para obtener una conclusión, se calcula la función de pertenencia a cada variable de entrada y, al final, se combinan todas las reglas en un único conjunto difuso para definir la pertenencia", "Es el método más utilizado en la lógica difusa", "La salida del sistema se representa como un conjunto difuso", "Todas son correctas"],
        "correcta": "Todas son correctas"
    },
    {
        "pregunta": "¿Qué es un conjunto difuso?",
        "opciones": ["Una función que indica el grado de pertenencia de un valor difuso", "Un conjunto de valores numéricos", "Un conjunto de variables lingüísticas", "Una función que indica el grado de pertenencia de un valor numérico para una variable lingüística o difusa"],
        "correcta": "Una función que indica el grado de pertenencia de un valor numérico para una variable lingüística o difusa"
    }
]

# Mezclar el orden de las preguntas
random.shuffle(preguntas)

# Almacenar respuestas del usuario y resultados de validación
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'validaciones' not in st.session_state:
    st.session_state.validaciones = {}

# Mostrar cada pregunta con sus opciones
for idx, q in enumerate(preguntas):
    st.subheader(f"Pregunta {idx + 1}: {q['pregunta']}")
    
    # Mezclar opciones para esta pregunta
    opciones_mezcladas = q['opciones'].copy()
    random.shuffle(opciones_mezcladas)
    
    # Selección de respuesta por el usuario
    respuesta = st.radio(f"Selecciona una opción para la pregunta {idx + 1}", opciones_mezcladas, key=f"pregunta_{idx}")
    st.session_state.respuestas[idx] = respuesta
    
    # Botón para validar individualmente
    if st.button(f"Validar Pregunta {idx + 1}", key=f"validar_{idx}"):
        if respuesta == q['correcta']:
            st.session_state.validaciones[idx] = "¡Correcto!"
        else:
            st.session_state.validaciones[idx] = f"Incorrecto. La respuesta correcta es: {q['correcta']}"
    
    # Mostrar resultado de la validación si existe
    if idx in st.session_state.validaciones:
        st.write(st.session_state.validaciones[idx])

# Botón para finalizar el test
if st.button("Finalizar Test"):
    nota = 0
    total_preguntas = len(preguntas)
    
    # Calcular la nota
    for idx, q in enumerate(preguntas):
        if st.session_state.respuestas.get(idx) == q['correcta']:
            nota += 1
    
    # Mostrar resultado
    st.write(f"Tu nota es: {nota}/{total_preguntas}")
    st.write("Estas preguntas no son las definitivas, corresponden al año pasado.")
