<!-- 
    Title: Delete photo script.
    Date: 8/1/2016
    Author: Robert Reinert
    Description: Halts the Rover's current mission.

-->


<?php

$url = "http://localhost:9000/halt";
$response = file_get_contents($url);
echo $response;

?>