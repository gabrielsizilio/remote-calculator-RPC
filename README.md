# Calculadora Remota RPC em Python 🐍

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Protocol](https://img.shields.io/badge/Protocolo-XML--RPC-orange)
![Status](https://img.shields.io/badge/Status-Concluído-green)
![Disciplina](https://img.shields.io/badge/Disciplina-Sistemas%20Distribuídos-red)

A **Calculadora Remota RPC** é uma aplicação simples desenvolvida para a disciplina de **Sistemas Distribuídos**, com o objetivo de demonstrar e entender o funcionamento básico do protocolo **Remote Procedure Call (RPC)**, utilizando a biblioteca padrão XML-RPC do Python.

O projeto consiste em duas partes principais:
1.  **Servidor (`server.py`):** Implementa as funções matemáticas (`add`, `sub`, `mul`, `div`) e as expõe para chamadas remotas.
2.  **Cliente (`client.py`):** Atua como um *stub*, permitindo que o usuário insira a operação e os valores via terminal para serem processados no servidor remoto.

## 🚀 Tecnologias Utilizadas
* **Python 3.12**
* **XML-RPC:** Utilizando os módulos `xmlrpc.server` e `xmlrpc.client` (bibliotecas nativas do Python).

## ⚙️ Como Rodar o Projeto

Este projeto requer dois terminais separados para execução, um para o **Servidor** e outro para o **Cliente**, simulando a comunicação em rede.

### Pré-requisitos
* **Python 3.12** instalado.

---

### Passo a Passo

```bash
# 1. Clone o repositório
$ git clone https://github.com/gabrielsizilio/remote-calculator-RPC

# 2. Navegue até a pasta do projeto
$ cd remote-calculator-RPC

# 3. Inicie o server
$python3.12 server.py
```
Abra um novo terminal no mesmo diretório e inicie o client

```
# 4. Inicie o client
$python3.12 client.py
```
## 🎯 Funcionalidades
As operações são simples

- add (adição)
- sub (subtração)
- mul (multiplicação)
- div (divisão)

Basta digitar no terminal client a operação e 2 valores (x e y). Basta digitar na sequência seguidos da tecla Enter.
É possível verificar a operação sendo realizada no terminal do server.

## Contribuidores 😎

| <img src="https://github.com/gabrielsizilio.png" width="60px;"/> | <img src="https://github.com/beruasCS.png" width="60px;"/> 
|:---:|:---:|
| [@gabrielsizilio](https://github.com/gabrielsizilio) | [@yodemisj](https://github.com/beruasCS)
