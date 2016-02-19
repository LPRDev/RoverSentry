<!-- 
    Title: Snapshot script.
    Date: 12/22/2015
    Author: Robert Reinert
    Description: Takes a single photo using a php exec call, then
                returns back to the home page of the app.
-->
<!DOCTYPE html>
<html>

<head>

    <?php
        $date_stamp = date("ndYhis");
           
    
        echo $new_stamp;        
        //dd if=/dev/video0 of=/var/www/html/photos/snapshot.jpeg bs=11M count=1
        $exec_call = 'dd if=/dev/video0 of=/var/www/html/photos/snapshot_'. $date_stamp . '.jpeg bs=11M count=1';
        
        echo $exec_call;
    
        // Need to stop and restart the camera processes to take a photo because of a bug in UV4L.
        // This hack will need to be removed when a patch is released for UV4L.
        // Terminate the running driver.
        exec('sudo pkill uv4l');
		sleep(1);
    
        // Starting the driver.
        exec('uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg'); 
        sleep(1);
         // Take the snapshot.
        exec($exec_call); 
               
        // Terminate the running driver.
        exec('sudo pkill uv4l');
		sleep(1);
        // Starting the driver.
        exec('uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg'); 
        //Error check here and confirm photo was taken properly. 

        header("location: ../index.php");
    ?>


</head>

<body>
    <p> ...Photo is being taken...</p>
</body>


</html>
