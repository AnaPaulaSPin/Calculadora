## 📌 Projeto: Calculadora Inteligente (Versão 3)

### 🎯 Objetivo

* Tornar a calculadora **mais flexível e robusta**, permitindo entradas mais naturais e números maiores, inclusive com casas decimais.
* Praticar **manipulação de strings** e **validação de tipos numéricos**.

### ⚙️ Funcionalidades

1. **Operações matemáticas**:

   * Soma (+), Subtração (-), Multiplicação (\*), Divisão (/), Resto (%), Potência (^)

2. **Validação de entradas avançada**:

   * Reconhece **inteiros** e **floats**
   * Ignora **espaços extras**
   * Permite **números de qualquer tamanho**
   * Mantém a limitação: **apenas uma operação por vez**

3. **Histórico de operações** (herdado da versão 2):

   * Continua salvando todas as operações realizadas em arquivo
   * Pode ser consultado a qualquer momento

### 💡 Exemplo de uso

```
Entrada:  12.5  +  7.3
Saída: 19.8
Histórico salvo: "12.5 + 7.3 = 19.8"

Entrada: 1000*250
Saída: 250000
Histórico salvo: "1000 * 250 = 250000"
```

### 🛡️ Regras e melhorias

* A calculadora **ignora espaços**, então entradas como `"  3   + 4 "` ou `"7*  5"` funcionam normalmente
* Apenas **uma operação por vez** ainda é permitida
* Suporta **números grandes** e **decimais**

### 🔗 Demonstração
[Vídeo mostrando a versão 3 da calculadora]()