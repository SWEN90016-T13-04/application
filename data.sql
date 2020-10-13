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
INSERT INTO `addresses` VALUES (1,NULL,'40','Davies Street','Brunswick','VIC','Australia','3056'),(2,'2A','122','Albert Street','Port Melbourne','VIC','Australia','3207'),(3,'212','225','St. Kilda Road','Melbourne','VIC','Australia','3000');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `appointment_boking`
--

LOCK TABLES `appointment_boking` WRITE;
/*!40000 ALTER TABLE `appointment_boking` DISABLE KEYS */;
INSERT INTO `appointment_boking` VALUES (1,1,1,1,1,'2020-10-10','09:00:00','09:59:00',NULL),(2,1,2,2,2,'2020-10-10','10:00:00','10:59:00',NULL);
/*!40000 ALTER TABLE `appointment_boking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `beauty_care_services`
--

LOCK TABLES `beauty_care_services` WRITE;
/*!40000 ALTER TABLE `beauty_care_services` DISABLE KEYS */;
INSERT INTO `beauty_care_services` VALUES (1,'Haircut','35.00',60),(2,'Hair Wash & Dry','50.00',60),(3,'Hair Colour','75.00',60);
/*!40000 ALTER TABLE `beauty_care_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `biller_information`
--

LOCK TABLES `biller_information` WRITE;
/*!40000 ALTER TABLE `biller_information` DISABLE KEYS */;
INSERT INTO `biller_information` VALUES (1,'Johnny Cash','j.cash@gmail.com'),(2,'P Money','p.money@hotmail.com'),(3,'50 Cent','fiddy@yahoo.com.au'),(4,'Ceelo Green','clg@unimelb.edu.au');
/*!40000 ALTER TABLE `biller_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Hugh','Jass',5551234,1,1,'hjass@gmail.com','password','Has extremely long fingernails'),(2,'Lorretta','Schmetta',7896541,2,3,'hmu@email.com','password',NULL),(3,'Jimmy','Barnetsein',1597532,2,2,'hmu2@email.com','password',NULL),(4,'Gary','Oldman',1478569,3,2,'goldman@gmail.com','password','Not very mobile');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'beth@bb.com.au','password',1,1),(2,'neil@bb.com.au','password',0,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-13 16:16:52
