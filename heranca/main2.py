"""
Biblioteca
    Interface(Biblioteca) -> metodo_interface
        metodo_da_interface


main2 -> interface(está instanciando a interface)

"""


from heranca.tiraDuvidas.interface import Interface

#no main vai ser usado só a Interface porque a interface já herda de Biblioteca

i1 = Interface()
#i1.metodo_da_interface()
i1.chama_metodo_da_interface()