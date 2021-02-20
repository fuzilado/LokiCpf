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

    request = requests.get('http://191.235.78.142/cpf.php?cpf={}'.format(cpf))

    address_data = request.json()

    if 'status' not in address_data:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print('\033[1;32m>\033[1;35m>\033[1;32m>\033[1;34m ENCONTRADO! \033[1;32m<\033[1;35m<\033[1;32m<')
        print()
        print('\033[1;36mNome\033[1;33m:\033[1;92m {}'.format(address_data['nome']))
        print('\033[1;36mNome da mae\033[1;33m:\033[1;92m {}'.format(address_data['nomeMae']))
        print('\033[1;36mNome do pai\033[1;33m:\033[1;92m {}'.format(address_data['nomePai']))
        print('\033[1;36mSexo\033[1;33m:\033[1;92m {}'.format(address_data['sexoDescricao']))
        print('\033[1;36mCor\033[1;33m:\033[1;92m {}'.format(address_data['racaCorDescricao']))
        print('\033[1;36mTipo Sanguineo\033[1;33m:\033[1;92m {}'.format(address_data['tipoSanguineo']))
        print('\033[1;36mData Nascimento\033[1;33m:\033[1;92m {}'.format(address_data['dataNascimento']))
        print('\033[1;36mNacionalidade\033[1;33m:\033[1;92m {}'.format(address_data['nacionalidade']))
        print('\033[1;36mPais Nascimento\033[1;33m:\033[1;92m {}'.format(address_data['paisNascimento']))
        print('\033[1;36mMunicipio Nascimento\033[1;33m:\033[1;92m {}'.format(address_data['municipioNascimentoSemUF']))
        print('\033[1;36mEmail Principal\033[1;33m:\033[1;92m {}'.format(address_data['emailPrincipalValidado']))
        print('\033[1;36mEndereco Codigo\033[1;33m:\033[1;92m {}'.format(address_data['enderecoCodigo']))
        print('\033[1;36mRua\033[1;33m:\033[1;92m {}'.format(address_data['enderecoLogradouro']))
        print('\033[1;36mCasa\033[1;33m:\033[1;92m {}'.format(address_data['enderecoNumero']))
        print('\033[1;36mComplemento\033[1;33m:\033[1;92m {}'.format(address_data['enderecoComplemento']))
        print('\033[1;36mBairro\033[1;33m:\033[1;92m {}'.format(address_data['enderecoBairro']))
        print('\033[1;36mCep\033[1;33m:\033[1;92m {}'.format(address_data['enderecoCep']))
        print('\033[1;36mRg\033[1;33m:\033[1;92m {}'.format(address_data['rgNumero']))
        print('\033[1;36mListaCns\033[1;33m:\033[1;92m {}'.format(address_data['listaCns']))

    else:
        print('\033[1;31mNão encontrado')

    opt = input('\n\033[1;33mDeseja fazer uma nova consulta? \033[1;32ms\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')
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
