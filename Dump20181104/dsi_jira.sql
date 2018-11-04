CREATE DATABASE  IF NOT EXISTS `dsi` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dsi`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: dsi
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jira`
--

DROP TABLE IF EXISTS `jira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jira` (
  `jirakey` varchar(8) NOT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `createdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`jirakey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jira`
--

LOCK TABLES `jira` WRITE;
/*!40000 ALTER TABLE `jira` DISABLE KEYS */;
INSERT INTO `jira` VALUES ('RCR-1','test ticket number one','This is a test ticket for Jira tickets related to Drug X','Closed','2018-10-26 23:27:23'),('RCR-2','Another ticket','Some text to dewcribe the ticket','In Progress','2018-10-26 23:27:23'),('RCR-3','Third ticket','Lorem ipsum','Open','2018-10-26 23:27:23'),('RCR-4','Fear Vier ','Lorem ipsum dimsum','Open','2018-10-26 23:27:23'),('RCR-5','Five Alive','Five a day is good for you','Open','2018-10-26 23:27:23'),('RCR-6','Six-Six-Six','I rolled a six','In Progress','2018-10-26 23:27:23'),('RCR-7','Seven Dwarves','Great number ','Open','2018-10-26 23:27:23');
/*!40000 ALTER TABLE `jira` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-04 21:03:28
