<!-- 
    Title: Pause/Resume script.
    Date: 1/7/2016
    Author: Robert Reinert
    Description: Pauses and resumes using an exec call to APM function.
-->


<?php 

//Make an exec call.
// testing the Pi to APM commands interface. The buttons should call the APM command function (see issue #13) using an exec call.

$url = "http://localhost:9000/resume";
$response = file_get_contents($url);
echo $response;

if($response == "") {
    
    echo "<h1><b>Error! The Cherry Py may be offline.</b></h1>";
}

sleep(1);
header('location: ../pages/index.php'); //redirect back to the other page

?>
