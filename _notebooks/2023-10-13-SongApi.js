var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var requestOptions = {
    method: "GET",  // Use "GET" instead of "get"
    headers: myHeaders,
    redirect: "follow"
};

fetch("https://v1.nocodeapi.com/jakeshim/spotify/gYJPBKzbVypPVhjU/browse/featured?country=us", requestOptions)
    .then(response => response.json())  // Parse the response as JSON
    .then(result => console.log(result))
    .catch(error => console.log('error', error));