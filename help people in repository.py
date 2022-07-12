import os
os.system('clear') or None

print("bem vindo ao: help people in repository")
print("")
print("help people in repository vem do inglês, ou seja..")
print("ajudar as pessoas no repositório")
print("a ferramenta foi crianda por mim e por um colega")
print("digita 'github' para ver o github do criador")

print(f'''
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/

''')

print("digita ferramentas para ver as que tem")
print("digita 0 para sair")
print("digita clear para limpar")
print("")

loop="positivo"
while loop == "positivo":

    resposta=input("pesquisa o repositório/ferramenta: ")

    #zphisher
    if resposta == "zphisher":
        print ("git clone https://github.com/htr-tech/zphisher ")
        print(f'''
        Zphisher é uma ferramenta poderosa de código aberto Phishing Tool.
        Tornou-se muito popular hoje em dia que é usado para fazer ataques
        de phishing no Target. Zphisher é mais fácil do que o Kit de ferramentas
        de engenharia social.
        ''')
        
    #zaproxy
    elif resposta == "zaproxy":
        print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

    #zaproxy
    elif resposta == "zaprox":
        print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

    #zaproxy
    elif resposta == "zap":
        print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

    #metasploit
    elif resposta == "metasploit":
                print(f'''
                git clone https://github.com/gushmazuko/metasploit_in_termux
                O Projeto Metasploit é um projeto de segurança de
                computadores que fornece informações sobre vulnerabilidades
                de segurança e ajuda em testes de penetração e desenvolvimento
                de assinaturas IDS. É propriedade da Rapid7, empresa de segurança
                sediada em Boston, Massachusetts.
                ''')

    #social engineering
    elif resposta == "social engineering":
            print(f'''
            git clone https://github.com/trustedsec/social-engineer-toolkit
    O Social Engineering Toolkit é uma ferramenta integrada com o Metasploit
    Framework com o objetivo de facilitar os testes, avaliações e ataques 
    relacionados à engenharia social.
            ''')

    #social engineering
    elif resposta == "engenharia social":
            print(f'''
            git clone git clone https://github.com/trustedsec/social-engineer-toolkit

            O Social Engineering Toolkit é uma ferramenta integrada com o Metasploit
            Framework com o objetivo de facilitar os testes, avaliações e ataques 
            relacionados à engenharia social.
            ''')
            
    elif resposta == "":
            print(f'''
            
            ''')

    elif resposta == "":
            print(f'''
            
            ''')

    #clear
    elif resposta == "clear":
            import os
            os.system('clear') or None
            print("bem vindo ao: help people in repository")
            print("")
            print("help people in repository vem do inglês, ou seja..")
            print("ajudar as pessoas no repositório")
            print("a ferramenta foi crianda por mim e por um colega")
            print("digita 'github' para ver o github do criador")
            print(f'''
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/


digita ferramentas para ver as que tem
digita 0 para sair
digita clear para limpar
            ''')

    #ferramentas
    elif resposta == "ferramentas":
            print(f'''
            metasploit
            social engineering
            zaproxy
            zphisher
            são poucas porque a ferramenta tá em beta
            ''')

    #meu github :)
    elif resposta == "github":
            print(f'''
            meu github: https://github.com/UIy2KHDkF6WPXx3k83Df8w
            eu botei meu nome em criptografia pra mim é legal
            ''')

    elif resposta == "0":
        print ("saindo da ferramenta...")
        
        loop="negativo"