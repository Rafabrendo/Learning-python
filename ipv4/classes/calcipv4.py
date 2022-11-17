import re
#Expressões regulares

class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()


    @property
    def rede(self):
        return self._rede


    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()



    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('Ip inválido.') #vou subir uma exceção se o ip não validar

        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)



    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        if not self._valida_ip(valor):
            raise ValueError('Máscara inválida')


        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        #Se eu já tiver mandado/configurado o prefixo. Daí não vai dar erro com essa condição
        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            #se não tem valor(None) não vai passar. vai retornar none. Se tem valor, o not transforma em falso
            #e daí, esse bloco não é executado
            return

        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser interiro.')

        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 bits.')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')


        #se eu já tiver enviado, daí não vai dar erro
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)


    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    #converti ip para binários
    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        #vai converter os numeros para binarios
        #fiz um fatiamento dentro, começando do 2
        #zfill vai preencher com zeros a esquerda
        return ''.join(blocos_binarios)#vou retornar os numeros juntos


    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0,32,n)]
        #vai gerar blocos dos ip's fatiados
        #int(x, base=2) vai retornar a mascar, já com os calculos feitos
        return '.'.join(blocos)


    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._broadcast


    def _get_numero_ips(self):
        return 2 ** (32-self.prefixo) - 2
        #Se eu não tivesse colocaddo o -2, eu teria a quantidade real
