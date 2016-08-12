<!-- 
    Title: HOME command.
    Date: 8/1/2016
    Author: Robert Reinert
    Description: Sends the Rover's current mission to go home.

-->


<?php

$url = "http://localhost:9000/home";
$response = file_get_contents($url);
echo $response;

if($response == "") {
    
}

sleep(1);

?>
