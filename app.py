from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Lista de produtos (exemplo)
    items = [
        {
            "nome": "Batburger",
            "descricao": "Pão de brioche negro, 180g de um blend de costela e peito bovino, Queijo cheddar inglês maturado e Maionese de alho negro defumado",
            "preco": "R$ 25,00",
            "imagem": "batman.jpg"
        },
        {
            "nome": "Super-Shake",
            "descricao": "Sorvete de baunilha batido com calda de blue raspberry e o copo é forrado com calda de morango",
            "preco": "R$ 18,00",
            "imagem": "superman.jpg"
        },
        {
            "nome": "Laço da Verdade",
            "descricao": "Tiras de frango grelhado,espinafre fresco, tomate cereja e queijo feta, tudo enrolado em uma tortilha dourada de milho ou cúrcuma",
            "preco": "R$ 22,00",
            "imagem": "wonderwoman.jpg"
        },
        {
            "nome": "Velocista Escarlate",
            "descricao": "Base crocante de biscoito, um recheio de cheesecake leve, e morangos frescos fatiados. Uma calda de morango brilhante cobrindo tudo, finalizada com raspas finas de casca de laranja ",
            "preco": "R$ 16,00",
            "imagem": "Flash.jpg"
        },

        {
            "nome": "Energia Esmeralda",
            "descricao": "Uma bebida verde vibrante pode ser um suco ou smoothiefeita com abacaxi, hortelã fresca e limão, ganhando sua cor intensa de um toque de espinafre",
            "preco": "R$ 10,00",
            "imagem": "lanternaverde.jpg"
        }
    ]
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
