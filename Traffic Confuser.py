#!/usr/bin/python3

# ______  ______  _______        ______   ______  __    __ ________ __    __  ______  ________ _______       _______  __      __         _____ __    __ __       ______  ______       __       __ ________ __        ______  
#|      \/      \|       \      /      \ /      \|  \  |  \        \  \  |  \/      \|        \       \     |       \|  \    /  \       |     \  \  |  \  \     |      \/      \     |  \     /  \        \  \      /      \ 
# \▓▓▓▓▓▓  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\    |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓\ | ▓▓ ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\    | ▓▓▓▓▓▓▓\\▓▓\  /  ▓▓        \▓▓▓▓▓ ▓▓  | ▓▓ ▓▓      \▓▓▓▓▓▓  ▓▓▓▓▓▓\    | ▓▓\   /  ▓▓ ▓▓▓▓▓▓▓▓ ▓▓     |  ▓▓▓▓▓▓\
#  | ▓▓ | ▓▓___\▓▓ ▓▓__/ ▓▓    | ▓▓   \▓▓ ▓▓  | ▓▓ ▓▓▓\| ▓▓ ▓▓__   | ▓▓  | ▓▓ ▓▓___\▓▓ ▓▓__   | ▓▓__| ▓▓    | ▓▓__/ ▓▓ \▓▓\/  ▓▓           | ▓▓ ▓▓  | ▓▓ ▓▓       | ▓▓ | ▓▓  | ▓▓    | ▓▓▓\ /  ▓▓▓ ▓▓__   | ▓▓     | ▓▓  | ▓▓
#  | ▓▓  \▓▓    \| ▓▓    ▓▓    | ▓▓     | ▓▓  | ▓▓ ▓▓▓▓\ ▓▓ ▓▓  \  | ▓▓  | ▓▓\▓▓    \| ▓▓  \  | ▓▓    ▓▓    | ▓▓    ▓▓  \▓▓  ▓▓       __   | ▓▓ ▓▓  | ▓▓ ▓▓       | ▓▓ | ▓▓  | ▓▓    | ▓▓▓▓\  ▓▓▓▓ ▓▓  \  | ▓▓     | ▓▓  | ▓▓
#  | ▓▓  _\▓▓▓▓▓▓\ ▓▓▓▓▓▓▓     | ▓▓   __| ▓▓  | ▓▓ ▓▓\▓▓ ▓▓ ▓▓▓▓▓  | ▓▓  | ▓▓_\▓▓▓▓▓▓\ ▓▓▓▓▓  | ▓▓▓▓▓▓▓\    | ▓▓▓▓▓▓▓\   \▓▓▓▓       |  \  | ▓▓ ▓▓  | ▓▓ ▓▓       | ▓▓ | ▓▓  | ▓▓    | ▓▓\▓▓ ▓▓ ▓▓ ▓▓▓▓▓  | ▓▓     | ▓▓  | ▓▓
# _| ▓▓_|  \__| ▓▓ ▓▓          | ▓▓__/  \ ▓▓__/ ▓▓ ▓▓ \▓▓▓▓ ▓▓     | ▓▓__/ ▓▓  \__| ▓▓ ▓▓_____| ▓▓  | ▓▓    | ▓▓__/ ▓▓   | ▓▓        | ▓▓__| ▓▓ ▓▓__/ ▓▓ ▓▓_____ _| ▓▓_| ▓▓__/ ▓▓    | ▓▓ \▓▓▓| ▓▓ ▓▓_____| ▓▓_____| ▓▓__/ ▓▓
#|   ▓▓ \\▓▓    ▓▓ ▓▓           \▓▓    ▓▓\▓▓    ▓▓ ▓▓  \▓▓▓ ▓▓      \▓▓    ▓▓\▓▓    ▓▓ ▓▓     \ ▓▓  | ▓▓    | ▓▓    ▓▓   | ▓▓         \▓▓    ▓▓\▓▓    ▓▓ ▓▓     \   ▓▓ \\▓▓    ▓▓    | ▓▓  \▓ | ▓▓ ▓▓     \ ▓▓     \\▓▓    ▓▓
# \▓▓▓▓▓▓ \▓▓▓▓▓▓ \▓▓            \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓   \▓▓\▓▓       \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓\▓▓   \▓▓     \▓▓▓▓▓▓▓     \▓▓          \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓\▓▓▓▓▓▓ \▓▓▓▓▓▓      \▓▓      \▓▓\▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓ \▓▓▓▓▓▓ 
LICENSE = """
MIT License

Copyright (c) 2022 Julio Melo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Contributors: Julio Melo
Licensed under the MIT License
"""                                                                                                                                                                                                                            
                                                                                                                                                                                                                            
