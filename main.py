import streamlit as st

yearbookCalled = False
artNhsCalled = False
busNHSCalled = False
redCrossCalled = False
scienceNHSCalled = False
sagaCalled = False

st.title("Welcome to club suggest")
st.markdown("***")
st.write("Here is how it works. Select the boxes which relate to you. Once you have selected all the boxes you want, "
         "continue below to a list of clubs as well a description and some information")
st.markdown("***Disclaimer: *** This site may not contain all clubs and/or may contain some clubs that are no longer "
            "running")

st.markdown("***")







################################################ Clubs ################################################
def acadec():
    with st.expander("Academic Decathlon"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.7tgntmnyw8f4)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/academic-decathlon)")
        st.markdown("*Contact Emails: *  \n"
                    "Mr.McCarthy: mccarthyk@franklinps.net  \n"
                    "Mr. Gary Reynolds: reynoldsg@franklinps.net")
        st.write(" ")
        st.write("The Academic Decathlon team is made up of nine students in A,B, or C categories based on their "
                 "G.P.A. Students compete in the areas of literature, social science, science, fine arts, math, "
                 "economics, and the Super Quiz. The topics in each area change yearly, and the schools with the "
                 "highest totals go on to the final state competition in March. At that time an essay, an interview, "
                 "and two speeches are added to the test and the Super Quiz portions. The school with the highest "
                 "point total goes to the national competition in April.")


# def alzheimerAwareness():# no info
#     " "

def artNHS(ran):
    global artNhsCalled
    if not ran:
        artNhsCalled = True
        with st.expander("Art NHS"):
            st.markdown("[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/honor-societies#h.77wyrzi6yeyj)  \n"
                        "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/art-national-honor-society)")
            st.markdown("*Contact Email:*  \n"
                        "Ms. Amy Edson: edsona@franklinps.net")
            st.markdown("Classroom code: --- None Given --- ")
            st.write("")
            st.write(
                "The purpose and mission are to:  \n - recognize those students who have shown outstanding dedication and commitment to art and design  \n - foster excellence in the pursuit of art and design  \n - encourage originality, innovation, and technique in the society’s members, as well as throughout the art department  \n - provide leadership in building community through art and design to the school and district  \n - increase awareness of art and design in relation to other areas of the school curriculum")

def bestBuddies():
    with st.expander("Best Buddies"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.vt76xqv5tc1w)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/best-buddies)")
        st.markdown("*Contact Emails: *  \n"
                    "Ms. Miriam Connolly: connollm@franklinps.net  \n"
                    "Mr. Nelson Corona: coronan@franklinps.net  \n"
                    "Ms. Mackenzie Easterbrooks: easterbrooksm@franklinps.net  \n"
                    "Ms. Laura Hayes: hayesl@franklinps.net  \n"
                    "Ms. Amanda Notz: notza@franklinps.net")
        st.write("")
        st.write("Best Buddies is an international organization designed to match students with disabilities with "
                 "their typical peers to create one-to-one friendships. Everyone is welcome and encouraged to "
                 "contribute to our group. Our meetings are after school every other Thursday with a combination of "
                 "informal gatherings and structured activities. We are also involved in some outside get-togethers "
                 "such as bowling, dances, going to the movies, attending high school events and sports etc. This is "
                 "a great place for all to make new friends")


# def bAndg(): #board and games # no info
#     " "

def businessNHS(ran):
    global busNHSCalled
    if not ran:
        busNHSCalled = True
        with st.expander("Business National Honor Society"):
            st.markdown(
                "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/business-national-honor-society)")
            st.markdown("*Contact Emails:*  \n"
                        "Mr. Paul Cadenhead: cadenheadp@franklinps.net  \n"
                        "Mr. Miguel Carmo: carmom@franklkinps.net")
            st.markdown("Classroom code: --- Not Given ---")
            st.write("")
            st.write("This club will bring honor and national recognition to our students who are part of our business "
                     "education department.")

# def book(): no info
#     " "

