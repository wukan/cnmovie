# CNMovie

Display Chinese Movie Showing in U.S. Theater
- A cron job create movie showtime job every day (or week).
- A movie showtime job fetches movie showtimes, and create movie info jobs.
- For each movie job, send API request to OMDb and write the movie info to database.
- Send digest email of in-theater Chinese movies every week.

Database columns
- ID
- Name
- Showtime
- Updated At
- Created At
- Country
- Other Info

Flixster API
- Theater: http://api.flixster.com/api/v1/showtimes/getTheaters?zip=94122&deviceType=RTO
- Showtimes: http://api.flixster.com/api/v1/showtimes/getShowtimes?theaters=322224933&theaters=322225107&theaters=322224998&theaters=322225382&theaters=764946741&theaters=322225130&theaters=322225333&theaters=322225035&theaters=322225265&theaters=322225225&theaters=764947053&theaters=322224919&theaters=322224957&theaters=341814388&theaters=322224902&theaters=341814416&theaters=322225099&theaters=322225002&theaters=322225365&theaters=764947029&date=2015-02-19&deviceType=RTO
