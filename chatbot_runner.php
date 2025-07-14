<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $userMessage = $_POST["message"];
    $escaped = escapeshellarg($userMessage);

    $command = "python chatbot.py $escaped";
    $output = shell_exec($command);
    echo $output;
}
?>