def chess():
    with st.expander("Chess Club"):
        st.markdown(
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/chess-club)  \n"
            "[Site](https://sites.google.com/franklinps.net/fhs-chess-club/home)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Byron Szymeczko: szymeczkob@franklinps.net")
        st.write("")
        st.markdown("Classroom code: [q2bauf4](https://classroom.google.com/c/MzgxOTA0MDE1MDBa?cjc=q2bauf4)")
        st.write("Welcome to the Chess Club, a warm, inviting, and entertaining environment in which to play one of "
                 "the most strategic games ever created. The one game that stretches for every bit of knowledge you "
                 "possess, reaches for it in order to outplay your opponent. Chess is one of the most fun and "
                 "brain-testing sports out there, and we invite you to give it a try. Whether you are a state "
                 "champion or someone who has never touched a rook in their life, we can guarantee a great learning "
                 "experience and challenging opponents. Join us to enhance your knowledge of the game through casual "
                 "tournaments and fun scrims, and meet others who share similar interests. We hope to see you there!")


# def classics(): no info
#     " "

def communityService():
    with st.expander("Community Service Club"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.h6pq49ybk1yq)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/community-service-club)")
        st.markdown("*Contact Email:  \n"
                    "Ms. Johnna MacLean: macleanj@franklinps.net")
        st.markdown("Classroom code: brt2mr4")
        st.write("")
        st.write("The Community Service Club is student run and we have about 100 members. Students find service "
                 "opportunities through public outreach and students sign up online. We have worked with large "
                 "organizations such as the Salvation Army, Relay for Life, and Making Strides.  We also work locally and "
                 "have collaborated with elementary and middle schools, police and fire associations, food pantry, "
                 "etc... We are always open to suggestions for new activities as well.")


def computers():
    with st.expander("Computers Club"):
        st.markdown("[Site](https://fhscomputerclub.github.io/Website/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.4femh6v45xa8)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/computer-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Trevor Barron: barront@franklinps.net")
        st.markdown("Classroom code: [echxrly](https://classroom.google.com/c/Nzg5MjU1NTg1Mlpa?cjc=echxrly)")
        st.write("")
        st.write(
            "The computer club was established to promote student  learning and collaboration in all things related "
            "to computers and technology. Students meet to discuss emerging topics in the field of computing, "
            "gain experience with hardware and software, and explore computer technology in general. No experience "
            "required.")


def cancer():
    with st.expander("Connect 4 Cancer"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.nddlf16kckea)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/connect-4-cancer)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Colleen Gordon: gordonc@franklinps.net")
        st.markdown("Classroom code: gmwceaq")

        st.write("")
        st.write("The three essential parts of this club are advocacy, education and awareness. We would like to "
                 "raise awareness about the disease to FHS students and the Franklin community. We aim to raise funds "
                 "and also provide to the local hospitals and cancer patients, while also providing club members and "
                 "the larger FHS community with a better understanding of the disease.")


def deca():
    with st.expander("DECA"):
        st.markdown("[Site](https://www.deca.org/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.pk28c23x1xa9)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/deca)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Miguel Carmo: carmom@franklinps.net  \n"
                    "Mr. Paul Cadenhead: cadenheadp@franklinps.net")
        st.markdown("Classroom code: rvt6dtx")
        st.write("")
        st.write("DECA prepares emerging leaders and entrepreneurs to be college and career ready.")


def diversity():
    with st.expander("Diversity Awareness Club"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.g1chejualltw)  \n"
            "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/diversity-awareness-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Paul O'Donaghue: odonoghuep@franklinps.net")
        st.markdown("Classroom code: 3t5tpyd")
        st.write("")
        st.write("The goal of the group is to raise awareness among students and staff by representing different "
                 "cultures in many ways. All students and staff are welcome.")


def emptyBowls():
    with st.expander("Empty Bowls Club"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.pni0qxe48c3p)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/empty-bowls-club)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Brenna Johnson: johnsonb@franklinps.net")
        st.write("")
        st.write("Franklin High School is participating in an international charity project called Empty Bowls, "
                 "which supports food based education and fundraising initiatives in local communities around the "
                 "world. The first part of this project is to make 300 ceramic bowls with students at FHS, "
                 "students within the Franklin SchoolDistrict, and community members. Then, the Empty Bowls Club and "
                 "the Franklin Food Pantry will co-host a community meal of soup and bread. The fundraiser will take "
                 "place either online or at FHS in May 2021.All proceeds raised at this event through ticket sales, "
                 "a silent auction, and a Giving Wall are donated directly to The Franklin Food Pantry.")


