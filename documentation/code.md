# Requêtes sparql

```sparql
### Most common occupations among astronauts (besides being an astronaut)

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?occupation ?occupationLabel (COUNT(*) AS ?count)
WHERE {
  ?person wdt:P106 wd:Q11631;       # Person is an astronaut
          wdt:P106 ?occupation.     # Get all their occupations
  FILTER(?occupation != wd:Q11631)  # Exclude "astronaut" itself

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?occupation ?occupationLabel
ORDER BY DESC(?count)
LIMIT 20


```
