# Yhteenvetokyselyt

### 1. 

Kysely, joka selvittää milloin viimeisin viimeisin viesti on kirjoitettu aiheeseen

```SQL
SELECT Topic.id, MAX(Message.date_created) FROM Message
LEFT JOIN Topic ON Topic.id = Message.topic_id
GROUP BY Topic.id, Message.date_created
ORDER BY Message.date_created DESC;
```

### 2.

Kysely, joka kertoo kuinka monta vastausta aiheessa on

```SQL
SELECT Topic.id, COUNT(Message.topic_id) as count FROM Topic
INNER JOIN Message ON Topic.id = Message.topic_id
GROUP BY Topic.id
ORDER BY count DESC;
```
