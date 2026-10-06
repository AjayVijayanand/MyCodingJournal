# Web experiment

An early look at how a web form talks to a database.

| File | Contents |
| --- | --- |
| `Display.html` | A form for setting up a cricket game: number of players and what each player does on winning the toss |
| `action.php` | Receives the form, connects to a local MySQL server and creates a database |

The MySQL password is read from the `DB_PASSWORD` environment variable.

Built with HTML, PHP and MySQL. For newer web work, see the
[portfolio website](../../PortfolioWebsite).
