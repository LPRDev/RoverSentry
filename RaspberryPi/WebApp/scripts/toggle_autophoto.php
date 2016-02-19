<!-- 
    Title: Toggle Automated snapshot.
    Date: 1/14/2016
    Author: Robert Reinert
    Description: Writes to a text file to toggle the python 
        script for aumated PIR photos.
-->

<!-- Bootstrap CSS -->

<<<<<<< HEAD
<!-- DELETE HTML LATER AFTER TESTING! -->
<!--
 Bootstrap CSS 
=======
>>>>>>> master
<html>

<head>
    <link rel="stylesheet" href="../source/bootstrap-3.3.6-dist/css/bootstrap.min.css">
    
    <script type="text/javascript">
    
        setTimeout(redirect, 10000);
        // Redirect back to the home page after 10 seconds.
        function redirect() {
            window.location.assign("../pages/index.php");            
        }
    
    </script>
</head>

<body>
    <div class="container">

        <div class="panel panel-default centerize">
            <div class="panel-body">
                <a href="../pages/index.php" id="home"> Back to home </a>

                <h1>PIR SENSOR automated photo options.</h1>
            </div>

        </div>
<<<<<<< HEAD
-->
=======
>>>>>>> master


        <?php 

// Open the file for reading.
$toggle = fopen("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt","r") or die("Unable to open file!");
//Read from the file.
$toggle_data = fread($toggle, filesize("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt"));

//Close the file, then reopen with w+ editing mode activated.
fclose($toggle);
$toggle = fopen("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt","w+") or die("Unable to open file!");



// If the auto program is currently on, turn off.
if ($toggle_data == "ON") {
    // Print out page content.
     echo "<div class=\"alert alert-danger\"> Automated toggle file is now OFF. <a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a></div>";

    fwrite($toggle, "OFF");
    echo "
            <script type=\"text/javascript\">
                alert(\"Automated PIR photo is now OFF.\");
            </script>
        ";
} else {
    // Print out page content.
     echo "<div class=\"alert alert-success\"> Automated toggle file is now: ON. <a href=\"#\" class=\"close\" data-dismiss=\"alert\" aria-label=\"close\">&times;</a></div>";
   
    // Turn on the auto PIR.
    fwrite($toggle, "ON");
    echo "
            <script type=\"text/javascript\">
                alert(\"Automated PIR photo is now ON.\");
            </script>
        ";
}

//Close the file.
fclose($toggle);

// For debugging purposes. Remove later.
<<<<<<< HEAD
header("location: ../index.php");
?>

<!--

=======
//header("location: ../index.php");
?>

>>>>>>> master
    </div>

</body>

</html>
<<<<<<< HEAD
-->
=======
>>>>>>> master
