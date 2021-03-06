<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Web App for RoverSentry.">
    <meta name="author" content="Robert Reinert">

    <title> RoverSentry Web App </title>

    <!-- Tab Icon: -->
    <!--    <LINK REL="SHORTCUT ICON" HREF="TurnigyBuggy.jpg" /> NOTE THAT THE ICON DOESNT WORK-->

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../source/bootstrap-3.3.6-dist/css/bootstrap.min.css">
    <!-- Basic CSS Styling: -->
    <link rel="stylesheet" href="../style/app_STYLE.css">
    <!-- Include JQUERY CDN: -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Bootstrap core JavaScript: -->
    <script src="../source/bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

    <!-- Script file for buttons on home page -->
    <script type="text/javascript" src="../scripts/index_buttons.js"></script>


</head>

<body>

    <div class="cont">

        <div id="menutop">
            <!-- PHP Script: -->
            <?php include 'menu_bar.html'; ?>
        </div>

        <div class="box">
            <h1>Live Feed:</h1>
        </div>

        <div id="video_stream" class="centerize" style="width:100%; height:500px;" width=100% min-width="320" min-height="240" ;>

            <?php 
            
            echo '<iframe id="camera_stream" class="centerize" src="http://' . gethostname() . ':8080/stream" style="border:none;" scrolling="yes" seamless sandbox width=100% height=100%>    
                </iframe>';    
                
            ?>


        </div>

        <div class="button_board">

            <div class="container">

                <div class="centerize" style="max-width: 700px;">

                    <div class="col-sm-3">
                        <button id="snapshot" class="btn btn-info btn-lg btn-block" role="button">Take Snapshot</button>
                    </div>

                    <div class="col-sm-3">
                        <button id="video" class="btn btn-warning btn-lg btn-block" role="button">Record Video</button>
                    </div>

                    <div class="col-sm-3">
                        <button id="hide_controls" class="btn btn-danger btn-lg btn-block" role="button">Cam Options</button>
                    </div>
                    <div class="col-sm-3">
                        <button id="restart" class="btn btn-success btn-lg btn-block" role="button">Restart UV4L</button>
                    </div>
                </div>
            </div>

        </div>




        <div class="control_board white">


            <?php 
            
            echo '<iframe id="controls" src="http://' . gethostname() . ':8080/panel" width=99% height=400> </iframe>';    
                
            ?>

        </div>

        <div class="button_board">
            <p>Coming soon... More controls go here...</p>


            <div class="container">

                <div class="centerize" style="max-width: 700px;">

                    <div class="col-sm-3">
                        <button id="homeButton" class="btn btn-info btn-lg btn-block" role="button">Home</button>
                    </div>

                    <div class="col-sm-3">

                        <?php 
                        
                        //Access the status page and find the groundspeed to determine whether to start or halt.
                        
                        
                        
                        ?>

                            <button id="haltButton" class="btn btn-warning btn-lg btn-block" role="button">Halt </button>
                    </div>


                    <div class="col-sm-3">
                        <button id="resumeButton" class="btn btn-warning btn-lg btn-block" role="button">Resume </button>
                    </div>

                    <div class="col-sm-3">
                        <?php
                
                            // Open the file for reading.
                                $toggle = fopen("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt","r") or die("Unable to open file!");
                                $data= fread($toggle, filesize("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt"));
                    
                            // If the auto PIR is on, make the button green and on.
                            if($data == "ON") {
                                echo '<button style="color: green;" type="button" id="photo_toggle"> Auto-Photo: ON </button>';
                            } else {
                                echo '<button style="color: red;" type="button" id="photo_toggle"> Auto-Photo: OFF </button>';
                            }
            
                            //Close the toggle file.
                            fclose($toggle);         
                        ?>
                    </div>


                </div>
            </div>

        </div>


    </div>

    <div class="footer">
        <?php include 'footer.html'; ?>
    </div>


</body>

</html>
