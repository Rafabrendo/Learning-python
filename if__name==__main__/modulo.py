def soma(x: float, y: float) -> float:
    return x + y


def main() -> None:
    print(soma(10, 20))
    print(soma(20, 20))


#print(__name__)
#isso para quando eu importar o modulo, eu não faça essas execuções
#if __name__ == "__main__":
#   print(soma(10, 20))
#   print(soma(20, 20))

if __name__ == '__main__':
    main()
    #Aqui eu vou chamar a função main()