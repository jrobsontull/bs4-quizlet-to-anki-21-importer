# bs4-quizlet-to-anki-21-importer
A modern approach for importing quizlet sets into Anki. Uses HTML scraping rather than a Regex/JSON-based approach.

## Challenges with Developing a Quizlet Importer

- Lack of quiz API
- Frequent updates to frontend Quizlet code
   - Means parsing functions need to be constantly updated
- Other add-ons parse the request with Regex and use JSON to handle the result
   - Debugging is hard as code uncommented and numerous transformation functions


## Possible Improvements

- Use Beautiful Soup for HTML parsing
    - Makes debugging easier as can select HTML elements by class
- Useful code comments for quick community fixes
