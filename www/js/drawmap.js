function initMap() {
    loadMap(42.2000, -81.2000);
}

function loadMap(lat, long){
    var location = new google.maps.LatLng(lat, long);
    var mapCanvas = document.getElementById('map');
    var mapOptions = {
        center: location,
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    }
    var map = new google.maps.Map(mapCanvas, mapOptions);
}

$(function () {
    initMap();

    $('#submit').click(function () {
        var lat = $("#lat").val(); 
        var long = $("#long").val(); 
        loadMap(lat, long);
    });
});