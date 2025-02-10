import cohere
from flask import Flask, render_template, request, jsonify

cohere_api_key = "fXBvKmFpAdRFftY1qyx08dbmtsRuxTHZqW2CIwUh"
co = cohere.Client(cohere_api_key)

app = Flask(__name__)

def generar_prompt(sentimientos, estres, miedos, apoyo, comentarios):
    return f"""
    Evalúa la siguiente información y responde de manera empática, constructiva y cálida en español:
    
    Sentimientos: {sentimientos}
    Estrés: {estres}
    Miedos: {miedos}
    Apoyo: {apoyo}
    Comentarios adicionales: {comentarios}
    
    Por favor, responde completamente en español. Tu respuesta debe cumplir con lo siguiente:
    1. Usa un tono amigable y humano, como si estuvieras conversando de manera cercana.
    2. No hagas referencia directa a la persona (evita palabras como "señor/a" o "tú").
    3. Brinda sugerencias claras y útiles para mejorar el bienestar, enfocándote en soluciones prácticas y apoyo emocional.
    4. Estructura tus ideas de forma fluida y natural, asegurándote de que la respuesta sea concisa, pero enriquecida.
    5. La respuesta debe ser completamente en español. No uses ningún otro idioma.
    """

def obtener_respuesta(prompt):
    try:
        response = co.generate(
            model="command-r-plus-08-2024",
            prompt=prompt,
            max_tokens=185, 
            temperature=0.7 
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error inesperado: {e}"

@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    sentimientos = request.form['sentimientos']
    estres = request.form['estres']
    miedos = request.form['miedos']
    apoyo = request.form['apoyo']
    comentarios = request.form['comentarios']
    
    prompt = generar_prompt(sentimientos, estres, miedos, apoyo, comentarios)
    respuesta = obtener_respuesta(prompt)
    
    return jsonify({'response': respuesta})

if __name__ == '__main__':
    app.run(debug=True)