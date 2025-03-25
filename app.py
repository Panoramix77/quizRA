import streamlit as st
import random

# Lista de preguntas
quiz = [
    {
        "question": "¿Qué caracteriza al razonamiento aproximado?",
        "options": ["Se basa únicamente en reglas estrictas y precisas", "Obtiene conclusiones a partir de premisas con un grado de incertidumbre", "Es un sistema determinista sin variaciones", "Solo se aplica en entornos matemáticos"],
        "correct": 2
    },
    {
        "question": "¿Por qué la lógica formal es menos flexible que el razonamiento aproximado?",
        "options": ["Porque no permite alteraciones en el modelo", "Porque siempre incluye incertidumbre", "Porque se basa en heurísticas", "Porque no utiliza premisas"],
        "correct": 1
    },
    {
        "question": "¿Cuál de las siguientes es una fuente de incertidumbre?",
        "options": ["Información precisa y completa", "Agentes del mundo real no deterministas", "Modelos perfectos y exactos", "Sistemas sin variables externas"],
        "correct": 2
    },
    {
        "question": "¿Qué tipo de razonamiento utiliza la lógica formal?",
        "options": ["Inductivo", "Deductivo", "Aproximado", "Heurístico"],
        "correct": 2
    },
    {
        "question": "¿Cuál es una característica del razonamiento aproximado en comparación con la lógica formal?",
        "options": ["Mayor rigor y precisión", "Menos flexibilidad", "Uso de heurísticas y aproximaciones", "Aplicación solo en matemáticas"],
        "correct": 3
    },
    {
        "question": "¿Qué ámbito de aplicación se asocia más al razonamiento aproximado?",
        "options": ["Matemáticas puras", "Negocios y ciencias sociales", "Física teórica", "Química experimental"],
        "correct": 2
    },
    {
        "question": "¿En qué se basa el método deductivo?",
        "options": ["Observaciones del entorno para generar patrones", "Reglas generales para llegar a conclusiones específicas", "Probabilidades subjetivas", "Modelos incompletos"],
        "correct": 2
    },
    {
        "question": "¿Qué principio lógico es la base de los sistemas basados en reglas?",
        "options": ["Teorema de Bayes", "Modus Ponens", "Lógica difusa", "Combinatoria evidencial"],
        "correct": 2
    },
    {
        "question": "¿Cuál es un componente principal de un sistema basado en reglas?",
        "options": ["Base de conocimiento", "Red neuronal", "Algoritmo de aprendizaje profundo", "Simulación de Monte Carlo"],
        "correct": 1
    },
    {
        "question": "¿Qué hace el mecanismo de inferencia en un sistema basado en reglas?",
        "options": ["Almacena datos", "Aplica las reglas para tomar decisiones", "Genera gráficos", "Resuelve conflictos automáticamente"],
        "correct": 2
    },
    {
        "question": "¿Cuál es una ventaja de los sistemas basados en reglas?",
        "options": ["Capacidad de aprendizaje automático", "Transparencia en la toma de decisiones", "Complejidad en el mantenimiento", "Uso de conocimiento incompleto"],
        "correct": 2
    },
    {
        "question": "¿Qué desventaja tienen los sistemas basados en reglas?",
        "options": ["Falta de flexibilidad", "Incapacidad para manejar grandes cantidades de datos", "Falta de aprendizaje de los datos utilizados", "Complejidad computacional extrema"],
        "correct": 1
    },
    {
        "question": "¿En qué se basan los métodos bayesianos?",
        "options": ["Reglas estrictas sin incertidumbre", "Probabilidad subjetiva y el Teorema de Bayes", "Lógica difusa", "Sistemas deterministas"],
        "correct": 2
    },
    {
        "question": "¿Qué combina el Teorema de Bayes?",
        "options": ["Conocimiento a priori con muestras obtenidas", "Reglas deductivas con heurísticas", "Probabilidades absolutas sin evidencia", "Datos incompletos sin análisis"],
        "correct": 1
    },
    {
        "question": "¿Qué aportó Judea Pearl a los métodos bayesianos?",
        "options": ["La teoría de Dempster-Shafer", "Las redes bayesianas", "La lógica difusa", "El método de Monte Carlo"],
        "correct": 2
    },
    {
        "question": "¿Qué diferencia trata de abordar la teoría de Dempster-Shafer?",
        "options": ["Entre certeza y precisión", "Entre incertidumbre e ignorancia", "Entre deducción e inducción", "Entre reglas y heurísticas"],
        "correct": 2
    },
    {
        "question": "¿Qué representa el grado de creencia en DST?",
        "options": ["Una probabilidad fija de 0 o 1", "Un valor entre 0 y 1 basado en evidencias", "Una estimación sin incertidumbre", "Un cálculo determinista"],
        "correct": 2
    },
    {
        "question": "¿Qué es el marco de discernimiento en DST?",
        "options": ["Un conjunto de reglas fijas", "Todos los posibles subgrupos de hipótesis", "Una base de datos de premisas", "Un modelo gráfico probabilístico"],
        "correct": 2
    },
    {
        "question": "¿Qué permite cuantificar la lógica difusa?",
        "options": ["Certeza absoluta", "Incertidumbre del mundo real", "Reglas estrictas", "Probabilidades fijas"],
        "correct": 2
    },
    {
        "question": "¿Qué componente NO es parte de la lógica difusa?",
        "options": ["Proceso de fuzzyficación", "Mecanismo de inferencia", "Proceso de defuzzyficación", "Red neuronal profunda"],
        "correct": 4
    },
    {
        "question": "¿Qué inspira el nombre del método de Monte Carlo?",
        "options": ["Un físico famoso", "El casino de Monte Carlo y su ruleta", "Una ecuación matemática", "Un experimento de laboratorio"],
        "correct": 2
    },
    {
        "question": "¿Quiénes inventaron el método de Monte Carlo en los años 40?",
        "options": ["Bayes y Laplace", "Ulam y von Neumann", "Pearl y Shafer", "Turing y Zadeh"],
        "correct": 2
    },
    {
        "question": "¿Para qué es especialmente útil el método de Monte Carlo?",
        "options": ["Problemas unidimensionales simples", "Problemas multidimensionales complejos", "Cálculos deterministas exactos", "Modelos sin incertidumbre"],
        "correct": 2
    },
    {
        "question": "¿Qué tipo de grafo usa una red bayesiana?",
        "options": ["Grafo cíclico no dirigido", "Grafo acíclico dirigido (DAG)", "Grafo completo", "Grafo aleatorio"],
        "correct": 2
    },
    {
        "question": "¿Qué representa la probabilidad condicionada en una red bayesiana?",
        "options": ["La probabilidad de un evento aislado", "La probabilidad de un evento dado otro evento", "La suma de todas las probabilidades", "Una estimación sin evidencia"],
        "correct": 2
    },
    {
        "question": "En el problema de Monty Hall, ¿qué aumenta la probabilidad de ganar?",
        "options": ["Mantener la puerta inicial", "Cambiar a la puerta restante", "Elegir al azar sin cambiar", "No hacer ninguna elección"],
        "correct": 2
    },
    {
        "question": "¿Qué librería se usa en Python para redes bayesianas?",
        "options": ["Scikit-learn", "Pgmpy", "Simpful", "Matplotlib"],
        "correct": 2
    },
    {
        "question": "¿Qué ofrece Variational Bayes frente a Monte Carlo?",
        "options": ["Una solución analítica más eficiente", "Un muestreo más costoso", "Resultados menos precisos", "Una aproximación determinista"],
        "correct": 1
    },
    {
        "question": "¿Qué mide la esperanza matemática en una variable aleatoria continua?",
        "options": ["El valor más probable", "El valor medio del fenómeno", "La desviación estándar", "La probabilidad máxima"],
        "correct": 2
    },
    {
        "question": "¿Qué afirma la Ley Fuerte de los Grandes Números?",
        "options": ["El error crece con más muestras", "La media converge a μ con muchas muestras", "Las variables son siempre independientes", "La distribución es siempre normal"],
        "correct": 2
    }
]