try:
    import random, os
    from ssl import SSL_ERROR_INVALID_ERROR_CODE, SSL_ERROR_SSL, SSL_ERROR_WANT_CONNECT
    from colorama import init
    import requests as r
    from time import sleep
    init(convert=True)
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print("Parece que existem algumas bibliotecas faltando.., deseja instalar? S/n")
    modules = input("")
    if modules == "s":
        print("Instalando bibliotecas...")
        os.system("pip install requests")
        os.system("pip install colorama")
        print("\nExecute o programa novamente.")
        exit()
    else:
        print("Saindo.")
        exit()

#LISTA DE URLS + HEADERS ##190 SITES
url = ['http://hulu.com', 'http://google.com','http://facebook.com', 'http://youtube.com', 'http://juliostravino.com.br','http://pt.wikipedia.org', 'http://globo.com', 'http://instagram.com', 'http://www.windows93.net', 'http://letras.mus.br', 'http://alertabahia.com.br', 'http://futebolplayhd.com', 'http://r7.com', 'http://neilpatel.com/br/', 'http://tuasaude.com', 'http://netshoes.com.br', 'http://www.tiktok.com/', 'http://elitepvpers.com', 'http://naver.com', 'http://msn.com', 'http://qq.com', 'https://www.tp-link.com', 'http://tencent.com', 'http://dropbox.com', 'http://instructure.com', 'http://google.fr', 'http://deviantart.com', 'http://cricbuzz.com', 'http://theguardian.com', 'http://daum.net','http://ikea.com','http://ifeng.com','http://samsung.com','http://mozilla.org','http://shaparak.ir','http://foxnews.com','http://rctiplus.com','http://ninisite.com', 'http://hubski.com','http://www.codecademy.com','http://www.whatshouldireadnext.com','http://thisissand.com','http://www.poptropica.com','http://youarelistening.to','http://www.dafont.com/','http://mint.intuit.com','http://mint.intuit.com','http://www.uninove.br','http://www.unicid.edu.br','http://www.guiadacarreira.com.br','http://www.instructables.com','http://www.snopes.com','http://estacio.br','http://www.unifesp.br','http://www.mackenzie.br','http://metodista.br','http://www.mercadolivre.com.br','http://www.mercadolivre.com.br','http://www.chess.com','http://www.netflix.com/br/','http://www.detran.sp.gov.br/','http://www.sptrans.com.br','http://www.ifood.com.br','http://exame.com','http://www.vakinha.com.br','http://www.tse.jus.br','http://www.mediafire.com','http://m.sendspace.com','http://mega.io','http://sertao.com.br','http://noticiasdatv.uol.com.br','http://medicinadosertao.com.br','http://ccrl.chessdom.com','http://pt.quora.com','http://www.skype.com','http://www.estadao.com.br','http://broadcast.com.br','http://www.kenoby.com','http://www.udemy.com','http://www.nasa.gov','http://www.folha.uol.com.br','http://www.cruzvermelha.org.br','http://www.campograndenews.com.br','http://www.reddit.com','http://www.conexos.com.br','http://en.bignox.com','http://archive.org','https://tribunnews.com','https://merdeka.com','https://www.akamai.com','https://flipkart.com','https://hao.com','https://nytimes.com','https://ok.ru','https://www.ebay.com','https://iqiyi.com','https://kompas.com','https://espn.com','https://freepik.com','https://animeflv.net','https://www.xerox.com','https://nicovideo.jp','https://metropoles.com','https://intuit.com','http://www.donothingfor2minutes.com','https://ikea.com','https://huanqiu.com','https://www.apple.com','https://proiezionidiborsa.it','https://healthline.com','https://sciencedirect.com','https://namu.wiki','https://stripe.com','https://healthline.com','https://readmanganato.com','https://ninisite.com','https://hdfcbank.com','https://formula.com','https://divar.ir','https://rtbrvdirect.com','https://sindonews.com','https://remove.bg','https://outbrain.com','https://sporx.com','https://fardanews.com','https://www.microsoft.com','https://lowes.com','https://zoho.com','https://vaghtesobh.com','https://ign.com','https://livejournal.com','https://ultimate-guitar.com','https://eluniverso.com','https://alodokter.com','https://repubblica.it','https://miookiloogif.com','https://springer.com','https://saednews.com','https://snapchat.com','https://files.wordpress.com','https://protonmail.com','https://convertio.co','https://www.lacoste.com/us/','https://imagetwist.com','https://asus.com','https://beeg.com','https://flashscore.com','https://inews.id','https://banvenez.com','https://togetter.com','https://usnews.com','https://nyaa.si','https://pcgamer.com','https://stanford.edu','https://www.gov.uk','https://made-in-china.com','https://shomanews.com','https://btnull.re','https://wordhippo.com','https://nextdoor.com','https://asos.com','https://newgrounds.com','https://lefigaro.fr','https://business.site','https://hindustantimes.com','https://azure.com','https://indiatoday.in','https://nature.com','https://momoshop.com.tw','https://dogdrip.net','https://smallseotools.com','https://dictionary.com','https://ithome.com','https://norton.com','https://xiaomi.com','https://tenor.com','https://emojipedia.org','https://lifewire.com','https://katfile.com','https://last.fm','https://videosection.com','https://olx.pl','https://ctrip.com','https://www.sri.com','https://superuser.com','https://funimation.com','https://docusign.com','https://utorrent.com','https://cisco.com','https://imgbox.com']
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4369.0 Safari/537.36"}
#LISTA DE URLS + HEADERS

