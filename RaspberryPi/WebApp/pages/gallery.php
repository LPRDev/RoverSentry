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

    <!-- Scripts: -->
    <script type="text/javascript">
        //Global variable for view index.
        var curr_index = 1;
        var increment = 3;

        //JQUERY Code.
        $(document).ready(function() {

            // Code for loading gallery feed.
            $("#oldest").click(function() {
                $("#gallery_board").load("../scripts/robert_gallery.php?sort=1");
            });

            // Code for loading gallery feed.
            $("#newest").click(function() {
                $("#gallery_board").load("../scripts/robert_gallery.php?sort=0");
            });

            //Toolbar naviagation:
            $("#prev").click(function() {
                if (curr_index > increment) {
                    curr_index -= increment;
                    window.location = "#" + (curr_index);
                } else
                    window.alert("Can't go any lower!");
            });
            
            $("#prev").dblclick(function() {
               window.location = "#menutop"; 
            });

            $("#options").click(function() {
                var r = prompt("Input a page interval size:", 3);
                increment = parseInt(r);
            });

            $("#next").click(function() {
                curr_index += increment;
                window.location = "#" + (curr_index);
            });

        });

        // Delete a photo from the photos directory.
        function delete_photo(photo_name) {

            var r = confirm("Are you sure you want to delete this photo?");

            if (r == true)
                window.location.assign("../scripts/delete_photo.php?file=" + photo_name + "");

            return true;
        }

        //Downloads the photo, returns true upon success.
        function download_photo(photo_name) {

            var r = confirm("Are you sure you want to download this photo?");

            if (r == true)
                window.location.assign("../scripts/download_photo.php?file=" + photo_name + "");

            return true;
        }

    </script>

</head>

<body>

    <div class="cont">

        <div id="menutop">
            <!-- PHP Script: -->
            <?php include 'menu_bar.html'; ?>
        </div>

        <div class="box">
            <p>This is the photo gallery. Click on a photo thumbnail to view the larger file. Use the buttons to download or delete an individual photo. Use the options button to change the page increments.</p>
        </div>

        <div class="button_board">
            <button type="button" id="oldest"> Oldest First </button>
            <button type="button" id="newest"> Newest First </button>
            <button type="button" id="options"> Options </button>
        </div>

        <div class="toolbar_board navbar-fixed-bottom">
            <button type="button" id="prev" onclick=""> Prev Page </button>
            <button type="button" id="next" onclick=""> Next Page </button>
        </div>

        <div id="gallery_board">
            <?php include "../scripts/robert_gallery.php"; ?>

        </div>


    </div>

    <div class="footer">
        <?php include 'footer.html'; ?>
    </div>


</body>

</html>