# Inicialización del estado
if 'quiz' not in st.session_state:
    st.session_state.quiz = quiz.copy()
    random.shuffle(st.session_state.quiz)
    for q in st.session_state.quiz:
        q["options_shuffled"] = q["options"].copy()
        random.shuffle(q["options_shuffled"])
        q["correct_index"] = q["options_shuffled"].index(q["options"][q["correct"] - 1]) + 1
        q["user_answer"] = None
        q["confirmed"] = False
        q["is_correct"] = None
    st.session_state.score = 0
    st.session_state.submitted = False

# Interfaz de la app
st.title("Test de prueba de Razonamiento Aproximado (Curso IA/ML 2025)")

for i, q in enumerate(st.session_state.quiz, 1):
    st.subheader(f"Pregunta {i}: {q['question']}")
    
    # Selección de respuesta
    answer = st.radio(
        "Selecciona una opción",
        q["options_shuffled"],
        key=f"q{i}",
        index=None if q["user_answer"] is None else q["options_shuffled"].index(q["user_answer"])
    )
    q["user_answer"] = answer

    # Botón de confirmación para cada pregunta
    if st.button("Confirmar respuesta", key=f"confirm_q{i}"):
        if q["user_answer"] is not None:
            q["confirmed"] = True
            q["is_correct"] = (q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"])
            if q["is_correct"]:
                st.success("¡Correcto!")
                st.session_state.score += 1
            else:
                correct_answer = q["options"][q["correct"] - 1]
                st.error(f"Incorrecto. La respuesta correcta es: {correct_answer}")
        else:
            st.warning("Por favor, selecciona una opción antes de confirmar.")

    # Mostrar estado de la pregunta
    if q["confirmed"]:
        if q["is_correct"]:
            st.write("✅ Respuesta confirmada como correcta.")
        else:
            st.write("❌ Respuesta confirmada como incorrecta.")

# Botón para finalizar el test
if st.button("Finalizar test"):
    if all(q["confirmed"] for q in st.session_state.quiz):
        st.session_state.submitted = True
    else:
        st.warning("Por favor, confirma todas las respuestas antes de finalizar.")

# Mostrar resultados finales
if st.session_state.submitted:
    percentage = (st.session_state.score / len(st.session_state.quiz)) * 100
    st.success(f"Test finalizado. Tu puntuación: {st.session_state.score}/{len(st.session_state.quiz)}")
    st.write(f"Porcentaje de aciertos: {percentage:.2f}%")
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.experimental_rerun()
