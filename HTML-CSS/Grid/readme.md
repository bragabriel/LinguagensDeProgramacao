# CSS GRID
-> Podemos fatiar nossa tela com colunas e linhas,
colocando o que queremos onde queremos

- Bidimensional (não mais tudo para baixo)
- Divisão de toda a página em linhas e colunas
- Colocar elementos onde quiser nessa Divisão

---

## GRID OU FLEXBOX?
- Grid: Duas dimensões (Colunas e Linhas)
- FlexBox: Uma dimensão (Ou Coluna Ou Linha)

-> Um complementa o outro. <br>
Obs: Verificar quais navegadores ainda não aceitam GRID.

---

## Propriedades:
Vamos separar em dois grupos: 'container' e 'item(s)'

### Container
- display: grid; (inicia o container falando que é um Grid).
- grid-template-columns; (começa a fatiar as colunas).
- grid-template-rows; (começa a fatias as linhas).
- grid-gap (espaçamentos)
    - grid-row-gap; (espaçamentos em linha).
    - grid-column-gap; (espaçamentos em colunas).
- grid-template-areas; (delimita áreas).

... e mais 4 propriedades e [**alinhamento**](https://github.com/bragabriel/LinguagensDeProgramacao/blob/main/HTML-CSS/Grid/Propriedades-Alinhamento.md)

<br>

### Item(s)

- grid-column (vai dizer onde fica o item na coluna).
    - grid-column-start;
    - grid-column-end;
- grid-row (vai dizer onde fica o item na linha).
    - grid-row-start;
    - grid-row-end;
- grid-area; (vai dizer onde fica o item na área).

... e mais 4 propriedades e [**alinhamento**](https://github.com/bragabriel/LinguagensDeProgramacao/blob/main/HTML-CSS/Grid/Propriedades-Alinhamento.md)

<br>

---

#### Vídeo-Aula do tutorial disponível em: [Desvendando o CSS Grid na prática | Mayk Brito](https://www.youtube.com/watch?v=HN1UjzRSdBk&ab_channel=Rocketseat)