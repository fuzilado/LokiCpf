import requests
import os
from time import sleep

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[1;36mBem vindo ao \033[1;41mLokiCpf\033[0;0m \n
        \033[1;35mDigite o numero do \033[1;41m\033[1;36mcpf\033[0;0m\033[1;35m sem - ou .\n   
    """)

    cpf = input("\033[1;34m>>> \033[1;36m")
    print("\n\033[1;92mConsultando... Aquarde\n")

    request = requests.get('http://104.41.5.41:12345/cpf.php?lista={}'.format(cpf))

    address_data = request.json()

    if 'erro' not in address_data:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print('\033[1;32m>\033[1;35m>\033[1;32m>\033[1;34m ENCONTRADO! \033[1;32m<\033[1;35m<\033[1;32m<')
        print()
        print('\033[1;36mNome\033[1;33m:\033[1;92m {}'.format(address_data['Nome']))
        print('\033[1;36mNascimento\033[1;33m:\033[1;92m {}'.format(address_data['Nacimento']))
        print('\033[1;36mRua\033[1;33m:\033[1;92m {}'.format(address_data['Nologradouro']))
        print('\033[1;36mCasa\033[1;33m:\033[1;92m {}'.format(address_data['Nrlogradouro']))
        print('\033[1;36mBairro\033[1;33m:\033[1;92m {}'.format(address_data['Bairro']))
        print('\033[1;36mCep\033[1;33m:\033[1;92m {}'.format(address_data['Cep']))
        print('\033[1;36mCidade\033[1;33m:\033[1;92m {}'.format(address_data['Municipio'])) 
        print('\033[1;36mEstado\033[1;33m:\033[1;92m {}'.format(address_data['Estado']))
        print('\033[1;36mMae\033[1;33m:\033[1;92m {}'.format(address_data['Mae']))
        print('\033[1;36mComplemento\033[1;33m:\033[1;92m {}'.format(address_data['Complemento']))
        print()

    opt = input('\033[1;33mDeseja fazer uma nova consulta? \033[1;32ms\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')
    if opt == 's':
        main()

    if opt == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;31m
+----------------------------------------------------------------------------+
| Criador: Near Shelby                                                       |
| Canal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ/featured   |
| Git Hub: https://github.com/nearshelby-yt                                  |
| Instagram: @nearshelby_yt                                                  |
| Twitter: @NearShelby                                                       |
| Telegram: @NearShelby_yt                                                   |
+----------------------------------------------------------------------------+
        """)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;35m
+----------------------------------------------------------------------------+
| Criador: Near Shelby                                                       |
| Canal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ/featured   |
| Git Hub: https://github.com/nearshelby-yt                                  |
| Instagram: @nearshelby_yt                                                  |
| Twitter: @NearShelby                                                       |
| Telegram: @NearShelby_yt                                                   |
+----------------------------------------------------------------------------+
        """)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;36m
+----------------------------------------------------------------------------+
| Criador: Near Shelby                                                       |
| Canal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ/featured   |
| Git Hub: https://github.com/nearshelby-yt                                  |
| Instagram: @nearshelby_yt                                                  |
| Twitter: @NearShelby                                                       |
| Telegram: @NearShelby_yt                                                   |
+----------------------------------------------------------------------------+
        """)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;32m
+----------------------------------------------------------------------------+
| Criador: Near Shelby                                                       |
| Canal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ/featured   |
| Git Hub: https://github.com/nearshelby-yt                                  |
| Instagram: @nearshelby_yt                                                  |
| Twitter: @NearShelby                                                       |
| Telegram: @NearShelby_yt                                                   |
+----------------------------------------------------------------------------+
        """)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;33m
+----------------------------------------------------------------------------+
| Criador: Near Shelby                                                       |
| Canal: https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ/featured   |
| Git Hub: https://github.com/nearshelby-yt                                  |
| Instagram: @nearshelby_yt                                                  |
| Twitter: @NearShelby                                                       |
| Telegram: @NearShelby_yt                                                   |
+----------------------------------------------------------------------------+
        """)

    else:
        print("\033[1;35mTchauzinho +_+")

if __name__== '__main__':
    main()
