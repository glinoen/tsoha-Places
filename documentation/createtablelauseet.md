# CREATE TABLE-lauseet


## Topic

```SQL
CREATE TABLE topic (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(100) NOT NULL, 
	place_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(place_id) REFERENCES place (id)
)
```

## Message

```SQL
CREATE TABLE message (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	topic_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	content VARCHAR(1000) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(topic_id) REFERENCES topic (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
```

## Account

```SQL
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id)
)
```

## Place

```SQL
CREATE TABLE place (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(20) NOT NULL, 
	parent_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES place (id)
)
```

## topic_account

```SQL
CREATE TABLE topic_account (
	topic_id INTEGER, 
	account_id INTEGER, 
	FOREIGN KEY(topic_id) REFERENCES topic (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
```

