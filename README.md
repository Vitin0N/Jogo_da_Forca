# 🎮 Jogo da Forca (Python)

Bem-vindo ao **Jogo da Forca**, um clássico jogo de adivinhação de palavras totalmente feito em Python! Fiz esse jogo para aperfeiçoar meus conhecimentos em Python.

---

## 📦 Requisitos

- Python 3.6 ou superior  
- Um arquivo `palavras.json` contendo as categorias e listas de palavras

---

## 📂 Estrutura

- `forca.py` → Arquivo principal com todo o código do jogo
- `palavras.json` → Arquivo com as categorias e palavras do jogo, por exemplo:

```json
{
  "Animais": ["cachorro", "gato", "elefante"],
  "Cores": ["vermelho", "azul", "amarelo"],
  "Frutas": ["banana", "maçã", "uva"]
}
```

---

## ▶️ Como Jogar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/forca-python.git
cd forca-python
```

2. Execute o jogo:

```bash
python forca.py
```

3. Escolha entre:
   - Sortear uma palavra aleatória
   - Escolher um tema específico

4. Durante o jogo, você pode:
   - Tentar adivinhar uma letra
   - Chutar a palavra completa
   - Desistir da rodada

---

## 🧠 Lógica Principal

- O jogo começa escolhendo ou sorteando um tema.
- O jogador tem 5 vidas representadas por corações (❤️).
- A cada letra errada, uma vida é perdida.
- Ao acertar todas as letras ou a palavra, o jogador vence.
- Ao acabar as vidas ou errar o chute completo, o jogador perde.

---

## 🔧 Personalização

Você pode adicionar novas categorias ou palavras editando o arquivo `palavras.json`.

```json
{
  "Novos Temas": ["palavra1", "palavra2"]
}
```
---

Feito para desevolvimento e prática de Python 
Obrigado por visitar ~(￣▽￣)~