def requests():
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT)
    for k in range(xexec):
        sleep(xsleep)
        try:
            arrx =len(url)
            arrx = arrx - 1
            i = random.randint(0,arrx)
            x = r.get(url[i],timeout=xtimeout,headers=headers)
            print(Fore.GREEN + url[i] + " - STATUS: 200 OK" + Back.BLACK + Style.BRIGHT)
            k + 1
        except r.ConnectionError:
            print(Fore.RED + "Ocorreu um erro de CONEXÃO, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except r.exceptions.Timeout:
            print(Fore.YELLOW + "Ocorreu um erro de TIMED-OUT, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except IndexError:
            print(Fore.YELLOW + "Ocorreu um erro de INDEX, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except SSL_ERROR_SSL:
            print(Fore.YELLOW + "Ocorreu um erro de SSL, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except SSL_ERROR_WANT_CONNECT:
            print(Fore.YELLOW + "Ocorreu um erro de SSL, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except SSL_ERROR_INVALID_ERROR_CODE:
            print(Fore.YELLOW + "Ocorreu um erro de SSL, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except requests.exceptions.SSLError:
            print(Fore.YELLOW + "Ocorreu um erro de SSL, " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Style.BRIGHT+Fore.MAGENTA + "{}".format(logo))
            print(Fore.GREEN + "\n" + Back.BLACK + Style.BRIGHT)
            print(Style.BRIGHT+Fore.YELLOW + "{}".format(end))
            break
        except:
            print(Fore.RED + "Ocorreu um erro desconhecido. " + Back.BLACK + Style.BRIGHT + 'ao acessar o site: {}'.format(url[i]))
        continue

def main():
    global xtimeout ,xsleep, xexec
    xtimeout = int(input('Digite o TIMEOUT de cada request [3]Recomendado :'))
    xsleep = int(input('Digite a velocidade entre cada REQUEST [4]Medio [1]Rapido(Perigoso) [6]Recomendado : '))
    xexec = int(input('Numero de vezes deseja EXECUTAR o programa: [999] : '))
    requests()
    return

logo = """░▀█▀░▒█▀▀▀█░▒█▀▀█░░░█▀▄░▄▀▀▄░█▀▀▄░█▀▀░█░▒█░█▀▀░█▀▀░█▀▀▄░░░█▀▀▄░█░░█░░░░░░▒█░█░▒█░█░░░▀░░▄▀▀▄░░░▒█▀▄▀█░█▀▀░█░░▄▀▀▄
░▒█░░░▀▀▀▄▄░▒█▄▄█░░░█░░░█░░█░█░▒█░█▀░░█░▒█░▀▀▄░█▀▀░█▄▄▀░░░█▀▀▄░█▄▄█░░░░░░▒█░█░▒█░█░░░█▀░█░░█░░░▒█▒█▒█░█▀▀░█░░█░░█
░▄█▄░▒█▄▄▄█░▒█░░░░░░▀▀▀░░▀▀░░▀░░▀░▀░░░░▀▀▀░▀▀▀░▀▀▀░▀░▀▀░░░▀▀▀▀░▄▄▄▀░░░▒█▄▄█░░▀▀▀░▀▀░▀▀▀░░▀▀░░░░▒█░░▒█░▀▀▀░▀▀░░▀▀░
"""
end = """░▒█▀▀▀█░█▀▀▄░█▀▀▄░░▀░░█▀▀▀░█▀▀▄░█▀▄░▄▀▀▄░░░▄▀▀▄░▄▀▀▄░█▀▀▄░░░█░▒█░█▀▀░█▀▀▄░█▀▀▄
░▒█░░▒█░█▀▀▄░█▄▄▀░░█▀░█░▀▄░█▄▄█░█░█░█░░█░░░█▄▄█░█░░█░█▄▄▀░░░█░▒█░▀▀▄░█▄▄█░█▄▄▀
░▒█▄▄▄█░▀▀▀▀░▀░▀▀░▀▀▀░▀▀▀▀░▀░░▀░▀▀░░░▀▀░░░░█░░░░░▀▀░░▀░▀▀░░░░▀▀▀░▀▀▀░▀░░▀░▀░▀▀
"""

os.system('cls' if os.name == 'nt' else 'clear')
print(Style.BRIGHT+Fore.MAGENTA + "{}".format(logo))
print(Fore.GREEN + "" + Back.BLACK + Style.BRIGHT)
main()
