//global variables
var map;
var infWindow;
var dataArray = locations;

//map error catch
var mapError = function errorAlert() {
	alert('Unable to load Google Maps. Please try again.');
};

//populate the InfoWindow
var popInfoWindow = function (marker, infoWindow) {
	infoWindow.marker = marker;
	infoWindow.setContent('');

	var clientId = 'XKJDNTQ1T0I4Y0TMISGQ4WRFTAQY0OKVFG3WW0BIPQTXSKX3';
	var client_secret = 'THVGBZPQR0NNYTMWGHOCVYZLDMKD3W5GAMWR1MAFRAKMVH2A';
	var requestURL =
		'https://api.foursquare.com/v2/venues/search?query="' +
		marker.title +
		'"&ll=' +
		marker.position.lat() +
		',' +
		marker.position.lng() +
		'&client_id=' +
		clientId +
		'&client_secret=' +
		client_secret +
		'&v=20180321';

	$.getJSON(requestURL)
		.done(function (data) {
			var response = data.response.venues['0'];
			// set display values
			self.name = response.name;
			self.address =
				(response.location.formattedAddress[0] || '') +
				' ' +
				(response.location.formattedAddress[1] || '');
			self.here = response.hereNow.summary;

			// InfoWindow output
			self.infoContent =
				'<div class="infowin"><h3>' +
				self.name +
				'</h3><string>' +
				self.address +
				'<br>' +
				'There is ' +
				self.here +
				'</string></div>';
			infoWindow.setContent(infoContent);
		})
		.fail(function () {
		 	//InfoWindow error output
			self.infoContent =
				'<div class="infowin"><h3>' +
				marker.title +
				'</h3><string>Error occured loading the FourSquare API</string></div>';
			infoWindow.setContent(infoContent);
		});

	infoWindow.open(map, marker);
	infoWindow.addListener('closeclick', function () {
		infoWindow.marker = null;
	});
};

//main view model
var ViewModel = function () {
	var self = this;
	this.markers = [];
	this.searchBar = ko.observable('');
	var centerLocation = { lat: -31.9530948, lng: 115.854724 };

	//create and populate marker infoWindow's
	this.createInfo = function () {
		popInfoWindow(this, infWindow);
		this.setAnimation(google.maps.Animation.BOUNCE);
		setTimeout(() => {
			this.setAnimation(null);
		}, 1500);
	};

	//display map
	this.initMap = function () {
		map = new google.maps.Map(document.getElementById('map'), {
			styles: mapStyle,
			zoom: 17,
			center: new google.maps.LatLng(centerLocation),
		});

		//create InfoWindow
		infWindow = new google.maps.InfoWindow();

		//create markers
		var marker;
		//loop through places.js placing markers on map
		for (var i = 0, len = dataArray.length; i < len; i++) {
			marker = new google.maps.Marker({
				position: new google.maps.LatLng(dataArray[i].lat, dataArray[i].lng),
				map: map,
				title: dataArray[i].title,
				animation: google.maps.Animation.DROP,
			});
			//push marker into marker array
			self.markers.push(marker);
			//set marker listener for click events
			marker.addListener('click', self.createInfo);
		}

		//close infowindow when clicking on map
		map.addListener('click', function () {
			infWindow.close();
		});
	};
	this.initMap();

	//filter list and markers
	this.filteredItems = ko.computed(function () {
		var filteredLocations = [];
		for (var i = 0, len = this.markers.length; i < len; i++) {
			var pointer = this.markers[i];
			var query = pointer.title.toLowerCase();
			if (query.includes(this.searchBar().toLowerCase())) {
				filteredLocations.push(pointer);
				this.markers[i].setVisible(true);
			} else {
				this.markers[i].setVisible(false);
			}
		}
		return filteredLocations;
	}, this);
};

function startApp() {
	// Initialise the view model
	ko.applyBindings(new ViewModel());
}
