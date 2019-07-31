<html>
<body>
<h1> NEWSER</h1>
<h2> THE ULTIMATE CLI TO CHECK INSTANT TOP HEADLINES FROM TOP NEWS SOURCES</h2>
<p>It's basically a command line tool which uses a news api, and shows you the top headlines of daily news, but , according to the user's interests.</p>
<p>The basic tools or libraries used here are 
<ul>
<li>Sockets</li>
<li>MySQL</li>
<li>Requests</li>
<li>OS</li>
<li>JSON</li>
<li>Getpass</li>
</ul>
</p>
<div>In this version of this cli tool we need to run 2 files ,the "main.py" (as a server) , and then run "xterm -e python authenticate.py" using the terminal (basically it acts as the client interface).</div>
<div>This page will ask for basic authentication (signup or login into an existing account) , and then update or check the data in the mysql database which gets create once you clone the repository in system and run the "main.py" file.</div>
<div>Then user's interest are retrieved from the database and sent back to the server file(main.py) , which requests the news from the source , according to the country of user and his/her choice of interests.</div>
<div>The news will then get printed over your terminal screen , according to the genres ( repeated ones will be printed only once )</div>
<div>After the news has been printed , the user has an option to exit immediately, or else the page will auto update , which inturn will clear the terminal and print the updated news (which is after approx 5 minutes , although it depends on the sources ).</div>
  <h3> PLEASE TRY THIS SIMPLE CLI AND GIVE YOUR SUGGESTIONS...</h3>
</body>
</html>
