 $(document).ready(function() {

            $(".control_board").hide();

            //If desktop, center the video feed.
            if (screen.width > 660) {
                $("#video_stream").attr("style", "width: 660px; height: 500px;")
            }

            // Code for hiding the control board.
            $("#hide_controls").click(function() {
                $(".control_board").toggle(900);
            });

            // Take a photo.
            $("#snapshot").click(function() {
                //Exec call here.
                //window.alert("Photo will be taken.");
                window.location.href = "../scripts/snapshot.php";
            });

            //Record a video.
            $("#video").click(function() {
                window.alert("Record Video! Coming Soon!");
            });

            // Restart Drivers.
            $("#restart").click(function() {
                var r = confirm("Are you sure you want to restart drivers?");

                //Yes/no box, true = yes.
                if (r == true)
                    window.location.href = "../scripts/restart_drivers.php";
            });

            //Home function
            $("#homeButton").click(function() {
                window.location.href = "../scripts/home.php";
            });

            //Halt function
            $("#haltButton").click(function() {
                window.location.href = "../scripts/halt.php";
            });

            // APM Pause/Resume toggle.
            $("#resumeButton").click(function() {
                window.location.href = "../scripts/pause_resume.php";
            });

            // Toggle the auto snapshot python process.
            $("#photo_toggle").click(function() {
                window.location.href = "../scripts/toggle_autophoto.php";
            });

        });
