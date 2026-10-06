# Study Grove

A website my team built and deployed for the iNTUition Hackathon in 2021.

Study Grove is a study planner: you sign in with a Google account and the
site reads your Google Calendar so that notes, timelines and tasks sit in
one place.

| File | Contents |
| --- | --- |
| `StartPage.html` | Landing page |
| `home.html` | Main page, with Google sign-in and the calendar view |
| `Scripts.js` | Signs the user in and fetches their events through the Google Calendar API |
| `styles.css` | Styling |

To run it, create a Google Cloud project with the Calendar API enabled and
put your own client ID and API key at the top of `Scripts.js`.

Built with HTML, CSS, JavaScript and the Google Calendar API.
