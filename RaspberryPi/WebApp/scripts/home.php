<!-- 
    Title: HOME command.
    Date: 8/1/2016
    Author: Robert Reinert
    Description: Sends the Rover's current mission to go home.

-->


<?php

// Open the file for reading.
$toggle = fopen("host_config.txt","r") or die("Unable to open file!");
$url= fread($url, filesize("host_config.txt"));

 //Close the toggle file.
fclose($url);  

//Concat the string to home url.
$url .= "/home";

//$url = "http://localhost:9000/home";
$response = file_get_contents($url);
echo $response;

if($response == "") {
    
    echo "<h1><b>Error! The Cherry Py may be offline.</b></h1>";
}

sleep(1);
header('location: ../pages/index.php'); //redirect back to the other page

?>
