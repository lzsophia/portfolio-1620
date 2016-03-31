<?php
// require_once 'google/appengine/api/mail/Message.php';
use \google\appengine\api\mail\Message;
Check for empty fields
if(empty($_POST['name'])  		||
   empty($_POST['email']) 		||
   empty($_POST['phone']) 		||
   empty($_POST['message'])	||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
	echo "No arguments Provided!";
	return false;
   }
try {
   $name = $_POST['name'];
   $email_address = $_POST['email'];
   $phone = $_POST['phone'];
   $message = $_POST['message'];
    $message = new Message();
    $email_subject = "Website Contact Form:  $name";
    $email_body = "You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\nEmail: $email_address\n\nPhone: $phone\n\nMessage:\n$message";
    $message->setSender("noreply@portfolio-1620.appspot.com");
    $message->addTo("lzsophia@umich.edu");
    $message->setSubject($email_subject);
    $message->setTextBody($email_Body);
    $message->send();

    header("Location:contact_me.php");

}catch (InvalidArgumentException $e) {

    $error = "Unable to send mail. $e";
}
// $name = $_POST['name'];
// $email_address = $_POST['email'];
// $phone = $_POST['phone'];
// $message = $_POST['message'];
	
// Create the email and send the message
// $to = 'lzsophia@umich.edu'; // Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
// $email_subject = "Website Contact Form:  $name";
// $email_body = "You have received a new message from your website contact form.\n\n"."Here are the details:\n\nName: $name\n\nEmail: $email_address\n\nPhone: $phone\n\nMessage:\n$message";
// $headers = "From: noreply@yourdomain.com\n"; // This is the email address the generated message will be from. We recommend using something like noreply@yourdomain.com.
// $headers .= "Reply-To: $email_address";	
// mail($to,$email_subject,$email_body,$headers);
// return true;			
?>