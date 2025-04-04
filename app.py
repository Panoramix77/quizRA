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
        "question": "¿Qué desventaja tienen los sistemas basados en reglas? *Gracias David!",
        "options": ["Falta de flexibilidad", "Incapacidad para manejar grandes cantidades de datos", "Falta de aprendizaje de los datos utilizados", "Complejidad computacional extrema"],
        "correct": 3
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
    },
    {
        "question": "¿Cuál es la principal diferencia entre los métodos Mamdani y Takagi-Sugeno en términos de las salidas de las reglas difusas?",
        "options": ["Mamdani usa valores numéricos y Takagi-Sugeno usa conjuntos difusos", "Mamdani usa conjuntos difusos y Takagi-Sugeno usa expresiones matemáticas", "Ambos usan conjuntos difusos, pero Mamdani es más rápido", "Ambos usan expresiones matemáticas, pero Takagi-Sugeno es más intuitivo"],
        "correct": 2
    },
    {
        "question": "¿En qué situación sería preferible usar el método de Mamdani en lugar de Takagi-Sugeno?",
        "options": ["Cuando se necesita una respuesta numérica rápida sin defuzzificación", "Cuando se desea modelar un sistema basado en razonamiento humano intuitivo", "Cuando las reglas son exclusivamente matemáticas y lineales", "Cuando el sistema no requiere una base de conocimiento difusa"],
        "correct": 2
    },
    {
        "question": "¿Qué diferencia hay en el proceso de defuzzificación entre Mamdani y Takagi-Sugeno?",
        "options": ["Mamdani no requiere defuzzificación, mientras que Takagi-Sugeno sí", "Ambos requieren defuzzificación, pero Mamdani es más complejo", "Mamdani requiere defuzzificación, mientras que Takagi-Sugeno no", "Takagi-Sugeno requiere más pasos de defuzzificación que Mamdani"],
        "correct": 3
    },
    {
        "question": "¿Qué tipo de salidas son típicas en el método de Takagi-Sugeno?",
        "options": ["Conjuntos difusos como 'propina generosa'", "Funciones trapezoidales o triangulares", "Constantes o funciones lineales de las entradas", "Valores probabilísticos entre 0 y 1 exclusivamente"],
        "correct": 3
    },
    {
        "question": "¿Cuál es una ventaja clave del método de Takagi-Sugeno en términos de eficiencia computacional?",
        "options": ["Permite representar salidas con conjuntos difusos más complejos", "Elimina la necesidad de defuzzificación al usar valores numéricos directos", "Usa menos reglas difusas que el método de Mamdani", "Requiere menos variables lingüísticas en la entrada"],
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
        q["user_answer"] = None  # Respuesta del usuario
    st.session_state.submitted = False

# Interfaz de la aplicación
st.title("Test de Razonamiento Aproximado (Curso IA-ML 2025)")

# Mostrar cada pregunta
for i, q in enumerate(st.session_state.quiz, 1):
    st.subheader(f"Pregunta {i}: {q['question']}")
    
    # Selección de respuesta por el usuario
    answer = st.radio(
        "Selecciona una opción",
        q["options_shuffled"],
        key=f"q{i}",
        index=None if q["user_answer"] is None else q["options_shuffled"].index(q["user_answer"])
    )
    q["user_answer"] = answer  # Guardar la respuesta seleccionada
    
    # Botón "Corregir" para retroalimentación opcional
    if st.button("Corregir", key=f"check_q{i}"):
        if q["user_answer"] is None:
            st.warning("Por favor, selecciona una opción antes, que no soy adivino!.")
        else:
            if q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"]:
                st.success("¡Opa! ¡Correcto!")
            else:
                correct_answer = q["options"][q["correct"] - 1]
                st.error(f"Vaya tela... la respuesta correcta es: {correct_answer}. Revísalo anda!")

# Botón para finalizar el test
if st.button("Finalizar el Test"):
    st.session_state.submitted = True

# Mostrar resultados al finalizar
if st.session_state.submitted:
    total_questions = len(st.session_state.quiz)
    correct = 0
    incorrect = 0
    unanswered = 0
    
    # Evaluar todas las respuestas
    for q in st.session_state.quiz:
        if q["user_answer"] is None:
            unanswered += 1
        elif q["options_shuffled"].index(q["user_answer"]) + 1 == q["correct_index"]:
            correct += 1
        else:
            incorrect += 1
    
    # Calcular porcentajes
    percentage_correct = (correct / total_questions) * 100 if total_questions > 0 else 0
    percentage_incorrect = (incorrect / total_questions) * 100 if total_questions > 0 else 0
    percentage_unanswered = (unanswered / total_questions) * 100 if total_questions > 0 else 0
    
    # Mostrar resultados
    st.success(f"Test finalizado. Tu puntuación: {correct}/{total_questions}")
    st.write(f"**Número de aciertos:** {correct} ({percentage_correct:.2f}%)")
    st.write(f"**Número de fallos:** {incorrect} ({percentage_incorrect:.2f}%)")
    st.write(f"**Preguntas no contestadas:** {unanswered} ({percentage_unanswered:.2f}%)")
    
    # Opción para reiniciar
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.experimental_rerun()
