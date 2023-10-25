---
toc: true
comments: false
layout: post
title: Homepage
description: finder
type: plans
courses: { compsci: {week: 3} }
---
## Home page
Welcome to our website

<html>
<head>
    <title>visit website</title>
</head>
<body>
    <button id="movieButton">visit movie search</button>

<button id="songButton">visit song search</button>

   <script>
        // Add a click event listener to the movie button
        document.getElementById("movieButton").addEventListener("click", function() {
            // Redirect to the specified link
            window.location.href = "https://jkaeshim.github.io/Nighthawk-Pages//2023/10/12/MovieImproved_IPYNB_2_.html";
        });

        // Add a click event listener to the song button
        document.getElementById("songButton").addEventListener("click", function() {
            // Redirect to the specified link
            window.location.href = "https://jkaeshim.github.io/Nighthawk-Pages//2023/10/13/MovieImproved2_IPYNB_2_.html";
        });

        // Function to change the background color
        function changeBackgroundColor(color) {
            document.body.style.backgroundColor = color;
        }
    </script>
</body>
</html>
<button onclick="changeBackgroundColor('blue')">Change Background Color</button>
<div style="background-color: yellow;">
This is a block of text with a yellow background.
</div>
