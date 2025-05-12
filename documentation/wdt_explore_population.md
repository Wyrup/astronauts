## Explore Wikidata
We try to see the basics knowledge of the population of astronauts.
### Inspecting the numbers of people qualified as astronauts
```sparql
SELECT (COUNT(*) AS ?numberOfAstronauts)
WHERE {
  ?item wdt:P31 wd:Q5;         # human
        wdt:P106 wd:Q11631.    # astronaut
}
```
### Inspecting Modern astronauts (born after the end of the Apollo program)
```sparql
SELECT (COUNT(*) AS ?modernAstronauts)
WHERE {
  ?item wdt:P31 wd:Q5;
        wdt:P106 wd:Q11631;
        wdt:P569 ?birthDate.

  BIND(REPLACE(str(?birthDate), "(.*)([0-9]{4})(.*)", "$2") AS ?year)
  FILTER(xsd:integer(?year) > 1972)
}
```
### Inspecting the property of the astronauts in a certain section of time
```sparql
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?p ?propLabel (COUNT(*) AS ?eff)
WHERE {
  ?item wdt:P106 wd:Q11631;  # astronaut
        wdt:P569 ?birthDate;
        ?p ?o.

  BIND(REPLACE(str(?birthDate), "(.*)([0-9]{4})(.*)", "$2") AS ?year)
  FILTER(xsd:integer(?year) >= 1950 && xsd:integer(?year) <= 1980)

  ?prop wikibase:directClaim ?p.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?p ?propLabel
ORDER BY DESC(?eff)
```
### Most common occupations among astronauts (besides being an astronaut)
```sparql
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
### Sexe distribution among the astronauts
```sparql
SELECT ?sexLabel (COUNT(*) AS ?n)
WHERE {
  ?person wdt:P106 wd:Q11631;
          wdt:P21 ?sex.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?sexLabel
ORDER BY DESC(?n)
```
### Nationality distribution among the astronauts
```sparql
SELECT ?countryLabel (COUNT(*) AS ?n)
WHERE {
  ?person wdt:P106 wd:Q11631;
          wdt:P27 ?country.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?countryLabel
ORDER BY DESC(?n)
```
### Most frequented educational school
```sparql
SELECT ?educationLabel (COUNT(*) AS ?n)
WHERE {
  ?person wdt:P106 wd:Q11631;
          wdt:P69 ?education.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?educationLabel
ORDER BY DESC(?n)
```
### Which organisation does the astronauts belongs to
```sparql
SELECT ?orgLabel (COUNT(*) AS ?n)
WHERE {
  ?person wdt:P106 wd:Q11631;
          wdt:P463 ?org.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?orgLabel
ORDER BY DESC(?n)

```

