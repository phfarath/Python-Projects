import bcrypt

class GerenciadorSenha:
    @staticmethod
    def gerar_hash_senha(senha):
        """
        Gera um hash seguro para a senha fornecida.
        """
        # Gera o salt para adicionar aleatoriedade ao hash
        salt = bcrypt.gensalt()
        # Gera o hash da senha
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return hash_senha

    @staticmethod
    def verificar_senha(senha, hash_senha):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.
        """
        # Compara a senha fornecida com o hash 
        return bcrypt.checkpw(senha.encode('utf-8'), hash_senha)

if __name__ == "__main__":
    # Usuário insere a senha
    senha_usuario = input('Digite sua senha: ')

    # Criptografa a senha
    hash_armazenado = GerenciadorSenha.gerar_hash_senha(senha_usuario)
    print(f"Hash armazenado: {hash_armazenado.decode()}")

    # Verifica a senha
    senha_tentativa = input('Tente sua senha criada: ')
    if GerenciadorSenha.verificar_senha(senha_tentativa, hash_armazenado):
        print("A senha está correta!")
    else:
        print("Senha incorreta!")
