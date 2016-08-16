<!-- 
    Title: Pause/Resume script.
    Date: 1/7/2016
    Author: Robert Reinert
    Description: Pauses and resumes using an exec call to APM function.
-->


<?php 

// Open the file for reading.
$toggle = fopen("host_config.txt","r") or die("Unable to open file!");
$url= fread($url, filesize("host_config.txt"));

 //Close the toggle file.
fclose($url);  

//Concat the string to halt url.
$url .= "/resume";

//$url = "http://localhost:9000/resume";

$response = file_get_contents($url);
echo $response;

if($response == "") {
    
    echo "<h1><b>Error! The Cherry Py may be offline.</b></h1>";
}

sleep(1);
header('location: ../pages/index.php'); //redirect back to the other page

?>
