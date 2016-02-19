<!-- 
    Title: Photo Gallery.
    Date: 12/22/2015
    Author: Robert Reinert
    Description: Basic photo gallery that allows the downloading
    and deleting of files. Requires bootstrap.
-->


<?php 
    //This is the code to loop and display the photos.   
    
    $directory = "../photos/*.jpeg"; // directory where photos are stored.
    $files = array(); // Create an array of files.
    $index= 0; //index counter for displaying photos.
    $sort_type = $_GET["sort"]; //Get param from query.
    $i= 0; //Index counter for sorting.
    

    // Use glob to store the jpeg files into an array.
    $files = glob($directory);
    
//    foreach ($files as $photo) {
//        echo "Photo: " . $photo . " | " . filemtime($photo);
////        //$files[$i] = $photo; //Assign file to array at index i.
//        $files[$photo] = filemtime($photo); //Set key to mod time.
//        $i++; //Increment the array index counter.
//    }

<<<<<<< HEAD

//function scan_dir($dir) {
//    $ignored = array('.', '..', '.svn', '.htaccess');
//
//    $files = array();    
//    foreach (scandir($dir) as $file) {
//        if (in_array($file, $ignored)) continue;
//        $files[$file] = filemtime($dir . '/' . $file);
//    }
//
//    arsort($files);
//    $files = array_keys($files);
//
//    return ($files) ? $files : false;
//}

   
    // Sort the files array based on parameter.
=======
    // Change order of photos being displayed based on filename.
>>>>>>> master
    switch($sort_type) {
        case 0:
            rsort($files);
            echo "Sorting with newest first. <br>";
        break;
        case 1:
            sort($files);
            echo "Sorting with oldest first. <br>";
        break;
            
        default:
            rsort($files);
            echo "Sorting with newest first. <br>";
    }

    
    // Count number of files and store them to variable..
    $num_files = count($files);
    echo "There are " . $num_files . " photos in the directory. <br><br>";
    
    echo '<div class="container">';

// Loop thru the photos in directory. Put into rows of 4 photos.
    for ($i= 0; $i < $num_files/3; $i++) {
                        
        echo '<div class="row"> ';
        
        //Put 4 photos in each row.
        for ($x= 0; $x < 3; $x++) {
                
            $index= (3*$i) + $x;
            $file= $files[$index]; //Calculate the photo to put in.
            $file_name= strstr($file, "_", false); //Remove path from file name.
            $file_name= substr($file_name,1); //Get rid of the underscore in the name.
            
            if (strlen($file) > 0) { //Acount for an odd number of photos.
                        
            echo '<div class="col-md-4"> <div id="'.($index+1).'" class = "panel panel-info">' .
                    '<div class="panel-heading" > <p>'.($index+1).') '.$file_name.'</p> </div>' .
                    '<div class="panel-body"> <a href="'.$file.'">' . 
                        '<img class="box photo" src="' .$file. '"></a>' .
            "<button type=\"button\" onclick=\"download_photo('$file')\"> Download </button> " .
                        "<button type=\"button\" onclick=\"delete_photo('$file');\">" .
                        ' Delete </button> '.
                 '</div> </div> </div>';
            }
                    
        }
        echo '</div>';
                                
    }
        
echo '</div>';
               

?>
