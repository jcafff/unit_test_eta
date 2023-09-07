class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido' # Retorno errado, tava 'Nme invalido'
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido' # Retorno errado, tava 'Nome invalio'
        if '%' in name:
            return 'Nome invalido'

        if len(number) <= 0: # Uma lista/dicionário não tem como ter um valor menor que 0, tava 'if len(number) < 0'
            return 'Numero invalido' # Retorno Errado, tava 'Numero invalid'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido' # Retorno inválido, tava 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido' # Retorno Inválido, tava 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido' # Retorno Inválido, tava 'Nome nvalido'

        return self.entries[name]

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return list(self.entries.keys()) # tava sem cast de list(entries.keys()), assim: return self.entries.keys()

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        return list(self.entries.values()) # tava sem cast de list(entries.values()), assim: return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name: # not in deveria ser "in", tava 'if search_name not in name'
                result.append((name, number)) # troquei as {name, number} por (name, number), pra formar uma tupla e n um dict
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items()) # Não está fazendo nada, apenas retornando o dicionário do jeito que está, tava 'return self.entries'

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), reverse=True) # Não está fazendo nada, apenas retornando o dicionário do jeito que está, tava 'return self.entries'

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'
