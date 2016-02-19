<!-- 
    Title: Delete photo script.
    Date: 12/30/2015
    Author: Robert Reinert
    Description: Deletes a photo from the photo directory.

-->



<?php

    $filename = $_GET["file"]; //Get the filename

    echo $filename;

    //Delete the file.
    unlink('../photos'.DIRECTORY_SEPARATOR.$filename); //delete it
    header('location: ../pages/gallery.php'); //redirect back to the other page

    
?>