def theaterCompany():
    with st.expander("FHS Theater Company"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/visual-performing-arts#h.5vpq0alrsoar)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/drama-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Grossman: grossmans@franklinps.net")
        st.markdown("Classroom code: [lfpdost](https://classroom.google.com/c/MTYzMDM0ODY1MjI1?cjc=lfpdost)")
        st.write("")
        st.write("Theater Company is an after-school organization where students are encouraged to showcase their "
                 "acting, designing, lighting, sound, and video skills. We put on plays and musicals throughout the "
                 "year where students are able to express themselves creatively and make friends along the way. ")


def FAA():
    with st.expander("Franklin Arts Academy"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/visual-performing-arts#h.z26zzzr4dgak)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/franklin-arts-academy)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Skylar Grossman, FAA Director: grossmans@franklinps.net  \n"
                    "Ms. Helen Hoffenberg: hoffenbergh@franklinps.net  \n"
                    "tarantoa@franklinps.net: tarantoa@franklinps.net")
        st.markdown("Classroom code: w4emk5g")
        st.write("")
        st.markdown("The Franklin Arts Academy (FAA) is a rich Academic Program that fosters the link between "
                    "critical and creative thinking through academic rigor, high expectations, and interdisciplinary "
                    "connections with the Arts. Students flourish in the community-focused FAA through multiple "
                    "intelligence approaches to learning. Furthermore, the FAA offers both Honors and College "
                    "Preparatory course credit levels.Begun in 2010, Franklin Arts Academy is a three-year pathway "
                    "within Franklin High School. FAA prepares a diverse community of aspiring scholars and artists "
                    "to be successful in their college and professional careers and to be engaged members of our "
                    "democratic society. FAA operates as a focused learning community within the comprehensive school "
                    "system of FHS.Students can become part of the FAA through application their Sophomore or Junior "
                    "year.**Since this is not a club, there is no activity fee associated with joining the FAA.**")


def girlUP():
    with st.expander("Girl Up"):
        st.markdown("[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h"
                    ".ljvl9ii4zu9g)  \n[Description site]("
                    "https://www.franklinps.net/franklin-high-school/clubs-activities/pages/girl)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Andrea Brear: breara@franklinps.net")
        st.write("")
        st.write("Girl Up is a non-profit organization that advocates for girls rights in other countries (Liberia, "
                 "Guatemala, India, Malawi, Uganda, Ethiopia) and for specific issues such as woman’s health rights, "
                 "birth certificates, and education for refugees. It is a part of the United Nations Organization. "
                 "The focus is investing in the girls of our future.")


def girlsWhoCode():
    with st.expander("Girls Who Code"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.d7ip721dvd8r)  \n"
            "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/girls-who-code)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Alyssa Taranto: tarantoa@franklinps.net")
        st.markdown("Classroom code: 5c4axz6")
        st.write("")
        st.write("Girls who code is a nonprofit organization which aims to support and increase the number of women "
                 "in computer science by equipping young women with the necessary computing skills to pursue 21st "
                 "century opportunities")


def greenTeam():
    with st.expander("Green Team"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.7cflfkmf6vi)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/green-team)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Kasey Kilbride: kilbridek@franklinps.net")
        st.markdown("Classroom code: zvvmh27")
        st.write("")
        st.write("Green Team is FHS’ environmental club. We discuss environmental issues and solutions, and provide "
                 "awareness on such topics and sustainable living to the community and ourselves,especially through "
                 "creative outlets. Some of our past activities include making awareness posters and building "
                 "hydroponics, a plant-growing system using recycled water to grow plants, in which we grow food used "
                 "by the cafeteria. We hope to continue this, as it got disrupted by the school shut down last year.")


