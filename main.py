from bitcubit_compiler.lexer import tokenize
from bitcubit_compiler.parser import parse
from bitcubit_compiler.codegen import generar_codigo

if __name__ == "__main__":
    #código de ejemplo de BIT&CUBIT Tours
    codigo = "total = 5 + 3;"

    print("Código fuente:")
    print(codigo)
    print("\nTokens:")
    tokens = list(tokenize(codigo))
    for t in tokens:
        print(t)

    print("\nÁrbol sintáctico:")
    parsed = parse(tokens)
    print(parsed)

    print("\nCódigo generado:")
    result = generar_codigo(parsed)
    print(result)