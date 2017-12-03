# CSEqual (Computer Science Equality Photo Booth Application)
A photo booth web application to be used at social gatherings such as Hackathons. Provides the ability for client entertainment as well as the ability to collect age and gender data for future analysis.

## The Idea
The intention of this project was to a fun application that could also provide social change. Bridging the gender gap in the STEM fields, especially in STEM fields related to technology is currently a priority across the world. Having equal representation of male and female participants at events such as Hackathon's ensures fair access to education, increases diversity, improves creativity and allows the world to become more inclusive as a whole. By making a photo booth application that tracks gender and age without any external intervention, data is collected without any extra hassle. Photo booths are already common equipment at such events due to their social entertainment value, however using our web application it can provide much more than that.

## How It Works
The web application is built using HTML, CSS and javascript hosted on GitHub's pages for simplicity. The javascript ensures that the camera is enabled for the user, photos can be captured and downloaded, and is responsible for making REST API calls to the backend. The IBM Watson Visual Recognition API is provided the image and in turn returns inform based on the user's face. This includes gender, age, clothing etc. The web application will save this data per each session to show a summary of who attended the event. Currently the summary is limited to participant's gender. The application does support multiple individuals in each image and allows the images to be saved locally for later distribution. The HTML and CSS are used for formatting and designing the application as a whole. Node JS was used for all backend processing involved for manipulating the data received by the IBM Watson Visual Recognition API.

## Tools Used
* IBM Watson Visual Recognition API : https://www.ibm.com/watson/services/visual-recognition/
* GitHub Pages : https://pages.github.com
* Node Js : https://nodejs.org/en/

## How to use
1. Clone this repository
2. Launch the backend by executing "node app.js". Ensure NodeJs is installed and any other prerequisites necessary.
3. Navigate to http://localhost:3000/ to test out the app locally. See screenshots below for information on how to use the user interface.

## Expansion Ideas
 * Host the backend on a cloud server.
 	* Currently the backend is hosted on a local machine which is not condusive to multiple front end units or for transferring the application between computers. Launching the backend on a server can be as simple as running "node app.js" in an Amazon AWS or Microsoft Azure instance.
 * Include more statistics in summary, including age, emotion (happy, sad, angry), and ethnicity.
 * Provide an in-depth report with creative visuals for displaying trend information.
 	* Could make use of ElasticSearch and Kibana for displaying visuals such as graphs.
 * Improve the user interface and appearance of the application.
 * Purchase domain for Front End application.
 * Ensure individuals are not double-counted.
 	* Can be done by using "compare" functionality of IBM Watson Visual Recognition API.

## Screenshots
Front Page:
* Live camera view can be seen on the left hand side.
* Image can be captured by pressing "Take my Photo!" button.
* If satisfied with image start analysis and picture download by pressing "Download Photo and Run Analysis!".
![alt text](https://github.com/johan1252/CSEqual/blob/master/Screenshots/Start_Screen.png?raw=true)

Loading Screen displayed for 1-2 seconds after pressing "Download Photo and Run Analysis!":
![alt text](https://github.com/johan1252/CSEqual/blob/master/Screenshots/Analyzing.png?raw=true)

Results Screen:
* Instant results displayed in left hand bottom corner.
* Cumulative gender summary results seen in right hand bottom corner.
![alt text](https://github.com/johan1252/CSEqual/blob/master/Screenshots/Results.png?raw=true)

## Authors
* Parv Mital
* Johan Cornelissen
