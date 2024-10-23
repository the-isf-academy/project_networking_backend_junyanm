# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
***My API allows users to post and view exercises and drills specifically catered to improving your swimming ability***

### Model
Swim_Drill : Stores swimming drills and other information about it such as the difficulty, repetitions, and instructions etc.
### Endpoints

*Replace this with a guide to your endpoints and model. You can write a Markdown chart [here](https://www.tablesgenerator.com/markdown_tables)*

|Route Name     |Payload   	                                        |Description   	                              |   	
|---------------|---------------------------------------------------|---------------------------------------------|
|POST/new       |id, distance, instructions, repetitions, difficulty|Creates a new swim drill   	              |
|POST/like   	|id                                                 |Likes a post and shows how many likes it has |
|GET/difficulty |difficulty  	                                    |Returns all drills with the chosen difficulty|
|GET/all   	    |N/A   	                                            |Returns all drills in the database           |   	
|GET/one   	    |id  	                                            |Returns drill with the id selected           |   	



---

## Setup
poetry shell
banjo --debug

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



