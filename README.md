# Book Tracker

<h2>Description</h2>

Very simple app for tracking how many books you have read from a given date. The app allows 
you to create and edit a reading list, then when you mark a book as read it will adjust the 
counter to show you how many books you have read.

<h2>Running the App</h2>

 - Adjust the start date (hard-coded in core/templates/index.html) to your preferred date
 - Create a local SQL database instance (I am using PostgreSQL)
 - Create a <code>.env</code> file

Your <code>.env</code> file should contain the following:

<code>export FLASK_APP="app.py"</code><br />
<code>export APP_SETTINGS="config.DevelopmentConfig"</code><br />
<code>export DATABASE_URL="your_database_uri"</code><br />
<code>export SECRET_KEY="some_secret_key"</code><br />

Once that's done, in the <code>app</code> directory run:

<code>python app.py</code>

I have not chosen to put this app online, but the basic config is there in <code>config.py</code>
should you wish to add user login/logout and user account functionality to the app and stick it 
on the Web.

<h2>License</h2>

<a href="https://github.com/sedexdev/book_tracker/blob/main/LICENSE">MIT</a>
