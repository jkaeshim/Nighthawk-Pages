<body>
    <h1>/root/vscode/Nighthawk-Pages/images/download.jpg</h1>
    <a href="https://jkaeshim.github.io/Nighthawk-Pages/2023/10/12/MovieImproved_IPYNB_2_.html">
        <button>![Alt text](image.png)</button>
    </a>
</body>

<!DOCTYPE html>
<html>
<head>
  <style>
    /* Define the button's appearance as an image */
    .image-button {
      background-image: url(![Alt text](../images/download.jpg)); /* Replace 'your-image-url.png' with your image URL */
      background-size: cover;
      width: 150px;
      height: 50px;
      border: none;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <!-- The button element with the image appearance -->
  <button class="image-button" id="myButton"></button>

  <script>
    // JavaScript code to handle button click
    document.getElementById("myButton").addEventListener("click", function() {
      // Add your desired functionality here when the button is clicked
      alert("Button Clicked!");
    });
  </script>
</body>
</html>
