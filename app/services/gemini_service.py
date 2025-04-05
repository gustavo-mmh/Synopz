import google.generativeai as genai

def sum_up_with_gemini(text, api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = f"""Crie um resumo profissional e objetivo do seguinte curso, 
        destacando os principais pontos e insights. O resumo deve ser estruturado 
        em tópicos claros, com uma introdução, Principais Pontos e conclusão:

        CURSO: {text}

        FORMATO DO RESUMO:
        
        ## Introdução ao Tema
        [Breve contextualização do conteúdo]

        ## Principais Pontos
        [Liste os Principais pontos com uma Descrição sucinta]
        
        ## Conclusão
        [Síntese dos principais insights]
        """

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro na geração do resumo: {str(e)}"