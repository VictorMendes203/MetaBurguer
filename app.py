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
        },
        {
            "nome": "Maré Alta",
            "descricao": "Uma limonada suíça feita com curaçau blue, o que lhe dá uma cor azul oceânica profunda e um leve sabor cítrico.Servido com uma rodela de limão siciliano e uma leve borda de sal no copo.",
            "preco": "R$ 10,00",
            "imagem": "aquaman.jpg"
        },
        {
            "nome": "Poder de Shazam!",
            "descricao": "Um pão australiano (escuro, lembrando o uniforme clássico) com peito de frango empanado e frito, queijo muçarela derretido e um molho barbecue com um toque agridoce.Acompanha uma porção de batatas fritas em formato de raio.",
            "preco": "R$ 30,00",
            "imagem": "shazam.jpg"
        }

    ]
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
