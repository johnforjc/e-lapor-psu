// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.
// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
function initAutocomplete() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: -33.8688, lng: 151.2195 },
      zoom: 13,
      mapTypeId: "roadmap"
    });
    // Create the search box and link it to the UI element.
    const input = document.getElementById("pac-input");
    const searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    // Bias the SearchBox results towards current map's viewport.
    map.addListener("bounds_changed", () => {
      searchBox.setBounds(map.getBounds());
    });
    let markers = [];
    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener("places_changed", () => {
      const places = searchBox.getPlaces();
  
      if (places.length == 0) {
        return;
      }
      // Clear out the old markers.
      markers.forEach(marker => {
        marker.setMap(null);
      });
      markers = [];
      // For each place, get the icon, name and location.
      const bounds = new google.maps.LatLngBounds();
      places.forEach(place => {
        if (!place.geometry) {
          console.log("Returned place contains no geometry");
          return;
        }
        const icon = {
          url: place.icon,
          size: new google.maps.Size(71, 71),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(17, 34),
          scaledSize: new google.maps.Size(25, 25)
        };
        // Create a marker for each place.
        markers.push(
          new google.maps.Marker({
            map,
            icon,
            title: place.name,
            position: place.geometry.location
          })
        );
  
        if (place.geometry.viewport) {
          // Only geocodes have viewport.
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
      });
      map.fitBounds(bounds);
    });
  }

  
var inputList = document.querySelectorAll('input');
for(let i=0; i<inputList.length; i++)
{
  if(inputList[i].name='csrfmiddlewaretoken')
  {
    var csrfmiddlewaretoken=inputList[i].value;
    console.log(csrfmiddlewaretoken)
    break;
  }
}

function remover()
{
  if(document.getElementById('idBell'))
  {
    // // AJAX MULAI DARI SINI
    var idList = document.querySelectorAll('.list_id');
    // var idArray = []
    var form = document.getElementById('list_id_form');
    var inputList = document.querySelectorAll('input');

    var csrfmiddlewaretoken='';

    for(let i=0; i<inputList.length; i++)
    {
      if(inputList[i].name='csrfmiddlewaretoken')
      {
        csrfmiddlewaretoken=inputList[i].value;
        break;
      }
    }

    for(let i = 0; i<idList.length; i++)
    {
      const xhr = new XMLHttpRequest();
      var url = form.action + '/' +idList[i].value + '/';

      xhr.open(form.method, url);

      xhr.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken);

      var data = "idList="+idList[i].value;

      xhr.send(data);
    }

    // 
    // // AJAX SELESAI DISINI

    var notification = document.getElementById('idBell');
    notification.classList.remove('countBell');
  }
}