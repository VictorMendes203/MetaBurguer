from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Lista de produtos (exemplo)
    items = [
        {
            "nome": "Batburger",
            "descricao": "Hambúrguer negro com queijo cheddar e molho secreto do Batman",
            "preco": "R$ 25,00",
            "imagem": "batman.jpg"
        },
        {
            "nome": "Super Shake",
            "descricao": "Milkshake azul e vermelho com chantilly",
            "preco": "R$ 18,00",
            "imagem": "superman.jpg"
        },
        {
            "nome": "Laço da Verdade",
            "descricao": "Wrap de frango grelhado com molho dourado da Mulher-Maravilha",
            "preco": "R$ 22,00",
            "imagem": "wonderwoman.jpg"
        },
        {
            "nome": "Velocidade Escarlate",
            "descricao": "Torta de morango com cobertura flamejante",
            "preco": "R$ 16,00",
            "imagem": "Flash.jpg"
        }
    ]
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
