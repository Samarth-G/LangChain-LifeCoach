from flask import Flask, render_template, request
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

template = """Act like a motivating life coach that tries to help the user with whatever issue, concern or problem they have.
This life coach is also a Bollywood fanatic so use popular lines from Bollywood movies translated from hindi to english in your advice. 
Keep response to approximately 100 words.

Input from user: {input}
"""

prompt = ChatPromptTemplate.from_template(template)

# Use openai_api_key = "API_KEY" if API key not in env
# export OPENAI_API_KEY="API_KEY"
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = "May take a few minutes..."

    if request.method == 'POST':
        userInput = request.form['Input']
        result = chain.invoke({"input": userInput})
        print(result)
        message = f"Coach: {result}"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

