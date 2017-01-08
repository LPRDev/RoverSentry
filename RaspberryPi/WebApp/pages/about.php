<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Web App for RoverSentry.">
    <meta name="author" content="Robert Reinert">

    <title> RoverSentry Web App </title>


    <!-- Tab Icon: -->
    <LINK REL="SHORTCUT ICON" HREF="http://nuc2.home/Rdev/RoverSentry/uploads/73a331a2d6a51225c5cb9c91397fd2ff/TurnigyBuggy.jpg" />


    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../source/bootstrap-3.3.6-dist/css/bootstrap.min.css">
    <!-- Basic CSS Styling: -->
    <link rel="stylesheet" href="../style/app_STYLE.css">
    <!-- Include JQUERY CDN: -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Bootstrap core JavaScript: -->
    <script src="../source/bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>


    <script type="text/javascript">
        $(document).ready(function() {


        });

    </script>

</head>

<body>

    <div class="cont">

        <div id="menutop">
            <?php include 'menu_bar.html'; ?>
        </div>

        <div class="box">
            <p>This is a test of the about page.</p>
            <pre>
            App Version: 1.0
            Author: Robert
            Release Date: 12/31/2015
            
            </pre>

            <?php
            
            //Fetch the read me file from the github page.
                $url = 'https://github.com/LPRDev/RoverSentry/blob/master/README.md';
                $response = file_get_contents($url);
            
            //Open the stored txt file
                $source = fopen("help_source.txt","r") or die("Unable to open file!");
                $content= fread($source, filesize("help_source.txt"));

            //Close the toggle file.
                fclose($source);  
            
            //Test to see if the connection exists before trying to display.
                if ($response == "") {
                   
                    //echo "Error, could not fetch about information.";
                    echo $content;
                    
                }
                else {
                                 
                    //Cut out the readme file from the webpage and display.
                    $source_header = strstr($response, '</head>', true);
                    $start_concat = strpos($response, '<div id="readme" class="readme blob instapaper_body">');
                   
                    $response = substr($response, $start_concat);
                                            
                    $readme = $source_header . strstr($response, 'site-footer-container', true);
                    
                    
                    //add comparison to store the most up to date readme code.                   
                    if($content != $readme) {
                        //Update the content to be the latest version from GitHub.
                        $content = $readme
                     
                        //Open the stored txt file
                        $source = fopen("help_source.txt","w");
                        //Write the content to the file.
                        fwrite($source, $content);
                        
                        fclose($source); 
                    }
                    
                    
                    //Display the up to date code from the web page.                    
                    echo $readme;
                }
            
            
               
            
            ?>


        </div>



    </div>

    <div class="footer">
        <?php include 'footer.html'; ?>
    </div>


</body>

</html>
