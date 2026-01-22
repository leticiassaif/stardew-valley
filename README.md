# 🌻 Titico's Garden

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/pygame-2D-green?style=for-the-badge)

> **Titico's Garden** é um jogo de simulação de fazenda em 2D desenvolvido em Python utilizando a biblioteca Pygame. O projeto combina mecânicas de cultivo, gerenciamento de recursos e economia em um ambiente relaxante.

## 📖 Sobre

No **Titico's Garden**, o jogador assume o papel de um fazendeiro que deve cuidar de suas plantações e gerenciar recursos para prosperar. O jogo conta com um ciclo de dia e noite, onde o jogador deve equilibrar suas atividades com sua energia disponível.

O projeto foi desenvolvido para aplicar conceitos de:
* Programação Orientada a Objetos (POO).
* Máquina de estados para animações de sprites.
* Lógica de colisão e interação em grids (Tiles).
* Gerenciamento de inventário e economia simples.

## 🎮 Funcionalidades

* **Cultivo:** Are a terra, plante sementes (Milho e Tomate) e regue-as para vê-las crescer.
* **Colheita e Coleta:** Colha seus frutos para vender e corte árvores para obter madeira.
* **Ferramentas:** Alterne entre Enxada, Machado e Regador para realizar diferentes tarefas.
* **Economia:** Interaja com o Mercador para vender sua produção e comprar mais sementes.
* **Sistema de RPG:**
    * **Energia:** Gerencie sua barra de energia que diminui a cada ação.
    * **XP e Nível:** Ganhe experiência trabalhando e suba de nível.
* **Ciclo Dia/Noite:** Durma em sua casa para recuperar energia e salvar o progresso do dia.

## 🕹️ Controles

| Tecla | Ação |
| :--- | :--- |
| **W, A, S, D** ou **Setas** | Movimentar o personagem |
| **Espaço** | Usar a ferramenta selecionada |
| **Q** | Trocar ferramenta (Enxada / Machado / Regador) |
| **LCTRL** | Plantar semente |
| **E** | Trocar tipo de semente (Milho / Tomate) |
| **Enter** ou **Shift Esquerdo** | Interagir (Dormir / Abrir Loja) |
| **P** | Pausar o jogo |

## 🛠️ Instalação e Execução

### Pré-requisitos

Certifique-se de ter o Python e o Pygame instalados:

* [Python 3.x](https://www.python.org/downloads/)
* [Pygame](https://pypi.org/project/pygame/)

### Como rodar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/seu-usuario/titico-garden.git](https://github.com/seu-usuario/titico-garden.git)
    ```

2.  Instale as dependências (caso ainda não tenha o Pygame):
    ```bash
    pip install pygame
    ```

3.  Acesse a pasta do projeto e execute o jogo:
    ```bash
    cd titico-garden
    python code/main.py
    ```

## 📂 Estrutura do Projeto

* `code/`: Contém a lógica do jogo (`main.py`, `player.py`, `level.py`, etc).
* `graphics/`: Sprites do personagem, cenário, itens e interfaces.
* `audio/`: Efeitos sonoros e músicas de fundo.
* `data/`: Arquivos de mapa (Tiled) e configurações de tilesets.

---
*Desenvolvido com 💚 e Python.*
