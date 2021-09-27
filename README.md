
<h1>TicTacToe Game </h1>
<p>I have build tictactoe game using django, javascript,html and css. It is real time game where logged in user can play game with other in same room in real time. It uses concept of websocket and django channels.Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.</p>
<p>The backend is handled by django and front is handled with the help of javascript,css and html.All the authentication information (user login) are saved in database(SQlite).
<h2>Features</h2>
    <ol>
        <li>Real time</li>
        <li>Multi player(two)</li>
        <li>Authentication</li>
    </ol>
<h2>Files and Directories</h2>
<ul>
    <li><mark>game</mark> - Main directory.
        <ol>
            <li><mark>static</mark> - contain all js and css static file.</li>
            <li><mark>templates</mark> - contain all application templates.
                <ol>
                    <li><mark>layout.html</mark> - base layout to be used by other html page.</li>
                    <li><mark>game.html</mark> - layout to be used display game page.</li>
                    <li><mark>index.html</mark> -  layout to be used to display home page</li>
                    <li><mark>login.html</mark> - layout to be used to display login page.</li>
                    <li><mark>register.html</mark> - layout to be used to display register page.</li>
                </ol>
                </li>
            <li><mark>admin.py</mark> - here i addes user class to be displayed in admin user interface.</li>
            <li><mark>routing.py</mark> - urlspattern to consumer.py.</li>
            <li><mark>consumers.py</mark> - it is just like regular views.py but is used for ASGI using django channels to communicate between client and server                using websocket to render the defined views. In this case it is used to communicate information realted to the game between client and server so that               both user can see same information.</li>
            <li><mark>urls.py</mark> -  Contains all view functions for ProjecContains all url paths for Project. </li>
        </ol>
    </li>
    <li><mark>Mygame</mark> - Project directory.</li>
</ul>
<h2>Distinctiveness and Complexity</h2>
    <p><b>Justification</b></p>
    <p>The project is different from other project because of following reason:</p>
    <ul>
        <li>Mobile responsive</li>
        <li>User Authentication</li>
        <li>Real time game</li>
        <Li>Uses concept of websocket</Li>
        <li>Uses django-channels</li>
        <li>Implementation of tictactoe game logic.</li>
    </ul>
<h2>How to run application</h2>
<ul>
    <li>First clone the project.</li>
    <li> Install all the dependencies in requirements.txt.</li>
    <li>Start redis server and run project.(redis-server & python manage.py runserver )</li>
    <li>Register your account.</li>
    <li>Create another dummy account.</li>
    <li>Play game.</li>
</ul>

<h2>Requirements</h2>
<p>ALl the required dependencies are in requirement.txt file. So please install before running the project</p>


