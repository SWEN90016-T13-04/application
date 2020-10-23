-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` (`address_id`, `unit`, `building`, `street`, `city`, `state`, `country`, `post_code`) VALUES (1,NULL,'40','Davies Street','Brunswick','VIC','Australia','3056');
INSERT INTO `addresses` (`address_id`, `unit`, `building`, `street`, `city`, `state`, `country`, `post_code`) VALUES (2,'2A','122','Albert Street','Port Melbourne','VIC','Australia','3207');
INSERT INTO `addresses` (`address_id`, `unit`, `building`, `street`, `city`, `state`, `country`, `post_code`) VALUES (3,'212','225','St. Kilda Road','Melbourne','VIC','Australia','3000');
INSERT INTO `addresses` (`address_id`, `unit`, `building`, `street`, `city`, `state`, `country`, `post_code`) VALUES (4,'55','59','Perciville Crescent','Moonee Ponds','VIC','Australia','3654');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `appointment_booking`
--

LOCK TABLES `appointment_booking` WRITE;
/*!40000 ALTER TABLE `appointment_booking` DISABLE KEYS */;
INSERT INTO `appointment_booking` (`appointment_id`, `beauty_carer_id`, `service_id`, `location`, `customer_id`, `date`, `start_time`, `end_time`, `message`) VALUES (1,1,1,1,1,'2020-10-10','09:00:00','09:59:00',NULL);
INSERT INTO `appointment_booking` (`appointment_id`, `beauty_carer_id`, `service_id`, `location`, `customer_id`, `date`, `start_time`, `end_time`, `message`) VALUES (2,1,2,2,2,'2020-10-10','10:00:00','10:59:00',NULL);
/*!40000 ALTER TABLE `appointment_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `beauty_care_services`
--

LOCK TABLES `beauty_care_services` WRITE;
/*!40000 ALTER TABLE `beauty_care_services` DISABLE KEYS */;
INSERT INTO `beauty_care_services` (`service_id`, `service_name`, `cost`, `duration_minutes`) VALUES (1,'Haircut','35.00',60);
INSERT INTO `beauty_care_services` (`service_id`, `service_name`, `cost`, `duration_minutes`) VALUES (2,'Hair Wash & Dry','50.00',60);
INSERT INTO `beauty_care_services` (`service_id`, `service_name`, `cost`, `duration_minutes`) VALUES (3,'Hair Colour','75.00',60);
INSERT INTO `beauty_care_services` (`service_id`, `service_name`, `cost`, `duration_minutes`) VALUES (4,'Blow Dry','75',60);
/*!40000 ALTER TABLE `beauty_care_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `biller_information`
--

LOCK TABLES `biller_information` WRITE;
/*!40000 ALTER TABLE `biller_information` DISABLE KEYS */;
INSERT INTO `biller_information` (`biller_id`, `name`, `email`) VALUES (1,'Johnny Cash','j.cash@gmail.com');
INSERT INTO `biller_information` (`biller_id`, `name`, `email`) VALUES (2,'P Money','p.money@hotmail.com');
INSERT INTO `biller_information` (`biller_id`, `name`, `email`) VALUES (3,'50 Cent','fiddy@yahoo.com.au');
INSERT INTO `biller_information` (`biller_id`, `name`, `email`) VALUES (4,'Ceelo Green','clg@unimelb.edu.au');
/*!40000 ALTER TABLE `biller_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` (`customer_id`, `first_name`, `last_name`, `phone_number`, `address_id`, `email`, `password`, `extra_information`, `biller_id`, `authenticated`) VALUES (1,'Hugh','Jass',5551234,1,'hjass@gmail.com','password','Is fragile',1,0);
INSERT INTO `customers` (`customer_id`, `first_name`, `last_name`, `phone_number`, `address_id`, `email`, `password`, `extra_information`, `biller_id`, `authenticated`) VALUES (2,'Lorretta','Schmetta',7896541,2,'hmu@email.com','password','Is old',2,0);
INSERT INTO `customers` (`customer_id`, `first_name`, `last_name`, `phone_number`, `address_id`, `email`, `password`, `extra_information`, `biller_id`, `authenticated`) VALUES (3,'Jimmy','Barnetsein',1597532,2,'hmu2@email.com','password','Smells like boiled cabbage',3,0);
INSERT INTO `customers` (`customer_id`, `first_name`, `last_name`, `phone_number`, `address_id`, `email`, `password`, `extra_information`, `biller_id`, `authenticated`) VALUES (4,'Gary','Oldman',1478569,3,'goldman@gmail.com','password','Can\''t walk',0,0);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`user_id`, `username`, `password`, `is_admin`, `is_beauty_carer`, `first_name`, `last_name`, `authenticated`) VALUES (1,'beth@bb.com.au','password',1,1,'Beth','McBeth',0);
INSERT INTO `users` (`user_id`, `username`, `password`, `is_admin`, `is_beauty_carer`, `first_name`, `last_name`, `authenticated`) VALUES (2,'neil@bb.com.au','password',0,1,'Niel','Lentils',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-17 17:04:23
