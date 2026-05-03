import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import pandas as pd


def scrape_anp():
    url = "https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/levantamento-de-precos-de-combustiveis-ultimas-semanas-pesquisadas"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    lista_links = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        lista = soup.find_all("ul")

        if lista is not None:
            for ul in lista:
                elemento_anterior = ul.find_previous_sibling()
                
                if isinstance(elemento_anterior, Tag):
                    texto_anterior = elemento_anterior.get_text(strip=True)

                    if texto_anterior and texto_anterior[0].isdigit():
                        itens_ul = ul.find_all("li")
                        if len(itens_ul) > 1 :
                            link_tag = itens_ul[1].find("a")

                            if link_tag and 'href' in link_tag.attrs:
                                link = link_tag['href'] 
                                print(f"Link encontrado: {link}")
                                lista_links.append(link)
                    
    else:
        print("Erro ao acessar a página. Código:", response.status_code)
    
    return lista_links 

def main():
    links = scrape_anp()
    print(f"Total de links encontrados: {len(links)}")

if __name__ == "__main__":
    main()