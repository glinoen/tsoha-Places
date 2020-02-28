# Käyttäjätarinoita ja niiden SQL-kyselyitä

#### Pystyy aloittamaan uuden keskustelun

Lisätään aihe tauluun Topic:

```SQL 
INSERT INTO Topic (id, date_created, date_modified, name, place_id) 
VALUES (?, 'aika', 'aika muokatessa', 'keskustelun nimi', uuden_aiheen_paikan_id);
```

Id:n kohdalle sqlalchemy laittaa uniikin id:n ja date_created kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään.


#### Pystyy kommentoimaan aiheita


```SQL
INSERT INTO Message (id, date_created, date_modified, topic_id, account_id, content) 
VALUES (?, 'aika', 'aika muokatessa', kommentoitavan_aiheen_id, käyttäjän_id, 'viestin sisältö');
``` 

Id:n kohdalle sqlalchemy laittaa uniikin id:n ja date_created kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään.



#### Pystyy muokkaamaan omaa aihetta

SQL-kysely, jolla muokataan aihetta

```SQL
Update Topic SET Name ='uusi_title', date_modified = 'aika muokatessa' 
WHERE id = muokattavan_aiheen_id;
```

SQL-kysely, jolla muokataan aiheen paikkaa

```SQL
Update Topic SET Topic_id ='uusi_paikka', date_modified = 'aika muokatessa' 
WHERE id = muokattavan_aiheen_id;
```


#### Pystyy poistamaan oman aiheen ja siihen liittyvät kommentit

Aiheen poisto

```SQL 
DELETE FROM Topic WHERE id = poistettavan_aiheen_id;
```

Kommenttien poisto

```SQL 
DELETE FROM Message WHERE Message.topic_id = poistettavan_aiheen_id;
```

#### Pystyy poistamaan oman kommentin


```SQL 
DELETE FROM Message WHERE id = poistettavan_kommentin_id;
```

#### Pystyy muokkaamaan omaa kommenttia

```SQL
Update Message SET message_content ='uusi kommentti', date_modified = 'aika muokatessa' 
WHERE id = muokattavan_kommentin_id;
```




#### Pystyy lukemaan aiheita

SQL-kysely, jolla saa kaikki tietyn aiheen tiedot:

```SQL
SELECT * FROM Topic
WHERE id = threadin_id;
```

SQL-kysely, jolla saadaan aiheeseen liittyvät kommentit: 

```SQL
SELECT Topic.name, Message.date_created, Topic.id, Message.id, Message.content FROM Topic
INNER JOIN Message ON (Message.topic_id = Topic.id);
```

SQL-kysely, jolla saadaan aiheisiin kommentoineet käyttäjät: 

```SQL
SELECT * FROM topic_account;
```

