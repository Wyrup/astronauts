## Explore Wikidata
```sparql
SELECT (COUNT(*) AS ?numberOfAstronauts)
WHERE {
  ?item wdt:P31 wd:Q5;         # human
        wdt:P106 wd:Q11631.    # astronaut
}
```
