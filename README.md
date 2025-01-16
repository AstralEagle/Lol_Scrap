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
Nous avons utilisé `request` car il est simple d'utilisation et rapide à mettre en place. Il ne nécessite pas de grande configuration et permet de récupérer très facilement les informations dont nous avons besoin. De plus, nous avons une certaine appétence avec cette librairie.

### Flash
Nous avons utilisé `flask` car, tout comme `request`, il est simple d'utilisation et rapide à mettre en place. De plus, il est très léger Ce qui permettra de charger rapidement la page, car le scrapping mettra beaucoup de temps vu la quantité de champions dans le jeu League of Legends.