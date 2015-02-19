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
