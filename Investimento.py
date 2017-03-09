class investimento:
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, item):
        if item in ["data_compra","valor_investimento","data_vencimento","taxa_compra","taxa_adm","taxa_inflacao","valor_liquido"]:
                   return self.__dict__[item]