def happiness():
    with st.expander("Happiness Club (40% Club)"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/more-clubs-activities#h.vfzt1suzqkop)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/happiness-club)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Carolyn Beaton: beatonc@franklinps.net  \n"
                    "Mr. Jack McKay: Mckayj@franklinps.net")
        st.markdown("Classroom code: klag2tm")
        st.write("")
        st.write("The Happiness Club (The 40%) seeks to improve the overall happiness of club members, the school, "
                 "and the Franklin community.  The objective of the first meeting is to discuss happiness, "
                 "find ways to overcome stress and anxiety, and to plan a happiness initiative for the following "
                 "meeting.  On that second meeting, we will meet briefly but then the focus of the meeting will be to "
                 "carry out a happiness initiative so that others may feel a better state of happiness in their "
                 "lives. Any student who either is happy or would like to become happier should consider joining this "
                 "club. We aspire to change the world.")


def hiking():
    with st.expander("Hiking Club"):
        st.markdown("[Site](https://sites.google.com/franklinps.net/fhs-hiking-club/home)  \n"
                    "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/hiking-club)")
        st.markdown("*Contact Emails: *  \n"
                    "Ms. Chaisson: chaissone@franklinps.net  \n"
                    "Ms. Balliro: ballirom@franklinps.net")
        st.markdown("*Classroom Code:* qs6ktti")


def jazz():
    with st.expander("Jazz Band"):
        st.markdown(
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/jazz-band)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Leighanne Rudsit: rudsitl@franklinps.net")
        st.write("")
        st.write(" --- No information can be found. Email advisor for information --- ")


# def latinNHS():
#     " "


def math():
    with st.expander("Math Team"):
        st.markdown("[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/math-team)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Jason Chetlen: chetlenj@franklinps.net")
        st.markdown("Classroom code: --- Not found. Email advisor for code --- ")
        st.write("")
        st.write("The FHS Math Team is a competitive team that competes in the Southeastern Mass Math League "
                 "consisting of 30 schools. Teams participate in 4 meets held at each school in their respective "
                 "division on the first Thursday of November, December, January and February. The top teams compete "
                 "in the State Meet in March.")


def mock():
    with st.expander("Mock Trial"):
        st.markdown("[Site](https://sites.google.com/franklinps.net/fhs-mock-trial/announcements)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/government-politics#h.bbf99otc3h6j)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/mock-trial-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Michael Walsh (V): walshm@franklinps.net  \n"
                    "Mr. John Perkins (JV): perkinsj@franklinps.net")
        st.markdown("Classroom code: n4inotj")
        st.write("")
        st.write("In Mock Trial Club, students learn the rules and procedures of the courtroom experience.   They "
                 "study a case, rehearse and perform as attorneys or witnesses.  The Mock Trial Club meets regularly "
                 "for students who are at the beginning or intermediate level of Mock Trial.  Club competitions are "
                 "limited to intersquad performances.")


def modCongress():
    with st.expander("Model Congress"):
        st.markdown("[Site](https://fhsmodelcongress.weebly.com)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/government-politics#h.gmkmj1c3vp2o)  \n"
                    "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/model-congress)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. John Perkins: perkinsj@franklinps.net")
        st.markdown("Classroom code: 75gn5l7")
        st.write("")
        st.write("Students in Model Congress learn parliamentary procedures, prepare and defend proposed bills, "
                 "and participate in active debate.  A regional competition occurs in April for those who qualify.   "
                 "All students are welcome.")


