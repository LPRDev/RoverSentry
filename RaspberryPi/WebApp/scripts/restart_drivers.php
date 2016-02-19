<!-- 
    Title: Restart Drivers script.
    Date: 12/22/2015
    Author: Robert Reinert
    Description: Resets the UV4L Camera drivers to allow photos
                to be taken without the 0byte error.
-->
<!DOCTYPE html>
<html>

<head>

    <?php
        $output = array();
		// test the exec with a simple command, retval should be 0 form most cases 
//        exec("pwd",$output, $retval);
//		echo "pwd  Return Value = ",$retval , "<br>Command response = ";	
//		var_dump($output);
//        unset($output);
		
		//exec('sudo service uv4l_raspicam restart');  // Terminate the running driver.
			
		//echo "<br>Command = \"$cmd\"";
		exec('pkill uv4l 2>&1', $output, $retval);
		echo "<br>pkill Return Value = $retval";
		echo "<br>Command response = ";
		var_dump($output);
		sleep(1);
        // Starting the driver.
	   
	    unset($output);
		exec('uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg 2>&1',$output,$retval );
        //$retval = shell_exec('sudo uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg'); 
		echo "<br>uv4l Return Value = $retval";
		echo "<br>Command response = ";
		var_dump($output);
        // Sleep for 1 seconds.
        sleep(1);
        header("location: ../index.php");
    ?>

</head>

<body>
    <p> ...Raspicam drivers are restarting ...</p>
</body>


</html>
