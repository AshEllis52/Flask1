from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
	return("Hello World!") #indent this line
if __name__ == "__main__":
	app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080

	
	<!DOCTYPE html>
<html>
<head>
	<title> Mayo Fishing Lodge</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	<div id="wrapper">
		<header>
			<ul class="nav-links">
				<li class="nav-link-button-active">Home</li>
				<a href="gallery/index.html">
					<li class="nav-link-buttons">Gallery</li>
				</a>
				<a href="fishing/index.html">
					<li class="nav-link-buttons">Amenities</li>
				</a>
				<a href="contact/index.html">
					<li class="nav-link-buttons">Contact</li>
				</a>
			</ul>
		</header>
		
		<main>
			<h1>"Not all those who wander are lost" - J.R.R. Tolkien</h1>

				<div id="Intro-Text">

				<h2>  Mayo Fishing Lodge </h2>


				<div id="Intro-Text-Left"> 
			<p> Situated above the beautiful Callow Lake in central Mayo, our Fishing Lodge is the dream getaway. Sit in the back garden and watch the birds in trees or take a walk by the lake to see the Swans and Otters. We have a 6 person rowboat that can be used to crusie the lake and find the best spots to fish the native brown trout.

				<ul class="entire"> 
				<span class="iconify" data-icon="fa-solid:house-user" data-inline="false"></span> Entire Home <br>
				You will have the entire house to yourself. </ul>


				<ul class="amenities">
				<span class="iconify" data-icon="mdi:alpha-a-circle" data-inline="false"></span> Amenities<br>
				Five Beds, Three Bathrooms, Full Kitchen, Parking, Row Boat, Fishing Gear </ul>

				<ul class="location">
				<span class="iconify" data-icon="bx:bxs-compass" data-inline="false"></span> Location<br>
				Central Mayo, 35 Kilometers from Knock Airport </ul>

				<a href="fishing/index.html">
				<ul class="AmLink"> see more... </ul>
				</a>
			</p>



				</div>

					
					<div id="Intro-Text-Right">
					<div id="first-row">
						<a href="gallery/index.html" target="_blank"> 
						<img src="Images/fish.jpg" alt="Picture of  fish">
						</a>
					</div>
					
					<div id="second-row">
						<a href="gallery/index.html" target="_blank"> 
						<img src="Images/lake3.jpg" alt="Picture of the lake">
						</a>
					</div>
						</div>
							</div>
						

					

				<div id="Intro-Text2"> 
					<div id="Intro-Text2-Left">
						<h3> Reviews</h3>
			<p> 
				<li> 
				This is without doubt one of the best fishing lodges in Ireland. Kevin puts in so much work to make the angler enjoy the best of Irish fishing. Facilities are first class and the fish guiding services by Kevin are first class. - Mark Wahlberg <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				</li>
				<br>
				<li> 
				What a place to stay, peace and quiet, and when the fishing is good it's really good. If you don't fish its still a great place to relax and forget about the day to day grind, well worth a visit.  - Keanu Reeves <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				</li>
				<br>
				<li> 
				Would highly recommend a stay here anytime of the year. Kevin is very welcoming and friendly. Anytime we needed anything it wasn’t an issue. Beautiful scenery with Lough Callow at your door step. - George Bush jr <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				<span class="fa fa-star checked"></span>
				</li>


			</p>

			</div>
					<div id="Intro-Text2-Right">
					<div id="third-row">
						<a href="gallery/index.html" target="_blank"> 
						<img src="Images/drive.jpg" alt="Picture of the drive">
						</a>
					</div>
					
					<div id="fourth-row">
						<a href="gallery/index.html" target="_blank"> 
						<img src="Images/sun.jpg" alt="Picture of the sun">
						</a>
					</div>
							</div>
									</div>			
		</main>

	</div>

	<footer> HD Fishing &copy; 2019 
			<h4> Please follow us on Facebook & instagram	
				<span class="iconify" data-icon="ant-design:facebook-filled" data-inline="false"></span>
				<span class="iconify" data-icon="brandico:instagram-filled" data-inline="false"></span>
			</h4>
	</footer>

			<script src="js/main.js"></script>
			<script src="https://code.iconify.design/1/1.0.6/iconify.min.js"></script>	

</body>
</html>
