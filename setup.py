from main import db, Users, Threads, Posts
import hashlib
import os


os.system('cls')

# TODO create the user/database and grant privileges


# create all the tables
print("Blogz assignment setup\n=============================\n")
print("The following procedure will recreate all the needed tables and will populate them with some mock data.\n")
print("The MySQL database 'blogz' must exist prior to continue!")
print("The user 'blogz' must exist. Password 'urdans'")

r = input("Proceed (y/n): ")

if r in ("yY"):
    db.drop_all()
    db.create_all()

    thread = Threads('Is there liquid water on Mars?')
    db.session.add(thread)

    thread = Threads('Why so many programming languages out there?')
    db.session.add(thread)

    thread = Threads('All about ketogenic diet')
    db.session.add(thread)

    thread = Threads("Don't go to scholl, watch YouTube")
    db.session.add(thread)

    user = Users("martian1999", "mart19@gmail.com",
                    hashlib.sha1("martian".encode('utf-8')).hexdigest())
    db.session.add(user)

    user = Users("doubledunder", "mikestephano@aol.com",
                    hashlib.sha1("2dunder".encode('utf-8')).hexdigest())
    db.session.add(user)

    user = Users("urdans", "urdans@gmail.com",
                    hashlib.sha1("urdis".encode('utf-8')).hexdigest())
    db.session.add(user)

    user = Users("theKnight", "blackknight@att.net",
                    hashlib.sha1("knight".encode('utf-8')).hexdigest())
    db.session.add(user)

    post = Posts(1, 3, """New findings from NASA's Mars Reconnaissance Orbiter (MRO) provide the strongest evidence yet that liquid water flows intermittently on present-day Mars.
Using an imaging spectrometer on MRO, researchers detected signatures of hydrated minerals on slopes where mysterious streaks are seen on the Red Planet. These darkish streaks appear to ebb and flow over time. They darken and appear to flow down steep slopes during warm seasons, and then fade in cooler seasons. They appear in several locations on Mars when temperatures are above minus 10 degrees Fahrenheit (minus 23 Celsius), and disappear at colder times.
“Our quest on Mars has been to ‘follow the water,’ in our search for life in the universe, and now we have convincing science that validates what we’ve long suspected,” said John Grunsfeld, astronaut and associate administrator of NASA’s Science Mission Directorate in Washington. “This is a significant development, as it appears to confirm that water -- albeit briny -- is flowing today on the surface of Mars.”
These downhill flows, known as recurring slope lineae (RSL), often have been described as possibly related to liquid water. The new findings of hydrated salts on the slopes point to what that relationship may be to these dark features. The hydrated salts would lower the freezing point of a liquid brine, just as salt on roads here on Earth causes ice and snow to melt more rapidly. Scientists say it’s likely a shallow subsurface flow, with enough water wicking to the surface to explain the darkening.""",
        date="2018-01-24")
    db.session.add(post)

    post = Posts(1, 1, """The spectrometer observations show signatures of hydrated salts at multiple RSL locations, but only when the dark features were relatively wide. When the researchers looked at the same locations and RSL weren't as extensive, they detected no hydrated salt.  
Ojha and his co-authors interpret the spectral signatures as caused by hydrated minerals called perchlorates. The hydrated salts most consistent with the chemical signatures are likely a mixture of magnesium perchlorate, magnesium chlorate and sodium perchlorate. Some perchlorates have been shown to keep liquids from freezing even when conditions are as cold as minus 94 degrees Fahrenheit (minus 70 Celsius). On Earth, naturally produced perchlorates are concentrated in deserts, and some types of perchlorates can be used as rocket propellant.
Perchlorates have previously been seen on Mars. NASA's Phoenix lander and Curiosity rover both found them in the planet's soil, and some scientists believe that the Viking missions in the 1970s measured signatures of these salts. However, this study of RSL detected perchlorates, now in hydrated form, in different areas than those explored by the landers. This also is the first time perchlorates have been identified from orbit.""",
        date="2018-01-24", repply_id=1)
    db.session.add(post)

    post = Posts(2, 2, """New programming languages often learn from existing languages and add, remove and combine features in a new way. There is a few different paradigms like object oriented and functional and many modern languages try to mix features from them both.
There is also new problems that needs to be solved, e.g. the increase of multi-core CPUs. The most common solution to that have been threads, but some programming languages try to solve the concurrency problem in a different way e.g. the Actor Model.""",
        date="2018-05-15")
    db.session.add(post)

    post = Posts(2, 3, """It is a cycle. You start a new language, and you are free to get away from all of the bad syntax and poor choices from your predecessors. In version 1, the language looks great because it doesn't have any of that baggage, and it gets the job done. Then, in newer versions, you start to experiment with features that may not work out, or you bring in features from other, newer languages that cause your syntax to be a little kludgey. Lo and behold, after a few more versions, you realize that your language is now as complicated as the one you replaced, with silly syntax issues and legacy baggage. And suddenly, you realize that if you created a new language, you could fix all that...""",
        date="2018-05-17")
    db.session.add(post)

    post = Posts(2, 2, """For the same reason there are hammers, screwdrivers, handsaws, bandsaws, jackhammers, crowbars, and a host of other tools: not every language is perfect for every task. Some languages are targeted at specific problem domains: R is particularly good for statistical analysis, C is particularly good for writing operating system kernels, Haskell is particularly good for math-heavy or financial computations, Erlang is particularly good at concurrent programming, etc.
Also, for the same reason that shirts come in different colors: some people just like the "style" of one language over another.
And, of course, a lot of programmers find it fun to invent a new language, just to see what happens, or perhaps because they have some knowledge about languages and want to scratch an itch, or try out some ideas.""",
        date="2018-05-18", repply_id=4)
    db.session.add(post)

    post = Posts(4, 4, """It isn't all about cat videos. YouTube generates billions of views a day across news, music, movies, shows, live streams, and vlogs, covering just about every topic you can think of. What's more, all this content is free, as long as you don't mind sitting through a few ads.
Among the millions of hours of uploaded video, you can find a host of educational guides dishing out advice, tutorials, lessons, and more. Which means you can learn a myriad of skills from the comfort of your couch. Here are 8 abilities you can start learning for free.""",
        date="2018-10-01")
    db.session.add(post)

    post = Posts(3, 1, """In essence, it is a diet that causes the body to release ketones into the bloodstream. Most cells prefer to use blood sugar, which comes from carbohydrates, as the body’s main source of energy. In the absence of circulating blood sugar from food, we start breaking down stored fat into molecules called ketone bodies (the process is called ketosis). Once you reach ketosis, most cells will use ketone bodies to generate energy until we start eating carbohydrates again. The shift, from using circulating glucose to breaking down stored fat as a source of energy, usually happens over two to four days of eating fewer than 20 to 50 grams of carbohydrates per day. Keep in mind that this is a highly individualized process, and some people need a more restricted diet to start producing enough ketones.
Because it lacks carbohydrates, a ketogenic diet is rich in proteins and fats. It typically includes plenty of meats, eggs, processed meats, sausages, cheeses, fish, nuts, butter, oils, seeds, and fibrous vegetables. Because it is so restrictive, it is really hard to follow over the long run. Carbohydrates normally account for at least 50% of the typical American diet. One of the main criticisms of this diet is that many people tend to eat too much protein and poor-quality fats from processed foods, with very few fruits and vegetables. Patients with kidney disease need to be cautious because this diet could worsen their condition. Additionally, some patients may feel a little tired in the beginning, while some may have bad breath, nausea, vomiting, constipation, and sleep problems.""",
        date="2018-10-13")
    db.session.add(post)

    db.session.commit()

    print("\n\nAll done!")
    quit()