def musicPro():  # and podcast club
    with st.expander("Music Production/ Podcast club"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/visual-performing-arts#h.dwtl7jt7rpgs)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/music-production-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Matthew Geisinger: geisingerm@franklinps.net")
        st.markdown("Classroom code: ttmylci")
        st.write("")
        st.write("Music Production/Podcast Club is a place where we learn to produce music both by using software "
                 "instruments as well as by recording live instruments. We also learn about mixing, editing, "
                 "and effects processing of music.Students can also record and produce podcasts and learn to edit "
                 "these on the computer, by cutting, fading, putting in music, and sound effects. We have "
                 "professional level gear for all of these endeavours. We host open mic nights throughout the year. "
                 "Anyone is welcome to perform or attend these events. Open mic nights will be held online this year "
                 "until further notice. Sign-ups for these events and info for attendance will be provided on the "
                 "club google classroom page as well as on Twitter. ")


def nhs():
    with st.expander("National Honor Society"):
        st.markdown("[Site](https://www.nhs.us/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/honor-societies#h.5elxsy1h2mgx)  \n"
                    "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/national-honor-society-fhs-chapter)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Nelson Corona: coronan@franklinps.net  \n"
                    "Dr. Charles Fidler: fidlerc@franklinps.net")
        st.markdown("Classroom code: -- Must be invited --- ")
        st.write("")
        st.write("The National Honor Society (NHS) is the nation’s premier organization established to recognize "
                 "outstanding high school students. More than just an honor roll, NHS serves to recognize "
                 "those students who have demonstrated excellence in the areas of scholarship, service, leadership, "
                 "and character. These characteristics have been associated with membership in the organization "
                 "since its beginning in 1921.Today, it is estimated that more than one million students participate "
                 "in NHS activities. NHS chapters are found in all 50 states, the District of Columbia, Puerto Rico, "
                 "many U.S. territories, andCanada. Chapter membership not only recognizes students for their "
                 "accomplishments, but challenges them to develop further through active involvement in school "
                 "activities and community service.")


def oskey():
    with st.expander("OSKEY Production"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/visual-performing-arts#h.dvz8xegkb9s2)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/oskey-production)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Skylar Grossman: grossmans@franklinps.net")
        st.markdown("Classroom code: fqegtpv")
        st.write("")
        st.write("This club is put together so the class of 2021 can work on OSKEY and prepare for the performance in "
                 "the Spring. Any Senior is welcome to join the club and get their hands on any aspect of the show ("
                 "script writing, performing, theater tech and more!) ")


def pantherbook():
    with st.expander("Pantherbook"):
        st.markdown("[Site](https://franklinpanthers.us/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/more-clubs-activities#h.8jdo4lw72nyi)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/pantherbook-newspaper-club)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Leighton: leightonj@franklinps.net")
        st.markdown("Classroom code: e4e6cap")
        st.write("")
        st.write("Calling all writers, photographers, and videographers! Pantherbook, Franklin High School’s online "
                 "newspaper, is seeking new staff members. The best part of Pantherbook is the complete freedom staff "
                 "members have over what topics they "
                 "choose to discuss. What are you interested in? Click the site below to see some of our most popular "
                 "articles on each subject.")


def peerLeader():
    with st.expander("Peer Leaders"):
        st.markdown(
            "[Application information](https://docs.google.com/document/d/121V5D8hcDPhrcSHwX5pDvvYrsT2_gF6gHYuq0WEJ_Hw/edit)  \n"
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/more-clubs-activities#h.prlnkfipf1df)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/peer-leadership)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Jennifer Briggs: briggsj@franklips.net  \n"
                    "Ms. Michelle Hess: hessm@franklinps.net")
        st.markdown("Classroom code: --- not given --- ")
        st.write("")
        st.write("The Franklin High School Peer Leaders are a group of compassionate and responsible students who "
                 "choose to lead by example. In this role, students choose to abstain from dangerous substances and "
                 "take on many important roles in the school. The leaders not only help ease the transition of "
                 "underclassmen or new students, but they also volunteer over the summer at the high school "
                 "orientation and at every open house/parent night that FHS offers. The Peer Leaders also facilitate "
                 "many school and community programs. Peer leaders demonstrate their care and compassion for others "
                 "throughout the year.")


def redCross(ran):
    global redCrossCalled
    if not ran:
        redCrossCalled = True
        with st.expander("Red Cross Club"):
            st.markdown(
                "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.vk959oszq0bq)  \n"
                "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/red-cross-club)")
            st.markdown("*Contact Email:*  \n"
                        "Mr. Nicholas Bailey: baileyn@franklinps.net")
            st.markdown("Classroom code: 4uonujy")
            st.write("")
            st.write("This club is an extension of the American Red Cross Organization and is specifically meant for High "
                     "School Students. Any member of the club is automatically a Red Cross Volunteer and will receive "
                     "volunteer hours.")


def robotics():
    with st.expander("Robotics Club"):
        st.markdown("[Site](https://sites.google.com/franklinps.net/fhsrobotics/home)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.fl81w5ce487s)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/robotics-club)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Alyssa Taranto: tarantoa@franklinps.net")
        st.markdown("Classroom code: 2qi5cek")
        st.write("")
        st.write("The Franklin High School Robotics Team is a club for anyone who has an interest in Engineering, "
                 "Coding, or Computers and applying those skills to design and build robots for competition. The club "
                 "welcomes all students and no prior knowledge of robotics is needed! ")


def sadd():
    with st.expander("Students Against Destructive Decisions"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.94gmtu38678i)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/sadd)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Kristin Letendre: bletendrek@franklinps.net")
        st.markdown("Classroom code: h65evqy")
        st.write("")
        st.write("Franklin High School is participating in an international charity project called Empty Bowls, "
                 "which supports food based education and fundraising initiatives in local communities around the "
                 "world. The first part of this project is to make 300 ceramic bowls with students at FHS, "
                 "students within the Franklin SchoolDistrict, and community members. Then, the Empty Bowls Club and "
                 "the Franklin Food Pantry will co-host a community meal of soup and bread. The fundraiser will take "
                 "place either online or at FHS in May 2021.All proceeds raised at this event through ticket sales, "
                 "a silent auction, and a Giving Wall are donated directly to The Franklin Food Pantry.")


def scienceNHS(ran):
    global scienceNHSCalled
    if not ran:
        scienceNHSCalled = True
        with st.expander("Science National Honor Society"):
            st.markdown("[Site](https://sciencenhs.org/)  \n"
                        "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/science-national-honor-society)")
            st.markdown("*Contact Email:*  \n"
                        "Ms. Jennifer Curley: curleyj@franklinps.net  \n"
                        "Mr. Joe Chung: chungj@franklinps.net")
            st.markdown("Classroom code: owm6gno")
            st.write("")
            st.write("FHS Science National Honor Society is an honor bestowed upon juniors and seniors")


def scienceOlympiad():
    with st.expander("Science Olympiad Club"):
        st.markdown("[Site](https://www.soinc.org/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.bypea27wawy)  \n"
                    "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/science-olympiad-club)")
        st.markdown("*Contact Email:*  \n"
                    "Dr. Charles Fidler: fidlerc@franklinps.net")
        st.markdown("Classroom code: 4gwxhhz")
        st.write("")
        st.write(
            "The Science Olympiad is a national organization that covers all types of science topics including "
            "biology, chemistry, physics, earth science and engineering. Students should express interest in "
            "participating in science knowledge and problem solving competitions. Annually, approximately 60 schools "
            "compete in State competitions with finalists advancing to National level events.")

def saga(ran):
    global sagaCalled
    if not ran:
        sagaCalled = True
        with st.expander("Sexuality & Gender Awareness (SAGA)"):
            st.markdown(
                "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.94gmtu38678i)  \n"
                "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/sexuality-gender-awareness-club)")
            st.markdown("*Contact Email:*  \n"
                        "Ms. Achin-Housman: achinr@franklinps.net  \n"
                        "Mx. H. Bialer: bialerh@franklinps.net")
            st.markdown("Classroom code: 6stzduj")
            st.write("")
            st.write("The goal of the Sexuality and Gender Awareness Club is to educate and bring awareness about the "
                     "LGBTQ+ issues at Franklin High School and the larger world community. We meet once a week to "
                     "discuss current events in the community and help bring about change where needed in FHS by "
                     "advocating for the LGBTQ+ students.")



def skiAndBoard():
    with st.expander("Ski & Board Club"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/more-clubs-activities#h.yjdy5go3lfls)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/ski-board-club)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Julia Zarbetski: zarbetskij@franklinps.net")
        st.markdown("Classroom code: himni40")
        st.write("")
        st.write(
            "The Ski and Board Club meets on Tuesdays after school starting in Jan. 2021 (depending on COVID situation). We leave right after school and head to Wachusett MT  - returning to FHS at 9 PM. We take 6 trips!")


def studentGov():
    with st.expander("Student Government"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/government-politics#h.ay66vitgiki)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/student-government)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. John Leighton: leightonj@franklinps.net  \n"
                    "Mr. Dustin Picillo: picillod@franklinps.net")
        st.markdown("Classroom code: pd2ohy7")
        st.write("")
        st.write("The goals of student government are to solve student issues, facilitate communication between "
                 "students and administration, serve the greater community, and improve the student experience at "
                 "Franklin High School. Student government representatives and officers are leaders seeking a more "
                 "active role in their community. Any student is welcome at our meetings to bring an issue to light "
                 "or suggest a new idea, and all are encouraged to run as representatives for their class.")


def tastebuds():
    with st.expander("Tastebuds"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.2m14tho4rfrw)  \n"
            "[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/tastebuds)")
        st.markdown("*Contact Email:*  \n"
                    "Ms Kaleigh Rodarte: rodartek@franklinps.net")
        st.markdown("Classroom code: acc6ft2")
        st.write("")
        st.write("Our mission is to connect with other community members and share our love of cooking, as well as to "
                 "benefit Franklin as a whole. We meet once a month to bake and decorate together, and coordinate "
                 "bake sales and other fundraisers in order to raise money for the Franklin Food Pantry. We collect "
                 "canned goods, run food drives, share recipes, and revel in the joy of sweet treats!")


def unifiedMusic():
    with st.expander("Unified Music Club"):
        st.markdown("[Description site](https://www.franklinps.net/fhs/clubs-activities/pages/unified-music-club)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Leighanne Rudsit: rudsitl@franklinps.net")
        st.markdown("Classroom code: --- not given. Contact Advisor if interested --- ")


def worldOfDiffernce():
    with st.expander("World of Difference"):
        st.markdown(
            "[Site](https://www.adl.org/who-we-are/our-organization/signature-programs/a-world-of-difference-institute)  \n"
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/awareness-charities#h.gkxvl5eqbd79)  \n"
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/world-of-difference)")
        st.markdown("*Contact Email:*  \n"
                    "Ms. Jenna Calcagno: calcagnoj@franklinps.net  \n"
                    "Ms. Shannon Picillo: picillos@franklinps.net")
        st.markdown("Classroom code: esbv7vv")
        st.write("")
        st.write("The mission of A World of Difference (tm) is to recognize bias and the harm it inflicts on "
                 "individuals and society, build understanding of the values and benefits of diversity, "
                 "improve intergroup relations and confront racism, anti-Semitism, and all other forms of bigotry. A "
                 "World of Difference leaders will facilitate conversations with their peers about these topics. ")


def yearbook(ran):
    global yearbookCalled
    if not ran:
        yearbookCalled = True
        with st.expander("Yearbook"):
            st.markdown(
                "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/academic-clubs#h.xc6mu9sd44u1)  \n"
                "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/yearbook)")
            st.markdown("*Contact Email:*  \n"
                        "Ms. Alyssa Taranto: tarantoa@franklinps.net")
            st.markdown("Classroom code: --- Not given")
            st.write("")
            st.write("The yearbook is a full year, 3 credit, course that students can enroll in as early as Sophomore "
                     "year. Students in this class will be responsible for designing, editing, and producing  the  annual "
                     " OSKEY Yearbook on the computer using the Adobe Creative Suite  and Jostens Publishing software. "
                     "This includes  page design, copywriting, proofreading, editing and photography.")

def youngInvestors():
    with st.expander("Young Investors Society"):
        st.markdown(
            "[Description site](https://www.franklinps.net/franklin-high-school/clubs-activities/pages/young-investors-society)")
        st.markdown("*Contact Email:*  \n"
                    "Mr. Paul Cadenhead: cadenheadp@franklinps.net")
        st.markdown("Classroom code: gbjfq5r")
        st.write("")
        st.write("The Mission of the Young Investors Society is to prepare the next generation of outstanding "
                 "investors. This will be accomplished by pursuing the following principles:  \n - Vision:  The Young "
                 "Investors Society seeks to inspire kids to think critically for themselves.  To evaluate business "
                 "and the world around them with insightful, long-term perspectives.  \n - Real-life Experience:  Youth "
                 "will get actual, hands-on experience evaluating companies, building financial models, and buying "
                 "and selling stocks.  \n - Leadership:  Each local chapter of the Young Investor Society will be run by "
                 "the students, recommending and investing in stocks themselves, organizing business and financial "
                 "professional visits, and mentoring new members.")


def triM():
    with st.expander("Tri M Music Honor Society"):
        st.markdown("[Site](https://www.musichonors.com/)  \n"
                    "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/honor-societies#h.nnc39bfgqa9c)  \n")
        st.markdown("*Contact Email:*  \n"
                    "Mrs. Beatrice: beatrices@franklinps.net  \n"
                    "Mrs. Plouffe: plouffed@franklinps.net")
        st.markdown("Classroom code: --- Not given. Contact Advisors for information --- ")
        st.write("")
        st.write(
            "The Music Honor Society")


def mirageLiteracy():
    with st.expander("Mirage Literacy Magazine"):
        st.markdown(
            "[Club fair site](https://sites.google.com/franklinps.net/fhsclubfair/visual-performing-arts#h.gqkqbbwynjvq)  \n")
        st.markdown("*Contact Email:*  \n"
                    " --- None Given --- ")
        st.markdown("Classroom code: lheh6yv")
        st.write("")
        st.write(
            "Franklin High's literacy magazine")


currentIssues = st.checkbox(
    "Do you feel you are interested in current-world issues?")  # alzheimer awareness, connect4cancer, diversity awareness, empty bowls, girl up, green team, red cross, SAGA, world of difference

arts = st.checkbox(
    "Are you interested in the arts?")  # Art NHS, FHS theater company, FAA, OSKEY production, yearbook

learning = st.checkbox(
    "Are you interested in academic oriented clubs?")  # Acadec, Math team, science NHS, Science olympiad

schoolImpacting = st.checkbox(
    "Are you interested in community-impacting clubs?")  # Best buddies, community service, 40%, Pantherbook Newspaper Club, red cross, SADD, SAGA, yearbook, tastebuds

busAndFinance = st.checkbox("Are you interested in business and finance?")  # business NHS, DECA, young investors

govAndPol = st.checkbox(
    "Are you interest in Government and politics?")  # Mock trial, Model congress, peer leadership, Student government

honorSociety = st.checkbox(
    "Are you interested in joining some honor societies?")  # Art NHS, business NHS, Latin NHS, NHS, Science NHS
if honorSociety:
    st.caption("I would suggest not going specifically for all honor societies in hope of it looking good on your "
               "resume. Go for the ones that interest you. Additionally, for most, you need to be in a certain grade "
               "to join, so make sure to pay attention to that")

adventure = st.checkbox("Are you interested in adventure?")  # hiking, Ski and board club

technology = st.checkbox("Are you interested in engineering/technology")  # computer club, Girls who code, robotics

music = st.checkbox(
    "Are you interested in music?")  # jazz band, Music production/podcast club, unified music, tri-m


# other: board and games, Book Club, Chess Club, Classics club,  Mirage literacy magazine
st.markdown("***")
st.header("Here are your suggestions")
if currentIssues:
    greenTeam()
    cancer()
    diversity()
    emptyBowls()
    girlUP()
    redCross(redCrossCalled)
    saga(sagaCalled)
    worldOfDiffernce()

if arts:
    artNHS(artNhsCalled)
    theaterCompany()
    FAA()
    oskey()
    yearbook(yearbookCalled)

if learning:
    acadec()
    math()
    scienceNHS(scienceNHSCalled)
    scienceOlympiad()

if schoolImpacting:
    bestBuddies()
    communityService()
    happiness()
    pantherbook()
    redCross(redCrossCalled)
    sadd()
    saga(sagaCalled)
    yearbook(yearbookCalled)
    tastebuds()

if busAndFinance:
    businessNHS(busNHSCalled)
    deca()
    youngInvestors()

if govAndPol:
    mock()
    modCongress()
    peerLeader()
    studentGov()

if honorSociety:
    artNHS(artNhsCalled)
    businessNHS(busNHSCalled)
    nhs()
    scienceNHS(scienceNHSCalled)

if adventure:
    hiking()
    skiAndBoard()

if technology:
    robotics()
    computers()
    girlsWhoCode()


if music:
    jazz()
    musicPro()
    unifiedMusic()
    triM()

st.markdown("***")
st.header("Here are some other interesting clubs")
chess()
mirageLiteracy()
st.markdown("***")
st.caption("Developed by Arav Tyagi. View code here: https://github.com/TyagiArav/Club_Suggest")
