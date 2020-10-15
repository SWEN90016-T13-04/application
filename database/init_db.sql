CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydb`;
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
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `unit` varchar(45) DEFAULT NULL,
  `building` varchar(45) DEFAULT NULL,
  `street` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `post_code` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (1,NULL,'40','Davies Street','Brunswick','VIC','Australia','3056'),(2,'2A','122','Albert Street','Port Melbourne','VIC','Australia','3207'),(3,'212','225','St. Kilda Road','Melbourne','VIC','Australia','3000'),(4,'55','59','Perciville Crescent','Moonee Ponds','VIC','Australia','3654');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment_boking`
--

DROP TABLE IF EXISTS `appointment_boking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment_boking` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `beauty_carer_id` int NOT NULL,
  `service_id` int NOT NULL,
  `location` int NOT NULL,
  `customer_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `message` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`,`beauty_carer_id`,`service_id`,`location`,`customer_id`),
  KEY `fk_appointment_boking_users1_idx` (`beauty_carer_id`),
  KEY `fk_appointment_boking_beauty_care_services1_idx` (`service_id`),
  KEY `fk_appointment_boking_addresses1_idx` (`location`),
  KEY `fk_appointment_boking_customers1_idx` (`customer_id`),
  CONSTRAINT `fk_appointment_boking_addresses1` FOREIGN KEY (`location`) REFERENCES `addresses` (`address_id`),
  CONSTRAINT `fk_appointment_boking_beauty_care_services1` FOREIGN KEY (`service_id`) REFERENCES `beauty_care_services` (`service_id`),
  CONSTRAINT `fk_appointment_boking_customers1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `fk_appointment_boking_users1` FOREIGN KEY (`beauty_carer_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment_boking`
--

LOCK TABLES `appointment_boking` WRITE;
/*!40000 ALTER TABLE `appointment_boking` DISABLE KEYS */;
INSERT INTO `appointment_boking` VALUES (1,1,1,1,1,'2020-10-10','09:00:00','09:59:00',NULL),(2,1,2,2,2,'2020-10-10','10:00:00','10:59:00',NULL);
/*!40000 ALTER TABLE `appointment_boking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beauty_care_services`
--

DROP TABLE IF EXISTS `beauty_care_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beauty_care_services` (
  `service_id` int NOT NULL AUTO_INCREMENT,
  `service_name` varchar(45) DEFAULT NULL,
  `cost` varchar(45) DEFAULT NULL,
  `duration_minutes` int DEFAULT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beauty_care_services`
--

LOCK TABLES `beauty_care_services` WRITE;
/*!40000 ALTER TABLE `beauty_care_services` DISABLE KEYS */;
INSERT INTO `beauty_care_services` VALUES (1,'Haircut','35.00',60),(2,'Hair Wash & Dry','50.00',60),(3,'Hair Colour','75.00',60);
/*!40000 ALTER TABLE `beauty_care_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biller_information`
--

DROP TABLE IF EXISTS `biller_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `biller_information` (
  `biller_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`biller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biller_information`
--

LOCK TABLES `biller_information` WRITE;
/*!40000 ALTER TABLE `biller_information` DISABLE KEYS */;
INSERT INTO `biller_information` VALUES (1,'Johnny Cash','j.cash@gmail.com'),(2,'P Money','p.money@hotmail.com'),(3,'50 Cent','fiddy@yahoo.com.au'),(4,'Ceelo Green','clg@unimelb.edu.au');
/*!40000 ALTER TABLE `biller_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `phone_number` int DEFAULT NULL,
  `address_id` int NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `extra_information` varchar(250) DEFAULT NULL,
  `biller_id` int NOT NULL,
  PRIMARY KEY (`customer_id`,`address_id`,`biller_id`),
  KEY `fk_customers_addresses_idx` (`address_id`),
  KEY `fk_customers_biller_information1_idx1` (`biller_id`),
  CONSTRAINT `fk_customers_addresses` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`address_id`),
  CONSTRAINT `fk_customers_biller_information1` FOREIGN KEY (`biller_id`) REFERENCES `biller_information` (`biller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Hugh','Jass',5551234,1,'hjass@gmail.com','password','Is fragile',1),(2,'Lorretta','Schmetta',7896541,2,'hmu@email.com','password','Is old',2),(3,'Jimmy','Barnetsein',1597532,2,'hmu2@email.com','password','Smells like boiled cabbage',3),(4,'Gary','Oldman',1478569,3,'goldman@gmail.com','password','Can\'t walk',0);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `is_admin` tinyint NOT NULL,
  `is_beauty_carer` tinyint NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'beth@bb.com.au','password',1,1),(2,'neil@bb.com.au','password',0,1);
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

-- Dump completed on 2020-10-15 14:44:21


-- Crete Flask App User
USE `mydb`;
CREATE USER IF NOT EXISTS 'flask'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON mydb.* TO 'flask'@'localhost';
FLUSH PRIVILEGES;