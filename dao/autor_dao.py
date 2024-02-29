from model.autor import Autor


class AutorDAO:


    def __init__(self):
        self.__autores: list[Autor] = list()


    def listar(self) -> list[Autor]:
        return self.__autores


    def adicionar(self, autores: Autor) -> None:
        self.__autores.append(autores)


    def remover(self, autores_id: int) -> bool:
        encontrado = False
        for c in self.__autores:
            if (c.id == autores_id):
                index = self.__autores.index(c)
                self.__autores.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, autores_id) -> Autor:
        aut = None
        for c in self.__autores:
            if (c.id == autores_id):
                aut = c
                break
        return aut
   
    def ultimo_id(self) -> int:
        index = len(self.__autores) -1
        if (index == -1):
            id = 0
        else:
            id = self.__autores[index].id
        return id
   
