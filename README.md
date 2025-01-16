# Scrap League Of Legend Champions

## Installation

```bash
pip install -r requirements.txt
```

## Launch

### Web Site

```bash
python app.py
```
### Listing All Champions

```bash
python main.py
```


## Explication

### Request
Nous avons utilisé `requests` car c'est la lib la plus simple afin de pouvoir faire des requêtes en python, elle est aussi très utilisé donc c'est plus simple pour debug

### Flash
Nous avons utilisé `flask` car, il est simple d'utilisation et rapide à mettre en place. De plus, il est très léger Ce qui permettra de charger rapidement la page, car le scrapping mettra beaucoup de temps vu la quantité de champions dans le jeu League of Legends.